"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from product.views import *
# from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view
from user import urls
# from .views import schema_view

# schema_view = get_swagger_view(title="Swagger Docs")
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_info = openapi.Info(
    title="The API",
    default_version='v1',
    description="""This is a api document for Custom project.

The `swagger-ui` view can be found [here](/cached/swagger).  
The `ReDoc` view can be found [here](/cached/redoc).  
The swagger YAML document can be found [here](/cached/swagger.yaml).  

You can log in using the pre-existing `admin` user with password `Gcsvn123`."""
)

SchemaView = get_schema_view(
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    url(r'^cached/swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=None), name='cschema-json'),
    url(r'^cached/swagger', SchemaView.with_ui('swagger', cache_timeout=None), name='cschema-swagger-ui'),
    url(r'^cached/redoc', SchemaView.with_ui('redoc', cache_timeout=None), name='cschema-redoc'),
    url(r'^admin/', admin.site.urls),
    # url(r'^getData/', get_data),
    # url(r'^swagger/', schema_view),
    url(r'^api/', include('product.urls')),
    url(r'^api/', include('user.urls')),
    url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]

