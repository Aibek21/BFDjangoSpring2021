from django.urls import path
from main.views import BookViewSet, AuthorApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='main')

urlpatterns = [
    # path('books/', BookViewSet.as_view({'get': 'list'})),
    # path('books/<int:pk>/', BookApiView.as_view()),
    path('authors/<int:pk>/', AuthorApiView.as_view())
]

urlpatterns += router.urls
