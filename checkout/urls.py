from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('<int:id>/',
         views.CreateStripeCheckoutSessionView.as_view(), name='checkout'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
