from django.urls import path

from company import views

app_name = 'company'

urlpatterns = [
    path('company', views.CompanyApi),
    path('company/([0-9]+)', views.CompanyApi)
]
