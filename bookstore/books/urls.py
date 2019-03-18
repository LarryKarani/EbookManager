from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView 


urlpatterns = {
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/books/', CreateView.as_view(), name="create"),
    path('api/v1/books/<int:pk>/', DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)