from django.urls import path
from django.urls.conf import include
from friends import views
from rest_framework import routers

friends_router = routers.SimpleRouter()
friends_router.register(
    "",
    views.FriendModelViewSet,
    basename="friends-crud",
)

urlpatterns = [
    path("crud/", include(friends_router.urls)),
    path("search/", views.FriendSearchAPIView.as_view(), name="friends-search"),
]
