high = int(input('请输入你的身高'))
money = int(input('请输入你的身价'))
nice = int(input('请输入你的颜值'))

if high>=180 and money>=1000000 and nice>=90:
	print('高富帅')
elif high<=180 and money>=1000000 and nice>=90:
	print('富帅')
elif high<=180 and money<=1000000 and nice>=90:
	print('帅')
elif high<=160 and money<=100 and nice<=60:
	print('矮矬穷')
