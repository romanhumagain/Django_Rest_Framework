from rest_framework import serializers
from APItest. models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
  first_name = serializers.CharField()
  username = serializers.CharField()
  email = serializers.EmailField()
  password = serializers.CharField()
  
  def validate(self, data):
    if data['username']:
       if User.objects.filter(username = data['username']).exists():
         raise serializers.ValidationError("this username already exists !!")
    if data['email']:
      if User.objects.filter(email = data['email']).exists():
        raise serializers.ValidationError("this email already exists !!")

    return data
  
  def create(self, validated_data):
    user = User.objects.create(first_name = validated_data['first_name'], username = validated_data['username'] , email = validated_data['email'])
    user.set_password(validated_data['password'])
    user.save()
    
    return validated_data
        
class LoginSerailizer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person_Skill
    fields = '__all__'

class PersonSerailizer(serializers.ModelSerializer):
  skill = SkillSerializer(read_only = True)
  class Meta:
    model = Person
    fields = '__all__'
    
  def validate(self , data):
    age = data.get('age')
    if age:
      if data['age']<18:
        raise serializers.ValidationError("Age cannot be less then 18")
      
    special_character = "~!@#$%^*&^()"
    for letter in data['name']:
        if letter in special_character:
          raise serializers.ValidationError("name should't contain any special character")
        
    return data
        
        
    
    