#!/bin/python3
"""
https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking&h_r=next-challenge&h_v=zen
"""
import math
import os
import random
import re
import sys

def p(c):
   for yy in c:
      print(yy)

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    palabras=words.split(';')
    y = len(crossword)
    x = len(crossword[0])
    
    libres = []
    pos = []
    for i in palabras:
      pos.append([0,0,'x',1])

    cruces = []
    sig=0
    j=0
    while j < y:
        i=0
        while i < x:
            if ( 
                 crossword[j][i] == '-' 
                 or (i+1 < x and crossword[j][i] == 'v' and crossword[j][i+1] == '-')
                 or (j+1 < y and crossword[j][i] == 'h' and crossword[j+1][i] == '-')
               ):
                  if crossword[j][i] != '-':
                     cruces.append([sig,i,j])
                  crossword[j] = crossword[j][:i] + "i" + crossword[j][i + 1:]
                  pos[sig][0]=i
                  pos[sig][1]=j
                  sig += 1
                  ii = i+1
                  jj = j+1
                  while ii < x and (crossword[j][ii] == '-' or crossword[j][ii] == 'v'):
                     pos[sig-1][2]='h'
                     pos[sig-1][3]+=1
                     if crossword[j][ii] == 'v':
                        crossword[j] = crossword[j][:ii] + "x" + crossword[j][ii + 1:]
                        cruces.append([sig-1,ii,j])
                     else:
                        crossword[j] = crossword[j][:ii] + "h" + crossword[j][ii + 1:]
                     ii += 1
                  while jj < y and (crossword[jj][i] == '-' or crossword[jj][i] == 'h'):
                     pos[sig-1][2]='v'
                     pos[sig-1][3]+=1
                     if crossword[jj][i] == 'h':
                        crossword[jj] = crossword[jj][:i] + "x" + crossword[jj][i + 1:]
                        cruces.append([sig-1,i,jj])
                     else:
                        crossword[jj] = crossword[jj][:i] + "v" + crossword[jj][i + 1:]
                     jj += 1
            i += 1
        j += 1
    
    for p1 in pos:
       posibles = []
       for pal in palabras:
          if len(pal) == p1[3]:
             posibles.append(pal)
       p1.append(posibles)
    
    for c in cruces:
       i = 0
       while i < len(pos):
           if pos[i][2] == 'h':
              if pos[i][0] <= c[1] and pos[i][0] + pos[i][3] >= c[1] and pos[i][1] == c[2]:
                 break;
           if pos[i][2] == 'v':
              if pos[i][1] <= c[2] and pos[i][1] + pos[i][3] >= c[2] and pos[i][0] == c[1]:
                 break;
           i += 1
       letra1 = abs(c[1] - pos[i][0] + c[2] - pos[i][1])
       letra2 = abs(pos[c[0]][0] - c[1] + pos[c[0]][1] - c[2])
       p1 = ""
       p2 = ""
       for pal1 in pos[i][4]:
          for pal2 in pos[c[0]][4]:
              if pal1[letra1] == pal2[letra2]:
                  p1 = pal1
                  p2 = pal2
                  break
       pos[i][4] = [p1]
       pos[c[0]][4] = [p2]

    for pal in pos:
       if pal[2] == 'h':
           crossword[pal[1]] = crossword[pal[1]][:pal[0]] + pal[4][0] + crossword[pal[1]][pal[0]+pal[3]:]
       else:
           i=0
           while i < pal[3]:
              crossword[pal[1]+i] = crossword[pal[1]+i][:pal[0]] + pal[4][0][i] + crossword[pal[1]+i][pal[0]+1:]
              i += 1

    return crossword

if __name__ == '__main__':
    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)
    p(result)
    #print(result)
