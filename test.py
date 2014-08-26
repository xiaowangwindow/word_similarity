# -*- encoding: utf-8 -*-
import glossary
import random
import getsim
i=0
word1=''
word2=''
while i<1000:
    value1 = random.randint(1, 53309)
    value2 = random.randint(1, 53309)
    count = 0
    for key,value in glossary.words.items():
        count += 1
        if count == value1:
            word1 = key
        if count == value2:
            word2 = key
    i += 1
    print i
    print word1
    print word2
    print getsim.get_sim(word1, word2)

