from django.urls import path
from mainApp.views import (
    PostList,
    PostDetail,
    search,
    NewsCreateView,
    NewsUpdateView,
    PostDeleteView,
    upgrade_me, CategorySubscribe, subscribe_category, unsubscribe_category
)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('',  cache_page(60*1)(PostList.as_view()), name='home'),
    path('<int:pk>',  cache_page(60*5)(PostDetail.as_view()), name='post_details'),
    path('search', search, name='search_post'),
    path('create/', NewsCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),

    # subscribe to category urls
    path('category/<int:pk>/', CategorySubscribe.as_view(), name='post_category'),
    path('category/<int:pk>/subscribe/', subscribe_category, name='subscribe_category'),
    path('category/<int:pk>/unsubscribe', unsubscribe_category, name='unsubscribe_category'),
]