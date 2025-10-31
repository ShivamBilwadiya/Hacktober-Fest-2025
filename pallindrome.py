L = int(input())
R = int(input())
for i in range(L,R+1):
    if i == 1 :
        continue 

    X = i 
    Y = 0
    is_palindrome = True
    while X > 0:
        d = X%10
        Y = Y*10 + d
        X = X//10
    if i != Y:
        is_palindrome = False 

            
    is_prime = True    
    for j in range(2,int(i**0.5)+1):
        if i % j == 0 :
           is_prime = False
           break
    if is_prime and is_palindrome :
        print(i , end = " ")
