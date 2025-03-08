from django.contrib import admin

from subjects.models.review import Review
from subjects.models.subject import Subject

admin.site.register(Subject)
admin.site.register(Review)
