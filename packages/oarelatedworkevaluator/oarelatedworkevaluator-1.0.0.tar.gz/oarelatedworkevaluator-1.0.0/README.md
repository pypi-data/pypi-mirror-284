# Evaluation
This folder contains evaluation scripts for experiments on OARelatedWork dataset.

## Install

    pip install oarelatedworkevaluator

## Usage

It can be run as:

    oarelatedworkevaluator toy_example/example.csv res.json

See help for more information.

## Format of related works

Each related work section is represented by following format.

Each headline is prefixed with appropriate number of `# ` according to its level and stands on own line. So, for example (## 2.2. Dependency treebank for other languages), is headline of the first level related work subsection that will be prefixed with `##`.

The headline (e.g., 2. Related work) of related work section itself is omitted.

Each paragraph is on its own line. Sentences are separated by space.

Formulas are masked with <eq>.

Citations have the following format:

    <cite>{'UNK' if bib_entry.id is None else bib_entry.id}<sep>{bib_entry.title}<sep>{first_author}</cite>

When citation has no bib_entry it is just:`<cite>UNK</cite>`. Similar if the first author is not known:`<cite>{'UNK' if bib_entry.id is None else bib_entry.id}<sep>{bib_entry.title}<sep>UNK</cite>`.

References use similar format as citations:

    <ref>type_of_ref_target</ref>

Thus, for figure it will be `<ref>figure</ref>`. When reference has unknown type it is just:`<ref>UNK</ref>`.

### Example

```
First paragraph of related work section.
## 2.1. headline of subsection
First sentence of first paragraph of subsection. Second sentence of first paragraph of subsection.
## 2.2. Graph Attention Networks
Recently, attention networks have achieved state-of-the-art results in many tasks <cite>4931429<sep>Show, attend and tell: Neural image caption generation with visual attention<sep>Kelvin Xu</cite>. By using learnable weights on each input, the attention mechanism determines how much attention to give to each input. GATs <cite>555880<sep>Graph attention networks<sep>Petar Veličković</cite> utilize an attention-based aggregator to generate attention coefficients over all neighbors of a node for feature aggregation. In particular, the aggregator function of GATs is
<eq>
Later, <cite>94675806<sep>How attentive are graph attention networks?<sep>Shaked Brody</cite> pointed out that ...
We also provide a comprehensive performance comparison in <ref>table</ref>.
```

## Format of results for evaluation
By default, it is expected that the results are stored as csv file with two fields **sample_id** and **summary** (you can also use **sequence** alias instead of **summary**). However, it is possible to use a different format with the --file_format argument.

There is also toy example results file `example.csv` in `toy_example` folder with oracle summary.
