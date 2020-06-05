for i in range(51):
    if(i%3==0 and i%5==0):
        print(i,"\t\t fizzbuzz")
    elif(i%3==0):
        print(i,"\t\t fizz")
    elif(i%5==0):
        print(i,"\t\t buzz")
    else:
        print(i)