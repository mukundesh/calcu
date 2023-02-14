# calcu


[![pypi](https://img.shields.io/pypi/v/calcu.svg)](https://pypi.org/project/calcu/)
[![python](https://img.shields.io/pypi/pyversions/calcu.svg)](https://pypi.org/project/calcu/)
[![Build Status](https://github.com/mukundesh/calcu/actions/workflows/dev.yml/badge.svg)](https://github.com/mukundesh/calcu/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/mukundesh/calcu/branch/main/graphs/badge.svg)](https://codecov.io/github/mukundesh/calcu)



Please Ignore.


* Documentation: <https://mukundesh.github.io/calcu>
* GitHub: <https://github.com/mukundesh/calcu>
* PyPI: <https://pypi.org/project/calcu/>
* Free software: MIT


## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.






```mermaid
graph TD;
	buildOrder/table_[<div align=leg>buildOrder/table_</div><br/>input: 278<br/>output: 269] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 810<br/>output: 810];
	buildOrder/list_[<div align=leg>buildOrder/list_</div><br/>input: 306<br/>output: 306] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 810<br/>output: 810];
	buildOrder/manual_[<div align=leg>buildOrder/manual_</div><br/>input: 26<br/>output: 26] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 810<br/>output: 810];
	buildOrder/para_[<div align=leg>buildOrder/para_</div><br/>input: 209<br/>output: 209] --> buildTenure_[<div align=leg>buildTenure_</div><br/>input: 810<br/>output: 810];
	annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/table_;
	annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/list_;
	annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/manual_;
	annotateFirst_[<div align=leg>annotateFirst_</div><br/>input: 904<br/>output: 904] --> buildOrder/para_;
	doOcr_[<div align=leg>doOcr_</div><br/>input: 904<br/>output: 904] --> annotateFirst_;
	import/documents --> doOcr_;
	buildTenure_ --> export/data/schema;
	buildTenure_ --> export/data;
	buildTenure_ --> export/data/orders;
	click buildOrder/list_ href "https://github.com/orgpedia/cabsec/tree/main/flow/buildOrder/list_" "buildOrder/list_" _blank
	click buildOrder/para_ href "https://github.com/orgpedia/cabsec/tree/main/flow/buildOrder/para_" "buildOrder/para_" _blank
	click doOcr_ href "https://github.com/orgpedia/cabsec/tree/main/flow/doOcr_" "doOcr_" _blank
	click buildTenure_ "https://github.com/orgpedia/cabsec/tree/main/flow/buildTenure_" "buildTenure_";
	click annotateFirst_ "https://github.com/orgpedia/cabsec/tree/main/flow/annotateFirst_" "annotateFirst_";
	click buildOrder/table_ "https://github.com/orgpedia/cabsec/tree/main/flow/buildOrder/table_" "buildOrder/table_";
	click buildOrder/manual_ "https://github.com/orgpedia/cabsec/tree/main/flow/buildOrder/manual_" "buildOrder/manual_";
	click export/data/orders "https://github.com/orgpedia/cabsec/tree/main/export/data/orders" "export/data/orders";
	click export/data "https://github.com/orgpedia/cabsec/tree/main/export/data" "export/data";
	click export/data/schema "https://github.com/orgpedia/cabsec/tree/main/export/data/schema" "export/data/schema";
	click import/documents "https://github.com/orgpedia/cabsec/tree/main/import/documents" "import/documents";
```
