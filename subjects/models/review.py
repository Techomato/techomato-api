from auth_api.models.base_models.base_model import GenericBaseModel
from django.db import models

from auth_api.models.user_models.user import User


class Review(GenericBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.user.name} -> {self.rating}"
