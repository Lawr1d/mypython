print("""Есть уравнение
ax+b=0
Посморим чему равен x и при введённых 
значениях a и b""")
a = input("Введите число a")
b = input("Веедите число b")
a = int(a)
b = int(b)

if (a==0 and b==0):
    print("INF")

if (a==0 and b!=0):
    print("NO")

if (a!=0 and b/a!=0):
    print("NO")

if (a!=0 and b/a==0):
    n = int(-b/a)
    print(n)