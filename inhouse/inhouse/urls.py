from django.contrib import admin
from django.urls import include, path
from boardmanlab.views import index, login, helpsessions, calendarMonth, error, calendarDay, myAccount_Student, myAccount_Helper, myAccount_Student_Edit, myAccount_Helper_Edit
#from inhouse.boardmanlab.views import myAccount_Helper
import oauth2_provider.views as oauth2_views
from django.conf import settings
from boardmanlab.views import ApiEndpoint, Home

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('home/', index),
    path('helpsessions/', helpsessions),
    path('calendarMonth', calendarMonth, name='calendarMonth'),
    path('calendarMonth/<int:year>/<int:month>/<int:day>/', calendarMonth),
    path('calendarDay/<int:year>/<int:month>/<int:day>/', calendarDay, name='calendarDay'),
    path('error/', error),
    path('', login),
    path('allauth', Home.as_view(), name='home'), # new
    # OAuth 2 endpoints:
    # need to pass in a tuple of the endpoints as well as the app's name
    # because the app_name attribute is not set in the included module
    path('o/', include((oauth2_endpoint_views, 'oauth2_provider'), namespace="oauth2_provider")),
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    path('accounts/', include('allauth.urls')),
    path('myAccount_Student/', myAccount_Student),
    path('myAccount_Helper/', myAccount_Helper),
    path('myAccount_Student_Edit/', myAccount_Student_Edit)
]

# Error handling

handler404 = 'boardmanlab.views.error_404'
handler500 = 'boardmanlab.views.error_500'
handler403 = 'boardmanlab.views.error_403'
handler400 = 'boardmanlab.views.error_400'