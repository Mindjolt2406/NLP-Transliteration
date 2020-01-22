s = input()
t = "cap_vowel = {"
while(s!="0"):
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
