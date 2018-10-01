import tensorflow as tf
'''
Session 是 Tensorflow 为了控制,和输出文件的执行的语句
'''
mat1=tf.constant([[3,3]])#矩阵
mat2=tf.constant([[3],[2]])

product=tf.matmul(mat1,mat2)#两个矩阵相乘
'''
product无法执行，只能通过session的一个对象来run，才能运行
2种运行tf.Session()方式
'''
#1.
# with tf.Session() as sess:
#     result=sess.run(product)
#     print(result)
# #[[15]]

#2.
sess=tf.Session()
res=sess.run(product)
print(res)
sess.close()
