from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
from typing import Any

from azure.ai.documentintelligence.models import (
    AnalyzeResult,
    DocumentFigure,
    DocumentFormula,
    DocumentPage,
    DocumentTable,
    DocumentWord,
    DocumentSpan,
    DocumentFormulaKind,
)


def polygon2midpoint(polygon: list[float]):
    """Calculate the midpoint of a polygon"""
    x_coords = polygon[0::2]
    y_coords = polygon[1::2]
    middle_x = sum(x_coords) / len(x_coords)
    middle_y = sum(y_coords) / len(y_coords)
    return (middle_x, middle_y)


def polygon2bbox(polygon: list[float]):
    """Calculate the bounding box of a polygon"""
    x_coords = polygon[0::2]
    y_coords = polygon[1::2]
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    return (min_x, min_y, max_x, max_y)


@dataclass(frozen=True, slots=True)
class DocModel(ABC):
    """
    Base class for all the models in the doc intelligence package
    """

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    @classmethod
    def from_obj(cls, obj: Any):
        return cls.from_dict(dict(obj))

    def to_dict(self):
        return asdict(self)

    @abstractmethod
    def from_azure(cls, obj: Any):
        pass

    def from_self(self, **kwargs):
        self_data = self.to_dict()
        self_data.update(kwargs)
        return self.from_dict(self_data)


@dataclass(frozen=True, slots=True)
class DocSpan(DocModel):
    """
    DocumentSpan replication
    """

    offset: int
    length: int

    @classmethod
    def from_azure(cls, span: DocumentSpan):
        return cls.from_obj(span)


@dataclass(frozen=True, slots=True, order=True)
class DocWord(DocModel):
    """
    DocumentWord using midpoint instead of polygon and without confidence attribute
    """

    sort_index: int = field(init=False, repr=False)  # Sort in pages by y, then x
    content: str
    midpoint: tuple[float, float]
    span: DocSpan

    def __post_init__(self):
        # TODO: research about the rounding method
        midpoint_rounded = round(self.midpoint[1], 1), self.midpoint[0]
        object.__setattr__(self, "sort_index", midpoint_rounded)

    @classmethod
    def from_azure(cls, word: DocumentWord):
        if not word.polygon:
            raise ValueError("DocumentWord must have a polygon")
        midpoint = polygon2midpoint(word.polygon)
        span = DocSpan.from_azure(word.span)
        return cls(word.content, midpoint, span)

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["content"], d["midpoint"], DocSpan.from_dict(d["span"]))


@dataclass(frozen=True, slots=True)
class DocFormula(DocModel):
    """
    DocumentFormula using midpoint instead of polygon and without confidence attribute
    """

    sort_index: int = field(init=False, repr=False)  # Sort in pages by y, then x
    value: str
    midpoint: tuple[float, float]
    kind: DocumentFormulaKind
    span: DocSpan

    def __post_init__(self):
        midpoint_rounded = round(self.midpoint[1], 1), self.midpoint[0]
        object.__setattr__(self, "sort_index", midpoint_rounded)

    @classmethod
    def from_azure(cls, formula: DocumentFormula):
        if not formula.polygon:
            raise ValueError("DocumentFormula must have a polygon")
        midpoint = polygon2midpoint(formula.polygon)
        kind = DocumentFormulaKind(formula.kind)
        span = DocSpan.from_azure(formula.span)
        return cls(formula.value, midpoint, kind, span)

    @classmethod
    def from_dict(cls, d: dict):
        kind = DocumentFormulaKind(d["kind"])
        span = DocSpan.from_dict(d["span"])
        return cls(d["value"], d["midpoint"], kind, span)


@dataclass(frozen=True, slots=True)
class DocFigure(DocModel):
    """
    DocumentFigure using bounding box instead of polygon, single span and removing the confidence and the elements attribute
    """

    bounding_box: tuple[float, float, float, float]
    span: DocSpan
    caption: str | None = None

    @classmethod
    def from_azure(cls, figure: DocumentFigure):
        bounding_regions = figure.bounding_regions
        if not bounding_regions:
            raise ValueError("DocumentFigure must have at least 1 bounding region")
        if not figure.spans:
            raise ValueError("DocumentFigure must have at least 1 span")
        bounding_box = polygon2bbox(bounding_regions[0].polygon)
        span = DocSpan.from_azure(figure.spans[0])
        caption = figure.caption.content if figure.caption else None
        return cls(bounding_box, span, caption)

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["bounding_box"], DocSpan.from_dict(d["span"]), d.get("caption"))


@dataclass(frozen=True, slots=True)
class DocTable(DocModel):
    """
    DocumentTable using bounding box instead of polygon, single span and removing the confidence and the elements attribute
    """

    # TODO: consider if it is useful to include list of DocTable

    bounding_box: tuple[float, float, float, float]
    row_count: int
    column_count: int
    span: DocSpan

    @classmethod
    def from_azure(cls, table: DocumentTable):
        bounding_regions = table.bounding_regions
        if not bounding_regions:
            raise ValueError("DocumentTable must have at least 1 bounding region")
        bounding_box = polygon2bbox(bounding_regions[0].polygon)
        span = DocSpan.from_azure(table.spans[0])
        return cls(bounding_box, table.row_count, table.column_count, span)

    @classmethod
    def from_dict(cls, d: dict):
        span = DocSpan.from_dict(d["span"])
        return cls(d["bounding_box"], d["row_count"], d["column_count"], span)


@dataclass(frozen=True, slots=True)
class DocPage(DocModel):
    """
    DocumentPage which have associated figures and without angle, page_number, height, width and unit attributes
    """

    number: int
    words: list[DocWord]
    formulas: list[DocFormula]
    figures: list[DocFigure]
    span: DocSpan

    @classmethod
    def from_azure(cls, page: DocumentPage, doc_figures: list[DocFigure] | None = None):
        if not page.spans:
            raise ValueError("DocumentPage must have at least 1 one span")
        words = [DocWord.from_azure(w) for w in (page.words or [])]
        formulas = [DocFormula.from_azure(f) for f in (page.formulas or [])]
        figures = doc_figures or []
        span = DocSpan.from_azure(page.spans[0])
        return cls(page.page_number, words, formulas, figures, span)

    @classmethod
    def from_dict(cls, d: dict):
        words = [DocWord.from_dict(w) for w in d["words"]]
        formulas = [DocFormula.from_dict(f) for f in d["formulas"]]
        figures = [DocFigure.from_dict(f) for f in d["figures"]]
        span = DocSpan.from_dict(d["span"])
        return cls(d["number"], words, formulas, figures, span)


@dataclass(frozen=True, slots=True)
class AnlResult(DocModel):
    """
    Lite version of AnalyzeResult
    """

    api_version: str
    content: str
    pages: list[DocPage]

    @classmethod
    def from_azure(cls, result: AnalyzeResult):
        pagenum2figs: dict[int, list[DocFigure]] = defaultdict(list)
        for fig in result.figures or []:  # Group figures by page number
            if not fig.bounding_regions:
                raise ValueError("DocumentFigure must have at least 1 bounding region")
            fig_page_num = fig.bounding_regions[0].page_number  # NOTE: is 1-indexed
            pagenum2figs[fig_page_num].append(DocFigure.from_azure(fig))
        pages = [
            DocPage.from_azure(page, pagenum2figs.get(page.page_number, []))
            for page in result.pages
        ]
        return cls(result.api_version, result.content, pages)

    @classmethod
    def from_dict(cls, d: dict):
        pages = [DocPage.from_dict(p) for p in d["pages"]]
        return cls(d["api_version"], d["content"], pages)

    @classmethod
    def from_json(cls, filepath: str | Path):
        with open(filepath, "r") as f:
            data: dict[str, Any] = json.load(f)
        return cls.from_dict(data)

    @classmethod
    def from_analyze_result_json(cls, filepath: str | Path):
        with open(filepath, "r") as f:
            data: dict[str, Any] = json.load(f)
        return cls.from_azure(AnalyzeResult(data))

    def to_json(self, filepath: str | Path):
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    def __repr__(self) -> str:
        return f"AnalyzeResultLite(api_version={self.api_version}, content={self.content}, num_pages={len(self.pages)})"
