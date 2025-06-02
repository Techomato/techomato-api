from django.contrib import admin

from generic_test.models.daily_test import DailyTest
from generic_test.models.daily_test_question import DailyTestQuestion
from generic_test.models.daily_test_question_options import QuestionOption
from generic_test.models.generic_test import GenericTest

admin.site.register(GenericTest)
admin.site.register(DailyTest)
admin.site.register(DailyTestQuestion)
admin.site.register(QuestionOption)
