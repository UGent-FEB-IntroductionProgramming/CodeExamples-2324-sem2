import random

number1 = random.randint(1, 100)
number2 = random.randint(1,100)

#print("De som van " + number1 + " en " + number2 +" is :")

result = int(input("De som van " + str(number1) + " en " + str(number2) +" is :"))

#if result == number2 + number1:
#    print("juist")
#else:
#    print("fout")

print(result == number1 + number2)