from rest_framework import serializers
from users.models import User
from issues.models import JiraniIssue
from announcements.models import Announcement
from notifications.models import Notification


# users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number']


# issues 

class JiraniIssueSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = JiraniIssue
        fields = ['title', 'description', 'user']

    def create(self, validated_data):
        # Check if the user is authenticated
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['user'] = user
        else:
            validated_data['user'] = User.objects.get(username='anonymous')  # Assign a default user or create one
        return super().create(validated_data)


# announcements 
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'content', 'created_at', 'image']



# notifications



class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    issue = JiraniIssueSerializer(required=False)
    announcement = AnnouncementSerializer(required=False)

    class Meta:
        model = Notification
        fields = ['id', 'notification_type', 'message', 'user', 'issue', 'announcement', 'created_at']

