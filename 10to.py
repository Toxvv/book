from pythonds import stack
def baseConverter(decNumber,base):
    digits = '0123456789ABCDEF'

    remstack=stack.Stack()

    while decNumber>0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = " "
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

s=baseConverter(100,2)
print(s)