#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import openpyxl as xl
import re
import unicodedata

#read the excel
wb = xl.load_workbook(filename='Entries.xlsx')
ws = wb['Entries']


#the output file
finglish_dict = open('finglish_dictionary.txt' , 'w')
grammer_rules = open('grammer.txt' , 'w')
#the input file
input_file_name = 'persian_story.txt'

#the output file
output_file = open('finglish_story.txt' , 'w')


# the word mapping needed for persian letters
letters = {
u'ا':'',
u'آ':'a',
u'ئ':"a",
u'ء':"",
u'ب':"b",
u'پ':"p",
u'ت':"t",
u'ث':"s",
u'ج':"j",
u'چ':"ch",
u'ح':"h",
u'خ':"kh",
u'د':"d",
u'ذ':"z",
u'ر':"r",
u'ز':"z",
u'ژ':"zh",
u'س':"s",
u'ش':"sh",
u'ص':"s",
u'ض':"z",
u'ط':"t",
u'ظ':"z",
u'ع':"",
u'غ':"gh",
u'ف':"f",
u'ق':"gh",
u'ک':"k",
u'گ':"g",
u'ل':"l",
u'م':"m",
u'ن':"n",
u'و':'v',
u'ه':"h",
u'ی':'y',
u'ي':'y',
'@' : 'aa'
}

#to save the map
maping = {}
grammatic_usage = {}
check = u''
counter = 0
for row in ws.rows :
    rowEnt = []
    counter +=1
    if(counter > 41 ):
        for cell in row:
            rowEnt.append(cell.value)

        #pishvand haa va pasvand haa
        maping[(unicode)(rowEnt[1])] = (unicode)(rowEnt[0])
        maping[(unicode)(rowEnt[1]) + u'ها'] = (unicode)(rowEnt[0]) + 'ha'
        maping[(unicode)(rowEnt[1]) + u'های'] = (unicode)(rowEnt[0]) + 'haye'

        maping[(unicode)(rowEnt[1]) + u'ان'] = (unicode)(rowEnt[0]) + 'an'
        maping[(unicode)(rowEnt[1]) + u'اني'] = (unicode)(rowEnt[0]) + 'ani'

        maping[(unicode)(rowEnt[1]) + u'ات'] = (unicode)(rowEnt[0]) + 'at'
        maping[(unicode)(rowEnt[1]) + u'اتی'] = (unicode)(rowEnt[0]) + 'ati'

        maping[(unicode)(rowEnt[1]) + u'بند'] = (unicode)(rowEnt[0]) + 'band'

        maping[(unicode)(rowEnt[1]) + u'تر'] = (unicode)(rowEnt[0]) + 'tar'
        maping[(unicode)(rowEnt[1]) + u'ترین'] = (unicode)(rowEnt[0]) + 'tarin'

        maping[(unicode)(rowEnt[1]) + u'دان'] = (unicode)(rowEnt[0]) + 'dan'
        maping[(unicode)(rowEnt[1]) + u'دانان'] = (unicode)(rowEnt[0]) + 'danan'
        maping[(unicode)(rowEnt[1]) + u'دانانی'] = (unicode)(rowEnt[0]) + 'danani'

        maping[(unicode)(rowEnt[1]) + u'شناس'] = (unicode)(rowEnt[0]) + 'shenas'
        maping[(unicode)(rowEnt[1]) + u'شناسان'] = (unicode)(rowEnt[0]) + 'shenasan'
        maping[(unicode)(rowEnt[1]) + u'شناسانی'] = (unicode)(rowEnt[0]) + 'shenasani'

        maping[(unicode)(rowEnt[1]) + u'مند'] = (unicode)(rowEnt[0]) + 'mand'
        maping[(unicode)(rowEnt[1]) + u'مندان'] = (unicode)(rowEnt[0]) + 'mandan'
        maping[(unicode)(rowEnt[1]) + u'مندانی'] = (unicode)(rowEnt[0]) + 'mandani'


        maping[(unicode)(rowEnt[1]) + u'اند'] = (unicode)(rowEnt[0]) + 'and'
        maping[(unicode)(rowEnt[1]) + u'ند'] = (unicode)(rowEnt[0]) + 'and'
        maping[(unicode)(rowEnt[1]) + u'د'] = (unicode)(rowEnt[0]) + 'ad'
        maping[(unicode)(rowEnt[1]) + u'ن'] = (unicode)(rowEnt[0]) + 'an'
        maping[(unicode)(rowEnt[1]) + u'م'] = (unicode)(rowEnt[0]) + 'm'
        maping[(unicode)(rowEnt[1]) + u'ی'] = (unicode)(rowEnt[0]) + 'i'
        maping[(unicode)(rowEnt[1]) + u'یم'] = (unicode)(rowEnt[0]) + 'im'
        maping[(unicode)(rowEnt[1]) + u'ید'] = (unicode)(rowEnt[0]) + 'id'
        maping[(unicode)(rowEnt[1]) + u'ند'] = (unicode)(rowEnt[0]) + 'and'


        maping[  u'می' +(unicode)(rowEnt[1]) ] = 'mi' +(unicode)(rowEnt[0])



        maping[u'می'+(unicode)(rowEnt[1]) + u'اند'] = 'mi' + (unicode)(rowEnt[0]) + 'and'
        maping[u'می'+(unicode)(rowEnt[1]) + u'ند'] = 'mi' + (unicode)(rowEnt[0]) + 'and'
        maping[u'می'+(unicode)(rowEnt[1]) + u'م'] = 'mi' + (unicode)(rowEnt[0]) + 'm'
        maping[u'می'+(unicode)(rowEnt[1]) + u'ی'] = 'mi' + (unicode)(rowEnt[0]) + 'i'
        maping[u'می'+(unicode)(rowEnt[1]) + u'یم'] = 'mi' + (unicode)(rowEnt[0]) + 'im'
        maping[u'می'+(unicode)(rowEnt[1]) + u'ید'] = 'mi' + (unicode)(rowEnt[0]) + 'id'



        temp = u'نمی' +(unicode)(rowEnt[1])
        maping[ temp ] = 'nemi' +(unicode)(rowEnt[0])

        maping[(unicode)(temp) + u'اند'] = 'nemi' + (unicode)(rowEnt[0]) + 'and'
        maping[(unicode)(temp) + u'ند'] = 'nemi' + (unicode)(rowEnt[0]) + 'and'
        maping[(unicode)(temp) + u'م'] = 'nemi' + (unicode)(rowEnt[0]) + 'm'
        maping[(unicode)(temp) + u'ی'] = 'nemi' + (unicode)(rowEnt[0]) + 'i'
        maping[(unicode)(temp) + u'یم'] = 'nemi' + (unicode)(rowEnt[0]) + 'im'
        maping[(unicode)(temp) + u'ید'] = 'nemi' + (unicode)(rowEnt[0]) + 'id'






def translate(s):

    if s ==u'در':
        return ["dar" , 1]

    if s == u'و':
        return ['va' , 1]

    if s == u'.':
        return ['.' , 1]

    if s == u',':
        return [',' , 1]


    res = ""
    a = 0
    if s in maping:
        a = 1
        for char in maping[s]:
            if char in letters:
                res += letters[char]
            elif char != '^' :
                if char != ' ':
                    res += char
    else:
         res = s
    return [res , a]





# #translate the dictionary
# with open('UPC-2016.txt') as fp :
#     inp = []
#     role = ""
#     for line in fp:
#         inp = line.split()
#         res = ''
#         if len(inp) > 1 :
#             res = inp[0]
#             role = inp[1]
#             grammer_rules.write(role + ' ')
#             if role == "DELM":
#                 grammer_rules.write('\n')
#
#
#             sentence = inp[0].decode('utf-8')
#             sentence = sentence.replace(u'\u200c' , '')
#
#
#         grammatic_usage[translate(sentence)[0]] = role
#
#         if translate(sentence)[1]:
#             finglish_dict.write(translate(sentence)[0] + " " + role + "\n")
#
# finglish_dict.write("unknown" + ' ' + 'unknown' + '\n')
#
#



#translate the input
with open(input_file_name) as ip :
    inp = []

    for line in ip:
        inp = line.split()
        for kalame in inp:

            kalame = kalame.decode('utf-8')
            kalame = kalame.replace(u'\u200c' , '' )

            # if kalame == '.':
            #     output_file.write('\n')
            if translate(kalame)[1]:
                output_file.write(translate(kalame)[0] + ' ')
                
            else :

                res = ''
                for harf in kalame:
                    if harf in letters:
                        res += letters[harf]

                output_file.write(res + ' ')

        output_file.write("\n")
