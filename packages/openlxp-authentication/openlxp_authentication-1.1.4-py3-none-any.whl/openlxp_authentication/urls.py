from django.urls import include, path

from .views import saml_metadata_view

urlpatterns = [
    path('saml/metadata/', saml_metadata_view),
    path('', include('social_django.urls', namespace='social')),
]
