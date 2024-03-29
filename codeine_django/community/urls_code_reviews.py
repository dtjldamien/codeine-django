from django.urls import path

from . import views_code_review, views_code_review_comments

urlpatterns = [
    # code review views
    path('', views_code_review.code_review_view,
         name='Create/Get all/Search Code Reviews'),
    path('/<slug:pk>', views_code_review.single_code_review_view,
         name='Read/update/delete for Code Review'),
    path('/user/', views_code_review.user_code_review_view,
         name='Get user\'s Code Review'),
    path('/<slug:pk>/engagements', views_code_review.code_review_engagement_view,
         name='Like/Unlike Code Review'),

    # code review comment views
    path('/<slug:code_review_id>/comments', views_code_review_comments.code_review_comment_view,
         name='Create/Get all/Search Code Review Comments'),
    path('/<slug:code_review_id>/comments/<slug:pk>', views_code_review_comments.single_code_review_comment_view,
         name='Read/update/delete Code Review Comments'),
    path('/<slug:code_review_id>/comments/<slug:pk>/engagements', views_code_review_comments.code_review_comment_engagement_view,
         name='Like/Unlike article comments'),

    # code review engagement views
    #     path('/<slug:code_review_id>/engagement', views_code_review_engagement.code_review_engagement_view,
    #          name='Create/Get all/Search Engagements'),
    #     path('/<slug:code_review_id>/engagement/<slug:pk>',
    #          views_code_review_engagement.single_code_review_engagement_view, name='Read/update/delete for Engagements'),
]
