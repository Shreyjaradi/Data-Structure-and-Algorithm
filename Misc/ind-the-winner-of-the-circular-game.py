
#Leet Code prob : https://leetcode.com/problems/find-the-winner-of-the-circular-game/

def winner(n,k):
    count = 1
    i = 0
    while( len(n) > 1):
        i  += k - 1
        print (f"i : {i}")
        i %= len(n)
        print(f"i check : {i}")
        del n[i]
    return n
        
            

n = [1,2,3,4,5]
k = 2
win = winner(n,k)
print(win)
