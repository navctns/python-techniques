#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:06:45 2019

@author: naveen
"""

#shuffle a deck of cards
import random
def card(sign,num):
    cardstr=''
                                        
    cardstr+='________________________\n'
                                    
    #cardstr+='\n|\n|  {}          {}\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|_____________________'.format(sign,num)
    cardstr+=2*'|\n'+'  '+str(sign)+10*' '+str(num)+'\t'+'|\n'+11*('|'+3*'\t'+'|\n')
    cardstr+=" ________________________"
    return cardstr

#print(card("Hearts",1))
signs=['Hearts','Diamonds','Spades','Clovers']
value=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
#print(random.choice(signs))

"""
for i,j in zip(random.choice(signs),random.choice(value)):
    print(i,j)
for i,j in zip(signs,value):
    print(card(i,j))
"""
for i in signs:
    for j in value:
        #card(i,j)
        print(card(i,j))

while True:
    for i in range(40):
        print(card(random.choice(signs),random.choice(value)))
    ch=int(input("Shuffle again\n1.Yes\n2.No"))
    if ch==2:
        break      
     
    
