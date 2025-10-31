import random
while True:
    list=["rock","paper","scissor"]
    user=input("enter your choice rock,paper,scissor ")
    computer=random.choice(list)
    if user==computer:
            print("both user choose same, so match is tie or try again later.")
    elif user==("paper"):
        if computer==("scissor"):
            print("scissor cuts paper, so computer win")

        else:
            print("scissor cuts paper, so user win")
    elif user==("rock"):
        if computer==("scissor"):
            print("rock break scissor, so user win")

        else:
            print("rock break scissor, so computer win")
    elif user==("rock"):
        if computer==("paper"):
            print("paper holds rocks, so computer win")

        else:
            print("paper holds rocks, so user win")
        break
    else:
        ("Choose right! rock,paper,scissor ")


