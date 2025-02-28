from typing import Optional
from rest_framework import serializers

from auth_api.export_types.validation_types.validation_result import ValidationResult
from auth_api.models.user_models.user import User
from auth_api.services.encryption_services.encryption_service import EncryptionServices
from auth_api.services.helpers import (
    validate_email,
    validate_name,
    validate_password,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> Optional[bool]:
        email = data.get("email")
        name = data.get("name")
        password = data.get("password")
        username = data.get("username")

        # Email Validation
        if email and email != "" and isinstance(email, str):
            validation_result_email: ValidationResult = validate_email(email)
            is_validated_email = validation_result_email.is_validated
            if not is_validated_email:
                raise serializers.ValidationError(detail=validation_result_email.error)
        else:
            raise serializers.ValidationError(detail="Email should not be empty.")

        # Name Validation
        if name and name != "" and isinstance(name, str):
            validation_result_name: ValidationResult = validate_name(name)
            is_validated_name = validation_result_name.is_validated
            if not is_validated_name:
                raise serializers.ValidationError(detail=validation_result_name.error)
        else:
            raise serializers.ValidationError(detail="Name should not be empty.")

        # Username Validation
        if not username and username != "" and isinstance(username, str):
            raise serializers.ValidationError(detail="Username should not be empty.")

        # Password Validation
        if password and password != "" and isinstance(password, str):
            validation_result_password: ValidationResult = validate_password(password)
            is_validated_password = validation_result_password.is_validated
            if not is_validated_password:
                raise serializers.ValidationError(validation_result_password.error)
        else:
            raise serializers.ValidationError(detail="Password should not be empty.")

        return True

    def create(self, data: dict) -> User:
        if self.validate(data):
            email = data.get("email")
            name = data.get("name")
            password = data.get("password")
            username = data.get("username")
            user = User(
                username=username,
                email=email,
                name=name,
                password=EncryptionServices().encrypt(password),
            )
            user.save()
            return user
