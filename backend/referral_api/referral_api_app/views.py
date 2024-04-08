# referral_api/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UserProfile, Referral
from .serializers import UserProfileSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"user_id": serializer.data['id'], "message": "User registered successfully"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user_profile = request.user.userprofile
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    user_profile = request.user.userprofile
    referred_users = Referral.objects.filter(referring_user=user_profile)
    serializer = UserProfileSerializer(referred_users, many=True)
    return Response(serializer.data)
