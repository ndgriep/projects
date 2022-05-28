
answer = "yes";
guess = input("is bruce a gooba? ")
if guess == answer:
    print("correct")
else:
    while guess != answer:
        print("incorrect, try again")
        guess = input("is bruce a gooba? ")
        if guess == answer:
            print("yes,correct!")
