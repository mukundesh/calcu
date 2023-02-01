# buildOrder/table_

| Directory    | Files                          | Counts |
|--------------|--------------------------------|--------|
| input        | .pdf.annotfirst.json           |    275 |
| output       | .pdf.order.json                |    269 |
| intermediate | .pdf.orderdetails.json         |    269 |
| conf         | findnum[274], table_finder[13], tableorder[78], ordertagger[42], id_assigner[59] |    466 |

## Skipped Docs
0. [1_Upload_1990.pdf](/import/images/1_Upload_1990): buildOrder.yml Lot of dirty text,  two orders 1 of resignation and 1 of assumption, IMPORTANT - Rajiv Gandhi
1. [1_Upload_2686.pdf](/import/images/1_Upload_2686): buildOrder.yml Faded paper unable to read
2. [1_Upload_2811.pdf](/import/images/1_Upload_2811): buildOrder.yml Hindi Department
3. [1_Upload_2812.pdf](/import/images/1_Upload_2812): buildOrder.yml Hindi Department / English Department
4. [1_Upload_2910.pdf](/import/images/1_Upload_2910): buildOrder.yml Black scan, with lots of mistakes
5. [1_Upload_2431.pdf](/import/images/1_Upload_2431): buildOrder.yml Reversed Department followed by name

## Sub Tasks
There are 9 sub_tasks.

### num_marker
    Errors: 35 []
    Edits: 2415 [clearWords: 247, replaceStr: 1144, newWord: 670, newAdjWord: 31, mergeWords: 303, splitWord: 5, clearChar: 15]
    Conf: 274

### rotation_detector
    Errors: 0 []
    Edits: 0 []
    Conf: 0

### line_finder
    Errors: 0 []
    Edits: 0 []
    Conf: 0

### list_finder2
    Errors: 0 []
    Edits: 0 []
    Conf: 0

### table_finder
    Errors: 0 []
    Edits: 0 []
    Conf: 13

### table_order_builder
    Errors: 1007 []
    Edits: 28 [mergeWords: 11, clearWords: 2, replaceStr: 15]
    Conf: 78

### order_tagger
    Errors: 0 []
    Edits: 0 []
    Conf: 42

### id_assigner_vocab
    Errors: 0 []
    Edits: 0 []
    Conf: 59

### details_differ
    Errors: 0 []
    Edits: 0 []
    Conf: 0

