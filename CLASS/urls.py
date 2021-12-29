from django.urls import path
from .views import CLASSViews
urlpatterns = [
    path('class_detail/',CLASSViews.as_view())
]
