import random


def main():
    level = get_level()             
    correct = generate_integer(level)
    print(f"Score: {correct}")     


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1, 2, 3}:
                return level
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        correct = 0
        for i in range(0,10):
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            incorrect = 0

            while True:
                try:
                    eq = f"{num1} + {num2} = "
                    ans = (num1 + num2)
                    calc = int(input(eq))

                    if incorrect == 2:
                        print("EEE")
                        print(f"{num1} + {num2} = {ans}")
                        break

                    elif calc != (num1+num2):
                        print("EEE")
                        incorrect = incorrect + 1
                        continue

                    else:
                        correct = correct + 1
                        i = i + 1
                        break

                except ValueError:
                    continue


    elif level == 2:
        correct = 0
        for i in range(0,10):
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            incorrect = 0

            while True:
                try:
                    eq = f"{num1} + {num2} = "
                    ans = (num1 + num2)
                    calc = int(input(eq))

                    if incorrect == 2:
                        print("EEE")
                        print(f"{num1} + {num2} = {ans}")
                        break

                    elif calc != (num1+num2):
                        print("EEE")
                        incorrect = incorrect + 1
                        continue

                    else:
                        correct = correct + 1
                        i = i + 1
                        break

                except ValueError:
                    continue


    elif level == 3:
        correct = 0
        for i in range(0,10):
            num1 = random.randint(100,999)
            num2 = random.randint(100,999)
            incorrect = 0

            while True:
                try:
                    eq = f"{num1} + {num2} = "
                    ans = (num1 + num2)
                    calc = int(input(eq))

                    if incorrect == 2:
                        print("EEE")
                        print(f"{num1} + {num2} = {ans}")
                        break

                    elif calc != (num1+num2):
                        print("EEE")
                        incorrect = incorrect + 1
                        continue

                    else:
                        correct = correct + 1
                        i = i + 1
                        break

                except ValueError:
                    continue

    return correct




if __name__ == "__main__":
    main()