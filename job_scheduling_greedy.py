def printJobScheduling(arr,t):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i][2]<arr[j][2]:
                arr[i],arr[j]=arr[j],arr[i]
    result=[False]*t
    job=['-1']*t
    for i in range(n):
        for j in range(min(t - 1,arr[i][1]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                job[j]=arr[i][0]
                break
    print(job)

arr = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]]
print(arr)

print("Following is maximum profit sequence of jobs")
printJobScheduling(arr, 3)

# It means that the loop will go from the starting value (determined by min(t - 1, arr[i][1] - 1)) towards -1, decreasing by 1 in each iteration.