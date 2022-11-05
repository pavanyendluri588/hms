def gcd_or_hcf_of_two_nums(num1,num2):
    num_div=None
    if num1>=num2:
        num_div=num2
    else:
        num_div=num1
    for i in range(num_div,0,-1):
        if num1%i == 0 and num2%i ==0:
            print("gcd or hcf of nums",num1,num2," is ",i)
            return i

"""
    while num1%num_div != 0 and num2%num_div !=0:
        num_div= num_div-1
        print("round(num1/num_div,2),=",round(num1/num_div,2),"div = ",num_div)
    print("gcd or hcf of nums",num1,num2," is ",num_div)
    return num_div
    """
gcd_or_hcf_of_two_nums(4,6)
gcd_or_hcf_of_two_nums(100,200)
gcd_or_hcf_of_two_nums(7,13)