# 1.画方块的代码太长了，有没有什么办法能缩短点？

'''
使用循环

for i in range(循环次数)：
   [输入代码]
'''

# 2.如果只想画个半圆，该怎么办？

'''
用circle在半径后增加一个变量，是他的圆弧，如180就是半圆

import turtle as t

t.circle(100, 180)
t.done()
'''

# 画正五边形怎么写代码？正六边形呢？正七八九……边形呢？他们之间有什么规律吗？

'''
for i in range(几边形)
   t.forward(100)
   t.left((n-2)*180/n )n为几边形
'''
