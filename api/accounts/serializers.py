from rest_framework import serializers

from accounts.models import User, Verification


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('verification_link',)



class UserSerializer(serializers.ModelSerializer):
    verification = VerificationSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'verification')


