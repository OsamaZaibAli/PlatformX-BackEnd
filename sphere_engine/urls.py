from django.urls import include, path, re_path

from .views import create_test

urlpatterns = [
    path('test/create/', create_test)
    # path('fyp/<uuid:id>/', get_fyp),
    # path('fyp/create/', create_fyp),
    # path('fyp/delete/', delete_fyp),
    # path('fyp/', get_organization_fyp),
    # path('fyps/', get_all_fyps),
]
