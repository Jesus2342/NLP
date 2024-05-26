import re
emails="""""

miemail@gmail.com
segundo.email@uni.edu
jesus-321@my-work.net
"""

urls= """""
https://www.google.com
http://corey.com
https://youtube.com
https://www.nasa.gov


"""


pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)")

pattern2= re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

#(www\.)?\w  el www es opcional,y puede aceptar cualquier valor con w

#w+\. aceptar cualquier caracter mayor a 1 hasta llegar al punto

#(\w+) domain google or youtube

#(\.\w+)" dot domain like .gov or .com



# "+" we want to match one or more of those all the way up until we hit the @ symbol
matches=pattern2.finditer(urls)

for match in matches:
        print(match)
