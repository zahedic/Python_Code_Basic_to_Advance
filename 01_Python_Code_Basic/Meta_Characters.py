import re
pattern=r"ice(-)?cream"

if re.match(pattern,"icecream"):
    print('This is match')
else:
    print('This is not match')

