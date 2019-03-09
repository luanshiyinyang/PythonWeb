# Django模型层
- 简述
	- Django框架处理业务的逻辑一般如下（省略图，源于网络，侵删）
		- ![Django业务逻辑图](https://img-blog.csdnimg.cn/2019030909512814.png)
	- 可以看到，Django自带了一套ORM机制，这也是Django框架的核心---“全面”，将一切能帮开发者完成的率先完成。使用Django开发，只需要知道它的模型层如何使用，甚至可以不用系统学习过数据库及其使用。
	- 在[之前的博客](https://blog.csdn.net/zhouchen1998/article/details/87438165)，我已经初步介绍了Django的主要组件，以及搭建了一个小站点，在这篇，将详细谈一谈Django模型层的点点滴滴。
- 注意
	- 使用Django的ORM模型，那么建议预先创建相关的模型文件再进行数据库的迁移。
	- 每个模型类都会被映射到数据库中的一个表，类的属性被映射为表中的字段。（这就是ORM的核心思路）。除此之外，数据库的主键、外键、约束都可以通过类属性定义。
- 基本操作
	- 模型类定义
		- 一般在该app的models.py文件中
		- 所有Django模型都必须继承自django.db.models.Model类，否则无法完成向实际数据库的迁移。
		- 一般格式
			- ```python
				class ModelName(models.Model):
				    field1 = models.XField(...)
				    field2 = models.XField(...)
				    ...
				    class Meta:
				        db_table = ...
				        other_metas = ...
				```
		- 解析
			- 继承自Model类
			- 通过类属性定义模型字段，必须是某种models.XField类型
				- DjangoField类型与数据库中数据类型对应如下（见源码，这里只列举了常用的MySQL的，其余的可以到django.db.backends.DBName中base.py查看）
					- ```python
						_data_types = {
						        'AutoField': 'integer AUTO_INCREMENT',
						        'BinaryField': 'longblob',
						        'BooleanField': 'bool',
						        'CharField': 'varchar(%(max_length)s)',
						        'CommaSeparatedIntegerField': 'varchar(%(max_length)s)',
						        'DateField': 'date',
						        'DateTimeField': 'datetime',
						        'DecimalField': 'numeric(%(max_digits)s, %(decimal_places)s)',
						        'DurationField': 'bigint',
						        'FileField': 'varchar(%(max_length)s)',
						        'FilePathField': 'varchar(%(max_length)s)',
						        'FloatField': 'double precision',
						        'IntegerField': 'integer',
						        'BigIntegerField': 'bigint',
						        'IPAddressField': 'char(15)',
						        'GenericIPAddressField': 'char(39)',
						        'NullBooleanField': 'bool',
						        'OneToOneField': 'integer',
						        'PositiveIntegerField': 'integer UNSIGNED',
						        'PositiveSmallIntegerField': 'smallint UNSIGNED',
						        'SlugField': 'varchar(%(max_length)s)',
						        'SmallIntegerField': 'smallint',
						        'TextField': 'longtext',
						        'TimeField': 'time',
						        'UUIDField': 'char(32)',
						    }
						```
				- 通过Meta子类定义元数据，如数据库表名，可读化名称，数据排序方式等。
					- Meta类属性名Django预定义，不可以超过这个范围。
						- verbose_name: 字符串表示，该模型的可读化名称。
						- verbose_name_plural: 字符串表示，上述名称的复数形式。
						- abstract: True or False，标识本类是否为抽象基类。
						- app_label: 字符串表示，定义本类所属的应用。
						- db_table: 字符串表示，映射的数据库表名，不写会默认生成一定格式的表名（应用名_模型名），可读性较差。
						- db_tablespace: 字符串表示，映射的表空间名称。表空间的概念只在某些数据库如Oracle中存在，没有这个概念的数据库忽略即可。
						- default_related_name: 字符串表示，定义本模型的反向关系引用名称，默认与模型名一致。
						- get_latest_by:日期或者整形的模型字段，定义按照哪个字段值排列以获得模型的开始或结束记录。
						- managed:True or False，定义Django的manage.py命令行工具是否管理本模型，默认为True。
						- order_with_respect_to: 定义本模型可以按照某外键引用的关系排序。
						- ordering:列表表示，定义本模型所有记录的默认排序字段，可以多个，默认升序，降序则在字段前加负号。（ordering = ['field1', 'field2']
						- default_permissions: 元组表示， 模型操作权限，默认为('add', 'change', 'delete')
						- proxy: True or False，本模型及其子模型是否为代理模型。
						- required_db_feathers: 列表表示，定义底层数据库所必备的特性。
						- required_db_cendor: 定义底层数据库类型，如SQLite，MySQL。
						- unique_together: 用来设置的不重复字段组合，必须唯一。如(('field1', 'field2'),)。
						- index_together: 定义联合索引的字段，可以多个。如[['field1', 'field2'],]。
	- 普通字段
		- 常用字段
			- CharField：字符串字段
			- AutoField:自增的整型字段
			- TextField：大容量文本字段
			- DateField：日期字段
			- 具体参考源码
		- 常用字段参数
			- null:设置该字段数据库字段是否可以为Null
			- blank:设置字段是否可以为空，用于字段的表单验证，即是否可以不输入。
			- choices:设置字段的可选值，二维元组传入，每个元组第一个值是实际存储的值，第二个值是HTML页面进行选择时显示的值。
			- default:设置默认值。
			- help_text：HTML页面输入控件的帮助字符串。
			- primary_key:设置字段是否为主键，只可以设置一个字段，若字段类型是AutoField，那么必须设置为主键。
			- unique:设置是否为字段定义数据库的唯一约束。
			- verbose_name:字段的人性化名称。
	- 关系字段（约束表与表之间）
		- 一对一关系
			- OneToOneField
		- 一对多关系
			- ForeignKey
		- 多对多关系
			- ManyToManyField
	- 基本操作(增删查改）
		- 创建模型
			- ```python
				class User(models.Model):
				    name = models.CharField(max_length=10, null=False, verbose_name="名字")
				    age = models.IntegerField(null=False, verbose_name="年龄")
				
				    class Meta:
				        db_table = 'User'
				        verbose_name = "用户"

					def __str__(self):
        					return self.name
				```
		- 数据库准备迁移
			- 命令行输入python manage.py makemigrations
			- 此时会输出数据库的改变（记住，app一定要加入settings.py文件中）
		- 数据库迁移
			- 命令行输入python manage.py migrate
			- ![](https://img-blog.csdnimg.cn/20190309110907444.png)
			- 此时会反馈数据库操作
			- 可以看到，数据库表创建成功，因为没有设置id这个字段，会自动补充并作为主键。
		- 增加
			- 传统的save方法（对对象操作）
				- ```python
					user = models.User()
					    user.name = "名称1"
					    user.age = 18
					    user.save()
					```
			- create方法
				- `models.User.objects.create(name="名称3", age=22)`
			- 数据的确加入到数据库中
				- ![](https://img-blog.csdnimg.cn/20190309113347739.png)
		- 删除
			- 删除所有
				- `User.objects.all().delete()`
			- 过滤删除
				- `User.objects.filter(name="名称1").delete()`
		- 查询
			- 查询所有
				- `User.objects.all()`
			- 查询指定数据
				- `User.objects.get(id=1)`
			- 过滤查询
				- `User.objects.filter(age=18).distinct()`
		- 修改
			- 获得对象再修改
				- `user = User.objects.get(id=1)`
				- `user.name="new"`
				- `user.save()`
			- 获得对象使用update
				- `User.objects.get(id=1).update(name="new")`
			- 获得对象集合，集体修改
				- `User.objects.filter(age=10).update(name="hhh")`
		- 注意：django有两种过滤器为filter和exclude，参数一致，前者返回符合条件的，后者返回不符合条件的。
- 补充说明
	- 具体介绍了模型层的相关内容
	- 本项目参考书为《Python高效开发实战》刘长龙著
	- 使用到的所有重要包会列在requirements.txt文件中
	- 具体代码可以查看我的GitHub，欢迎star或者fork