from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models

from auth_api.models.user_models.user import User
from subjects.models.review import Review


class Subject(GenericBaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=50)
    courseType = models.CharField(max_length=50)
    courseCategory = models.CharField(max_length=50)
    review = models.ManyToManyField(Review, on_delete=models.CASCADE, null=False)
    rating = models.PositiveIntegerField()
    courseDescription = models.TextField()
    image = models.ImageField(upload_to="subjectPics/")
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} -> {self.courseName}"
