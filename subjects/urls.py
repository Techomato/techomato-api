from django.urls import path

from subjects.views.create_subjects import CreateSubjectView

urlpatterns = [
    path("create-subject", CreateSubjectView.as_view(), name="Create-subject"),
]
