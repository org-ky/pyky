str1 = "hello"
str2 = "world"

print (str1+" "+str2)
print (3*(str1+" "))
print (str1[0])
print (str1[0:3])
print (str1[-2:])

str3 = "Hello, World!"
index = str3.find("ll")
if index >= 0: 
    print("a ", index, " trovato ", str3[index])

res = str.split(" ")
idx = 0
for r in res:
    idx += 1
    print(idx, " - ", r)

for i in range(0,len(str3)):
    print(str3[i])
