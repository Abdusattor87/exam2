from django.db import models
from student.models import Student
from course.models import Course

class  Grade(models.Model):

    student=models.ForeignKey("student.student",on_delete=models.CASCADE,related_name="students",verbose_name="Студент",null=False)
    course=models.ForeignKey("course.course",on_delete=models.CASCADE,related_name="courses",verbose_name="Оценки",null=False)
    grade =models.DecimalField("Оценка",max_length=10,max_digits=6,decimal_places=0) 

    class Meta:
        ordering=["grade"]
        verbose_name="Оценка"
        verbose_name_plural="Оценки"


 