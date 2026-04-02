from rest_framework import generics, permissions
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonListCreate(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return Lesson.objects.filter(course__id=course_id)

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.kwargs["course_id"])
        serializer.save(course=course)


# Create your views here.
