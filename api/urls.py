from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
        path("", views.index, name="index"),
        path("snip/", views.SnippetList.as_view()),
        path("snip/<int:pk>/", views.SnippetDetail.as_view()),
        path("users/", views.UserList.as_view()),
        path("users/<int:pk>/", views.UserDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
