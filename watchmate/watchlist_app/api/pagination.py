from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_number'
    page_size_query_param = 'size'              #allow users to define number of items to show in a screen
    max_page_size = 2           # max number of items to show per page. 
    last_page_strings = 'end'