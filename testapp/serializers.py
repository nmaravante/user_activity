from rest_framework import serializers
from testapp.models import *




class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileActivity
        fields = ['activity_start_date','start_date','end_date',]


#########################         StringRelatedField  #####

# class ProfileSerializer(serializers.ModelSerializer):
#     PRofile_Activity = serializers.StringRelatedField(many=True) 
#     class Meta:
#         model = Profile
#         fields = ['user_id', 'real_name', 'timezone','PRofile_Activity']


#######    primary key related field  $#######

# class ProfileSerializer(serializers.ModelSerializer):
#     PRofile_Activity = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     class Meta:
#         model = Profile
#         fields = ['user_id', 'real_name', 'timezone','PRofile_Activity']


########  nested relation ship   ###########

class ProfileSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['user_id', 'real_name', 'timezone','activity_periods']
