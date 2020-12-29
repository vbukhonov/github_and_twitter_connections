from django.urls import path
from .views import register, realtime

urlpatterns = [
    path('realtime/<slug:dev_1_id>/<slug:dev_2_id>/', realtime, name="realtime"),
    path('register/<slug:dev_1_id>/<slug:dev_2_id>/', register, name="register")
]
