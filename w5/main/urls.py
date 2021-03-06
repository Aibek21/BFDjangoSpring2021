from django.urls import path
from main.views import BookApiView, AuthorApiView

urlpatterns = [
    path('books/', BookApiView.as_view()),
    # path('books/<int:pk>/', BookApiView.as_view()),
    path('authors/<int:pk>/', AuthorApiView.as_view())
]
