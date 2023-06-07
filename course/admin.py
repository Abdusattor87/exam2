from django.contrib import admin 
from course.models import Course
from django.contrib.auth.models import Group

 
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    model=Course
    list_display=("title","description","duration")
    #list_filter=("category",)
    search_fields=("title",)
    list_display_links=("title",)
    list_per_page = 10
 