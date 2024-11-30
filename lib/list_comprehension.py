#!/usr/bin/env python3

def return_evens(num_list):
    even = [x for x in num_list if x % 2 == 0]
    return even

def make_exclamation(sentence_list):
    string =  [y + "!" for y in sentence_list]
    return string