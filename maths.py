equa_a = 23 * 3;
sumNum = equa_a;
print(sumNum);

def sumNum(a, b):
    return a + b;

print(sumNum(23, 3));


# Math operations
a = 2 + 3 * 6
print(a)

b = (2 + 3) * 6
print(b)

c = 48565878 * 578453
print(c)




z = 5

def modify_global():
    global z
    z = 10

modify_global()
print(z)  # Output: 10



def outer():
    a = 5

    def inner():
        nonlocal a
        a = 10
        print(a)  # Output: 10

    inner()
    print(a)  # Output: 10

outer()
