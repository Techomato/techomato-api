from django.contrib import admin

from subjects.models.category import Category
from subjects.models.enrollment import Enrollment
from subjects.models.review import Review
from subjects.models.subject import Subject

admin.site.register(Subject)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Enrollment)
