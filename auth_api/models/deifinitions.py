from django.db import models


class AccountType(models.TextChoices):
    REGULAR = "regular", "Regular"
    SELLER = "seller", "Seller"
    ADMIN = "admin", "Admin"
    STAFF = "staff", "Staff"


class CourseType(models.TextChoices):
    FREE = "free", "free"
    PAID = "paid", "paid"


class TestType(models.TextChoices):
    DAILY_TEST = "daily_test", "DAILY_TEST"
    COMPETITION = "competition", "COMPETITION"
