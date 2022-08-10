def sqrt_bisearch(n):
    lf,rt,ans=0,n,-1
    
    while lf<=rt: 
        m=(lf+rt)//2
             
        if m*m<=n:
            ans=m
            lf=m+1
        else:
            rt=m-1
         
    return ans


def sqrt_bisearch_newton(x):
    if x == 0:
        res = 0
    else:
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            
            x0 = xi

            print(x0)

        res = int(x0)
     
    return res


def test_sqrt_bisearch():
    for i in range(2,50):
        print(i,sqrt_bisearch(i),sqrt_bisearch_newton(i))


test_sqrt_bisearch()