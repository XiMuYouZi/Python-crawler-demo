# 次例子就是ORM的简单实现,重要部分已做注释
class Field(object):
    def __init__(self, name, type):
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
        print('SchoolMetaClass被调用')
        mapping = dict()
        for key, value in attrs.items():
            if isinstance(value, Field):
                print('类的属性和方法---%s:%s' % (key, value))
                mapping[key] = value
        # 移除类属性以免与对象属性发生冲突
        for key in mapping.keys():
            attrs.pop(key)
        print('设置之前的attr', attrs)
        attrs['__mapping__'] = mapping  # 类名和属性的映射
        attrs['__table__'] = name  # 表名
        print('设置之后的attr', attrs)
        return type.__new__(cls, name, bases, attrs)


class BaseSchool(dict, metaclass=SchoolMetaClass):
    def __init__(self, **keywords):
        print('BaseSchool的属性', keywords)
        # 继承字典,对象调用该方法传关键字参数
        super().__init__(**keywords)

    def __getattr__(self, key):
        print('call __getattr__')
        return self[key]

    def __setattr__(self, key, value):
        print('call __setattr__')
        self[key] = value

    def save(self):
        # 需要插入的列名
        fields = []
        # 需要插入的值
        args = []
        for key, value in self.__mapping__.items():
            print('key:{}--value:{}'.format(key, value))
            fields.append(value.name)
            args.append(getattr(self, key, 'xxx'))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(args))
        print('sql语句:%s' % (sql))
        print('fileds:{}---args:{}'.format(fields, args))


class School(BaseSchool):
    name = StringField('name')
    id = IntegerField('id')
    email = StringField('email')


# 测试
school = School(name='hehed', id='555', email='8064444')
school.save()
