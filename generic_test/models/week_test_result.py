from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models
from auth_api.models.user_models.user import User
from generic_test.models.generic_test import GenericTest


class WeekTestResult(GenericBaseModel):
    test = models.ForeignKey(GenericTest, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    percentage_marks = models.PositiveIntegerField(default=0)
    total_marks = models.PositiveIntegerField(default=0)
    is_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.test.name}"
