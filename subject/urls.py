from django.urls import path

from subject.views.create_subjects import CreateSubjectView
from subject.views.edit_subject import EditSubjectView
from subject.views.get_all_subjects import AllSubjectsView

urlpatterns = [
    path("create-subject", CreateSubjectView.as_view(), name="Create-subject"),
    path("all-subject", AllSubjectsView.as_view(), name="All-subjects"),
    path("edit-subject", EditSubjectView.as_view(), name="Edit-subject"),
]
