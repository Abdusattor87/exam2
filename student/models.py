from django.db import models

class  Student(models.Model):

    name =models.CharField("Имя",max_length=70,null=False)  
    surname =models.CharField("Фамилия",max_length=70,null=False)  
    mail =models.CharField("Почта",max_length=70,null=False)   
    #course=models.ManyToManyField("course.course" ,related_name="courses",verbose_name="Курс")

    class Meta:
        ordering=["name"]
        verbose_name="Имя"
        verbose_name_plural="Имя"

    def __str__(self) -> str:
        return self.name
 