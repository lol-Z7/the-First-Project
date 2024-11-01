while True:
    while True:
        try:
            input_1 = int(input("Choose a difficulty level from 1 2 3: "))
            if 1 <= input_1 <= 3:
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

    if input_1 == 1:
        while True:
            try:
                number = int(input("Choose a number between 1 and 10: "))
                if 1 <= number <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a number.")

        import random
        number = random.randint(1, 10)
        print("The number is", number)
        while True:
            try:
                ff = input("Do you want to guess again?y/n: ")
                if ff.lower() in ["n", "no"]:
                    print("Thanks for nothing")
                    break
                elif ff.lower() in ["y", "yes"]:
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            except ValueError:
                print("Please enter 'y' or 'n'.")
        continue

    elif input_1 == 2:
        while True:
            try:
                number = int(input("Choose a number between 1 and 50: "))
                if 1 <= number <= 50:
                    break
                else:
                    print("Please enter a number between 1 and 50.")
            except ValueError:
                print("Please enter a number.")

        import random
        number = random.randint(1, 50)
        print("The number is", number)
        while True:
            try:
                ff = input("Do you want to guess again?y/n: ")
                if ff.lower() in ["n", "no"]:
                    print("Thanks for nothing")
                    break
                elif ff.lower() in ["y", "yes"]:
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            except ValueError:
                print("Please enter 'y' or 'n'.")
        continue

    elif input_1 == 3:
        while True:
            try:
                number = int(input("Choose a number between 1 and 100: "))
                if 1 <= number <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Please enter a number.")

        import random
        number = random.randint(1, 100)
        print("The number is", number)
        while True:
            try:
                ff = input("Do you want to guess again?y/n: ")
                if ff.lower() in ["n", "no"]:
                    print("Thanks for nothing")
                    break
                elif ff.lower() in ["y", "yes"]:
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            except ValueError:
                print("Please enter 'y' or 'n'.")
        continue

    else:
        print("Please enter 1, 2, or 3.")