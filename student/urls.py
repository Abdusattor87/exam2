from django.urls import path, include
from rest_framework import routers
from student.views import StudentViewSet

router = routers.DefaultRouter()  
router.register("", StudentViewSet, "studentlist")  



urlpatterns = [
    path('', include(router.urls)), 
] 