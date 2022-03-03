"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from book import views
from django.conf import settings
from django.conf.urls.static import static
# import debug_toolbar

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +  [
    path('admin/', admin.site.urls),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('home/',views.homepage,name = "homepage"),
    path('show-all-books/', views.show_all_books, name="show_all_books"),
    path('edit/<int:id>/', views.edit_data, name="edit"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('delete-all-books/', views.delete_all_data, name="delete_all_data"),
    path('soft-delete/<int:id>', views.soft_delete, name="soft_delete"),
    path('form-home/<int:id>', views.form_home, name="form_home"),
]



# urlpatterns = [
#     re_path(r'^aaa$', views.view_a, name='view_a'),
#     re_path(r'^bbb$', views.view_b, name='view_b'),
#     re_path(r'^ccc$', views.view_c, name='view_c'),
#     re_path(r'^ddd$', views.view_d, name='view_d'),
# ]

# urlpatterns = [    
#     path('__debug__/', include('debug_toolbar.urls')),
# ]