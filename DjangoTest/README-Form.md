# Django表单
- 简述
	- 虽然在Django的核心组件中没有看到表单的影子，但是熟悉Web开发的都知道，表单控制是至关重要的。
	- 表单一般放在某个app目录下的forms.py文件中。
- 基本操作
	- 表单绑定状态
		- Django为继承自Form类的表单维护了一个绑定（bound）状态。
		- 如果一个表单对象在实例化后被赋予过数据内容，则称该表单出于bound状态。只有处于bound状态的表单才具有数据验证功能(validate data)功能。
		- 如果未被赋予过数据内容，则表单处于unbound状态。只有处于unbound状态的表单才能被赋予数据，使表单变为bound状态。
		- 可以通过Form对象的is_bound查看表单状态。
	- 表单数据验证
		- 在服务端利用Python代码验证表单数据的合法性，分为两类。
			- 字段属性验证
				- 验证表单中的字段是否符合特定的格式要求，如非空字段是否赋值。
			- 自定义逻辑验证
				- 验证开发者自定义的一些要求。
	- 检查变更字段
		- 当收到用户表单数据的POST请求时，经常需要验证用户是否修改了表单数据然后进行相应的处理，Django的Form提供了has_changed()来判断用户是否修改过表单数据。
- 尝试使用
	- 源码
	- views.py
		- ```python
			def formtest(request):
			    form = UserForm()
			    return render(request, 'render.html', {'user': form})
			
			
			def hello(request):
			    form = UserForm(request.POST)
			    if form.is_valid():
			        return HttpResponse("Hello World!!!")
			    else:
			        return HttpResponse("Error")
			```
	- forms.py
		- ```python
			
			from django.forms import ModelForm, ValidationError
			from app2.models import User
			
			
			class UserForm(ModelForm):
			    class Meta:
			        model = User
			        fields = '__all__'
			
			    def clean(self):
			        cleaned_data = super(UserForm, self).clean()
			        name = cleaned_data.get("name")
			        if name is None or name == "":
			            raise ValidationError("输入name")
			        return cleaned_data
			
			```
- 补充说明
	- 具体介绍了表单的相关内容
	- 本项目参考书为《Python高效开发实战》刘长龙著
	- 使用到的所有重要包会列在requirements.txt文件中
	- 具体代码可以查看我的GitHub，欢迎star或者fork
	- 关于admin定制即个性化管理员站点这里不叙述了，我自己也曾经用Django开发过一个购票Demo，可以查看[我的Github](https://github.com/luanshiyinyang/TicketSell)