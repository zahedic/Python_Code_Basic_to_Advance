word="pathlu"
chances=6
guessadd=[]
done=False

while not done:
    for letter in word:
        if letter.lower() in guessadd:
            print(letter,end =" ")
        else:
            print("_",end ="")

    user1=input(f"your chances is {chances},guess the letter: ")
    guessadd.append(user1.lower())
    if user1.lower()not in word.lower():
        chances=chances-1
        if chances == 0:
            break
    done=True
    for letter in  word:
        if letter.lower() not in guessadd:
            done = False

if done:
    print(f"you have won the game.\nnow you are king.\nThe word is {word}")
else:
    print(f"you have lost the game.\nyour are so vaggo lass man.\nThe word is {word}")