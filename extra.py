from numpy import ones, arange, cos, sin, pi
from matplotlib.pyplot import plot, subplot, title, xlabel, ylabel, show
from numpy import cos, linspace, pi
from math import sqrt


# for t_i,i in enumerate(l,start=1):
#     t = linspace(t_i-1, t_i, num=1000)
#     if i ==1:
#         s=cos(2*pi*f_c*t + (2*1-1)*(pi/4))
#     elif i ==2:
#         s=cos(2*pi*f_c*t + (2*2-1)*(pi/4))
#     elif i ==3:
#         s=cos(2*pi*f_c*t + (2*3-1)*(pi/4))
#     elif i ==4:
#         s=cos(2*pi*f_c*t + (2*4-1)*(pi/4))
#     plot(t,s,'g')

# show()

# %matplotlib inline

M = 4
i = range(0, M)
t = arange(0, 0.001+1, 0.001)
s1 = ones([len(i), len(t)])
s2 = ones([len(i), len(t)])
for i in range(0, M):
    s1[i, :] = [cos(2*pi*2*tt)*cos((2*i-1)*pi/4) for tt in t]
    s2[i, :] = [-sin(2*pi*2*tt)*sin((2*i-1)*pi/4) for tt in t]

S1 = []
S2 = []
S = []
Input_Sequence = [0, 1, 1, 0, 1, 0, 0, 0]
m = [3, 1, 1, 2]
for i in range(0, len(m)):
    S1 = S1+[s1[m[i], :]]
    S2 = S2+[s2[m[i], :]]
S = S1+S2
subplot(3, 1, 1)
plot(S1)
title('Binary PSK wave of Odd-numbered bits of input sequence')
subplot(3, 1, 2)
plot(S2)
title('Binary PSK wave of Even-numbered bits of input sequence')
subplot(3, 1, 3)
plot(S)
title('QPSK waveform')
show()


M = 4
i = range(0, M)
t = arange(0, 0.001+1, 0.001)
s1 = ones([len(i), len(t)])
s2 = ones([len(i), len(t)])
for i in range(0, M):
    s1[i, :] = [cos(2*pi*2*tt)*cos((2*i-1)*pi/4) for tt in t]
    s2[i, :] = [-sin(2*pi*2*tt)*sin((2*i-1)*pi/4) for tt in t]
plot(s1+s2)
show()



from commpy.modulation import QAMModem
from numpy.random import randint
# msg_bits = randint(0, 2, 50)
# l = QAMModem(4).modulate(msg_bits)
l = QAMModem(4)
plot(l)
show()
