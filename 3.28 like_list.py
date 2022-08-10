
P=1e9+7

def like_lst(n,k):
    t=0
    arr=[ [0]*n for _ in range(k) ]

    for i in range(k):
        for j in range(n):
            arr[j]=k
            for t in range(k):
             

            

        
    return t



def test_10():
    for n in range(6):
        for k in range(10):
            print(n,'-',k,': ',like_lst(n,k))

        
test_10()
