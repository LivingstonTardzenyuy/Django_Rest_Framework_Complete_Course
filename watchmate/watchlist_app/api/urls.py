from django.urls import path, include 

from watchlist_app.api.views import(
                                    WatchListAV,
                                    WatchListDetailAV,
                                    StreamPlatFormAV,
                                    StreamPlatFormDetailAV,
                                    ReviewList,
                                    ReviewDetails, ReviewCreate,
                                    StreamPlatFormViewSets,
                                    )

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatFormViewSets, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name ='list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name = 'movie-details'),


    # path('streamPlatform/', StreamPlatFormAV.as_view(), name = 'stream-list'),
    # path('stream/<int:pk>/', StreamPlatFormDetailAV.as_view(), name = 'StreamPlatFormDetailAV'),


    path('review_list/review-create/', ReviewCreate.as_view(), name = 'review_list'),
    path('review_list/<int:pk>/review/', ReviewList.as_view(), name = 'review_list'),

    path('stream/review/<int:pk>/',  ReviewDetails.as_view(), name = 'review_details'),


    path('', include(router.urls)),
]
