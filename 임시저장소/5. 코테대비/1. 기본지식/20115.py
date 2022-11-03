N = int(input())
xi = sorted(list(map(int, input().split())), reverse=True)

mix_sum = xi[0]

for i in xi[1:]:
    mix_sum += i/2
    
print(mix_sum)
