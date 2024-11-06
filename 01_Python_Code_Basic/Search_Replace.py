import re
pattern =r"fruiitts"
text1="My favourite fruiitts is manago. I like mango fruiitts a lot"
text2=re.sub(pattern,'fruits',text1)
print(text2)






