print("名片系统v1.0版本".center(30,"*"))

print("1:新增名片".center(30,"*"))

print("2:查找名片".center(30,"*"))

print("3:修改名片".center(30,"*"))

print("4:删除名片".center(30,"*"))

cards = []#定义空列表

while True:

	fun_number = int(input("请选择功能"))

	if fun_number ==1:

		print("新增")

		flag  = 0 #默认值 0代表不在里面

		card={}#定义空字典

		name = input("请输入名字")

		for temp in cards:
		count+=1

			if name == temp["name"]:

				flag = 1 #在里面

				break

			#[{1},{2},{3}]

		

		if flag == 1:

			print("查无此人")
		else:
			print('姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s'%(cards[count-1]['name'],cards[count-1]['job'],cards[count-1]['']))
			continue

		job = input("请输入职位")

		phone = int(input("请输入手机号"))

		company = input("请输入公司名字")

		address = input("请输入公司地址")

		#list = [{},{},{}]	

		#if flag == 0:

		card["name"] = name

		card["job"]  = job

		card["phone"] = phone

		card["company"] = company

		card["address"] = address

		#放到列表中

		cards.append(card)

		print("新增成功")

	elif fun_number == 2:

		print("查找")

	elif fun_number == 3:

		print("修改")

	elif fun_number == 4:

		print("删除")
