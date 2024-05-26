import re

#python interpretation
#print("\tTab")

#raw string
#print(r"\tTab")

text_to_search=""   """"
213abcdefghABC

correo.gmail.com

Ha HaHa

321-555-4321
123.555.1234
"""


#Meta characters (need to be escaped)

#Escaped means to add \ before the meta character
#  r"\.""
# . ^ $ * + ? { } [ ] \ | ( )



pattern1= re.compile(r"abc")  #Patter specified. It will find only the pattern abc. Not Cap.
pattern2= re.compile(r"correo\.gmail.com")  #Patter specified  it will find correo.gmail.com. Heads up, is it necessary to add
                                            #"\" before (.)

pattern4= re.compile(r"\d") #return digits (0-9)  ; \D will match anything that is not a digitl

pattern5= re.compile(r"\w") #Word Character (a-z, A-Z, 0-9, _ (underscore)) ; \W- Not a Word Character

pattern6= re.compile(r"\s") # Whitespace (space, tab, newline) ; \S- Not Whitespace(space,tab, newline)

pattern7= re.compile(r"\bHa") #\b - Word boundary. In this case, our word is Ha. 

#Word boundary can be considered as a white space, in our example Ha HaHa. it will return the first Ha and then 
#the Ha next to the whitespace.  it will not match the last Ha, because there is not a word boundary before it. 
#if we want to find the last Ha, we can change the lower case b by cap B as showed in pattern 8

pattern8= re.compile(r"\BHa")


sentence= "Start a sentece and then bring it to and end"

pattern9= re.compile(r"^Start")  #it will match only if the first letter is Start, otherwirse it wont return anything.

pattern10= re.compile(r"end$")  # it will match only if the last pattern is end. 

##--------------Numbers------------

pattern11=re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")


matches=pattern11.finditer(text_to_search)
matches2=pattern9.finditer(sentence)

for match in matches:
    print(match)    #span returns the start and the end of the match
                    #As we can see, only this loops returns the number of times where the pattern was founded. 
                    #  Pattern_1--  it will no return, the number, the pattern in caps like ABC.


#print(text_to_search[4:7]) #Slicing strings  - Pattern 1
#print(text_to_search[18:34]) #Slicing strings   
