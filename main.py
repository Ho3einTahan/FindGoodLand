def findGoodLand():
    
    matrix=[
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
    ]
    
    dp=[]
    maxLand=0
    cols=len(matrix[0])
    rows=len(matrix)
    
    dp=[[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if(matrix[i][j]==1):
                if(i==0 or j==0):
                    dp[i][j]=1
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            else:
                dp[i][j]=0
            maxLand=max(maxLand,dp[i][j])
    
    print("The size of the largest good land is:", maxLand*maxLand)

findGoodLand()