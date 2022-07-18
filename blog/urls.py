from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:post_id>', views.detail, name='detail')
]
