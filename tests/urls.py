from django.urls import path

from tests.views import TestsAPIView

urlpatterns = [
    path('', TestsAPIView.as_view()),
]