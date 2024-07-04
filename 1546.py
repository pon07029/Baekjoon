a = int(input())
dat = list(map(int, input().split()))

print(sum(dat)/max(dat)*100/len(dat))
