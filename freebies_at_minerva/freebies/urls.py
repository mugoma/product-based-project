from django.urls import path
from . import views

app_name = 'freebies'

urlpatterns = [

    path('create/', views.FreebiesCreateView.as_view(), name='create'),
    path('list/', views.FreebiesListView.as_view(), name='list'),
    path('search/', views.FreebiesSearchView.as_view(), name='search'),
    path('detail/<pk>/', views.FreebiesDetailView.as_view(), name="detail"),
    path('update/<pk>/', views.FreebiesUpdateView.as_view(), name="update"),
    path('delete/<pk>/', views.FreebiesDeleteView.as_view(), name='delete'),
    path('', views.FreebiesListView.as_view(), name='index')

]
