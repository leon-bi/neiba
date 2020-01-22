from django.urls import path
from Neighbour import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,NeighbourhoodListView,NeighbourhoodDetailView,NeighbourhoodCreateView,NeighbourhoodUpdateView,NeighbourhoodDeleteView,BusinessListView,BusinessDetailView,BusinessCreateView,BusinessUpdateView,BusinessDeleteView)



urlpatterns = [
    path('',PostListView.as_view(),name='home'), 
    path('neiba/',NeighbourhoodListView.as_view(),name='neiba-home'),
    path('business/',BusinessListView.as_view(),name='biz-home'),

    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('neiba/<int:pk>/',NeighbourhoodDetailView.as_view(),name = 'neiba-detail'),
    path('business/<int:pk>/',BusinessDetailView.as_view(),name = 'business-detail'), 

    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('neiba/new/',NeighbourhoodCreateView.as_view(),name = 'neiba-create'),
    path('business/new/',BusinessCreateView.as_view(),name = 'business-create'),

    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),
    path('neiba/<int:pk>/update/',NeighbourhoodUpdateView.as_view(),name = 'neiba-update'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(),name = 'business-update'),

    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    path('neiba/<int:pk>/delete/',NeighbourhoodDeleteView.as_view(),name = 'neiba-delete'),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(),name = 'business-delete'),

    
]
