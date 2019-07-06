print(14*" >", "\t n.B.a. \t", "< "*14)


for numbers in range(1,100):

    if numbers % 3 == 0 and numbers % 5 != 0:
        print("FIZZZ")
    elif numbers % 5 == 0 and numbers % 3 != 0:
        print("BUZZZ")
    elif numbers % 15 == 0:
        print("FIZZZ BUZZZ")
    else:
        print(numbers)




"""ALTERNATIVE VERSION

key = 1
while number < 100:
    key +=1
    if numbers % 3 == 0 and numbers % 5 != 0:
        print("FIZZZ")
    elif numbers % 5 == 0 and numbers % 3 != 0:
        print("BUZZZ")
    elif numbers % 15 == 0:
        print("FIZZZ BUZZZ")
    else:
        print(numbers) """