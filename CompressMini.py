import sys
def r(t,b="",B=0):
 for l in range(2,30):
  for p in range(len(t)-l):
   s=t[p:p+l]
   S=l*(t.count(s)-1)
   if S>B:b=s;B=S
 return b
def F(t):
 for c in range(32,127):
  C=chr(c)
  if C in"\"'\\":continue
  if C not in t:return C
def q(t):
 if "\n"in t:
  if not'"'in t:return'"""'+t+'"""'
  if not"'"in t:return"'''"+t+"'''"
 if not"'"in t:return"'"+t+"'"
 if not"\""in t:return"\""+t+"'"
 return repr(t)
T=t=sys.stdin.read();R = []
while 1:
 e=r(t)
 if e=="":break
 c=F(t)
 if c==None:break
 t=t.replace(e,c);R.append(c+e)
j=F("".join(R))
print(min(['s='+q(t)+'\nfor c in'+q(j.join(R[::-1]))+'.split("'+j+'"):s=s.replace(c[0],c[1:])\nprint s',"print "+(q(t)+".replace("+").replace(".join(q(r[0])+","+q(r[1:])for r in R)+")"),"print "+q(T)],key=len))
