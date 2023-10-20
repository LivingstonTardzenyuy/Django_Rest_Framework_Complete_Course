from django.urls import path, include 

from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatFormAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name ='list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name = 'movie-details'),


    path('streamPlatform/', StreamPlatFormAV.as_view(), name = 'StreamPlatFormAV'),
    # path('stream_details/<int:pk>/', StreamPlatFormDetailAV.as_view(), name = 'StreamPlatFormDetailAV'),
]
