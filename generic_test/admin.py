from django.contrib import admin

from generic_test.models.generic_test import GenericTest
from generic_test.models.week_test_result import WeekTestResult

admin.site.register(GenericTest)
admin.site.register(WeekTestResult)
