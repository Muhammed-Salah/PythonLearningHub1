def calculate(a,b,op):
    if Input.find('+') != -1:
        ans=a+b
    elif Input.find('-') != -1:
        ans=a-b
    elif Input.find('*') != -1:
        ans=a*b
    elif Input.find('/') != -1:
        ans=a/b
    else:
        ans=None
    return ans
Input=input("enter the operation:")
if Input.find('+') != -1:
    a, b = Input.split('+')
    op = '+'
elif Input.find('-') != -1:
    a, b = Input.split('-')
    op = '-'
elif Input.find('*') != -1:
    a, b = Input.split('*')
    op = '*'
elif Input.find('/') != -1:
    a, b = Input.split('/')
    op = '/'
else:
    print('Invalid input')
    exit()
a = int(a)
b= int(b)
res=calculate(a, b, op)
print(f"{a} {op} {b} = {res}")