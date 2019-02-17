# Python之Web开发
- 简述
	- 虽然，就如今的情况看来，Web开发领域，Java依然一家独大，Spring类框架仍然是后端框架的主流，但是随着人工智能等发展，Python这门语言逐渐被推上了风口浪尖，相信不久的未来，后端框架必有Python的一席之地。（实际上很多大企业后端都使用了Python框架）
	- 在这个项目，我们逐渐了解Python之Web开发的点点滴滴。
	- 本项目包含几个常见的Python编写的Web框架（共四个主要框架）以及每个框架的一个实战项目，在此之前，必须知道用Python进行Web开发的基础知识。
		- Python基础语法（数据类型、流程控制、函数、异常处理、面向对象）
		- Python之网络编程（TCP/IP网络、HTTP工作原理、Socket编程）
		- Web客户端编程技术（HTML、CSS、JavaScript、JQuery）
		- 数据库及ORM模型（常用数据库使用（PostgreSQL、MySQL、MS SQL Server）。常用ORM模型库使用（SQLAlchemy、Django ORM、Peewee、Storm、SQLObject））
- Python Web框架
	- 简述
		- 目前Python的网络编程框架已经多达几十个，逐个学习显然不现实。但是这些框架在系统架构和运行环境中有很多共通之处
	- 网络框架及MVC架构
		- 网络框架是指这样的一组Python包，它能够使开发者专注于网站应用业务逻辑的开发，而无需处理网络应用底层的协议、线程、进程等方面。这样能大大提高开发者的工作效率，同时提高网络应用程序的质量。
		- 在目前Python的几十个开发框架中，几乎所有的全栈网络框架都强制或者引导开发者使用MVC架构开发Web应用程序。即模型（Model，一般指向数据库）、视图（View，一般指向用户看到的界面）、控制器（Controller，一般指向业务逻辑）。
		- 所谓全栈网络框架，是指除了封装网络和线程操作，还提供HTTP栈、数据库读写管理、HTML模板引擎等一系列功能的网络框架。在后面介绍的Django、Tornado、Flask是全栈网络框架的典型标杆；而Twisted更专注于网络底层的高性能封装而不提供HTML模板引擎等界面功能，所以不能称为全栈框架。
	- 4种Python网络框架
		- Django
		- Tornado
		- Flask
		- Twisted
- 开发环境
	- 本项目及其子项目均使用venv而不是conda环境（venv使用自行百度，使用Pycharm可以直接导入我的虚拟环境）
	- 开发IDE选择为Pycharm
- Web服务器
	- 连接用户浏览器和Python服务器端程序的中间节点，在网站建立过程中起到重要作用。目前主流的Web服务器包括Nginx、Apache、lighthttpd、IIS等。Python服务器端程序在Linux平台下使用广泛的是Nginx。
	- 了解以下配置内容
		- WSGI接口
		- Linux+Nginx+uWSGI配置
		- 建立HTTPS网站（使用OpenSSL工具包）
- 补充说明
	- 本项目参考书为《Python高效开发实战》刘长龙著
	- 使用到的所有重要包会列在requirements.txt文件中
	- 欢迎star或者fork