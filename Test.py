import math

# name = input('please input your name:')
# print('hello,', name)
print(1024 * 768)

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m ok!')

print('包含中文')

boys = ['tom', 'dog', 'pig']

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

d = (3,)
print(d[0])

arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for a in arrays:
    i += a
print(i)

print(list(range(5)))

n = 1
while n < 5:
    print(n)
    n += 1

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('cc' in d)
# 通过get取得值,key不存在时返回None,或者返回自己指定的value
print(d.get('cc'))
print(d.get('cc'), -1)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(1))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))
