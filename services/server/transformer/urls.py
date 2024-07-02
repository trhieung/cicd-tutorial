from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# app_name = 'transformer'
# urlpatterns = [
#     # # for testing template
#     # path("clone_index/", views.clone_index, name="clone_index"),
#     # path("base/", views.base, name="base"),
#     # path("category/", views.category, name="category"),
#     # path("predict/", views.predict, name="predict"),

#     # # runing path
#     # path("", views.index, name="index"),
#     # path("Category/", views.index, name="index"),
    
#     # path('<str:category>/', views.category, name='category'),

#     # restcdjango
#     path('amazon_labels/', views.AmazonlabelsList.as_view()),
#     path('amazon_labels/<int:pk>/', views.AmazonLabelsDetail.as_view()),
#     path('amazon_labels/<int:pk>/highlight/', views.AmazonLabelsHighlight.as_view()),

#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),

#     path('', views.api_root),
# ]
app_name = 'transformer'
# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),

    path('labels/', views.AmazonlabelsList.as_view(), name='label-list'),
    path('labels/<int:pk>/', views.AmazonLabelsDetail.as_view(), name='label-detail'),
    path('labels/<int:pk>/highlight/', views.AmazonLabelsHighlight.as_view(), name='label-highlight'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])
