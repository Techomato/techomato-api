from typing import Optional
from rest_framework import serializers

from auth_api.auth_exceptions.user_exceptions import UserNotPermittedError
from auth_api.models.user_models.user import User
from subject.exceptions.subject_exceptions import (
    SubjectNotFoundError,
    AlreadyEnrolledError,
)
from subject.models.enrollment import Enrollment
from subject.models.subject import Subject


class SubjectEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> dict:
        uid: str = data.get("uid")
        subject_id: str = data.get("subject_id")

        try:
            user = User.objects.get(
                id=uid, is_admin=False, is_deleted=False, is_active=True
            )
        except User.DoesNotExist:
            raise UserNotPermittedError()

        try:
            subject = Subject.objects.get(
                id=subject_id, is_active=True, is_deleted=False
            )
        except Subject.DoesNotExist:
            raise SubjectNotFoundError()

        # Check if already enrolled
        if Enrollment.objects.filter(user=user, subjects=subject).exists():
            raise AlreadyEnrolledError()

        # Attach validated user and subject to the data
        data["user"] = user
        data["subject"] = subject
        return data

    def create(self, data: dict) -> Enrollment:
        validated_data = self.validate(data)

        # Create enrollment and associate the subject
        # enrollment = Enrollment.objects.create(user=validated_data["user"])
        # enrollment.subjects.add(validated_data["subject"])
        enrollment = Enrollment.objects.create(
            user=validated_data["user"]
        )  # Save the instance
        enrollment.subjects.add(
            validated_data["subject"]
        )  # Add the subject after saving

        return enrollment
