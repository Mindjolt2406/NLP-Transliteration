s = input()
t = "d = {"
while(s!="0"):
  print(s)
  if(s == ""):
    s = input()
    continue
  elif(s[0] == '#'):
    s = input()
    continue
  else:
    l = s.split(' ')
    t += "\""+l[0]+"\""+":"+l[2]+","
  
  s = input()

t += "}"
print(t)
