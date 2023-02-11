
def findNumberOfStrings(n):
    return int((n+1)*(n+2)*(n+3)*(n+4)/24)
 
# Driver Code
if __name__ == '__main__':
   
    N = 1
 
    # Function Call
    print(findNumberOfStrings(N))
