from django.urls import path
from django.conf.urls import include

from brightcore.insurance import apis as insurance_apis

urlpatterns = [
    path('v1/insurance/', include(insurance_apis)),
]
