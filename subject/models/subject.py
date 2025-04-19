from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models

from auth_api.models.deifinitions import CourseType
from auth_api.models.user_models.user import User
from subject.models.category import Category
from subject.models.review import Review


class Subject(GenericBaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=50)
    courseType = models.CharField(
        max_length=10, choices=CourseType.choices, default=CourseType.FREE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    courseCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    review = models.ManyToManyField(Review, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True, default=0)
    courseShortDescription = models.CharField(max_length=200)
    courseFullDescription = models.TextField(null=True, blank=True)
    image = models.CharField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.courseName} published by {self.author} on {self.created_at} ({self.courseType})"
