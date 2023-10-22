from django.urls import path, include 

from watchlist_app.api.views import(
                                    WatchListAV,
                                    WatchListDetailAV,
                                    StreamPlatFormAV,
                                    StreamPlatFormDetailAV,
                                    ReviewList,
                                    ReviewDetails)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name ='list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name = 'movie-details'),


    path('streamPlatform/', StreamPlatFormAV.as_view(), name = 'stream-list'),
    path('stream/<int:pk>/', StreamPlatFormDetailAV.as_view(), name = 'StreamPlatFormDetailAV'),



    path('review_list/', ReviewList.as_view(), name = 'review_list'),
    path('stream/review/<int:pk>/',  ReviewDetails.as_view(), name = 'review_details')
]
