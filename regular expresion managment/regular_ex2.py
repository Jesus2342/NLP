import re 


pattern=re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
pattern2=re.compile(r"\d\d\d[-.]\d\d\d[.-]\d\d\d\d")  #It will match the . and the - 
pattern3=re.compile(r"[53]23[-.]\d\d\d[.-]\d\d\d\d")   #will take only the numbers that stats with 
                                #5 or 3 and then the digits 23 then .- 3 digits .- 4 digits

with open("data.txt", "r") as f:
    contents = f.read()

    matches = pattern3.finditer(contents)

    for match in matches:
        print(match)

