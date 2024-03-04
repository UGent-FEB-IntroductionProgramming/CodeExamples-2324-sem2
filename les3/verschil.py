import random

number1 = random.randint(1, 100)
number2 = random.randint(1,100)

if number1 < number2:
    #temp = number1
    #number1 = number2
    #number2 = temp
    number1, number2 = number2, number1

result = int(input("Het verschil van " + str(number1) + " en " + str(number2) +" is :"))

if result == number1 - number2:
    print("juist")
else:
    print("fout")