from django.contrib import admin
from .models import Subject, Course, Module, Content

@admin.register(Subject)
class SubectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug':('title',)}

class ModuleIniline(admin.StackedInline):
	model = Module
	extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug':('title',)}
	inlines = [ModuleIniline]

class ContentInline(admin.StackedInline):
	model = Content
	extra = 0

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
	inlines = [ContentInline]