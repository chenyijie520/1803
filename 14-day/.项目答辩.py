#打印菜单

print('学生成绩管理系统1.0版本'，center(30'*'))
print('请输入成绩',center(30''))
print('查询成绩'center(30''))
print('修改成绩')
print('删除成绩')
print('打印所有成绩')
print('退出系统')

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
query()
print '请输入查询的学号'
stunum=input()
#判断输入的学号是否在学号的集合中。不会写
