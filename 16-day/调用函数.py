def regis                             ter(phone,pwd):
	result = diao(phone)
	if result:
		print('注册成功')
	else:
		print('注册失败')





def login (phone,pwd):
	result = diao(phone)
	if result:
		print('注册成功')
	else:
		print('注册失败')


def diao(phone):
	if phone.starswitch('1') and len(phone) == 11:
		ireturn True
	else



