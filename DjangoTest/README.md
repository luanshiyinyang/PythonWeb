# 企业级开发框架-Django
- 简介
	- Django于2003年诞生于美国Kansas州，最初用来制作在线新闻Web站点，于2005年加入BSD许可证家族，成为开源网络框架。根据比利时的爵士乐音乐家Django Reinhardt命名，作者这样命名Django意味着Django能优雅地演奏（开发）功能丰富的乐曲（Web应用）。
- 特点
	- 相对于Python的其他Web框架，Django的功能是最完整的，业内认为就是“全”。它定义了服务发布、路由映射、模板编程、数据处理的一整套功能。这也意味着Django模板之间紧密耦合，开发者需要学习Django自己定义的一整套技术。
		- 完善的文档：10多年的发展，在线文档十分完善。[中文文档地址](https://yiyibooks.cn/xx/django_182/index.html)。
		- 集成数据访问组件：Django的Model层自带数据库ORM组件，使开发者无需学习其他数据库访问技术（如DBI、SQLAlchemy等）。
		- 强大的URL映射技术：使用正则表达式管理URL映射，灵活性极高。
		- 后台管理系统自动生成：开发者只需要通过简单的几行配置和代码就可以实现完整的后台数据管理Web控制台。
		- 错误信息非常完整：在开发调试过程中如果出现运行异常，则Django可以提供非常完整的错误信息帮助开发者定位问题，比如缺少xxx组件的配置引用等，可以使开发者迅速调整错误。
- 组成结构
	- 管理工具（Management）：一套内置的创建站点、迁移数据、维护静态文件的命令工具。
	- 模型（Model）：提供数据访问接口和模块，包括数据字段、元数据、数据关系等的定义和操作。
	- 视图（View）：Django的视图层封装了HTTPRequest和Response的一系列操作和数据流，其功能主要是URL映射机制、绑定模板等。
	- 模板（Template）：是一套Django自己的页面渲染模板语言，用若干内置的tags和filters定义页面的生成方式。
	- 表单（Form）：通过内置的数据类型和控件生成HTML表单。
	- 管理站（Admin）：通过声明需要管理的Model，快速生成后台数据管理网站。
- 建站流程
	- 安装
		- 虚拟环境下安装
			- pip install django==1.9.2
	- 建立项目(会生成项目目录和默认子文件）
		-  django-admin startproject djangosite 
		-  ![](https://img-blog.csdnimg.cn/20190216173847324.png)
		-  默认生成的几个文件都非常重要，在今后的开发中要一直使用和维护它们。
			-  manage.py：是Django用于管理本项目的命令行工具，之后进行站点运行、数据库自动生成、静态文件收集等都要通过该文件完成。
			-  内层djangosite/目录中包含本项目的实际文件，同时因为包含__init__.py，所以又是一个Python包。
			-  djangosite/__init__.py：告诉Python该目录是一个Python包，暂无内容。
			-  djangosite/settings.py：Django的项目配置文件。默认时，在其中定义了本项目引用的Django组件、Django项目名等。在之后的开发中，还需要在其中配置数据库参数、导入其他的Python包等信息。
			-  djangosite/urls.py：维护项目的URL路由映射，即定义客户端访问的URL由哪一个Python模块解释并提供反馈。默认情况下，其中只定义了/admin即管理员站点的解释器。
			-  djangosite/wsgi.py：定义WSGI的接口信息，用于与其他Web服务器集成，一般本文件生成后不做改动。
	- 建立应用
		- python manage.py startapp app 
		- ![](https://img-blog.csdnimg.cn/20190216175030463.png)
		- 默认生成了一些关键文件。
			- __init__.py：其中暂无内容，使得该app成为一个Python包。
			- admin.py：管理站点模型的声明文件，默认为空。
			- apps.py：应用信息定义文件。在其中生成了类AppConfig，该类用于定义应用名等Meta数据。
			- migrations包：用于在之后定义引用迁移功能。
			- models.py：添加模型层数据类的文件。
			- tests.py：测试代码文件。
			- views.py：定义URL响应函数。
	- 基本视图
		- 在完成Django项目和应用的建立后，即可开始编写网站的应用代码，这里简单显示一个反馈来演示路由功能。
		- 在djangosite/app/views.py中建立路由响应函数。
			- ```python
				from django.http import HttpResponse
				
				
				def welcome(request):
				    return HttpResponse("<h1>Welcome to my site.</h1>")
				```
		- 接下来，通过URL映射将用户的HTTP访问与该函数绑定起来。
			- 在djangosite/app目录下新建urls.py，管理该app中的所有URL映射，其文件内容如下。
			- ```python
				from django.conf.urls import url
				from . import views
				
				
				urlpatterns = [
				    url(r'', views.welcome),
				]
				```
		- 在项目urls.py的urlpatterns中加一项，声明对app中urls.py文件的引用。
			- ```python
				from django.conf.urls import url, include
				from django.contrib import admin
				
				urlpatterns = [
				    url(r'^admin/', admin.site.urls),
				    url(r'app/', include('app.urls')),
				]
				```
	- 内置Web服务器
		- 启动Web服务器(命令行下)
			- python manage.py runserver 0.0.0.0:8000
			- 其中，runserver是启动网站关键字，后面参数为网站绑定的IP地址和端口号，用0.0.0.0表示绑定本机所有IP。在运行过程中将一直占用控制台，Ctrl+C退出。
		- 注意：这种方式启动的是Django内置的Web服务器，由于性能原因，一般只用于开发人员测试，正式运行的网站需要使用WSGI方式启动（后面介绍）。
	- 总结
		- 访问如下
			- ![](https://img-blog.csdnimg.cn/20190216181700333.png)
		- 到此，一个简单的站点建立了，麻雀虽小，五脏俱全，这个小站点以及包含了Django建站的一些基本东西。
- 项目实战
	- 模型类使用
		- 1）配置项目INSTALLED_APPS
			- 在django项目的settings.py文件中告诉Django需要安装应用app中的模型，在INSTALLED_APPS列表中添加一行。
				- 'app.apps.AppConfig'
		- 2）模型定义
			- 打开djangosite/app/models.py，在其中新建一个模型类Moment用来定义信息发布表。
				- ```python
					from django.db import models
					
					
					class Moment(models.Model):
					    content = models.CharField(max_length=200)
					    user_name = models.CharField(max_length=20)
					    kind = models.CharField(max_length=20)
					```
		- 3）生成数据迁移文件
			- 指的是将models.py定义的数据表转换为数据库生成脚本的过程。
			- python manage.py makemigrations app
			- 此时migrations文件夹下多了文件，这是数据库生成的中间文件，后面所有数据库改动（也就是models.py文件改动）都会生成在这个目录下。
		- 4）移植到数据库
			- 模型修改可以通过makemigrations生成中间移植文件，要让中间移植文件生效、修改真实数据库，通过migrate命令实现。
			- python manage.py migrate
			- 不修改数据库参数，默认使用sqlite。
			- 利用sqlite可视化工具查看数据库，确实生成了该表，其余的是Django需要的一些默认表。
			- ![](https://img-blog.csdnimg.cn/20190216183437514.png)
	- 表单视图使用
		- 1）定义表单类
			- 建立表单类文件djangosite/app/forms.py，在其中定义表单类MomentForm。
			- ```python
				from django.forms import ModelForm
				from app.models import Moment
				
				
				class MomentForm(ModelForm):
				    class Meta:
				        model = Moment
				        fields = '__all__'
				```
		- 2）修改模型类
			- ```python
				from django.db import models
				
				
				KIND_CHOICES = (
				    ('Python技术', 'Python技术'),
				    ('数据库技术', '数据库技术'),
				    ('其他', '其他'),
				)
				
				
				class Moment(models.Model):
				    content = models.CharField(max_length=200)
				    user_name = models.CharField(max_length=20)
				    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
				```
		- 3）开发模板文件
			- 新建目录djangosite/app/templates,在其中新建moments_input.html文件。
				- ![](https://img-blog.csdnimg.cn/20190216194348151.png)
		- 4）开发视图
			- 编写视图函数，使得表单类和页面模板衔接起来。
			- 在app/views.py编写代码
				- ```python
					from django.http import HttpResponse
					import os
					from app.forms import MomentForm
					from django.http import HttpResponseRedirect
					from django.core.urlresolvers import reverse
					from django.shortcuts import render
					
					
					def welcome(request):
					    return HttpResponse("<h1>Welcome to my site.</h1>")
					
					
					def moments_input(request):
					    if request.method == 'POST':
					        form = MomentForm(request.POST)
					        if form.is_valid():
					            moment = form.save()
					            moment.save()
					            return HttpResponseRedirect(reverse("app.views.welcome"))
					    else:
					        form = MomentForm()
					    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
					    return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moments_input.html'), {'form': form})
					```
			- ![](https://img-blog.csdnimg.cn/2019021619452092.png)
	- 使用管理界面
		- Django管理界面是一个通过简单配置就可以实现的数据模型后台的Web控制台。管理界面通常是给系统管理员使用的，以完成元数据的输入、删除、查询等工作。
		- 首先将管理界面需要管理的模型添加到djangosite/app/admin.py文件中。
			- ```python
				from django.contrib import admin
				from .models import Moment
				
				
				admin.site.register(Moment)
				```
		- 在第一次访问管理界面之前需要创建管理员账户，使用manage.py的createsuperuser建立。
			- ![](https://img-blog.csdnimg.cn/20190217105643183.png)
		- 之后可以通过http://127.0.0.1:8000/admin输入管理员信息后登陆。
			- ![](https://img-blog.csdnimg.cn/20190217105914664.png)
- 补充说明
	- 到此，初步了解了Django的一些构成，和网站搭建的基本步骤。
	- 本项目参考书为《Python高效开发实战》刘长龙著
	- 使用到的所有重要包会列在requirements.txt文件中
	- 具体代码可以查看我的GitHub，欢迎star或者fork