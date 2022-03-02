from django.urls import path, include

from . import views

urlpatterns = [
    path('/home', views.index, name='index'),
    path('', views.login, name='login'),
    path('/helpsessions', views.helpsessions, name='helpsessions'),
    path('/manageHelpSessions', views.managehelpsessions, name='manageHelpSessions'),
    path('/createHelpSession', views.createHelpSession, name='createHelpSession'),
    path('/editHelpSession', views.editHelpSession, name='editHelpSession'),
    path('calendar', views.calendar, name='calendar'),
    path('calendarMonth/<int:year>/<int:month>/<int:day>/', views.calendarMonth, name='calendarMonth'),
    path('calendarDay/<int:year>/<int:month>/<int:day>/', views.calendarDay, name='calendarDay'),
    path('/error', views.success, name='error'),
    path('/error', views.error, name='error'),
    path('/accounts', include('allauth.urls')),
]

