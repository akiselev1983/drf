from django.urls import path

from .views import (
    AdminToUserView,
    BlockAdminUserView,
    BlockUserView,
    TestEmail,
    UnBlockAdminUserView,
    UnBlockUserView,
    UserAddAvatarView,
    UserListCreateView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatar', UserAddAvatarView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),
    path('/<int:pk>/block_user', BlockUserView.as_view()),
    path('/<int:pk>/un_block_user', UnBlockUserView.as_view()),
    path('/<int:pk>/block_admin', BlockAdminUserView.as_view()),
    path('/<int:pk>/un_block_admin', UnBlockAdminUserView.as_view()),
    path('/email', TestEmail.as_view())
]
