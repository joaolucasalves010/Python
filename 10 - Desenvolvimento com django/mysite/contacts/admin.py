from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from app.models import Choice, Question
import math

# Register your models here.
class CustomAdminSite(admin.AdminSite):
  site_header = "Curso de Python Admin"

admin_site = CustomAdminSite()
admin_site.register(Choice)
admin_site.register(Question)
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
