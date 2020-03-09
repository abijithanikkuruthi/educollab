from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore, name="explore_index"),
    path('signup/', views.signup),
    path('profile/', views.myprofile, name="my_profile"),
    path('profile/edit', views.profile_edit, name="profile_edit"),
    path('profile/<str:uname>', views.profile_user),
    path('subject/<sid>', views.subject_index, name="subjects"),
    path('subject/<sid>/subscription/add', views.subject_subscription_create, name="subject_subscription_create"),
    path('subscription/', views.subscription_index, name="subscription_index"),
    path('subscription/<sid>/delete', views.subscription_delete, name="subscription_delete"),
    
    path('curriculum/', views.curriculum_index, name="curriculum_index"),
    path('curriculum/new', views.curriculum_create, name="curriculum_create"),
    path('curriculum/<int:c_id>', views.curriculum_show, name="curriculum_show"),
    path('curriculum/<int:c_id>/edit',
         views.curriculum_update, name="curriculum_update"),
    path('curriculum/<int:c_id>/subscription/add', views.curriculum_subscription_create, name="curriculum_subscription_create"),
    path('curriculum/<int:c_id>/bit/<int:b_id>/', views.update_bit, name="bit_show"),
    path('curriculum/<int:c_id>/bit/new', views.create_bit),
    path('curriculum/<int:c_id>/bit/<int:b_id>/edit', views.update_bit),
    path('curriculum/<int:c_id>/upvote/new', views.curriculum_upvote_create, name="curriculum_upvote_create"),
    path('curriculum/<int:c_id>/upvote/delete', views.curriculum_upvote_delete, name="curriculum_upvote_delete"),
    path('curriculum/<int:c_id>/comment/new', views.curriculum_comment_create, name="curriculum_comment_create"),
    path('feeds/<int:c_id>/comment/new', views.feeds_comment_create, name="feeds_comment_create"),
    path('feeds/<int:u_id>/upvote/new', views.feeds_upvote_create, name="feeds_upvote_create"),
    path('feeds/<int:u_id>/upvote/delete', views.feeds_upvote_delete, name="feeds_upvote_delete"),
    path('comment/<str:c_type>/<int:c_id>', views.comment),
    path('upvote/<str:u_type>/<int:u_id>', views.upvote, name="upvote"),
    path('downvote/<str:u_type>/<int:u_id>', views.downvote, name="downvote")
]
