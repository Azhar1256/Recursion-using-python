def power(m,n):
    
    if n==1:
        return m
    else:
        return (m * power(m,n-1))
    
    
m=int(input())
n=int(input())

power(m,n)
