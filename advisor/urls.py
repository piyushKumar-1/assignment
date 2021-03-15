from django.urls import path
from .views import AdminAddAdvisor, GetAdvisors, BookAdvisors, GetMyBookings

app_name="advisor"

urlpatterns = [
    path('admin/advisor/', AdminAddAdvisor.as_view(), name="addAdvisor"),
    path('user/<int:user_id>/advisor', GetAdvisors.as_view(), name="getAdvisors"),
    path('user/<int:user_id>/advisor/<int:advisor_id>', BookAdvisors.as_view(), name="bookAdvisors"),
    path('user/<int:user_id>/advisor/booking', GetMyBookings.as_view(), name="bookAdvisors"),
]
