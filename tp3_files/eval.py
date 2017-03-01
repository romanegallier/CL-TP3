#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import random
import fileinput
    
listtags=['(',')','$','#','CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','MD','NN','NNP','NNPS','NNS','PDT','POS','PRP','PRP$','PUNCT','RB','RBR','RBS','RP','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']
linecpt=0
nbrranomdtags=len(listtags)
ref=open(sys.argv[1])
hyp=open(sys.argv[2])
classref=[];
classrandom=[];
classhyp=[];
nbrtagref={};
nbrtaghyp={};
nbrtagok={};
for tag in listtags:
    nbrtagref[tag]=0
    nbrtaghyp[tag]=0
    nbrtagok[tag]=0
for line in ref:
    line=line.strip()
    tabline=line.split(' ')
    tagcpt=0
    lineref = []
    for tag in tabline:
        lineref.append(tag)
        #classref[linecpt][tagcpt]=
        if tag in nbrtagref.keys():
            nbrtagref[tag]=nbrtagref[tag]+1
        else:
            nbrtagref[tag]=1
        tagcpt=tagcpt+1
    classref.append(lineref)
    linecpt=linecpt+1
linemax=linecpt
linecpt=0
for line in hyp:
    line=line.strip()
    tabline=line.split(' ')
    tagcpt=0
    linehyp = []
    linerandom = []
    for tag in tabline:
        linehyp.append(tag)
        #tag=listtags[random.randint(0,nbrranomdtags)-1]
        linerandom.append(tag)
        if tag == classref[linecpt][tagcpt]:
            if tag in nbrtagok.keys():
                nbrtagok[tag]=nbrtagok[tag]+1
            else:
                nbrtagok[tag]=1
        tagcpt=tagcpt+1
        if tag in nbrtaghyp.keys():
            nbrtaghyp[tag]=nbrtaghyp[tag]+1
        else:
            nbrtaghyp[tag]=1
    classhyp.append(linehyp)
    classrandom.append(linerandom)
    linecpt=linecpt+1

tagcpt=0
fullprecision=0
fullrecall=0
precision={}
recall={}
for tag in listtags:
    if nbrtaghyp[tag] != 0:
        precision[tag]=nbrtagok[tag]/nbrtaghyp[tag]
    else:
        precision[tag]=0
    if nbrtagref[tag] != 0:
        recall[tag]=nbrtagok[tag]/nbrtagref[tag]
    else:
        recall[tag]=0
    fullprecision=fullprecision+precision[tag]
    fullrecall=fullrecall+recall[tag]
    tagcpt=tagcpt+1
    print("Precision "+tag+": "+str(100*precision[tag]))
    print("Recall    "+tag+": "+str(100*recall[tag]))
fullprecision=fullprecision/tagcpt
fullrecall=fullrecall/tagcpt

print("Precision: "+str(100*fullprecision))
print("Recall   : "+str(100*fullrecall))



