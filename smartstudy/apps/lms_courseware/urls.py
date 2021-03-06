"""lms_courseware urls file."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.lms_courseware.views import (
    ChapterViewSet,
    CourseViewSet,
    SubChapterViewSet,
    UserViewSet,
)

app_name = "lms_courseware"

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"chapters", ChapterViewSet, basename="chapters")
router.register(r"subchapters", SubChapterViewSet, basename="subchapters")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
