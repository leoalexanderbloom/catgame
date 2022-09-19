def question_one():
    print("What is special about Clouded Leopards?\n")
    print("\tA: They have very long tails")
    print("\tB: They can glow in the dark")
    print("\tC: They have the loudest roar of all cats")
    print("\tD: They can climb forwards down a tree\n")
    choice = input("Please choose: ").upper().strip()
    print("Your choice was: \"" + choice + "\"\n")
    if choice == "D":
        print("Correct Answer, Well Done\n")
        return 10
    else:
        print("Sorry Wrong Answer\n")
        return -5


def question_two():
    print("What is the largest big cat?\n")
    print("\tA: Siberian Tiger")
    print("\tB: Bengal Tiger")
    print("\tC: Lynx")
    print("\tD: Lion")
    print("\tE: Puma")
    print("\tF: Hyena\n")
    choice = input("Please choose: ").upper().strip()
    print("Your choice was: \"" + choice + "\"\n")
    if choice == "A":
        print("Correct Answer, Well Done\n")
        return 10
    else:
        print("Sorry Wrong Answer\n")
        return -5

def question_three():
    print("What is the fastest big cat?\n")
    print("\tA: Lion")
    print("\tB: Tiger")
    print("\tC: Cheetah")
    print("\tD: Snow Leopard")
    print("\tE: Clouded Leopard")
    print("\tF: Jaguar")
    print("\tG: Eiffel Tower")
    print("\tH: Cougar\n")
    choice = input("Please choose: ").upper().strip()
    print("Your choice was: \"" + choice + "\"\n")
    if choice == "C":
        print("Correct Answer, Well Done\n")
        return 10
    else:
        print("Sorry Wrong Answer\n")
        return -5


if __name__ == "__main__":
    score = 0
    player_name = input("What is you name?: ").strip()
    print("Please answer the following questions:\n")
    score = score + question_one()
    score = score + question_two()
    score = score + question_three()
    print(player_name + " got score " + str(score) + "\n")
