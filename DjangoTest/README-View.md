# Django视图层
- 简述
	- Django框架处理业务的逻辑一般如下（省略图，源于网络，侵删）
		- ![Django业务逻辑图](https://img-blog.csdnimg.cn/2019030909512814.png)
	- 可以看到，用户在输入网站的url之后看到的最直接的页面就是视图，而视图是基于HTML模板文件进行渲染的，数据来源于数据库也就是模型层。View是中间的关键部分，衔接HTTP请求、Python程序、HTML模板、ORM数据库。
- URL映射
	- URL分发（URL dispatcher）映射配置可以被看做Django项目的入口配置，通过URL dispatcher可以指定用户的每一个访问的后台Python处理函数是什么。
	- 普通URL映射
		- 每个Django项目都有一个urls.py文件用于维护URL dispatcher。
		- ```python
			from django.conf.urls import url, include
			from django.contrib import admin
			
			urlpatterns = [
			    url(r'^admin/', admin.site.urls),
			    url(r'app/', include('app.urls')),
			    url(r'app2', include('app2.urls'))
			]
			```
		- 不妨看上面这个路由演示文件。
			- 在urls.py文件中必须声明urlpatterns变量用来保存路由，每一个路由的形式为`url(r'pattern',view_func)`，第一个参数是一个正则表达式（关于正则表达式这里不多说了，自行学习，Django路由用到的正则表达式是很简单的，事实上对于很难的正则表达式有着一个说法：当你解决一个问题是决定要用正则表达式，那么。它就是两个问题了。），决定了路由匹配模式，第二个变量是一个view函数名，决定请求被如何处理，返回什么结果。（路由不包括主机名）
	- 命名URL映射
		- 在普通的URL参数映射中，固然可以通过URL传递参数，但是参数是按照路径中的顺序传递给view函数，这种方法不太友好。而命名URL参数映射使得开发者可以定义这些被传递参数的参数名称，定义方式一般为?P<param_name>pattern。
		- 如
			- `url(r'year/(?P<year>[0-9]{4})/', views.year),`
		- 访问及结果如下
			- ![](https://img-blog.csdnimg.cn/20190309192427885.png)
	- 分布式URL映射
		- 一般在开发中，将整个项目的路由堆到一个urls.py文件里面不好也不太现实，对于每一个app都可以新建一个urls.py文件，使用时利用django.conf.urls中的include函数将其加入主配置的urls.py文件即可。（如上面代码所示）app中的urls文件与主文件格式一致。
	- 反向解析
		- 除了从HTTP URL映射到视图函数的功能外，Django提供了反向的从映射名到URL地址的反向解析功能。URL反向解析使得开发者可以使用映射名代替很多需要写绝对URL映射的地方，提高了代码的可维护性。
		- 在模板文件中使用{% url %}标签调用反向解析（其实就是URL跳转）；在Python程序中使用django.core.urlresolvers.reverse()函数进行反向解析。
		- 注意，为了反向解析的参数名，url中需要添加第三个参数，name。
			- `url(r'year/(?P<year>[0-9]{4})/', views.year, name="when"),`
			- `url(r'year2', views.year2),`
		- 视图函数定义如下
			- ```python
				
				def year2(request):
				    return HttpResponseRedirect(reverse('when', args=['1998']))
				```
		- 输入http:127.0.0.1:8000/year2可以看到瞬间跳转命名的视图，并携带参数进行反向解析。
	- 视图函数
		- 前面已经使用了不少视图函数，这里来细说视图函数，
		- 当你输入一个URL时，Django会到urlpattern里面查找第一个符合条件的，并得到这个路由设置的函数，随即将request带给这个函数，函数得到request请求，从中获得数据，返回一个HTTP Response。
		- 构造返回的Response一般三种方式
			- 直接构造HTTP Body
			- 用数据渲染HTML模板
			- 如果存在逻辑错误，返回HTTP错误或者其他状态
		- 直接构造HTML页面
			- 对于简单需求，返回一个含有字符串的HTML页面即可，此时可以使用HttpResponse封装这个字符串。
			- django.http.HttpResponse
		- 用数据渲染HTML文件
			- 例如将之前的year函数修改如下，将URL传递过来的year参数渲染到HTML页面
			- ```python
				def year(request, year):
				    return render(request, 'render.html', {'year': year, })
				```
			- 此时访问/year/1998/就可以看到渲染后的结果。（注意HTML文件所在的templates文件夹需要在settings文件中模板相关的变量中设置路径，具体可以查看我的源码）
		- 返回HTTP错误
			- 可以使用HttpResponse传递参数status
			- 对于各种HTTP状态，Django已经封装了不少HttpResponse的子类，可以查看源码使用。
	- 模板语法
		- 模板文件主要就是HTML文件配套CSS或者JS文件。
		- 除了HTML原有的语法，Django自定义了一套模板语法。
		- 变量替换
			- 在HTML文件的**任何位置**，都可以使用变量替换。
			- `{{ data.a }}`
			- 这里的data就是render时传递的参数字典中的一个值。
		- 过滤器
			- 放在变量后用于控制变量显示格式的技术，变量与过滤器使用管道符"|"连接，有Linux基础的应该知道。
			- `{{ data.a | upper }}`
			- 将upper过滤器应用到a上。
			- 常见过滤器可以查看源码。
		- 流程控制
			- 循环逻辑
				- ```
						{% for data in datas %}
						<h> {{data.a}}</h>
						{% endfor %}
					```
			- 判断逻辑
				- ```
						{% if data.b < 10 %}
						<h1> {{data.a}}</h1>
						(% elif data.b < 20 %}
						<h2> {{data.a}} </h2>
						{% else %}
						<p> data.a </p>
					```
		- 模板继承
			- 利用extends语句
			- 不细说，现在前端自然会有一个较好的逻辑。
- 补充说明
	- 具体介绍了视图层的相关内容
	- 本项目参考书为《Python高效开发实战》刘长龙著
	- 使用到的所有重要包会列在requirements.txt文件中
	- 具体代码可以查看我的GitHub，欢迎star或者fork