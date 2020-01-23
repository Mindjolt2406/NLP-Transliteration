#If there's a space, treat it like an a, if there is no vowel

# Basic characters

#Matras
# an = chr(2362)
#The chandra bindu
nn = chr(2305) 
NK = chr(2306)
NHa = chr(2307) 
aa = chr(2366)
# i goes on the left (unlike everything else) 
i = chr(2367) 
ee = chr(2368)
ou = chr(2369)
oou = chr(2370)
re = chr(2371)
oh = chr(2379)
ao = chr(2380)
ae = chr(2375)
ey = chr(2376)
NN = chr(2364)
tr = chr(2371)

#Vowels 
Ah = chr(2309)
Aa = chr(2310)
I = chr(2311) 
Ee = chr(2312)
Ou = chr(2313)
Oou = chr(2314)
Tr = chr(2315)
Ay = chr(2319)
Ey = chr(2320)
Oh = chr(2323)
Ao = chr(2324)
Ank = Ah+NK
Aha = Ah+NHa
#Getter a better thing for this
Em = Ay+nn 

half = chr(2381)

# #Consonants
ka = chr(2325)
Kha = chr(2326)
ga = chr(2327)
Gha = chr(2328)
rda = chr(2329)

cha = chr(2330)
Chha = chr(2331)
ja = chr(2332)
Jha = chr(2333)
Nya = chr(2334)

tTa = chr(2335)  #Careful
Ttha = chr(2336) #Careful
dDa = chr(2337)  #Careful
Ddha = chr(2338) #Careful
Rra = chr(2339)

tta = chr(2340)
Tha = chr(2341)
dda = chr(2342)
Dha = chr(2343)
na = chr(2344)

Nna = chr(2345)

pa = chr(2346)
Pha = chr(2347)
fa = Pha+NN
ba = chr(2348)
Bha = chr(2349)
ma = chr(2350)

ya = chr(2351)
ra = chr(2352)
Rna = chr(2353)
la = chr(2354)
Lna = chr(2355)
va = chr(2357)

sha = chr(2358)
sHha = chr(2359)
Sa = chr(2360)
ha = chr(2361)
KSha = ka+half+sHha
TRa = tta+half+ra
Gya = ja+half+Nya

# Parsing the text
# Store the halves separately 
# If something is a half, check the matra assosciated
# If the letter is 'a', then check if the next letter is a vowel

halves = {"k":chr(2325),"Kh":chr(2326),"g":chr(2327),"Gh":chr(2328),"rd":chr(2329),"ch":chr(2330),"Chh":chr(2331),"j":chr(2332),"Jh":chr(2333),"Ny":chr(2334),"tT":chr(2335),"Tth":chr(2336),"dD":chr(2337),"Ddh":chr(2338),"Rr":chr(2339),"tt":chr(2340),"Th":chr(2341),"dd":chr(2342),"Dh":chr(2343),"n":chr(2344),"Nn":chr(2345),"p":chr(2346),"Ph":chr(2347),"f":Pha+NN,"b":chr(2348),"Bh":chr(2349),"m":chr(2350),"y":chr(2351),"r":chr(2352),"Rn":chr(2353),"l":chr(2354),"Ln":chr(2355),"v":chr(2357),"sh":chr(2358),"sHh":chr(2359),"S":chr(2360),"h":chr(2361),"KSh":ka+half+sHha,"TR":tta+half+ra,"Gy":ja+half+Nya}
cap_vowel = {"Ah":chr(2309),"Aa":chr(2310),"I":chr(2311),"Ee":chr(2312),"Ou":chr(2313),"Oou":chr(2314),"Tr":chr(2315),"Ay":chr(2319),"Ey":chr(2320),"Oh":chr(2323),"Ao":chr(2324),"Ank":Ah+NK,"Aha":Ah+NHa,"Em":Ay+nn}
matra = {"nn":chr(2305),"NK":chr(2306),"NHa":chr(2307),"aa":chr(2366),"i":chr(2367),"ee":chr(2368),"ou":chr(2369),"oou":chr(2370),"re":chr(2371),"oh":chr(2379),"ao":chr(2380),"ae":chr(2375),"ey":chr(2376),"NN":chr(2364),"tr":chr(2371),"stop":chr(2404)}
vow = ['a','e','i','o','u']

def f(s):
    sentence = s.split(' ')
    ans = ""
    for word in sentence:
        word += " " #Just in case
        
        i = 0
        while(i<len(word)):
            
            phrase = ""
            hindi_phrase = ""
            add_half = False
            
            while(i<len(word)):
                if(word[i] == '.'):
                    ans += matra["stop"]
                    i+=1
                    break
                    
                if(i != len(word)-1 and ord(word[i]) not in range(ord('a'),ord('z')+1) and ord(word[i]) not in range(ord('A'),ord('Z')+1)):
                    ans += word[i]
                    i+=1
                    break
                    
                if(word[i] == 'h' and i == len(word)-2):
                    ans += halves["h"] + half
                    i+=1
                    break
                    
                phrase += word[i]
#                 print(i,phrase,hindi_phrase)
                if(phrase == 'a'):
                    if(word[i+1] in vow):
                        phrase = 'a'+word[i+1]
                        hindi_phrase += matra[phrase]
                        i+=1
                    i+=1
                    break
                if(phrase in cap_vowel):
                    hindi_phrase += cap_vowel[phrase]
                    i+=1
                    break
                elif(phrase in matra):
                    add_half = False
                    hindi_phrase += matra[phrase]
                    
                    i+=1
                    break
                    
                elif(phrase in halves):
                    if(add_half):
                        hindi_phrase += half
                    
                    hindi_phrase += halves[phrase]
                    phrase = ""
                    
                    add_half = True
                i+=1
            
            ans += hindi_phrase
                        
        ans += " "
    return ans

s = input("Enter the hinglish text in our tranliteration scheme\n")
print(f(s))







