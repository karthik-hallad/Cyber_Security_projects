# Using deque from collections which has a better time complexity
import collections
import string
import os 
from wordlist import mylist

def caeser(st):
  final=[]
  csr=st.replace(" "," ")
  for i in range(1,26):  
    upper=collections.deque(string.ascii_uppercase)
    lower=collections.deque(string.ascii_lowercase)
    upper.rotate(i)
    lower.rotate(i)
    upper=''.join(upper)
    lower=''.join(lower)
    final.append(csr.translate(csr.maketrans(string.ascii_uppercase,upper)).translate(csr.maketrans(string.ascii_lowercase,lower)))
  caeser_breaker(final)

def caeser_breaker(final):
  for i in final:
    #print(i)
    for j in i.split(" "):
      if(j not in mylist):
        break;
      else:
        print(i);
        break;
          

st=input("Please Enter the text to be broken: \n")
print("The most probable combination is: ")
caeser(st)

