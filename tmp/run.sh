#! /bin/bash
python textgen.py
python finglish.py
python flex_maker.py
bison -d parser.y
flex tokenizer.flex
g++ lex.yy.c parser.tab.c -ll
./a.out finglish_story.txt > parser_output.txt
