# choose a number
num = input("Choose a number\n")

# choose Celsius or Fahrenheit
unit = input("Choose unit: Celsius or Fahrenheit\n").lower()

# convert Celsius to Fahrenheit
if unit == "celsius":
    temp = int(num) * 9/5 + 32
    print(num, "degrees Celsius converts to ", temp, "degrees Fahrenheit.")
elif unit == "fahrenheit":
    temp = (int(num) - 32) / (9/5)
    print(num, "degrees Fahrenheit converts to ", temp, "degrees Celsius.")
else:
    # I always mispell Fahrenheit lol
    print("Please check your unit spelling!")
