from django.contrib import admin 
from course.models import Course
from student.models import Student
from grade.models import Grade
from django.contrib.auth.models import Group

 
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):

    
    list_display=("student","course","grade")
 
    search_fields=("student",)
   # list_display_links=("grade")
    list_per_page = 10
 