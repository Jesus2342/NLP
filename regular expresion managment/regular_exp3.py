import re 

text_to_search=""   """"
213abcdefghABC

correo.gmail.com

Ha HaHa

321-555-4321
123.555.1234
342-342-1233
786-653-2525


cat 
mat 
pat 
bat

Mr. Schaler
Mr Smith 
Mr. T
Ms Davis 
Mrs. Robinson
"""

pattern=re.compile(r"[1-5]")   #It will retrive digits between 1 and 5
pattern2=re.compile(r"[a-z]")  #It will retrive letters between a and z
pattern3=re.compile(r"[a-zA-Z]") #It will retrive letters between a and z. Also between A and Z
pattern4=re.compile(r"[^a-zA-Z]") #It will retrive any letters between a and z. Also between A and Z
pattern5=re.compile(r"[^b]at")

pattern6=re.compile(r"\d{3}.\d{3}.\d{4}")
pattern7=re.compile(r"Mr\.?\s[A-Z]\w*")

#.? hace opcional el punto. 

pattern8=re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")

matches=pattern8.finditer(text_to_search)

for match in matches:
        print(match)