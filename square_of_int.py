#Read an integer N . For all non-negative integers i<n , print i^2
n = int(input())
#[print(i**2) for i in range(n)]
for i in range(0,n):
    print(i*i)
    i= i+1
