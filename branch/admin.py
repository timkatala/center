from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from django.utils.translation import gettext as _
from .models import *

class CustomUserAdmin(UserAdmin):

	list_filter = ('kassir','branch_head',)
	    
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('branch_head', 'head', 'kassir')}
    #      ),
    # )
	fieldsets = (
	        (_('Status'), {'fields': ('kassir','head','branch_head')}),
	)
	fieldsets += (
	    
	    (_('Shaxsiy malumotlar'), {'fields': ('first_name', 'last_name')}),
	    (_('Ruxsatlar'), {'fields': ('is_active', 'is_staff', 'is_superuser',
	                                 )}),
	    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
admin.site.register(User,CustomUserAdmin)

admin.site.register(Branch)