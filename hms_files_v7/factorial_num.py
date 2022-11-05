def factorial_num(num):
    if num < 2:
        return num
    else:
        print(num)
        return num*factorial_num(num-1)
num12=5
fact = factorial_num(num12)
print("factorial of ",num12," : ",fact)