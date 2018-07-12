d={
"a":".-",
"b":"-...",
"c" :"-.-.",
"d" :"-..",
"e" :".",
"f" :"..-.",  
"g" :"--.",
"h" :"....",
"i" :"..",
"j" :".---",
"k" :"-.-",
"l" :".-..",
"m" :"--",    
"n" :"-.",
"o" :"---",
"p" :".--.",
"q" :"--.-",
"r" :".-.",
"s" :"...",
"t" :"-",
"u" :"..-",
"v" :"...-",
"w" :".--",
"x" :"-..-",
"y" :"-.--",
"z" :"--.." 
}

def getMorseCode(word):
    s=""
    for i in word:
        s=s+d.get(i)
    return s
def gendups(wordsList):
    dups={}
    for i in wordsList:
        temp=getMorseCode(i)
        if(temp in dups.keys()):
            dups[temp]+=1
        else:
            dups[temp]=1
    print("dict",dups)
    return len(dups.keys())
print(gendups(["gin", "zen", "gig", "msg"]))
print(gendups(["a", "z", "g", "m"]))
print(gendups(["bhi", "vsv", "sgh", "vbi"]))
print(gendups(["a", "b", "c", "d"]))
print(gendups(["hig", "sip", "pot"]))