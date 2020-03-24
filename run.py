#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

#commands
textGenCommand = "python textgen.py"
finglishCommand = "python finglish.py"
flexMakerCommand = "python flex_maker.py"
bisonCommand = "bison -d parser.y"
flexCommand = "flex tokenizer.flex"
alignmentCommand = "python alignment.py"
normalizerCommand = "python normalizer.py"
cppCommand = "g++ lex.yy.c parser.tab.c -ll"
parserRunCommand = "./a.out finglish_story.txt > parser_output.txt"
tts_command = 'python tts.py'


#create the text and the flex file
os.system(textGenCommand)
os.system(finglishCommand)
os.system(flexMakerCommand)
os.system(bisonCommand)
os.system(flexCommand)
os.system(cppCommand)
os.system(alignmentCommand)
os.system(normalizerCommand)
print "done"

parsed_story = open('parsed_story.txt' , 'w')

##uncomment for using the parser
#===========================================================================

#give the text line by line
# story = open('persian_story.txt' , 'r')
# for line in story:
#     sentences = re.split(r'\.(?!\d)', line)
#
#     for sentece in sentences :
#         os.system('rm -rf persian_story.txt')
#         tempOut = open("persian_story.txt" , 'w')
#         tempOut.write(sentece + ' .')
#         os.system(finglishCommand)
#         os.system(flexCommand)
#         os.system(parserRunCommand)
#         pars_res = open("parser_output.txt" , 'r')
#         for pres in pars_res:
#             print pres
#             res = re.split(r' ' , pres)
#             if res[0] != 'Parse' :
#                 parsed_story.write(sentece)
#
#         pars_res.close()
#===========================================================================

os.system(tts_command)
