from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from course.models import Course
from course.serializers import  CourseSerializer

class CourseViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    serializer_class =  Course