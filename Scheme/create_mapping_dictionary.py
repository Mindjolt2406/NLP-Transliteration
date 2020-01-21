s = input()
t = "halves = {"
while(s!="0"):
  if(s == ""):
    s = input()
    continue
  elif(s[0] == '#'):
    s = input()
    continue
  else:
    l = s.split(' ')
    t += "\""+l[0][:-1]+"\""+":"+l[2]+","
  
  s = input()

t += "}"
print(t)
