from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)

class Referral(models.Model):
    referring_user = models.ForeignKey(UserProfile, related_name='referrals', on_delete=models.CASCADE)
    referred_user = models.ForeignKey(UserProfile, related_name='referred_by', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)