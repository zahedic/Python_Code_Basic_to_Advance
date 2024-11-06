import re
pattern=r"[A-Z][a-z][0-9]"

if re.match(pattern,'Aa2ggdd01242'):
    print('This is Match')
else:
    print('This is not Match')
