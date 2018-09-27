from rest_framework import serializers

from accounts.models import User, Verification

from api.profiles.serializers import ProfileSerializer


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('verification_link',)



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'profile')


