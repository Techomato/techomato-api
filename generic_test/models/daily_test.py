from django.db import models

from generic_test.models.generic_test import GenericTest
from subject.models.subject import Subject


class DailyTest(GenericTest):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    full_marks = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Daily Test"
        verbose_name_plural = "Daily Tests"

    def __str__(self):
        return f"{self.name} - {self.subject.courseName}"
