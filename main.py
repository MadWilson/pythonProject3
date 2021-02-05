'''
#4.47
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if (a == b) or (a == c) or (b ==c):
    print('Треугольник равнобедренный')
else:
    print('Треугольник не равнобедренный')
'''
'''
#4.50
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
if ((c - a >= 1) and (d - b >= 1)) or ((c - b >= 1) and (d - a >= 1)):
    print('Возможно')
else:
    print('Никак')
'''
'''
#4.72
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
e = max(a, b, c)
f = min(a, b, c)
print("Наибольшее число:", e)
print("Наименьшее число:", f)
'''
'''
#4.32
a = int(input())
a1 = a/1000
a2 = (a % 1000) / 100
a3 = (a % 100) / 10
a4 = a % 10
if a1 + a2 == a3 + a4:
    print('Равна')
else:
    print('Не равна')
'''
'''
#5.44
a = int(input())
b = int(input())
c = a+b
print(c)
'''

#5.47
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
s = a1*a2*a3*a4*a5*a6
print(s)
