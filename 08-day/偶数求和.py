i = 1
d_sum = 0#偶数和
s_sum = 0#奇数和
while i<= 100:
	if i%2 == 0:#偶数
		d_sum += i#加起来的一定是偶数
	else:
		s_sum += i #加起来的一定是奇数
	i+=1

print('偶数和是%d'%d_sum)
print("奇数和是%d"%s_sum)
