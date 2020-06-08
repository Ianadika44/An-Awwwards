from django.contrib import admin
from .models import User,Post



class UserAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)
    
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
