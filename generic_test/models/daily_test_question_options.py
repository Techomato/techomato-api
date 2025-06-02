from django.db import models

from generic_test.models.daily_test_question import DailyTestQuestion
#
#
# class Option(GenericBaseModel):
#     question = models.ForeignKey(DailyTestQuestion, on_delete=models.CASCADE, related_name="options")
#     label = models.CharField(max_length=1,blank=False, null=False)  # e.g., A, B, C, D
#     text = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         unique_together = ('question', 'label')
#         ordering = ['label']
#
#     def __str__(self):
#         return f"{self.label}. {self.text}"

class QuestionOption(models.Model):
    question = models.ForeignKey(DailyTestQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text