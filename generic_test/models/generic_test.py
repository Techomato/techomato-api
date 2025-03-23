from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models

from auth_api.models.deifinitions import TestType


class GenericTest(GenericBaseModel):
    name = models.CharField(max_length=100)
    test_type = models.CharField(choices=TestType.choices)
    date_start = models.DateTimeField(auto_now_add=True, editable=False)
    date_end = models.DateTimeField()
    image = models.CharField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
