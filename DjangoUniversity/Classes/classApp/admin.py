from django.contrib import admin
from .models import UniversityClasses
from campusApp.models import UniversityCampus

#register your models here
admin.site.register(UniversityClasses)
admin.site.register(UniversityCampus)