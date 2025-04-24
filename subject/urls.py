from django.urls import path

from subject.views.create_enroll_subject import EnrollSubjectView
from subject.views.create_subjects import CreateSubjectView
from subject.views.edit_subject import EditSubjectView
from subject.views.get_all_subjects import AllSubjectsView
from subject.views.get_subject import GetSubjectView

urlpatterns = [
    path("create-subject", CreateSubjectView.as_view(), name="Create-subject"),
    path("all-subject", AllSubjectsView.as_view(), name="All-subjects"),
    path("edit-subject", EditSubjectView.as_view(), name="Edit-subject"),
    path("get-subject", GetSubjectView.as_view(), name="Get-subject"),
    path("enroll-subject", EnrollSubjectView.as_view(), name="Enroll-Subject"),
]
