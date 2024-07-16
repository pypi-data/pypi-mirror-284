# -*- coding: UTF-8 -*-
"""
Created on 23.01.23

:author:     Martin Dočekal
"""
import copy
import dataclasses
import math
import re
from abc import ABC, abstractmethod
from typing import Optional, Union, List, Dict, Any, TypeVar, Generic, Type, Generator, Tuple, Callable, Pattern

from classconfig import ConfigurableValue, ConfigurableMixin
from classconfig.validators import BoolValidator


ABSTRACT_REGEX = re.compile(r"^((^|\s|\()((((X{1,3}(IX|IV|V?I{0,3}))|((IX|IV|I{1,3}|VI{0,3})))|"
                            r"[0-9]+|[a-z])(\.(((X{1,3}(IX|IV|V?I{0,3}))|((IX|IV|I{1,3}|VI{0,3})))|[0-9]+"
                            r"|[a-z]))*\.?)($|\s|\)))?\s*abstract\s*$", re.IGNORECASE)


@dataclasses.dataclass(slots=True)
class RefSpan:
    """
    Referencing span
    """

    index: Optional[int]
    """
    identifier of referenced entity
    it should be index to non_plaintext_content or bibliography
    null means that the source is unknown
    """
    start: int  #: span start offset
    end: int  #: span end offset (not inclusive)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RefSpan":
        """
        Creates this data class from dictionary.

        :param d: the dictionary used of instantiation
        :return: create RefSpan
        """
        return RefSpan(
            index=d["index"],
            start=d["start"],
            end=d["end"]
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts this data class to dictionary.

        :return: dictionary representation of this data class
        """
        return {
            "index": self.index,
            "start": self.start,
            "end": self.end
        }


@dataclasses.dataclass(slots=True)
class TextContent:
    text: str

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TextContent":
        """
        Creates this data class from dictionary.

        :param d: the dictionary used of instantiation
        :return: create TextContent
        """
        return TextContent(
            text=d["text"],
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts this data class to dictionary.

        :return: dictionary representation of this data class
        """
        return {
            "text": self.text
        }


@dataclasses.dataclass(slots=True)
class TextContentWithCitations(TextContent):
    citations: List[RefSpan]
    references: List[RefSpan]

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TextContentWithCitations":
        """
        Creates this data class from dictionary.

        :param d: the dictionary used of instantiation
        :return: create TextContentWithCitations
        """
        return TextContentWithCitations(
            text=d["text"],
            citations=[RefSpan.from_dict(c) for c in d["citations"]],
            references=[RefSpan.from_dict(r) for r in d["references"]]
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts this data class to dictionary.

        :return: dictionary representation of this data class
        """
        return {
            "text": self.text,
            "citations": [c.to_dict() for c in self.citations],
            "references": [r.to_dict() for r in self.references]
        }


T = TypeVar("T", bound="TextContent")


@dataclasses.dataclass(slots=True)
class ContentHierarchy(Generic[T]):
    """
    It is a tree like structure for representation of a document that allows to define hierarchical sections and their
    content.
    """

    parent: Optional["ContentHierarchy"]  #: parent of this document
    headline: Optional[str]  #: headline of a part
    content: Union[
        List["ContentHierarchy"], TextContent]  # content of a part could contain another parts or a text content
    mark: Optional[Any] = None  #: voluntary mark

    @staticmethod
    def from_dict(d: Dict[str, Any], text_content_type: Optional[Type[T]]) -> "ContentHierarchy":
        """
        Creates this data class from dictionary.

        Example:
            >>> d = {
            ...     "headline": "h1",
            ...     "content": [
            ...         {
            ...             "headline": "h2",
            ...             "content": [
            ...                 {
            ...                     "headline": "h3",
            ...                     "content": {
            ...                         "text": "text"
            ...                     }
            ...                 }
            ...             ]
            ...         }
            ...     ]
            ... }
            >>> h = ContentHierarchy.from_dict(d, TextContent)
            >>> h.headline
            'h1'
            >>> h.content[0].headline
            'h2'
            >>> h.content[0].content[0].headline
            'h3'
            >>> h.content[0].content[0].content.text
            'text'

        :param d: the dictionary used of instantiation
        :param text_content_type: type of the text content
            If None it is expcted that the text content is already instantiated.
        :return: create hierarchy
        """
        content = d["content"]
        res = ContentHierarchy(
            parent=None,
            headline=d["headline"],
            content=[],
            mark=d.get("mark", None)
        )
        if (text_content_type is None and isinstance(content, TextContent)) or \
                (text_content_type is not None and isinstance(content, dict)):
            res.content = content if text_content_type is None else text_content_type.from_dict(content)
            return res

        for i, c in enumerate(content):
            d = ContentHierarchy.from_dict(c, text_content_type)
            if d.headline is None:
                d.headline = f"[{i}]"
            d.parent = res
            res.content.append(d)

        return res

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts this data class to dictionary.
        Do not use as_dict method from dataclasses module as it will cause infinite recursion due to parent attribute.

        :return: dictionary representation of this data class
            the mark field is present only if it is not None
        """
        res = {
            "headline": self.headline,
            "content": [c.to_dict() for c in self.content] if isinstance(self.content, list)
            else dataclasses.asdict(self.content)
        }
        if self.mark is not None:
            res["mark"] = self.mark

        return res

    @property
    def height(self) -> int:
        """
        Height of hierarchy.
        """
        if isinstance(self.content, TextContent) or len(self.content) == 0:
            return 0
        return max(h.height + 1 for h in self.content)

    @property
    def depth(self) -> int:
        """
        Depth of this hierarchy.
        """
        if self.parent is None:
            return 0
        return self.parent.depth + 1

    @property
    def headline_path(self) -> List[Optional[str]]:
        """
        Returns the path of headlines from root to this hierarchy.

        :return: list of headlines
        """
        if self.parent is None:
            return [self.headline]

        return self.parent.headline_path + [self.headline]

    def pre_order(self) -> Generator["ContentHierarchy", None, None]:
        """
        Iterates all sub-hierarchies in pre-order like order.

        And yes, it also generates itself.

        :return: generator of sub-hierarchies
        """

        to_process = [self]

        while to_process:
            h = to_process.pop(-1)
            yield h
            if isinstance(h.content, list):
                for sub_hierarchy in reversed(h.content):
                    to_process.append(sub_hierarchy)

    def flatten(self) -> Generator[Tuple[List[Optional[str]], TextContent], None, None]:
        """
        Flattens the hierarchy.

        Example:
            >>> h = ContentHierarchy(
            ...     parent=None,
            ...     headline="h1",
            ...     content=[
            ...         ContentHierarchy(
            ...             parent=None,
            ...             headline="h2",
            ...             content=[
            ...                 ContentHierarchy(
            ...                     parent=None,
            ...                     headline="h3",
            ...                     content=TextContent("text")
            ...                 )
            ...             ]
            ...         )
            ...     ]
            ... )
            >>> list(h.flatten())
            [(['h1', 'h2', 'h3'], TextContent(text='text'))]

        :return: generator of flattened hierarchy
            it generates tuples of list of section headline paths and text content
        """
        for h in self.pre_order():
            if isinstance(h.content, TextContent):
                yield h.headline_path, h.content

    @classmethod
    def from_flattened(cls, flattened: List[Tuple[List[Optional[str]], TextContent]]) -> "ContentHierarchy":
        """
        Creates hierarchy from flattened hierarchy.

        Example:
            >>> h = ContentHierarchy(
            ...     parent=None,
            ...     headline="h1",
            ...     content=[
            ...         ContentHierarchy(
            ...             parent=None,
            ...             headline="h2",
            ...             content=[
            ...                 ContentHierarchy(
            ...                     parent=None,
            ...                     headline="h3",
            ...                     content=TextContent("text")
            ...                 )
            ...             ]
            ...         )
            ...     ]
            ... )
            >>> list(h.flatten())
            [(['h1', 'h2', 'h3'], TextContent(text='text'))]
            >>> ContentHierarchy.from_flattened(list(h.flatten()))
            StructuredDocument(parent=None, headline='h1', content=[StructuredDocument(parent=None, headline='h2', content=[StructuredDocument(parent=None, headline='h3', content=TextContent(text='text'))])])

        :param flattened: flattened hierarchy
        :return: hierarchy
        """
        hier_dict = {
            "headline": None,
            "content": []
        }

        for path, content in flattened:
            d = hier_dict
            for p in path:
                for c in d["content"]:
                    if c["headline"] == p:
                        d = c
                        break
                else:
                    new_d = {
                        "headline": p,
                        "content": []
                    }
                    d["content"].append(new_d)
                    d = new_d

            d["content"] = content

        return cls.from_dict(hier_dict["content"][0], None)

    def text_content_with_citations(self) -> Generator[TextContentWithCitations, None, None]:
        """
        Generates text contents, with citations, in hierarchy from the left most one to the right most one.

        :return: generator of TextContent
        """

        for h in self.pre_order():
            if isinstance(h.content, TextContentWithCitations):
                yield h.content

    def text_content(self) -> Generator[TextContent, None, None]:
        """
        Generates text contents in hierarchy from the left most one to the right most one.

        :return: generator of TextContent
        """

        for h in self.pre_order():
            if isinstance(h.content, TextContent):
                yield h.content

    def citation_spans(self) -> Generator[RefSpan, None, None]:
        """
        Generation of all citations spans in hierarchy.
        It iterates text content from the left most one to the right most one, but it does not guarantee left to right
        positioning of citation inside a single text content.,,,,,

        :return: generator of citation spans
        """
        for text in self.text_content_with_citations():
            for cit in text.citations:
                yield cit

    def filter(self, filter_func: Callable[["ContentHierarchy"], bool]) -> Optional["ContentHierarchy"]:
        """
        Filters the hierarchy.

        :param filter_func: the function used for filtering
            when it returns True, the hierarchy is kept, otherwise it is removed
        :return: filtered hierarchy
        """
        if not filter_func(self):
            return None

        res = copy.copy(self)

        if isinstance(res.content, list):
            new_content = []
            for sub_hierarchy in res.content:
                new_sub_hierarchy = sub_hierarchy.filter(filter_func)
                if new_sub_hierarchy is not None:
                    new_content.append(new_sub_hierarchy)
            res.content = new_content
        return res

    def template(self, b_sec_tok: str = "<sec>", e_sec_tok: str = "</sec>", p_sep_tok: str = "<p>") -> str:
        """
        Creates template of the hierarchy.

        Example:

            sentence 1 of paragraph 1 sentence 2 of paragraph 1
                Section 1
                sentence 1 of paragraph 1

                    Section 1.1
                    sentence 1 of paragraph 1 sentence 2 of paragraph 1
                    sentence 1 of paragraph 1 sentence 2 of paragraph 1

                Section 2
                sentence 1 of paragraph 1 sentence 2 of paragraph 1 sentence 3 of paragraph 1
                sentence 1 of paragraph 1 sentence 2 of paragraph 1

            Template (there are no new lines and white chars in the template):
                <sec>
                    2
                    <sec>
                        1
                        <sec>
                            2<p>2
                        </sec>
                    </sec>
                        3<p>2
                    </sec>
                </sec>

        The height is used to determine paragraph and sections. Hierarchies with height 1 are considered as paragraphs.
        Hierarchies with height 2 or higher are considered as sections. The template is created recursively.


        :param b_sec_tok: token used for beginning of section
        :param e_sec_tok: token used for end of section
        :param p_sep_tok: token used for separation of paragraphs
        :return: template of the hierarchy
        """
        if self.height == 0:
            return ""

        if self.height == 1:
            return str(len(self.content))

        res = b_sec_tok
        p_before = False
        for c in self.content:
            if c.height == 1:
                if p_before:
                    res += p_sep_tok
                p_before = True
                res += str(len(c.content))
            else:
                res += c.template(b_sec_tok, e_sec_tok, p_sep_tok)
                p_before = False

        res += e_sec_tok

        return res


    def get_part(self, headline_re: Pattern, max_h: float = math.inf, min_depth: float = 0,
                 max_depth: float = math.inf, return_path: bool = False) -> Union[List["Hierarchy"], List[Tuple[List["Hierarchy"], Tuple[int]]]]:
        """
        Searches in hierarchy for given headline and returns the whole sub-hierarchy associated to it.

        If a hierarchy with matching headline contains sub hierarchy with headline that also matches, it returns just
        the parent hierarchy.

        :param headline_re: compiled regex that will be used for headline matching
        :param max_h: maximal number of matching hierarchies after which the search is stopped
        :param min_depth: minimal depth of a node (root has zero depth)
        :param max_depth: maximal depth of a node
        :param return_path: if True, returns also path to the hierarchy
            path is represented by sequence of indices of sub-hierarchies
        :return: all searched hierarchies.
            If return_path is True, returns also path to the hierarchy
        """
        to_process = [(0, self, ())]

        res = []

        while to_process:
            depth, h, path = to_process.pop(-1)

            if h.headline is not None and depth >= min_depth:
                if headline_re.match(h.headline):
                    res.append((h, path) if return_path else h)
                    if len(res) >= max_h:
                        break
                    continue

            if isinstance(h.content, list) and depth < max_depth:
                for i, sub_hierarchy in zip(range(len(h.content)-1, -1, -1), reversed(h.content)):
                    to_process.append((depth + 1, sub_hierarchy, path + (i,)))

        return res

    def nodes_with_height(self, height: int) -> Generator["ContentHierarchy", None, None]:
        """
        Generates nodes with given height in pre-order fashion.

        :param height: height of nodes that are supposed to be generated
        :return: generator of nodes with given height
        """

        for n in self.pre_order():
            if n.height == height:
                yield n


@dataclasses.dataclass(slots=True)
class BibEntry:
    id: Optional[int]  # this is id of document in dataset may be None if this document is not in it
    title: str
    year: Optional[int]
    authors: Tuple[str, ...]

    def asdict(self) -> Dict[str, Any]:
        """
        Converts this data class to dictionary.

        :return: dictionary representation of this data class
        """
        # dataclasses.asdict is too slow
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "authors": self.authors
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "BibEntry":
        """
        Creates this data class from dictionary.

        :param d: the dictionary used of instantiation
        :return: bib entry
        """
        return cls(d["id"], d["title"], d["year"], tuple(d["authors"]))


@dataclasses.dataclass(slots=True)
class StructuredDocument:
    """
    Representation of a document with structured content.
    """

    id: int  #: identifier of a document
    s2orc_id: Optional[int]  #: identifier of a document
    mag_id: Optional[int]  #: mag identifier of a document
    doi: Optional[str]  #: Digital Object Identifier
    title: str  #: the title of a document
    authors: List[str]  #: authors of given document
    year: Optional[int]  #: year when the document was published
    fields_of_study: List[str]  # fields of study, such as "Mathematics", "Physics" ...
    citations: List[int]  #: identifiers of referenced documents
    hierarchy: Optional[ContentHierarchy]  #: hierarchical representation of a document
    bibliography: List[BibEntry]
    non_plaintext_content: List[
        Tuple[str, str]]  #: list of tuple in form of content type (figure, table) and description

    @classmethod
    def from_dict(cls, d: Dict[str, Any], **kwargs) -> "StructuredDocument":
        """
        Creates this data class from dictionary.

        :param d: the dictionary used of instantiation
        :param kwargs: can be used to override some values
        :return: create document
        """

        referenced = kwargs["referenced"] if "referenced" in kwargs else d.get("referenced", [])
        if referenced:
            citations = [r["id"] for r in referenced]
        else:
            citations = kwargs["citations"] if "citations" in kwargs else d.get("citations", [])

        hierarchy = None
        if "hierarchy" in kwargs:
            hierarchy = kwargs["hierarchy"]
        elif "hierarchy" in d and d["hierarchy"] is not None:
            hierarchy = ContentHierarchy.from_dict(d["hierarchy"], TextContentWithCitations)

        if "non_plaintext_content" in kwargs:
            non_plaintext_content = kwargs["non_plaintext_content"]
        else:
            # we support two versions
            if len(d["non_plaintext_content"]) > 0 and isinstance(d["non_plaintext_content"][0], dict):
                non_plaintext_content = [(x["type"], x["description"]) for x in d["non_plaintext_content"]]
            else:
                non_plaintext_content = d["non_plaintext_content"]

        fos = kwargs["fields_of_study"] if "fields_of_study" in kwargs else d["fields_of_study"]

        return cls(
            id=kwargs["id"] if "id" in kwargs else d["id"],
            s2orc_id=kwargs["s2orc_id"] if "s2orc_id" in kwargs else d.get("s2orc_id", None),  # voluntary
            mag_id=kwargs["mag_id"] if "mag_id" in kwargs else d["mag_id"],
            doi=kwargs["doi"] if "doi" in kwargs else d["doi"],
            title=kwargs["title"] if "title" in kwargs else d["title"],
            authors=kwargs["authors"] if "authors" in kwargs else d["authors"],
            year=kwargs["year"] if "year" in kwargs else d["year"],
            fields_of_study=[f if isinstance(f, str) else f[0] for f in fos],
            # to support loading the (field, score) format
            citations=citations,
            hierarchy=hierarchy,
            non_plaintext_content=non_plaintext_content,
            bibliography=kwargs["bibliography"] if "bibliography" in kwargs else \
                [BibEntry.from_dict(b) for b in d["bibliography"]]
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts this data class to dictionary.
        Do not use as_dict method from dataclasses module as it will cause infinite recursion due to parent attribute.

        :return: dictionary representation of this data class
        """
        return {
            "id": self.id,
            "s2orc_id": self.s2orc_id,
            "mag_id": self.mag_id,
            "doi": self.doi,
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "fields_of_study": self.fields_of_study,
            "citations": self.citations,
            "hierarchy": self.hierarchy.to_dict() if self.hierarchy is not None else None,
            "bibliography": [dataclasses.asdict(b) for b in self.bibliography],
            "non_plaintext_content": self.non_plaintext_content
        }

    @property
    def abstract(self) -> Optional[ContentHierarchy]:
        """
        Tries to extract abstract from document hierarchy.

        :return: abstract or None if not found
        """
        abstract_section = self.hierarchy.get_part(ABSTRACT_REGEX, max_h=1, min_depth=1, max_depth=1)

        if abstract_section and any(len(t_c.text) > 0 for t_c in abstract_section[0].text_content()):
            return abstract_section[0]


class StrucDoc2StrConvertor(ConfigurableMixin, ABC):
    """
    Abstract class for converting structured document to string.
    """

    include_id: bool = ConfigurableValue("If True, then document id will be included in the string.",
                                         user_default=False, validator=BoolValidator())
    include_authors: bool = ConfigurableValue("If True, then authors will be included in the string.",
                                              user_default=False, validator=BoolValidator())

    @abstractmethod
    def __call__(self, doc: StructuredDocument) -> str:
        """
        Converts structured document to string.

        :param doc: document to convert
        :return: string representation of the document
        """
        pass


class StructDoc2Markdown(StrucDoc2StrConvertor):
    """
    Converts structured document to markdown.
    """

    HEADLINE_IS_NUMBERING = re.compile(r"\[\d+\]")

    convert_citations_and_references: bool = ConfigurableValue("If True, then citations and references spans will be "
                                                               "converted to normalized format.",
                                                               user_default=True, validator=BoolValidator(),
                                                               voluntary=True)

    use_title_when_hierarchy_is_none: bool = ConfigurableValue("If True, then title will be when hierarchy is None.",
                                                               user_default=True, validator=BoolValidator(),
                                                               voluntary=True)
    omit_headlines: bool = ConfigurableValue("If True, then headlines will be omitted.",
                                             user_default=False, validator=BoolValidator(),
                                             voluntary=True)

    def __post_init__(self):
        self.sentences_sep = " "

    def __call__(self, doc: StructuredDocument) -> str:
        """
        Converts structured document to markdown.

        :param doc: document to convert
        :return: markdown representation of the document
        """
        res = ""
        if self.include_id:
            res += f"{doc.id}\n"
        if self.include_authors:
            res += f"{', '.join(doc.authors[:2])}{', et al.' if len(doc.authors) > 2 else ''}\n"

        if doc.hierarchy is not None:
            res += self.convert_section(doc, doc.hierarchy,
                                        sentence_sep=self.sentences_sep,
                                        convert_citations_and_references=self.convert_citations_and_references,
                                        omit_headlines=self.omit_headlines)
        elif self.use_title_when_hierarchy_is_none and not self.omit_headlines:
            res += f"# {doc.title}\n"

        return res

    @staticmethod
    def convert_text_content(doc: StructuredDocument, content: TextContentWithCitations) -> str:
        """
        Converts text content to markdown.

        :param doc: document
        :param content: text content from document
        :return: markdown representation of the text content
        """

        # let's convert all spans
        breakpoints = []
        for span in content.citations:
            try:
                bib_entry = doc.bibliography[span.index]
                first_author = bib_entry.authors[0] if len(bib_entry.authors) > 0 else "UNK"
                span_text = f"<cite>{'UNK' if bib_entry.id is None else bib_entry.id}<sep>{bib_entry.title}<sep>{first_author}</cite>"
            except TypeError:
                span_text = f"<cite>UNK</cite>"
            breakpoints.append((span.start, span.end, span_text))
        for span in content.references:
            try:
                non_plaintext_content = doc.non_plaintext_content[span.index]
                span_text = f"<ref>{non_plaintext_content[0]}</ref>"
            except TypeError:
                span_text = f"<ref>UNK</ref>"
            breakpoints.append((span.start, span.end, span_text))

        breakpoints = sorted(breakpoints, key=lambda x: x[0])  # there is no intersection of spans so this is ok

        # let's assemble the text
        text = ""
        last_offset = 0
        for i, b in enumerate(breakpoints):
            text += content.text[last_offset:b[0]]
            text += b[2]
            last_offset = b[1]
        text += content.text[last_offset:]

        return text

    @classmethod
    def convert_section(cls, doc: StructuredDocument, section: ContentHierarchy, sentence_sep: str = " ",
                        convert_citations_and_references: bool = True, omit_headlines: bool = False) -> str:
        """
        Converts section to markdown.

        :param doc: document
        :param section: document section to convert
        :param sentence_sep: string that will be added to separate sentences
        :param convert_citations_and_references: if True then citations and references will be converted to normalized
            format
        :param omit_headlines: if True, then headlines will be omitted
        :return: markdown representation of the section
        """
        res = ""
        if section.headline is not None and not cls.HEADLINE_IS_NUMBERING.match(section.headline) and not omit_headlines:
            # we want to skip formula headlines as there are artificially added for identification of
            # formulas section are: section.headline == "formula" and section.height == 0
            if section.headline != "formula" or section.height != 0:
                res = "#" * (section.depth + 1) + f" {section.headline}" + "\n"

        if isinstance(section.content, TextContentWithCitations):
            res += cls.convert_text_content(doc, section.content) if convert_citations_and_references else \
                section.content.text
        else:
            for i, c in enumerate(section.content):
                res += cls.convert_section(doc, c, sentence_sep=sentence_sep,
                                           convert_citations_and_references=convert_citations_and_references,
                                             omit_headlines=omit_headlines)
                if c.headline is None or cls.HEADLINE_IS_NUMBERING.match(c.headline):
                    if c.height == 1:
                        # end of paragraph
                        res += "\n"
                    elif c.height == 0 and i < len(section.content) - 1:
                        # end of sentence
                        res += sentence_sep
                elif c.headline == "formula" and c.height == 0:
                    # end of formula
                    res += "\n"

        return res


class StructDoc2Segments(ConfigurableMixin):
    """
    Converts structured document to string segments.
    """

    include_id: bool = ConfigurableValue("If True, then document id will be included as one segment.",
                                         user_default=False, validator=BoolValidator())
    include_authors: bool = ConfigurableValue("If True, then authors will be included as one segment.",
                                              user_default=False, validator=BoolValidator())

    convert_citations_and_references: bool = ConfigurableValue("If True, then citations and references spans will be "
                                                               "converted to normalized format.",
                                                               user_default=True, validator=BoolValidator(),
                                                               voluntary=True)

    use_title_when_hierarchy_is_none: bool = ConfigurableValue("If True, then title will be when hierarchy is None.",
                                                               user_default=True, validator=BoolValidator(),
                                                               voluntary=True)
    mark_sentences_only: bool = ConfigurableValue("If True, then only segments with marked sentences will have"
                                                  "mark True. Else all segments created for a sub-hierarchy with marked"
                                                  "sentence will be marked True.", user_default=True, validator=BoolValidator(),
                                                         voluntary=True)

    def __call__(self, doc: StructuredDocument) -> List[Tuple[bool, str]]:
        """
        Converts structured document to markdown.

        :param doc: document to convert
        :return: segments of the document each associated with hierarchy mark
        """
        res = []

        if self.include_id:
            res.append((doc.hierarchy.mark and not self.mark_sentences_only, f"{doc.id}"))

        if self.include_authors:
            res.append((doc.hierarchy.mark and not self.mark_sentences_only,
                        f"{', '.join(doc.authors[:2])}{', et al.' if len(doc.authors) > 2 else ''}"))

        if doc.hierarchy is not None:
            res.extend(self.convert_section(doc, doc.hierarchy,
                                            convert_citations_and_references=self.convert_citations_and_references,
                                            mark_sentences_only=self.mark_sentences_only))
        elif self.use_title_when_hierarchy_is_none:
            res.extend((doc.hierarchy.mark and not self.mark_sentences_only, f"# {doc.title}"))

        return res

    @classmethod
    def convert_section(cls, doc: StructuredDocument, section: ContentHierarchy,
                        convert_citations_and_references: bool = True, mark_sentences_only: bool = True) -> List[Tuple[bool, str]]:
        """
        Converts section to markdown.

        :param doc: document
        :param section: document section to convert
        :param convert_citations_and_references: if True then citations and references will be converted to normalized
            format
        :param mark_sentences_only: if True, then only segments with marked sentences will have mark True. Else all
        :return: Segments of the section each associated with hierarchy mark
        """
        res = []
        if section.headline is not None and not StructDoc2Markdown.HEADLINE_IS_NUMBERING.match(section.headline):
            # we want to skip formula headlines as there are artificially added for identification of
            # formulas section are: section.headline == "formula" and section.height == 0
            if section.headline != "formula" or section.height != 0:
                res.append((
                    section.mark and not mark_sentences_only,
                    "#" * (section.depth + 1) + f" {section.headline}"
                ))

        if isinstance(section.content, TextContentWithCitations):
            res.append((
                section.mark,
                StructDoc2Markdown.convert_text_content(doc, section.content) if convert_citations_and_references else \
                    section.content.text
            ))
        else:
            for i, c in enumerate(section.content):
                res.extend(
                    cls.convert_section(doc, c,
                                        convert_citations_and_references=convert_citations_and_references,
                                        mark_sentences_only=mark_sentences_only))

        return res
