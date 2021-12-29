from django.urls import path
from .views import SchoolViews
urlpatterns = [
    path('School/',SchoolViews.as_view())
]
