def lonesum_fun(a,b,c):
    if a==b==c:
        print("{},{},and{} values are same".format(a,b,c))
        print("Value is zero")

    elif a==b and a!=c:
        print("c={} value is different".format(c))
    elif a==c and a!=b:
        print("b={} value is different".format(b))
    elif b==c and b!=a:
        print("a={} value is different".format(a))

    else:
        print("{},{},and {} values are different".format(a,b,c))
        print("Sum:",a+b+c)


        
