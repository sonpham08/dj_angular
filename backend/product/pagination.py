from rest_framework.compat import coreapi, coreschema
from django.utils.encoding import force_text
from django.utils.translation import gettext_lazy as _
from rest_framework import pagination
from rest_framework.response import Response

class StandardResultsSetPagination(pagination.PageNumberPagination):
    """ Generic pagination for all response in vms
    """
    limit =100
    page_size_query_param ='limit'
    max_page_size =10000

    def get_paginated_response(self, data):
        return Response({
        'per_page' : self.page.paginator.per_page,
        'next': self.get_next_link(),

        'previous': self.get_previous_link(),

        'count': self.page.paginator.count,

        'total_pages': self.page.paginator.num_pages,

        'current': self.page.number,

        'results': data

        })