from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from student.models import Student
from student.serializers import  StudentSerializer

 
class StudentViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer