import matplotlib.pyplot as plt
import numpy as np
from operator import add

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

# m = list(map(int, input().split(" ")))
m = [4, 777, 8, 9, 5, 198, 45]
x = len(m)
l = prn[:x]
n = list(map(add, m, l))
# print(l)
# x = len(l)
tg = np.linspace(0, x, num=x*1000)
# tg = np.linspace(0, 127, num=127000)

f_c = 5


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


# print(signal(l))

# print(np.shape(z))
# z = np.asarray(z)
# z = z.flatten()
# plt.plot(tg[:1000], z[:1000])

plt.style.use('seaborn')


plt.subplot(3, 1, 1)
plt.plot(m)
plt.title('Message Signal '+str(m), fontsize=12)

plt.subplot(3, 1, 2)
plt.plot(tg, signal(l))
plt.title('PRN Signal '+str(l), fontsize=12)

plt.subplot(3, 1, 3)
plt.plot(tg, signal(n))
plt.title('Transmitted Signal '+str(n), fontsize=12)
# plt.rcParams["font.size"] = "8"
plt.tight_layout()
plt.show()

f = open('data.txt', 'w+')
for j in n:
    f.write(str(j))
    f.write(' ')
f.close()
