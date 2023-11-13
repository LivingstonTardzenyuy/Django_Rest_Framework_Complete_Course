from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'              #allow users to define number of items to show in a screen
    max_page_size = 2           # max number of items to show per page. 
    last_page_strings = 'end'   


class WatchListOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 6
    limit_query_param = 'start'



class WatchListCPagination(CursorPagination):
    page_size = 3
    ordering = '-created'
    cursor_query_param = 'record'
