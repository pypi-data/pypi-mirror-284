# custom_pagination/pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    """自定义分页类"""

    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "code": 200,
                "msg": "ok",
                "data": {
                    "result": data,
                    "total": self.page.paginator.count,
                    "page": self.page.number,
                    "previous": self.get_previous_link(),
                    "next": self.get_next_link(),
                },
            }
        )
