str1 = """%{
#include <iostream>
#include "parser.tab.h"
using namespace std;
#define YY_DECL extern "C" int yylex()

%}
%%


q|w|e|r|t|y|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|" "|"\\n"|"\\t" ;

"""
finglish_story = 'finglish_story.txt'
finglish_dict = 'finglish_dict.txt'
flex_file = 'tokenizer.flex'



if __name__ == '__main__':
	f = open(finglish_dict, 'r')
	dic = {} # the whole finglish dictionary
	text = [] # list of words in the story
	dic2 = {} # dictionary for words in the story
	str2 = ''
	for l in f:
		s = l.split()
		if len(s) == 2:
			dic[s[0]] = s[1]
	f.close()
	f = open(finglish_story, 'r')
	for l in f:
		text += l.split()
	f.close()
	text = list(set(text))
	for word in text:
		if word in dic:
			if not dic[word] in dic2:
				dic2[dic[word]] = []
			dic2[dic[word]].append(word)
	for x in dic2:
		xx = x.lower()
		if xx == 'int':
			xx = 'intt'
		ss = '|'.join(dic2[x]) + ' {\n\tyylval.' + xx.lower() + ' = strdup(yytext);\n\treturn ' + xx.upper() + ';\n}\n'
		str2 += ss
	f = open(flex_file, 'w')
	f.write(str1 + str2 + '%%')
	f.close()
