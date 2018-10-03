import tensorflow as tf
'''state是变量，counter只是变量的一个标签不能用中文做标签
NOTE: This constructor validates the given name. Valid scope
names match one of the following regular expressions:
[A-Za-z0-9.][A-Za-z0-9_.\\-/]* (for scopes at the root)
[A-Za-z0-9_.\\-/]* (for other scopes)
'''
state=tf.Variable(5,name='counter')
print(state.name)
'''
我的理解state是真正的一个变量名，指向创建的一个变量，那么它的作用就是一个指向作用，
那这个counter标签只是方便程序员识别这个变量，起到一个命名的作用。
'''
#常量1
one=tf.constant(1)
res=tf.add(state,one)
update=tf.assign(state,res)

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print("打印初始state:",sess.run(state))
    for _ in range(1,4):
        sess.run(update)
        print("打印state:",sess.run(state))
    
