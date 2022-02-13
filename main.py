b='utf8'
a='usernames.txt'
Z=' '
Y=range
X=int
W=input
N=''
M=open
J='\n'
A=print
from os import name
import requests as O
from bs4 import BeautifulSoup
import json,sys,random as P,colorama as Q
from colorama import Fore as C,Back,Style
Q.init(autoreset=True)
A(C.CYAN+'Twitter Username Tool')
A(C.RED+'Made by vicious#1509')
A(Z)
R='abcdefghijklmaopqrtuvwxyz'
D=W('Username Amount : ')
D=X(D)
E=W('Username Length : ')
E=X(E)
A(C.LIGHTMAGENTA_EX+'\n      Generated Usernames')
A(N)
F=M(a,'a')
for c in Y(D):
	G=N
	for B in Y(E):G+=P.choice(R)
	A(G);F.write(G+J)
F.write(J)
F.close()
A(J+C.MAGENTA+'       Checked Usernames')
A(N)
K=[]
H=[]
with M(a,'r',encoding=b)as I:
	for S in I:K.append(S.strip())
for B in K:
	T='https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22'+B+'%22%2C%22withHighlightedLabel%22%3Atrue%7D';U={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9,bn;q=0.8','authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA','content-type':'application/json','dnt':'1','origin':'https://twitter.com','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36','x-twitter-active-user':'yes','x-twitter-client-language':'en'};L=json.loads(O.get(T,headers=U).text)
	try:A(f"[31m{B}"+L['user']+'\x1b[0m')
	except:
		try:
			V=L['errors'][0]['message']
			if f"User '{B}' not found"==V:A(f"[0;31m{B} [Unavailable]");H.append(B)
			else:0
		except:A(f"[0;32m{B} [Available][0m");H.append(B)
with M('available.txt','w+',encoding=b)as I:
	for B in H:I.write(B+J)
A(Z)
A(C.LIGHTYELLOW_EX+'      Proccess Complete')