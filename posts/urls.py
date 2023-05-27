from django.urls import path
from django.urls.conf import include
from posts import views
from rest_framework import routers

posts_router = routers.SimpleRouter()
posts_router.register(
    "",
    views.PostModelViewSet,
    basename="posts-crud",
)

urlpatterns = [
    path("crud/", include(posts_router.urls)),
    path("timeline/", views.TimelineListAPIView.as_view(), name="timeline"),
]
