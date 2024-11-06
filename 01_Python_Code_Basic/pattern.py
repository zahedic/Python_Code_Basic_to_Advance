import re
pattern=r"a//b"

if re.match(pattern,"avbul"):
    print('This is match')
else:
    print('This is not match')
