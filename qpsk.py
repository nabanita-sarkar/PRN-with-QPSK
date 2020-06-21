
# %%
from numpy import ones, arange, cos, sin, pi
from matplotlib.pyplot import plot, subplot, title, xlabel, ylabel, show
from numpy import cos, linspace, pi
from math import sqrt
# from matplotlib.pyplot import plot, show
import numpy as np

start = 0x02
a = start
i = 1
c = 1
prn = []
while(i != start):
    newbit = (((a >> 6) ^ (a >> 5)) & 1)
    a = ((a << 1) | newbit) & 0x7f
    prn.append(a)
    # if (a==start):
    #     print('repetation period:',c)
    # break
    if (c == 8000):
        break
    c += 1
# print(prn)
# plot(prn)
# show()


tg = linspace(0, 4, num=4000)
# tg=np.asarray(tg)
# print(np.shape(tg))
E = 5
Tb = 5
f_c = 10
# l=[1,2,3,4]
l = [4, 2, 7, 1]
s = []
# l=prn
for t_i, i in enumerate(l, start=1):
    t = linspace(t_i-1, t_i, num=1000)
    s.append(cos(2*pi*f_c*t + (2*i-1)*(pi/4)))
    # plot(t,s,'g')

s = np.asarray(s)
s = s.flatten()
l = len(s)
prn = prn[:l]
# print(np.shape(prn))
# print(np.shape(s))
y = s+prn

# subplot(3, 1, 1)
# plot(tg, s)
# title('Message Signal')
# subplot(3, 1, 2)
# plot(tg, prn)
# title('PRN Signal')
# subplot(3, 1, 3)
# plot(tg, y)
# title('Transmitted Signal')


# show()


# %%
z = []
l = prn
for t_i, i in enumerate(l, start=1):
    t = linspace(t_i-1, t_i, num=1000)
    z.append(cos(2*pi*f_c*t + (2*i-1)*(pi/4)))
plot(z)
show()
# %%
