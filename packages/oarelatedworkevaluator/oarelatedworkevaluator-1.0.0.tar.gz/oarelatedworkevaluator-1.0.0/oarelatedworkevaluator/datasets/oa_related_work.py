# -*- coding: UTF-8 -*-

import itertools
from abc import ABC
from enum import Enum
from typing import Sequence, Dict, Optional, List, Tuple, Union

from classconfig import ConfigurableValue, RelativePathTransformer, ConfigurableMixin
from classconfig.transforms import EnumTransformer
from classconfig.validators import IsNoneValidator, StringValidator, AnyValidator
from datasets import load_dataset

from oarelatedworkevaluator.etl.data_structures.structured_document import ContentHierarchy, RefSpan, \
    TextContentWithCitations, StructuredDocument, BibEntry, StructDoc2Markdown
from oarelatedworkevaluator.etl.dataset import QueryBasedMultiDocumentSummarizationDataset, Dataset, \
    QueryBasedMultiStructuredDocumentSummarizationDataset, ToyValSplit
from oarelatedworkevaluator.etl.sample import QueryBasedMultiDocumentSummarizationSample, \
    QueryBasedMultiStructuredDocumentSummarizationSample


class OARWConfig(Enum):
    ABSTRACTS = "abstracts"
    FLATTENED_SECTIONS = "flattened_sections"
    GREEDY_ORACLE_SENTENCES = "greedy_oracle_sentences"
    GREEDY_ORACLE_PARAGRAPHS = "greedy_oracle_paragraphs"
    GREEDY_ORACLE_PER_INPUT_DOC_SENTENCES = "greedy_oracle_per_input_doc_sentences"
    GREEDY_ORACLE_PER_INPUT_DOC_PARAGRAPHS = "greedy_oracle_per_input_doc_paragraphs"
    ABSTRACTS_WITH_GREEDY_ORACLE_TARGET_SENTENCES = "abstracts_with_greedy_oracle_target_sentences"


class BaseOARelatedWork(Dataset, ConfigurableMixin, ABC):
    """
    Abstract base class for OARelatedWork datasets.
    """

    path: str = ConfigurableValue(desc="Path to the dataset.", transform=RelativePathTransformer())
    cache_dir: Optional[str] = ConfigurableValue("Path to cache directory.", user_default=None,
                                                 transform=RelativePathTransformer(allow_none=True),
                                                 voluntary=True)
    config_name: OARWConfig = ConfigurableValue(desc="Defining the name of the huggingface dataset configuration. "
                                                     "Available configurations are: "
                                                     f"{', '.join(f.name for f in OARWConfig)}",
                                                transform=EnumTransformer(OARWConfig))
    split: ToyValSplit = ConfigurableValue("Which dataset split should be used. Available formats are: "
                                           f"{', '.join(f.name for f in ToyValSplit)}",
                                           transform=EnumTransformer(ToyValSplit))

    mask_formulas_in_references: Optional[str] = ConfigurableValue(
        "You can choose string that will be used to mask formulas in referenced documents. "
        "If None, formulas will not be masked . "
        "If empty string, formulas will be removed.",
        user_default=None,
        validator=AnyValidator([IsNoneValidator(), StringValidator()]),
        voluntary=True)

    mask_formulas: Optional[str] = ConfigurableValue(
        "You can choose string that will be used to mask formulas in target summary. "
        "If None, formulas will not be masked . "
        "If empty string, formulas will be removed.",
        user_default="<eq>",
        validator=AnyValidator([IsNoneValidator(), StringValidator()]),
        voluntary=True)

    use_title_in_query: bool = ConfigurableValue("If True, the title of the paper will be used in a query. ",
                                                 user_default=True)
    use_abstract_in_query: bool = ConfigurableValue("If True, the abstract of the paper will be used in a query. ",
                                                    user_default=True)
    use_rest_of_paper_in_query: bool = ConfigurableValue(
        "If True, the rest of the paper (content without abstract and RW) will be used in a query.",
        user_default=False)

    put_rest_of_paper_in_input: bool = ConfigurableValue(
        "If True, the rest of the paper (content without abstract and RW) will be used in an input.",
        user_default=False)

    include_abstract_in_rest_of_paper: bool = ConfigurableValue(
        "If True, the abstract of the paper will be used in a target. Rest of paper will include also abstract.",
        user_default=False)

    put_target_abstract_in_input: bool = ConfigurableValue(
        "If True, the abstract of target paper will be used in an input.",
        user_default=False, voluntary=True)

    add_unk_cit_to_input: bool = ConfigurableValue("If True, the related work citations with UNK document id will be"
                                                   "added into input with bibliography data.",
                                                   user_default=True)

    toy_val_split_size: int = ConfigurableValue("Size of the toy validation split. It will select for n samples.",
                                                user_default=50, validator=lambda x: x > 0, voluntary=True)

    def __post_init__(self):
        self.raw_dataset = load_dataset(self.path, self.config_name.value, cache_dir=self.cache_dir)
        if self.split == ToyValSplit.VALIDATION_TOY:
            # we will use subset of validation set
            self.raw_dataset = self.raw_dataset[ToyValSplit.VALIDATION.value].select(range(self.toy_val_split_size))
        else:
            self.raw_dataset = self.raw_dataset[self.split.value]

    def __len__(self):
        return len(self.raw_dataset)

    @staticmethod
    def flatten_paragraph(paragraph: Sequence[Dict], mask_formulas: Optional[str] = None) \
            -> List[Tuple[List[Optional[str]], TextContentWithCitations]]:
        """
        Flattens the paragraph to a list of text headline paths and contents with citations.

        :param paragraph: Paragraph to flatten.
        :param mask_formulas: If not None, formulas will be masked with this string.
        :return: List of text headline paths and contents with citations that could be used to create
            a structured document.
        """
        flattened = []
        for t_c_dir in paragraph:
            text = t_c_dir["text"]
            if t_c_dir["title_path"][-1] == "formula":
                if mask_formulas is None:
                    text = "$$" + text + "$$"
                else:
                    text = mask_formulas
            text_content = TextContentWithCitations(
                text=text,
                citations=[RefSpan(x["index"], x["start"], x["end"]) for x in t_c_dir["citations"]],
                references=[RefSpan(x["index"], x["start"], x["end"]) for x in t_c_dir["references"]]
            )
            flattened.append((t_c_dir["title_path"], text_content))

        return flattened

    @classmethod
    def convert_paragraphs(cls, paragraphs: Sequence[Sequence[Dict]],
                           mask_formulas: Optional[str] = None) -> ContentHierarchy:
        """
        Converts a list of paragraphs to a structured document.

        :param paragraphs: List of paragraphs to convert.
        :param mask_formulas: If not None, formulas will be masked with this string.
        :return: Structured document.
        """
        flattened = []
        for paragraph in paragraphs:
            flattened.extend(cls.flatten_paragraph(paragraph, mask_formulas))
        return ContentHierarchy.from_flattened(flattened)

    @classmethod
    def paragraphs_to_str(cls, paragraphs: Sequence[Sequence[Dict]], mask_formulas: Optional[str] = None) -> str:
        """
        Converts a list of paragraphs to a string.

        :param paragraphs: List of paragraphs to convert.
        :param mask_formulas: If not None, formulas will be masked with this string.
        :return: String representing given paragraphs.
        """
        return " ".join(tc.text for p in paragraphs for _, tc in cls.flatten_paragraph(p, mask_formulas))

    @classmethod
    def convert_sections(cls, sections: Sequence[Dict], mask_formulas: Optional[str] = None) -> ContentHierarchy:
        """
        Converts flattened sections to structured document.

        :param sections: Sections
            a section is a dictionary
            {
            "title_path": List[str],
            "paragraphs": List[paragraph]
            }
            paragraph is a list of text content and text content is a dictionary
            {
            "title_path": List[str],
            "text": str,
            "citations": List[span]
            "references": List[span]
            }

            span is a dictionary
            {
            "index": int,
            "start": int,
            "end": int
            }

        :param mask_formulas: String that will be used to mask formulas in referenced documents.
            If None, formulas will not be masked .
        :return: structured document representing the sections
        """

        flattened = []
        for s in sections:
            for p in s["paragraphs"]:
                flattened.extend(cls.flatten_paragraph(p, mask_formulas))

        return ContentHierarchy.from_flattened(flattened)

    @classmethod
    def sections_to_str(cls, sections: Sequence[Dict], mask_formulas: Optional[str] = None) -> str:
        """
        Converts flattened sections to string.

        :param sections: Sections
            a section is a dictionary
            {
            "title_path": List[str],
            "paragraphs": List[paragraph]
            }
            paragraph is a list of text content and text content is a dictionary
            {
            "title_path": List[str],
            "text": str,
            "citations": List[span]
            "references": List[span]
            }

            span is a dictionary
            {
            "index": int,
            "start": int,
            "end": int
            }

        :param mask_formulas: String that will be used to mask formulas in referenced documents.
            If None, formulas will not be masked .
        :return: string representing the sections
        """
        flattened = itertools.chain.from_iterable(
            [cls.flatten_paragraph(p, mask_formulas) for s in sections for p in s["paragraphs"]]
        )
        return " ".join(tc.text for _, tc in flattened)

    @classmethod
    def stub_doc_2_str(cls, stub_doc: StructuredDocument) -> str:
        """
        Converts a stub document to string.

        :param stub_doc: Stub document.
        :return: String representing the stub document.
        """

        return f"{stub_doc.title}\n{', '.join(stub_doc.authors)}\n"

    @classmethod
    def make_stub_docs_from_hierarchy(cls, hierarchy: ContentHierarchy, bib_entries: List[BibEntry]) \
            -> List[StructuredDocument]:
        """
        Creates a stub documents from unknown citations, those that are matched with bib entry but not with a document
        id.

        :param hierarchy: Content hierarchy.
        :param bib_entries: Bib entries.
        :return: Content hierarchy with stub document.
        """

        return cls.make_stub_doc_from_unk_cite([cit.index for cit in hierarchy.citation_spans()], bib_entries)

    @classmethod
    def make_stub_docs_from_list_of_sections(cls, sections: Sequence[
        Dict["str", Union[Sequence[str], Sequence[Sequence[Dict]]]]],
                                             bib_entries: List[BibEntry]) -> List[StructuredDocument]:
        """
        Creates a stub documents from unknown citations, those that are matched with bib entry but not with a document
        id.

        :param sections: sections in which the citations are
        :param bib_entries: Bib entries.
        :return: Content hierarchy with stub document.
        """
        bib_indices = []
        for section in sections:
            for paragraph in section["paragraphs"]:
                for tc in paragraph:
                    for c in tc["citations"]:
                        bib_indices.append(c["index"])

        return cls.make_stub_doc_from_unk_cite(bib_indices, bib_entries)

    @classmethod
    def make_stub_doc_from_unk_cite(cls, bib_indices: List[Optional[int]], bib_entries: List[BibEntry]) \
            -> List[StructuredDocument]:
        """
        Creates a stub document from unknown citations, those that are matched with bib entry but not with a document
        id.

        :param bib_indices: indices of bib entries that should be used as candidates for stub documents
            it will check that the id is not None, and it will create just one stub document for each index
        :param bib_entries: Bib entries.
        :return: Content hierarchy with stub document.
        """
        seen_indices = set()
        docs = []
        for i in bib_indices:
            if i is not None and i not in seen_indices:
                seen_indices.add(i)
                bib_entry = bib_entries[i]
                if bib_entry.id is None:
                    # add this as partial input

                    docs.append(StructuredDocument.from_dict({
                        "id": -1,
                        "mag_id": None,
                        "doi": None,
                        "title": bib_entry.title,
                        "authors": bib_entry.authors,
                        "year": bib_entry.year,
                        "fields_of_study": [],
                        "citations": [],
                        "hierarchy": None,
                        "bibliography": [],
                        "non_plaintext_content": []
                    }))

        return docs

    def convert_doc(self, doc: Dict, allow_empty_hier: bool) -> StructuredDocument:
        """
        Converts raw doc to structured document.

        :param doc: Raw document.
        :param allow_empty_hier: If True, empty hierarchy will be allowed amd stub document will be created for this case.
        :return: structured document
        """
        target_abstract = None
        if self.include_abstract_in_rest_of_paper and "abstract" in doc and "related_work" in doc:
            # this is a target document and we want to include abstract in rest of paper
            target_abstract = self.convert_paragraphs(doc["abstract"], self.mask_formulas_in_references)
            # remove title as it will already be there
            target_abstract = target_abstract.content[0]

        if allow_empty_hier and not doc["hierarchy"]:
            # we have a stub document, this occurs when the document is pruned with greedy oracle
            if self.include_abstract_in_rest_of_paper and target_abstract is not None:
                # this is a target document and we want to include abstract in rest of paper
                return StructuredDocument.from_dict(doc, hierarchy=target_abstract)
            return StructuredDocument.from_dict(doc, hierarchy=None)
        else:
            hier = self.convert_sections(doc["hierarchy"], self.mask_formulas_in_references)
            if self.include_abstract_in_rest_of_paper and "abstract" in doc and "related_work" in doc:
                # this is a target document and we want to include abstract in rest of paper
                hier.content.insert(0, target_abstract)
            s_doc = StructuredDocument.from_dict(doc, hierarchy=hier)
            return s_doc


class OARelatedWork(BaseOARelatedWork, QueryBasedMultiDocumentSummarizationDataset):
    """
    Dataset for generation of related work like sections. The document structure is omitted (there are no headlines).

    Input: abstracts / whole content of referenced papers in summary
    Output: related work section of a scientific paper
    Query: title and abstract of an article from which the related work is taken
    """

    def convert_doc(self, doc: Dict, allow_empty_hier: bool) -> Tuple[StructuredDocument, str]:
        """
        Converts raw doc to structured document and stringified version of it.

        :param doc: Raw document.
        :return: Tuple of structured document and stringified version of it.
        """
        s_doc = super().convert_doc(doc, allow_empty_hier)
        if s_doc.hierarchy is None:
            return s_doc, self.stub_doc_2_str(s_doc)

        return s_doc, StructDoc2Markdown.convert_section(s_doc, s_doc.hierarchy)

    def __getitem__(self, item: int) -> QueryBasedMultiDocumentSummarizationSample:
        sample = self.raw_dataset[item]
        inputs = []
        inputs_doc = []
        oracle_configs = {OARWConfig.GREEDY_ORACLE_SENTENCES, OARWConfig.GREEDY_ORACLE_PARAGRAPHS,
                          OARWConfig.GREEDY_ORACLE_PER_INPUT_DOC_SENTENCES,
                          OARWConfig.GREEDY_ORACLE_PER_INPUT_DOC_PARAGRAPHS}

        if self.put_rest_of_paper_in_input or self.put_target_abstract_in_input:
            if self.config_name == OARWConfig.ABSTRACTS or self.put_target_abstract_in_input:
                inputs.append(self.paragraphs_to_str(sample["abstract"], self.mask_formulas_in_references))
                inputs_doc.append(
                    StructuredDocument.from_dict(sample,
                                                 hierarchy=self.convert_paragraphs(sample["abstract"],
                                                                                   self.mask_formulas_in_references)))
            if self.put_rest_of_paper_in_input and self.config_name != OARWConfig.ABSTRACTS:
                s_doc, stringified = self.convert_doc(sample,
                                                      allow_empty_hier=self.config_name in oracle_configs or
                                                                       self.config_name == OARWConfig.ABSTRACTS_WITH_GREEDY_ORACLE_TARGET_SENTENCES)
                inputs.append(stringified)
                inputs_doc.append(s_doc)

        if self.config_name in ({OARWConfig.FLATTENED_SECTIONS} | oracle_configs):
            for d in sample["referenced"]:
                s_doc, stringified = self.convert_doc(d, allow_empty_hier=self.config_name in oracle_configs)
                inputs.append(stringified)
                inputs_doc.append(s_doc)

        elif self.config_name in {OARWConfig.ABSTRACTS, OARWConfig.ABSTRACTS_WITH_GREEDY_ORACLE_TARGET_SENTENCES}:
            for d in sample["referenced"]:
                inputs.append(self.paragraphs_to_str(d["hierarchy"], self.mask_formulas_in_references))
                inputs_doc.append(StructuredDocument.from_dict(d,
                                                               hierarchy=self.convert_paragraphs(d["hierarchy"],
                                                                                                 self.mask_formulas_in_references)))

        else:
            NotImplementedError("Not implemented config branch.")

        query = []
        if self.use_title_in_query:
            query.append(sample["title"])

        if self.use_abstract_in_query:
            query.append(self.paragraphs_to_str(sample["abstract"], self.mask_formulas_in_references))

        if self.use_rest_of_paper_in_query:
            _, stringified = self.convert_doc(sample, allow_empty_hier=True)
            query.append(stringified)

        if self.add_unk_cit_to_input:
            bib_entries = [BibEntry.from_dict(bib_entry) for bib_entry in sample["bibliography"]]
            act_docs = self.make_stub_docs_from_list_of_sections(sample["related_work"], bib_entries)
            inputs.extend(
                self.stub_doc_2_str(d) for d in act_docs
            )
            inputs_doc.extend(act_docs)

        summary = self.convert_sections(sample["related_work"],
                                        self.mask_formulas)  # no need for .content[0] as related work omits the upper lvl hierarchy
        summary.parent = None
        summary.headline = None

        s_doc = StructuredDocument.from_dict(sample, hierarchy=summary)
        summary = StructDoc2Markdown.convert_section(s_doc, s_doc.hierarchy)

        return QueryBasedMultiDocumentSummarizationSample(sample_id=sample["id"],
                                                          inputs=inputs,
                                                          summary=summary,
                                                          inputs_metadata=[
                                                              {
                                                                  "id": i_doc.id,
                                                                  "title": i_doc.title,
                                                                  "first_author": i_doc.authors[0] if len(
                                                                      i_doc.authors) > 0 else None,
                                                                  "authors": i_doc.authors
                                                              } for i_doc in inputs_doc
                                                          ],
                                                          query=query)


class StructuredOARelatedWork(BaseOARelatedWork, QueryBasedMultiStructuredDocumentSummarizationDataset):
    """
    Dataset for generation of related work like sections.

    Input: abstracts / whole content of referenced papers in summary
    Output: related work section of a scientific paper
    Query: title and abstract of an article from which the related work is taken
    """

    def __getitem__(self, item: int) -> QueryBasedMultiStructuredDocumentSummarizationSample:
        sample = self.raw_dataset[item]
        inputs = []
        oracle_configs = {OARWConfig.GREEDY_ORACLE_SENTENCES, OARWConfig.GREEDY_ORACLE_PARAGRAPHS,
                          OARWConfig.GREEDY_ORACLE_PER_INPUT_DOC_SENTENCES,
                          OARWConfig.GREEDY_ORACLE_PER_INPUT_DOC_PARAGRAPHS}

        if self.put_target_abstract_in_input:
            inputs.append(
                StructuredDocument.from_dict(
                    sample,
                    hierarchy=self.convert_paragraphs(sample["abstract"], self.mask_formulas_in_references)
                )
            )

        if self.put_rest_of_paper_in_input:
            inputs.append(self.convert_doc(sample, allow_empty_hier=self.config_name in oracle_configs or
                                                                    self.config_name == OARWConfig.ABSTRACTS_WITH_GREEDY_ORACLE_TARGET_SENTENCES))

        if self.config_name in ({OARWConfig.FLATTENED_SECTIONS} | oracle_configs):
            for d in sample["referenced"]:
                inputs.append(self.convert_doc(d, allow_empty_hier=self.config_name in oracle_configs))
        elif self.config_name in {OARWConfig.ABSTRACTS, OARWConfig.ABSTRACTS_WITH_GREEDY_ORACLE_TARGET_SENTENCES}:
            for d in sample["referenced"]:
                s_doc = StructuredDocument.from_dict(d,
                                                     hierarchy=self.convert_paragraphs(d["hierarchy"],
                                                                                       self.mask_formulas_in_references))
                inputs.append(s_doc)
        else:
            NotImplementedError("Not implemented config branch.")

        query = []
        if self.use_title_in_query:
            query.append(sample["title"])

        if self.use_abstract_in_query:
            query.append(self.paragraphs_to_str(sample["abstract"], self.mask_formulas_in_references))

        if self.use_rest_of_paper_in_query:
            query.append(self.convert_doc(sample, allow_empty_hier=True))

        # remove the top lvl hierarchy from related work
        summary = self.convert_sections(sample["related_work"],
                                        self.mask_formulas)  # no need for .content[0] as related work omits the upper lvl hierarchy
        summary.parent = None
        summary.headline = None

        s_doc = StructuredDocument.from_dict(sample, hierarchy=summary)

        if self.add_unk_cit_to_input:
            act_docs = self.make_stub_docs_from_hierarchy(s_doc.hierarchy, s_doc.bibliography)
            inputs.extend(act_docs)

        return QueryBasedMultiStructuredDocumentSummarizationSample(sample_id=sample["id"],
                                                                    inputs=inputs,
                                                                    summary=s_doc,
                                                                    query=query,
                                                                    inputs_metadata=[
                                                                        {
                                                                            "id": i_doc.id,
                                                                            "title": i_doc.title,
                                                                            "first_author": i_doc.authors[0] if len(
                                                                                i_doc.authors) > 0 else None,
                                                                            "authors": i_doc.authors
                                                                        } for i_doc in inputs
                                                                    ])
