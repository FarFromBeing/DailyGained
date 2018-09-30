import os
import tensorflow as tf
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
'''构造一个代数形式'''
x_data=np.random.rand(100).astype(np.float32)#转换一个float32类型，且X是随机选的数
#构造的代数形式：y=0.1x+0.3
y_data=x_data*0.1+0.3
'''-----------------开始构建TF结构----------------
与代数中的参数对应：Weights,biases是神经网络训练参数
训练完成就是拟合参数
ps:这里的大写变量是由于这个变量可能是（多维）矩阵
'''
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))
#预测的y值
y=Weights*x_data+biases
#计算差别
loss=tf.reduce_mean(tf.square(y-y_data))
#构造一个优化器，其中学习效率0.5
optimizer=tf.train.GradientDescentOptimizer(0.5)
#使用优化器，将误差反向传递，来调整训练参数
train=optimizer.minimize(loss)
#初始化
init=tf.global_variables_initializer()
'''-----------------完成TF结构构造-----------------'''
sess=tf.Session()
sess.run(init)#激活
for step in range(50):
    sess.run(train)
    if step % 5 == 0:
        print(step,sess.run(Weights),sess.run(biases))