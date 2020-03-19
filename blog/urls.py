from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.PostListView.as_view(),name = 'list'),
    path('<int:id>/',views.post,name = 'post_detail'),
]

