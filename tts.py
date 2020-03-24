# -*- coding: utf-8 -*-

import pyttsx

input_file_name = "final_story.txt"

engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice' , 'persian')
engine.setProperty('rate' , rate-100)

with open(input_file_name) as ip :
    for line in ip:
        engine.say(line.decode("utf-8"))



engine.runAndWait()
