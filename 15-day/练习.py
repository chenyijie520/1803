def menu():
listunum=[1]
listuname=['张三']
lisub=['笔试:80.面试:90.机试:95']


#菜单
menu()
print('1.录入成绩')
print('2.查询成绩')
print('3.修改成绩')
print('4.删除成绩')
print('5.打印所有成绩')
print('6.退出成绩')
id=input()
if id==1:
def entry()
elif id==2:
def query()
elif id==3:
def modify()
elif id==4:
def del()
elif id==5:
def dy()
elif id==6:
def retreat()
else:
print '输入错误，重新输入'
def menu()


#录入成绩
entry()
print '请输入姓名'
name=input()
print '请输入笔试成绩'
written=input()
print '请输入面试成绩'
interview=input()
print '请输入机试成绩'
machine=input()
#学号自增1，唯一
num=listunum[-1]+1
#向集合的末尾添加一个元素append()函数
listunum.append(num)
listuname.append(name)
achievement='笔试:'+written+'.'+'面试:'+interview+'.'+'机试:'+machine
lisub.append(achievement)



#查询成绩
entnry()
print '请输入查询的学号'
stunum=input()
#判断输入的学号是否在学号的集合中。不会写





#如果在集合中
print '查询某科请按1查询所有请按2'
num=input()
if num==1:
print '请输入查询的科目'
sub=input()
	 if sub=='笔试'
	 
	 elif sub=='面试'

	 elif sub=='机试'

	 else:
	 print '输入错误'
	 def query()



elif num=2:

else:
print '输入错误'
def query()
#不在的话重新调用查询函数





#修改成绩
modify()
#删除成绩
del()
#打印全部成绩
dy()
#退出
retreat()
pass





