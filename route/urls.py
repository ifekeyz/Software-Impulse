from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('newstaff', views.register, name='newstaff'),
    path('logout', views.logout, name='logout'),
    path('features', views.features, name='features'),
    path('availabilty', views.availabilty, name='availabilty'),
    path('singleqty', views.singleqty, name='singleqty'),
    path('release_stoke', views.release_stoke, name='release_stoke'),
    path('bin_portal', views.bin_portal, name='bin_portal'),
    path('bin', views.bin, name='bin'),
    path('<int:singlebin_id>', views.singlebin, name='singlebin'),
    path('search', views.search, name='search'),
    path('filter_report', views.filter_report, name='filter_report'),
    path('report', views.report, name='report'),
    path('stock_position', views.stock_position, name='stock_position'),
]
