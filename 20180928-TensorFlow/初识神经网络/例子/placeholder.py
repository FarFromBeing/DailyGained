import tensorflow as tf
'''
placeholder()构造一个计算形式，
等待sess.run()时，传入的值
'''
input1=tf.placeholder(tf.float64)
input2=tf.placeholder(tf.float64)
output=tf.multiply(input1,input2)
with tf.Session() as sess:
    '''传值的工作交给了 sess.run() , 需要传入的值放在了feed_dict={}
    并一一对应每一个 input. placeholder 与 feed_dict={} 是绑定在一起出现的。
    '''
    print(sess.run(output,feed_dict={input1:7,input2:3}))

