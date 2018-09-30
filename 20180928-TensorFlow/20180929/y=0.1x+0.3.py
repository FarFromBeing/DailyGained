import os
import tensorflow as tf
import numpy as np

#构造一个代数形式
x_data=np.random.rand(100).astype(np.float32)#转换一个float32类型，且X是随机选的数
y_data=x_data*0.1+0.3#构造的代数形式：y=0.1x+0.3
'''开始构建TensorFlow结构
与代数中的参数对应：Weights--0.1，biases--0.3
这里的大写变量是由于这个变量可能是（多维）矩阵
'''
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))
y=Weights*x_data+biases#
loss=tf.reduce_mean(tf.square(y-y_data))#计算差别
optimizer=tf.train.GradientDescentOptimizer(0.5)#构造一个优化器，学习效率0.5
train=optimizer.minimize(loss)
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)#激活
for step in range(200):
    sess.run(train)
    if step % 2 == 0:
        print(step,sess.run(Weights),sess.run(biases))