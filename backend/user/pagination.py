from rest_framework.compat import coreapi, coreschema
from django.utils.encoding import force_text
from django.utils.translation import gettext_lazy as _
from rest_framework import pagination
from rest_framework.response import Response
 
# PAGE_SIZE = 100
# PAGE_SIZE_QUERY_PARAM = 'page_size'
# MAX_PAGE_SIZE = 10000

# class UserResultPagination(pagination.PageNumberPagination):
#     page_size = PAGE_SIZE
#     page_size_query_param = PAGE_SIZE_QUERY_PARAM
#     max_page_size = MAX_PAGE_SIZE
#     limit_query_param = 'limit'
#     limit_query_description = _('Only get limit perspective')
    
#     def get_paginated_response(self, data):
#         return Response({
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.page.paginator.count,
#             'total_pages': self.page.paginator.num_pages,
#             'results': data
#         })

#     def get_schema_fields(self, view):
#         assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
#         assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
#         return [
#             coreapi.Field(
#                 name=self.page_query_param,
#                 required=False,
#                 location='query',
#                 schema=coreschema.Integer(
#                     title='Limit',
#                     description=force_text(self.page_query_description)
#                 )
#             ),
#             coreapi.Field(
#                 name=self.limit_query_param,
#                 required=False,
#                 location='query',
#                 schema=coreschema.Integer(
#                     title='Limit',
#                     description=force_text(self.limit_query_description)
#                 )
#             )
#         ]

#     def get_schema_operation_parameters(self, view):
#         parameters = [
#             {
#                 'name': self.page_query_param,
#                 'required': False,
#                 'in': 'query',
#                 'description': force_text(self.page_query_description),
#                 'schema': {
#                     'type': 'integer',
#                 },
#             },
#             {
#                 'name': self.limit_query_param,
#                 'required': False,
#                 'in': 'query',
#                 'description': force_text(self.limit_query_description),
#                 'schema': {
#                     'type': 'integer',
#                 },
#             },
#         ]
#         return parameters


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