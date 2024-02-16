from django.contrib import admin
from .models import Parent,School,Teacher,Student,Balance,Menu,YearForm
# Register your models here.

admin.site.register(Parent)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Balance)
admin.site.register(Menu)
admin.site.register(YearForm)
