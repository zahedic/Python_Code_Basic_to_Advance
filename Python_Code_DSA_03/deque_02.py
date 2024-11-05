from collections import deque
bank=deque(['zawad','awad','soha'])


print(bank)

bank.popleft()
bank.popleft()
bank.popleft()

print(bank)

if not bank:
    print('No person left')