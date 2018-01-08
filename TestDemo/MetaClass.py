######################################################################################################################
# 这次例子就是ORM的简单实现,重要部分已做注释
class Field(object):
    def __init__(self, name, type):
        print('Field name:',name)
        self.name = name
        self.type = type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name, type='int(20)'):
        super().__init__(name, type)


class StringField(Field):
    def __init__(self, name, type='varchar(20)'):
        super().__init__(name, type)


class SchoolMetaClass(type):
    '''
    第一个参数是元类对象,第二个参数要创建的类名,第三个是要创建的类的父类,第四个参数很重要,是类的属性和方法
    __new__ 是在__init__之前被调用的特殊方法，__new__是用来创建对象并返回之的方法，而__init__只是用来将传入的参数初始化给对象
    你很少用到__new__，除非你希望能够控制对象的创建。这里创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    '''

    def __new__(cls, name, bases, attrs):
        #排除掉对BaseSchool类的修改；
        if name == 'BaseSchool':
            return type.__new__(cls, name, bases, attrs)
        mapping = dict()
        print('SchoolMetaClass的attrs:\n',attrs)
        #key是属性名字，就是id、name、email等，value是初始化id、name、email的后的对象
        for key, value in attrs.items():
            if isinstance(value, Field):
                mapping[key] = value
        # 移除类属性以免与对象属性发生冲突
        for key in mapping.keys():
            attrs.pop(key)
        attrs['__mapping__'] = mapping  # 对象和属性的映射
        attrs['__table__'] = name  # 表名
        print('mapping：',mapping)
        return type.__new__(cls, name, bases, attrs)


class BaseSchool(dict,metaclass=SchoolMetaClass):
    def __init__(self, **keywords):
        print('BaseSchool的传入参数', keywords)
        # 继承字典,对象调用该方法传关键字参数
        super().__init__(**keywords)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        # 需要插入的列名
        fields = []
        # 需要插入的值
        args = []
        for key, value in self.__mapping__.items():
            print('key:{}--value:{}'.format(key, type(value)))
            #取出__mapping__中的value，value是IntegerField等类实例化后的对象，然后取出这些对象的name属性，也就是namexx、idxx等
            fields.append(value.name)
            #通过属性名字来取值，这里的属性名和值的对应关系就是下面的School(id='12345', name='Michael', email='test@orm.org', password='my-pwd')传递进来的，本质是就是给dict的赋值，因为baseschool本身是dict
            args.append(getattr(self, key, 'None'))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(args))
        print('sql语句:%s' % (sql))
        print('fileds:{}---args:{}'.format(fields, args))


class School(BaseSchool):
    #括号内是列名，前面的name是类的属性
    name = StringField('namexx')
    id = IntegerField('idxx')
    email = StringField('emailxxx')
    password = StringField('agexx')


# 测试，
# 设置键值对，必须保证参数名和上面的School的属性名一致，因为到时候需要根据school的属性名来取值
school = School(id='12345', name='Michael', email='test@orm.org', password='my-pwd')
school.save()

print(school,type(School))






###############################################################################################################
class UpperClass(type):
    def __new__(cls, clsname, bases, clsdict):
        upper_dict = {}
        for key, val in clsdict.items():
            if key.startswith('_'):
                upper_dict[key] = val
            else:
                upper_dict[key.upper()] = val
        return type.__new__(cls, clsname, bases, upper_dict)


class D(metaclass=UpperClass):
    a = 'c'
    d = 'e'

print("*"*60)
print('测试2：', D.A)








###############################################################################################################
#次例子是学习元类来定制(创建)类
def add(self,value):
    self.append(value)
class MHMetaClass(type):
    #第一个参数是元类对象,第二个参数要创建的类名,第三个是要创建的类的父类,第四个参数很重要,是类的属性和方法(请记住不是对象的属性和方法,请自行查阅廖大之前教程以作区分)
    def __new__(cls,name,bases,attrs):
        print("通过元类来创建一个类:%s,%s,%s,%s" % (cls,name,bases,attrs))
        attrs['add'] = add
        return type.__new__(cls,name,bases,attrs)

class MHList(list,metaclass=MHMetaClass):
    pass
l = MHList()
l.append(1)
l.add(2)
print(l)