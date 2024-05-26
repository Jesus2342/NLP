import re
sentence= "Start a sentece and then bring it to and end"

pattern = re.compile(r"Start")

pattern2= re.compile(r"then")

pattern3 = re.compile(r"start", re.IGNORECASE)  #with this flag, we can ignore if the litter is cap or not

matches=pattern.match(sentence)  #Match only return an object, not a list.
            #Will return a value only if the string matches with the the string of the sentece



matches2= pattern2.search(sentence) #if you want to look the string in the entire pattern, 
                                    #it´s necessary to use method search


matches3= pattern3.search(sentence)  

print(matches3)