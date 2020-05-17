from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('', views.index, name='index'),
    path('review/<int:pk>', views.review, name='review'),
    path('review_list/', views.review_list, name='review_list'),
    path('review_detail/<int:pk>', views.review_detail, name='review_detail'),
    path('<int:pk>/like', views.like, name='like'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('comments/<int:pk>/',views.comments, name='comments'),
    path('<int:review_pk>/comments/<int:comment_pk>', views.comments_delete, name='comments_delete'),

    ]