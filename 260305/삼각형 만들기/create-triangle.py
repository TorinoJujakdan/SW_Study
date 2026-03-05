n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points] 

max_w = 0        
for i in range(n):
   for j in range(n):
      if i == j:
         continue
      if x[i] != x[j]:
         continue
      for k in range(n):
         if i == k or j == k: 
            continue
         if y[i] != y[k]:
            continue
         
         width = abs(y[i] - y[j])
         length = abs(x[i] - x[k])
         w = width * length

         if max_w < w:
            max_w = w

print(max_w)