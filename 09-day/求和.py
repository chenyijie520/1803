a = int(input('请输入一个数字'))
b = int(input('请输入一个数字'))
sum = 0
if a < b:
	for i in range(a,b+1):
		print(i)
		sum = sum+i
else:
	print('输入有误')


print(sum)



sum1 = 0
while a <= b:
	sum1 = sum1 +a
	a+=1
