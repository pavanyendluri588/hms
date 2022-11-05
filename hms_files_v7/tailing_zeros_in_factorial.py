def factorial_num(num):
    if num < 2:
        return num
    else:
        return num*factorial_num(num-1)
def no_of_tailing_zeros(num_org):
     zeros=0
     num_copy=num_org
     num = factorial_num(num_org)
     while int(str(num)[-1])==0:
        num=num//10
        zeros= zeros+1
     print("no of tailing zeros for",num_copy,"!=",zeros)
     return zeros
def efficient_no_of_tailing_zeros(num):
    i=5
    zeros=0
    while num>i:
        zeros=zeros+int(num/i)
        i=i*5
    print("effective no of tailing zeros for",num,"!=",zeros)
    return zeros

no_of_tailing_zeros(5)
no_of_tailing_zeros(10)
no_of_tailing_zeros(100)
no_of_tailing_zeros(500)


efficient_no_of_tailing_zeros(5)
efficient_no_of_tailing_zeros(10)
efficient_no_of_tailing_zeros(100)
efficient_no_of_tailing_zeros(500)