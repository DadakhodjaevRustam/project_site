from django.contrib import admin

# Register your models here.

from .models import Product,Access,Lesson,Group,GroupUser


admin.site.register(Product)
admin.site.register(Access)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(GroupUser)
