# Document Flow Diagram
This diagram is an auto-generated from directory structure of `flow` directory and links present in `input` and `output` sub-folders (tasks). Click the box (task) to explore more.

```mermaid
graph TD;
        buildOrder/table_[<div align=leg>buildOrder/table_</div><br/>input: 275<br/>output: 269] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 808<br/>output: 808];
        buildOrder/list_[<div align=leg>buildOrder/list_</div><br/>input: 306<br/>output: 306] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 808<br/>output: 808];
        buildOrder/manual_[<div align=leg>buildOrder/manual_</div><br/>input: 24<br/>output: 24] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 808<br/>output: 808];
        buildOrder/para_[<div align=leg>buildOrder/para_</div><br/>input: 209<br/>output: 209] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 808<br/>output: 808];
        annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/table_;
        annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/list_;
        annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/manual_;
        annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/para_;
        doOcr_[<div align=leg>doOcr_</div><br/>input: 904<br/>output: 904] --> annotateFirst_;
        import/docs --> doOcr_;
        buildTenure_ --> export/data/orders;
        buildTenure_ --> export/data;
        click buildTenure_ "https://github.com/orgpedia/cabsec2/tree/main/flow/buildTenure_" "buildTenure_";
        click annotateFirst_ "https://github.com/orgpedia/cabsec2/tree/main/flow/annotateFirst_" "annotateFirst_";
        click buildOrder/manual_ "https://github.com/orgpedia/cabsec2/tree/main/flow/buildOrder/manual_" "buildOrder/manual_";
        click buildOrder/list_ "https://github.com/orgpedia/cabsec2/tree/main/flow/buildOrder/list_" "buildOrder/list_";
        click buildOrder/para_ "https://github.com/orgpedia/cabsec2/tree/main/flow/buildOrder/para_" "buildOrder/para_";
        click buildOrder/table_ "https://github.com/orgpedia/cabsec2/tree/main/flow/buildOrder/table_" "buildOrder/table_";
        click doOcr_ "https://github.com/orgpedia/cabsec2/tree/main/flow/doOcr_" "doOcr_";
        click export/data "https://github.com/orgpedia/cabsec2/tree/main/export/data" "export/data";
        click export/data/orders "https://github.com/orgpedia/cabsec2/tree/main/export/data/orders" "export/data/orders";
        click import/docs "https://github.com/orgpedia/cabsec2/tree/main/import/docs" "import/docs";
```
## Unprocessed Documents: 93
### Ignored Documents:
  - [ignore/duplicates_](ignore/duplicates_): 11
  - [ignore/swearingin_](ignore/swearingin_): 63
  - [ignore/notRelevant_](ignore/notRelevant_): 6
  - [ignore/todo_](ignore/todo_): 3
  - [ignore/correction_](ignore/correction_): 4
### Skipped Documents:
  - [buildOrder/table_](buildOrder/table_): 6
