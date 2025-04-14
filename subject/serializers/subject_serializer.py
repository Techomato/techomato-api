from typing import Optional
from _decimal import Decimal
from rest_framework import serializers

from auth_api.models.user_models.user import User
from auth_api.services.helpers import is_valid_uuid
from subject.export_types.request_data_types.create_subject import (
    CreateSubjectRequestType,
)
from subject.models.category import Category
from subject.models.subject import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> Optional[bool]:
        request: CreateSubjectRequestType = data.get("request_data")
        uid: str = data.get("uid")

        try:
            User.objects.get(id=uid, is_admin=True)
        except User.DoesNotExist:
            raise ValueError("User does not exist or is not an admin.")

        courseName = request.courseName
        courseType = request.courseType
        course_price = request.course_price
        courseCategory = request.courseCategory
        courseShortDescription = request.courseShortDescription
        courseFullDescription = request.courseFullDescription
        image = request.image

        if isinstance(courseName, str) and courseName == "":
            raise ValueError("Course name cannot be empty.")

        if (
            courseName
            and Subject.objects.filter(courseName=courseName, author_id=uid).exists()
        ):
            raise ValueError(f"A subject with the name '{courseName}' already exists.")

        if isinstance(courseType, str) and courseType == "":
            raise ValueError("Course type cannot be empty.")

        if isinstance(courseCategory, str) and courseCategory == "":
            raise ValueError("Course category cannot be empty.")

        if (
            courseCategory
            and is_valid_uuid(courseCategory)
            and not Category.objects.filter(id=courseCategory).exists()
        ):
            raise ValueError("Course category does not exist.")

        if isinstance(courseShortDescription, str) and courseShortDescription == "":
            raise ValueError("Course short description cannot be empty.")

        if isinstance(courseFullDescription, str) and courseFullDescription == "":
            raise ValueError("Course full description cannot be empty.")

        if isinstance(image, str) and image == "":
            raise ValueError("Image cannot be empty.")

        if courseType == "paid":
            if not isinstance(course_price, Decimal):
                raise ValueError("Course Price must be a Decimal.")
            if course_price <= 0:
                raise ValueError("Course Price must be greater than zero.")

        return True

    def create(self, data: dict) -> Subject:
        if self.validate(data):
            request: CreateSubjectRequestType = data.get("request_data")
            uid: str = data.get("uid")

            author: User = User.objects.get(id=uid)

            category: Category = Category.objects.get(id=request.courseCategory)

            courseName = request.courseName
            courseType = request.courseType if request.courseType else "free"
            courseShortDescription = request.courseShortDescription
            courseFullDescription = (
                request.courseFullDescription if request.courseFullDescription else ""
            )
            image = request.image if request.image else ""

            course_price = request.course_price if request.course_price else Decimal(0)

            subject = Subject.objects.create(
                author=author,
                image=image,
                courseName=courseName,
                courseType=courseType,
                courseCategory=category,
                courseShortDescription=courseShortDescription,
                courseFullDescription=courseFullDescription,
                price=course_price,
                is_active=True,
            )

            return subject
