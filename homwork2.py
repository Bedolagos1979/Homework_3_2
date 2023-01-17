# 1 часть
n = int(input('введите целове число'))
c = 0
while n >= 1:
    n = n - 1
    a = (n + 1) ** 3
    print(a)
    c = c + a
print(c, 'сумма')

# 2 часть

x = int(input('введите целове число'))
y = 0
for i in range(x):
    i = i + 1
    t = i ** 3
    print(t)
    y = y + t
print(y, 'сумма')
