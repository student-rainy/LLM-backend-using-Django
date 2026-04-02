from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseListCreate.as_view(), name="courses"),
    path("courses/<int:pk>/", views.CourseDetail.as_view(), name="course-detail"),
    path(
        "courses/<int:course_id>/lessons/",
        views.LessonListCreate.as_view(),
        name="lesson-list-create",
    ),
]
