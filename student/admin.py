from django.contrib import admin 
from student.models import Student
from django.contrib.auth.models import Group

 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    model=Student
    list_display=("id",'name',"surname","mail")
    #list_filter=("category",)
    search_fields=("name",)
    list_display_links=("id","name")
    list_per_page = 10
 