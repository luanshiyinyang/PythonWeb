
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
