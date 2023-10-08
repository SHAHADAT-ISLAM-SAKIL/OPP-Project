from collections import defaultdict
def removalSequence(a):
    countD = defaultdict(int)
    for num in a:
        countD[num] += 1
    totalAll = 0
   
    for num,count in countD.items():
        print(count,num)
        if count>num:
            totalAll += count -num
        elif count<num:
            totalAll +=count
    
    return totalAll

N = int(input())
a = list(map(int, input().split()))
result = removalSequence(a)
print(result)

