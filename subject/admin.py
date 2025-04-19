from django.contrib import admin

from subject.models.category import Category
from subject.models.enrollment import Enrollment
from subject.models.review import Review
from subject.models.subject import Subject

admin.site.register(Subject)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Enrollment)
