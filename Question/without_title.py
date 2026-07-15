#WAP TO CONVERT A STRING TO TITLE CASE WITHOUT USING THE TITLE ()
s=input('enter the string')
L=[]
for i in s.split():
  L.append(i[0].upper()+i[1:].lower())
  print(" ".join(L))
