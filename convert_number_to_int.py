numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000
}
userinput = input("enter a number in english")
convert_number = ""
calculation = 0
result = 0
# loop to read user input
for element in userinput:

    # number conversion when space arrives
    if element == " ":
        # condition when hundred come in user input
        if convert_number == "hundred":
            if calculation == 0:
                result *= numbers[convert_number]
                convert_number = ""
                continue
            else:
                calculation *= numbers[convert_number]
                result += calculation
                convert_number = ""
                calculation = 0
                continue
        elif convert_number == "":
            continue
        # condition when thousand come in user input
        elif convert_number == "thousand":
            if calculation == 0:
                result *= numbers[convert_number]
                convert_number = ""
                continue
            else:
                calculation *= numbers[convert_number]
                result += calculation
                convert_number = ""
                calculation = 0
                continue
        else:
            calculation += numbers[convert_number]
            convert_number = ""
            continue

    convert_number += element

 # last number conversion

if convert_number == "hundred":
    if calculation == 0:
        result *= numbers[convert_number]
        convert_number = ""
    else:
        calculation *= numbers[convert_number]
        result += calculation
        calculation = 0
elif convert_number == "thousand":
    if calculation == 0:
        result *= numbers[convert_number]
        convert_number = ""
    else:
        calculation *= numbers[convert_number]
        result += calculation
        calculation = 0
else:
    calculation += numbers[convert_number]
    result += calculation
    calculation = 0

# to print user input in integer form
print(result)
