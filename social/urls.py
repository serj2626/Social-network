from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, \
    ProfileEditView, AddFollower, RemoveFollower, AddLike, AddDislike, UserSearch, ListFollowers, AddCommentLike, \
    AddCommentDislike

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment_like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment_dislike'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list_followers'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add_follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove_follower'),
    path('search/', UserSearch.as_view(), name='profile_search'),
]
