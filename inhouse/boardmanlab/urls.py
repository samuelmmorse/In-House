from django.urls import path, include

from . import views

urlpatterns = [
    path('/home', views.index, name='index'),
    path('', views.login, name='login'),
    path('/helpsessions', views.helpsessions, name='helpsessions'),
    path('calendar', views.calendar, name='calendar'),
    path('calendarMonth/<int:year>/<int:month>/<int:day>/', views.calendarMonth, name='calendarMonth'),
    path('calendarDay/<int:year>/<int:month>/<int:day>/', views.calendarDay, name='calendarDay'),
    path('/error', views.error, name='error'),
    path('/accounts', include('allauth.urls')),
    path('/Myaccount_Student', views.myAccount_Student, name='myAccount_Student'),
    path('/Myaccount_Helper', views.myAccount_Student, name='myAccount_Student'),
    path('/Myaccount_Student_Edit', views.myAccount_Student_Edit, name='myAccount_Student_Edit'),
]

