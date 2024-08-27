from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bookstore import view

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    re_path('bookstore/', include('order.urls')),
    re_path('bookstore/', include('product.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("update_server/", view.update, name="update"),
    path("hello/", view.hello_world, name="hello_world"),
]
urlpatterns += staticfiles_urlpatterns()