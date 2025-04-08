from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models


class Category(GenericBaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.id}"
