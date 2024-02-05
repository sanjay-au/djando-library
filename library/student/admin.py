from django.contrib import admin
from student.models import Students
from student.models import MyUser
# Register your models here.
admin.site.register(Students)
admin.site.register(MyUser)