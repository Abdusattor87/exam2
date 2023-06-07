from django.urls import path, include
from rest_framework import routers
from course.views import CourseViewSet

router = routers.DefaultRouter()  
router.register("", CourseViewSet, "courselist1")  



urlpatterns = [
    path('', include(router.urls)), 
] 