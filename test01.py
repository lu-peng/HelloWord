print("Hello Word ,你好，世界")

if True:
    print("true")
else:
    print("false")

total = 1 +\
         2 +\
         3
print(total)

print('hello')
print("hello")
# 三个引号字符串
print("""hello""")
import sys; xx='xxxx'; sys.stdout.write(xx+'\n');
x='a'
y='b'
print('-----------------')
print(x,end='')
print(y)

ssss='abcdefg'
print(ssss[0:3])
print(ssss*2)
print(ssss+'你好！')

import sys
for i in sys.argv:
    print(i)
print('python路径为：',sys.path)
"""导入特定成员"""
from sys import argv,path
print("path=",path)
print("argv=",argv)

#python 变量类型 字符串

a=b=c=1
q,w,e=1,2,'xx'

print(a,b,c)
print(q,w,e)
"""
不可变数据（四个）：Number（数字）、String（字符串）、Tuple（元组）、Sets（集合）；
可变数据（两个）：List（列表）、Dictionary（字典）。
"""
q,w,e,r=1,2.0,True,1+2j
print(type(q),type(w),type(e),type(r))

list=[1,2,3,'a','b','c']
arraylist=['test','hello word']

print(list[0])
print(list[-2])
print(list*2)
print(list[0:-3])
print(list+arraylist)

tuple=(1,2,3,'a','b','c')
tupletest=('test','hello word')

print(tuple[0])
print(tuple[-2])
print(tupletest*2)
print(tuple[0:-3])
print(tuple+tupletest)

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob',  'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])        # 输出键为 'one' 的值
print(dict[2])            # 输出键为 2 的值
print(tinydict)           # 输出完整的字典
print(tinydict.keys())    # 输出所有键
print(tinydict.values())  # 输出所有值
print(tinydict.get('code', "Hello"))
print(11111)
hstr = 'hello'
if str == 1:
    print("值为：", hstr)
elif str != 1:
    print("值为：", hstr)
if 'code' in tinydict:
    print('code in tinydict')
else:
    print('code not in tinydict')

a, b = 0, 1
while a <10:
    print(a+b)
    a=a+1


liststr = {'1': 'test', '2': 'test', '3': 'test', '4': 'test', '5': 'test'}

print(liststr)
print(liststr.keys())
print(liststr.values())
print(liststr['1'])
print(liststr.get('1'))
print(liststr.items())
print(liststr.pop('1'))
liststr.update(tinydict)
print(liststr)

seq = ('name', 'age', 'sex')
dicttest={'1':'2'}
dicttest = dicttest.fromkeys(seq)
print ("新的字典为 : %s" %  str(dicttest))

dicttest = dicttest.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(dicttest))


iter1 = iter(liststr)
print(next(iter1))
print(next(iter1))
for x in  iter1:
    print(x)

def printname(name):
    print(name)
printname('hello word')

def sumwh(w,h):
    return w+h
print(sumwh(1,2))

def printtest(args1,*aguments):
    print('输出')
    print(args1)
    for x in aguments:
        print('输出可变参数')
        print(x)
printtest('test',1,2,3)

sum1 = lambda arg1, arg2: arg1+arg2

print(sum1(10,20))

for i in  sys.argv:
    print(i)
    print(sys.path)

import fibo
fibo.fib(100)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


fn = open("D:\\test.txt", 'r+')
num = fn.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

fn.close()
fn = open("D:\\test.txt", 'r')
tnrline = fn.read()
print(tnrline, num)
fn.close()

import pickle

# 使用pickle模块将数据对象保存到文件
datadic = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

datalist = [1, 2, 3]

fw = open("data.pkl","wb")
pickle.dump(datadic,fw)
pickle.dump(datalist,fw)
fw.close()
fw = open("data.pkl","rb")
print(pickle.load(fw))
print(pickle.load(fw))


try:
    f = open('d:\\test.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


class  persion():
    def __init__(self,name,age):
        self.name = "张三"
        self.age = 10
    def persionpt(self):
        print('姓名：', self.name,'年龄：',self.age)
        print("姓名：%s 年龄：%d" % (self.name,self.age))
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
'''
pes = persion('卢鹏',31)
pes.persionpt()
print(pes.age)
'''
'''
继承
'''
class student(persion):
    grade=''
    def __init__(self,name,a,g):
        persion.__init__(self,name,a)
        self.grade = g
    def persionpt(self):
        print("%s 说我 %d 上 %s" %(self.name,self.age,self.grade))
'''
std = student('卢鹏',11,'四年级')
std.persionpt()
'''
'''
多继承
'''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = Vector(1,  2)
print(v1)
print(v1+v2)
print(v1+v2+v3)


