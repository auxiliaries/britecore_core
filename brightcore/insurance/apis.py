from django.urls import path

from . import views


urlpatterns = [
    path('risk_types/', views.RiskTypeAPIView.as_view()),
    path('risk_type/<slug:slug>/', views.RiskTypeAPIView.as_view()),
]
