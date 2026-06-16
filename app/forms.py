from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class myform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]

class myuserform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","last_login","date_joined","is_active"]


class myadminform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
