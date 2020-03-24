#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import unicodedata

words = []
presence = {}
story_sentence = {}
out_file = open('final_story.txt' , 'w')
inp_file = open('persian_story.txt' , 'r')
i = 0
for line in inp_file:
    lw = re.split(r' ' , line)
    for word in lw:
        words.append(word)

    sentences = re.split(r'\.(?!\d)', line)
    for sentece in sentences:
        # print "here"
        story_sentence[i] = sentece
        sw = re.split(r' ' , sentece)
        for word in sw:
            if i in presence:
                presence[i].append(word)

            else :
                presence[i] = [word]
        i+= 1

for i in presence:
    presence[i] = list(set(presence[i]))

words = list(set(words))


similarity = {}
for i  in presence:
    for j in presence:
        for word in presence[i]:
            if word in presence[j]:
                if (i,j) in similarity:
                    similarity[(i,j)] += 1
                else :
                    similarity[(i,j)] = 1

out_file.write(story_sentence[0] + '.')

last_index = 0
max_sim = -1100
max_index = -1
del presence[last_index]

while presence :
    for i  in presence:
        if similarity[(last_index , i)] > max_sim:
            max_sim = similarity[(last_index , i)]
            max_index = i

    #print max_index
    out_file.write(story_sentence[max_index] +'.')
    last_index = max_index
    print last_index
    max_sim = -100
    max_index = -1
    del presence[last_index]
