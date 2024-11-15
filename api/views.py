from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, JiraniIssueSerializer, AnnouncementSerializer, NotificationSerializer
from users.models import User
from issues.models import JiraniIssue
from announcements.models import Announcement
from notifications.models import Notification
from rest_framework.parsers import MultiPartParser, FormParser


# ---- User Views ----
class UserListView(APIView):
    """
    API view for listing and creating users.
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    """
    API view for retrieving, updating, and deleting a user.
    """
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'errors': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'errors': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'errors': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---- Issue Views ----
class IssueListCreateView(APIView):
    """
    API view for listing and creating issues.
    """
    def get(self, request):
        issues = JiraniIssue.objects.all()
        serializer = JiraniIssueSerializer(issues, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = JiraniIssueSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class IssueDetailView(APIView):
    """
    API view for retrieving, updating, and deleting issues.
    """
    def get(self, request, pk):
        try:
            issue = JiraniIssue.objects.get(pk=pk)
        except JiraniIssue.DoesNotExist:
            return Response({'errors': 'Issue not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = JiraniIssueSerializer(issue)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            issue = JiraniIssue.objects.get(pk=pk)
        except JiraniIssue.DoesNotExist:
            return Response({'errors': 'Issue not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = JiraniIssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            issue = JiraniIssue.objects.get(pk=pk)
        except JiraniIssue.DoesNotExist:
            return Response({'errors': 'Issue not found'}, status=status.HTTP_404_NOT_FOUND)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---- Announcement Views ----
class AnnouncementListCreateView(APIView):
    """
    API view for listing and creating announcements.
    """
    parser_classes = [MultiPartParser, FormParser]  # To handle file uploads

    def get(self, request):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UploadImageView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnouncementDetailView(APIView):
    """
    API view for retrieving, updating, and deleting an announcement.
    """
    def get(self, request, pk):
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({'errors': 'Announcement not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnouncementSerializer(announcement)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({'errors': 'Announcement not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnouncementSerializer(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({'errors': 'Announcement not found'}, status=status.HTTP_404_NOT_FOUND)
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---- Notification Views ----
class NotificationListView(APIView):
    """
    API view for listing notifications.
    """
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class NotificationDetailView(APIView):
    """
    API view for retrieving, updating, and deleting notifications.
    """
    def get(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            return Response({'errors': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(notification)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            return Response({'errors': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            return Response({'errors': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
