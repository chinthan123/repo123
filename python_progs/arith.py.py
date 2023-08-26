def add (n1,n2):
    return(n1+n2)

def sub (n1,n2):
    return(n1-n2)

def mul (n1,n2):
    return(n1*n2)

def div (n1,n2):
    return(n1/n2)
def sqr(n1,n2):
    return(n1**n2)

a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
print("Sum=",add(a,b))
print("Difference=",sub(a,b))
print("Product=",mul(a,b))
print("difference=",div(a,b))
print("square=",sqr(a,b))
