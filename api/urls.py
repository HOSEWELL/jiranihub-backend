from django.urls import path
from .views import (
    UserListView, UserDetailView,
    IssueListCreateView, IssueDetailView,
    AnnouncementListCreateView, AnnouncementDetailView,
    NotificationListView, NotificationDetailView, 
)

urlpatterns = [
    # User endpoints
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
    # Issue endpoints
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue-detail'),
    
    # Announcement endpoints
    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    
    # Notification endpoints
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
]

