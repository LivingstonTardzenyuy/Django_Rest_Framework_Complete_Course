from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottle(UserRateThrottle):               # the first name before Throttle delote the class name we are using.
    scope = 'review-create'


class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'



