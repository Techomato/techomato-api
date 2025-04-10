from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models

from auth_api.models.user_models.user import User
from subjects.models.subject import Subject


class Enrollment(GenericBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    enrolled_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.user.username} is enrolled to the {self.subjects.name}"
