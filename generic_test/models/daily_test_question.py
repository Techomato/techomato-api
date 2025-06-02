from django.db import models
from auth_api.models.base_models.base_model import GenericBaseModel
from generic_test.models.daily_test import DailyTest
from generic_test.models.daily_test_question_options import QuestionOption


#
#
# class DailyTestQuestion(GenericBaseModel):
#     test = models.ForeignKey(DailyTest, on_delete=models.CASCADE, related_name="questions")
#     question_text = models.TextField(blank=False, null=False)
#     answer = models.CharField(max_length=1)
#
#     def get_correct_option_text(self):
#         return self.options.filter(label=self.answer).first().text if self.answer else None
#
#     def clean(self):
#         """
#         Ensure the answer is one of the defined option labels.
#         """
#         if self.answer:
#             valid_labels = {opt.label for opt in self.options.all()}
#             if self.answer not in valid_labels:
#                 raise ValidationError({
#                     'answer': f"Answer '{self.answer}' is not among the defined options: {sorted(valid_labels)}"
#                 })
#
#     def save(self, *args, **kwargs):
#         self.full_clean()  # run validation before saving
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.question_text[:60]


class DailyTestQuestion(GenericBaseModel):
    test = models.ForeignKey(DailyTest, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    # The answer will point to one of the related options
    correct_option = models.ForeignKey(QuestionOption, on_delete=models.SET_NULL, null=True, blank=True, related_name='correct_for_questions')

    def __str__(self):
        return self.question_text