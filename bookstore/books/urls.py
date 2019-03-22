from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, CreateUserView, schema_view
from rest_framework_jwt.views import obtain_jwt_token
 



urlpatterns = {
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/books/', CreateView.as_view(), name="create"),
    path('api/v1/books/<int:pk>/', DetailsView.as_view(), name="details"),
    path('api/v1/auth/signup/', CreateUserView.as_view(), name='register'),
    path('swaggerdocs/', schema_view),
    path('api-token-auth/', obtain_jwt_token),
    
}


urlpatterns = format_suffix_patterns(urlpatterns)