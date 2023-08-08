from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
  first_name = serializers.CharField()
  username = serializers.CharField()
  email = serializers.EmailField()
  password = serializers.CharField()
  
  def validate(self , data):
    if data['username']:
      if User.objects.filter(username = data['username']).exists():
        raise serializers.ValidationError("username already exists")
      
    if data['email']:
      if User.objects.filter(email = data['email']).exists():
        raise serializers.ValidationError("This email is already taken !!")
        
    return data   
  
  def create(self , validated_data):
    user = User.objects.create(first_name = validated_data['first_name'] , username = validated_data['username'] , email = validated_data['email'])
    user.set_password(validated_data['password'])
    user.save()
    return validated_data
    print(validated_data)
  
  

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()


class SkillSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Skill
    fields = ['skill']
    
class DepartmentSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ['department']
    
class CourseSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['course']

class StudentSerailaizer(serializers.ModelSerializer):
  # course = CourseSerialzer()
  # skill = SkillSerialzer()
  # department = DepartmentSerialzer()
  
  college = serializers.SerializerMethodField
  
  class Meta:
    model = StudentInfo
    fields = '__all__'
    
  def get_college(self, obj) :
    return "PCPS College"
    
  def validate(self, data):
    if data['name']:
      special_character = "~!@#$%^*&^()"
      for character in data['name']:
        if character in special_character:
          raise serializers.ValidationError("Name should't contain special character")
    
    if data['age']<18:
      raise serializers.ValidationError("Age can't be less than 18 years old")
    
    return data
    
  