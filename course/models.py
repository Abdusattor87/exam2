from django.db import models

class Course(models.Model):

    title =models.CharField("Курс",max_length=70,null=False)    
    description =models.CharField("Описание",max_length=370,null=True)
    duration =models.DecimalField("Длительность",max_length=10,max_digits=6,decimal_places=0) 


    class Meta:
        ordering=["title"]
        verbose_name="Курс"
        verbose_name_plural="Курсы"

    def __str__(self) -> str:
        return self.title
 