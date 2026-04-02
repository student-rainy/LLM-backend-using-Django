from django.db import models
from django.contrib.auth.models import User




class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} ({self.course.title})"


# Create your models here.
