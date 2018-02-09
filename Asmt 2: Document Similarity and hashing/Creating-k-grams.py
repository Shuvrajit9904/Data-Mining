#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 17:19:02 2018

@author: shuvrajit
"""

import sys


#doc1 = open('Text1.txt')
#doc2 = open('Text2.txt')
#doc3 = open('Text3.txt')
#doc4 = open('Text4.txt')

def charcBigram(filename):    

    with open(filename) as doc1:
        kgram = {}
        text = doc1.read()
        text_list = list(text.strip())
        for i in range(1, len(text_list)):
            gram = "".join([text_list[i-1],text_list[i]])
            if gram in kgram:
                kgram[gram] += 1
            else:
                kgram[gram] = 1
                
        #return len(kgram)
        return kgram
    
def charcTrigram(filename):    

    with open(filename) as doc1:
        kgram = {}
        text = doc1.read()
        text_list = list(text.strip())
        for i in range(2, len(text_list)):
            gram = "".join([text_list[i-2],text_list[i-1],text_list[i]])
            if gram in kgram:
                kgram[gram] += 1
            else:
                kgram[gram] = 1
        #return len(kgram)    
        return kgram

def wordBigram(filename):
    
    with open(filename) as doc1:
        kgram = {}
        text = doc1.read()
        text_list = text.strip().split()
        for i in range(1, len(text_list)):
            gram = ",".join([text_list[i-1],text_list[i]])
            if gram in kgram:
                kgram[gram] += 1
            else:
                kgram[gram] = 1
        #print(kgram)
        #return len(kgram)
        return kgram    
    
#1A
#How many distinct k-grams are there for each document with each type of k-gram?
#You should report 4 × 3 = 12 different numbers.

#Document1
print("Size of Character Based 2-gram for Document 1:", len(charcBigram('Text1.txt')))
print("Size of Character Based 3-gram for Document 1:", len(charcTrigram('Text1.txt')))
print("Size of Word Based 2-gram for Document 1:", len(wordBigram('Text1.txt')))
print('\n')
#Document2
print("Size of Character Based 2-gram for Document 2:", len(charcBigram('Text2.txt')))
print("Size of Character Based 3-gram for Document 2:", len(charcTrigram('Text2.txt')))
print("Size of Word Based 2-gram for Document 2:", len(wordBigram('Text2.txt')))
print('\n')
#Document3
print("Size of Character Based 2-gram for Document 3:", len(charcBigram('Text3.txt')))
print("Size of Character Based 3-gram for Document 3:", len(charcTrigram('Text3.txt')))
print("Size of Word Based 2-gram for Document 3:", len(wordBigram('Text3.txt')))
print('\n')
#Document4
print("Size of Character Based 2-gram for Document 4:", len(charcBigram('Text4.txt')))
print("Size of Character Based 3-gram for Document 4:", len(charcTrigram('Text4.txt')))
print("Size of Word Based 2-gram for Document 4:", len(wordBigram('Text4.txt')))
print('\n')

#1B
#Compute the Jaccard similarity between all pairs of documents 
#for each type of k-gram. You should report 3 × 6 = 18 different numbers.
def jaccardSim(dict1, dict2):
    numer = len(dict1.keys() & dict2.keys())
    denom = len(dict1.keys() | dict2.keys())
    return numer/denom


#Jacccard Similarity for Character Bigrams
print("Jaccard Similarity (Document1, Document2) for Charcter Bigram: "
      ,jaccardSim(charcBigram('Text1.txt'),charcBigram('Text2.txt')))
print("Jaccard Similarity (Document1, Document3) for Charcter Bigram: "
      ,jaccardSim(charcBigram('Text1.txt'),charcBigram('Text3.txt')))
print("Jaccard Similarity (Document1, Document4) for Charcter Bigram: "
      ,jaccardSim(charcBigram('Text1.txt'),charcBigram('Text4.txt')))
print("Jaccard Similarity (Document2, Document3) for Charcter Bigram: "
      ,jaccardSim(charcBigram('Text2.txt'),charcBigram('Text3.txt')))
print("Jaccard Similarity (Document2, Document4) for Charcter Bigram: "
      ,jaccardSim(charcBigram('Text2.txt'),charcBigram('Text4.txt')))
print("Jaccard Similarity (Document3, Document4) for Charcter Bigram: "
      ,jaccardSim(charcBigram('Text3.txt'),charcBigram('Text4.txt')))
print('\n')

#Jacccard Similarity for Character trigrams
print("Jaccard Similarity (Document1, Document2) for Charcter Bigram: "
      ,jaccardSim(charcTrigram('Text1.txt'),charcTrigram('Text2.txt')))
print("Jaccard Similarity (Document1, Document3) for Charcter Bigram: "
      ,jaccardSim(charcTrigram('Text1.txt'),charcTrigram('Text3.txt')))
print("Jaccard Similarity (Document1, Document4) for Charcter Bigram: "
      ,jaccardSim(charcTrigram('Text1.txt'),charcTrigram('Text4.txt')))
print("Jaccard Similarity (Document2, Document3) for Charcter Bigram: "
      ,jaccardSim(charcTrigram('Text2.txt'),charcTrigram('Text3.txt')))
print("Jaccard Similarity (Document2, Document4) for Charcter Bigram: "
      ,jaccardSim(charcTrigram('Text2.txt'),charcTrigram('Text4.txt')))
print("Jaccard Similarity (Document3, Document4) for Charcter Bigram: "
      ,jaccardSim(charcTrigram('Text3.txt'),charcTrigram('Text4.txt')))
print('\n')

#Jacccard Similarity for Character Bigrams
print("Jaccard Similarity (Document1, Document2) for Word Bigram: "
      ,jaccardSim(wordBigram('Text1.txt'),wordBigram('Text2.txt')))
print("Jaccard Similarity (Document1, Document3) for Word Bigram: "
      ,jaccardSim(wordBigram('Text1.txt'),wordBigram('Text3.txt')))
print("Jaccard Similarity (Document1, Document4) for Word Bigram: "
      ,jaccardSim(wordBigram('Text1.txt'),wordBigram('Text4.txt')))
print("Jaccard Similarity (Document2, Document3) for Word Bigram: "
      ,jaccardSim(wordBigram('Text2.txt'),wordBigram('Text3.txt')))
print("Jaccard Similarity (Document2, Document4) for Word Bigram: "
      ,jaccardSim(wordBigram('Text2.txt'),wordBigram('Text4.txt')))
print("Jaccard Similarity (Document3, Document4) for Word Bigram: "
      ,jaccardSim(wordBigram('Text3.txt'),wordBigram('Text4.txt')))
print('\n')

#print(charcTrigram('Text1.txt'))
#print(wordBigram('Text1.txt'))

