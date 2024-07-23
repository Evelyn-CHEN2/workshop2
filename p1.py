count=0
num=int(input('Enter a number: '))
while num!=0:
    if num>0:
        count+=1
    num = int(input('Enter a number: '))
print('{} positive numbers were entered.'.format(count))

# counter=0
# n=int(input('Enter a number: '))
# while n!=0:
#     if n>0:
#         counter+=1
#     n = int(input('Enter a number: '))
# print('{:} positive numbers were entered'.format(counter))