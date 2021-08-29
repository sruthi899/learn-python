s = list(map(int, input().split()))
name = list(input().split())
#print(s,name)
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if  s[i] > s[j]:
            s[i], s[j] = s[j], s[i]
            name[i], name[j] = name[j], name[i]
print(s,"\n", name)


