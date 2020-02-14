from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from django.utils.translation import gettext as _
from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)
class CustomUserAdmin(UserAdmin):

	list_filter = ('kassir','branch_head',)
	    
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('branch_head', 'head', 'kassir')}
    #      ),
    # )
	fieldsets = (
	        (_('Status'), {'fields': ('branch','kassir','head','branch_head')}),
	)
	fieldsets += (
	    
	    (_('Shaxsiy malumotlar'), {'fields': ('first_name', 'last_name')}),

	    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
admin.site.register(User,CustomUserAdmin)

admin.site.register(Branch)