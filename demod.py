import matplotlib.pyplot as plt
import numpy as np
from operator import sub


start = 0x02
a = start
i = 1
c = 1
prn = []
while(i != start):
    newbit = (((a >> 6) ^ (a >> 5)) & 1)
    a = ((a << 1) | newbit) & 0x7f
    # print(a)
    prn.append(a)
    if (a == start):
        # print('repetation period:', c)
        break
    c += 1


f = open('data.txt', 'r')
n = f.read()
n = n.strip()
n = list(map(int, n.split(' ')))
# n = list(n)
# print(type(n))
f_c = 3

x = len(n)
l = prn[:x]
tg = np.linspace(0, x, num=x*1000)
m = list(map(sub, n, l))
print(m)


def signal(l):
    z = []
    for t_i, i in enumerate(l, start=1):
        t = np.linspace(t_i-1, t_i, num=1000)
        # z.append(np.cos(2*np.pi*f_c*t + (2*i-1)*(360/180)))
        z.append(np.cos(2*np.pi*f_c*t + (2*i-1)*(360/180)))
        # print((2*i-1)*(360/180))
    # plt.plot(z)
    z = np.asarray(z)
    z = z.flatten()
    return z


plt.style.use('seaborn')

plt.subplot(3, 1, 1)
plt.plot(tg, signal(n))
plt.title('Received Signal')

plt.subplot(3, 1, 2)
plt.plot(tg, signal(l))
plt.title('PRN Signal')

plt.subplot(3, 1, 3)
plt.plot(m)
plt.title('Recovered Message Signal')

plt.show()
