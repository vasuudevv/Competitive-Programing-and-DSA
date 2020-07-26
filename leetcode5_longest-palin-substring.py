
def longestPalindrome(s: str) -> str:
    n=len(s)
    if n < 1 :
        return ""
    start = 0
    end = 0
    
    for i in range(n):
        len1 = checkpalin(s,i,i)
        len2 = checkpalin(s,i,i+1)
        len3 = max(len1,len2)
        if len3 > end - start:
            start = int(i - ((len3-1) //2))
            end = int(i + len3 // 2 )             
    return s[start:end+1]


def checkpalin(s,left,right):
    if s == None or left > right:
        return 0 
    while(left>=0 and right < len(s) and s[left] == s[right]):
        left-=1
        right+=1
    return right - left - 1    

ans = longestPalindrome("illd")
print(ans)
