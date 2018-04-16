def jisuanqi(q,w,e):
     if e == "+":
         a = q+w
         print("和是%.02f"%a)
     elif e == "-":
         a = q-w
         print("差是%.02f"%a)
     elif e == "*":
         a = q*w
         print("积是%.02f"%a)
     elif e == "/":
         if w == 0:
             print("输入有误")
         else:
             a = q/w
             print("商是%.02f"%a)
x = float(input("请输入一个数字"))
y = float(input("请输入一个数字"))
z = input("请输入+-*/")
jisuanqi(x,y,z)

		
