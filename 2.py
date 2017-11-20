sum=0
i=0
while  i<10:
    sum=sum+i
    print sum
    i=i+1
a="vv is beautiful"
b="she smiles a lot"
math_string="3+4*2"
expression_string="a+' '+b+' i love u'"
print a+b
print eval(math_string)
print eval(math_string+"1")
print eval(expression_string)
print math_string.find("+")
number=input("enter a non-negative integer to take the factorial of:")
product=1
for i in range(number):
    product=product*(i+1)
print product
#factorial of user_input
def factorial(number):
    product=1
    for i in range(number):
        product=product*(i+1)
    return product
    
user_input=input("enter a non-negative integer to take the factorial of:")
factorial_of_user_input=factorial(user_input)
print factorial_of_user_input
print factorial(3)-factorial(2)
print factorial(4)
def factorial(number):
    if number <=1:
        return 1
    else:
        return number*factorial(number-1)
user_input=input("enter a non-negative integer to take the factorial of:")
factorial_of_user_input=factorial(user_input)
print factorial_of_user_input
#define febonacci numbers
def febonacci(number):
    if number <2:
        return number
    else:
        return febonacci(number-1)+febonacci(number-2)
user_input=input("enter a non-negative integer to take the febonacci of:")
febonacci_of_user_input=febonacci(user_input)
print febonacci_of_user_input
#define febonacci by diedai
def febonacci(n):
    terms=[0,1]
    i=2
    while i<=n:
        terms.append(terms(i-1)+terms(i-2))
        i=i+1
    return terms(n)

#define insertion_sorts
def insertion_sort(list):
    for index in range[1,len(list)]:
        value=list(index)
        i=indext-1
        while i>=0:
            if value<list[i]:
                list[i+1]=list[i]
                list[i]=value
                i=i-1
            else:
                break
s=(2+99*3)*50
print s
