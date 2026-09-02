from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

nums_counter = Counter(nums)

output = nums_counter.most_common(k)

result = []
for i, _ in output:
    result.append(i)
    
print(result)

