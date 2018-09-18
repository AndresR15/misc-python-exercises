# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:48:59 2018

@author: andres15
"""

print 'Hello World!'

salutations = 'Hello, Horld! Its me again.'

print salutations

hello_world_array = ["H", "e" , "l", "l", "o", ",", "W" , "o", "r", "l", "d", "!"]

prev_space_count = 1
post_space_count = 11

for x in hello_world_array:
    print '_' * prev_space_count + x + '_'*post_space_count 
    prev_space_count += 1
    post_space_count -= 1
