from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import CreateUserView 


urlpatterns = {
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/books/', CreateView.as_view(), name="create"),
    path('api/v1/books/<int:pk>/', DetailsView.as_view(), name="details"),
    path('api/v1/auth/signup/', CreateUserView.as_view(), name='register')
}


urlpatterns = format_suffix_patterns(urlpatterns)