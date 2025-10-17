def read_number():
    num=(input("enter a number of minimum 4 digits:"))
    if len(num)>=4 and num.isdigit():
        return int(num)                
    else:
        print("invalid number.Try a number of minimum 4 digits")
        return read_number()
def reverse(num):
    rev=0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev
number=read_number()
reverse=reverse(number)
print("the original number is:", number)
print("the reverse of number is:", reverse)

        

