#Greatest common divisor program



a=[]
def gcd(m,n):

    for i in range(1,max(m,n)):
        if ((m%i==0) and (n%i==0)):
            a.append(i)
        else:
            pass
    print(max(a))
gcd(8,12)
