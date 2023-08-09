from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from APItest.models import *
from APItest.serializer import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator

# Create your views here.

# --------using class based API view for simple API test
class IndexView(APIView):
  def get(self , request):
    return Response({'name':"Roman Humagain",
                     'class':"level 4" ,
                     'course':'BSC Hons' , 
                     'ID':2214109})
    
  def post(self, request):
    data = request.data
    print("data" , data)
    return Response({'data':data, 'message':"you hit the post method"})
    
  def put(self, request):
    return Response({"status":True, 'message':"you hit the put method"}, status=status.HTTP_200_OK )
  
  def patch(self , request):
    return Response({'status':True , 'message':"You hit the patch method"} , status=status.HTTP_200_OK)
  
  def delete(self , request):
    return Response({'status':True , 'message':"You hit the delete method"} , status=status.HTTP_200_OK)
  
  
class PersonView(APIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get(self , request):
    print("logged in" ,request.user)
    person =  Person.objects.all()
    page = request.GET.get('page' , 1)
    content_size_in_page = 2
    try:
      paginator = Paginator(person , content_size_in_page)
      serailizer = PersonSerailizer(paginator.page(page), many = True)
      return Response(serailizer.data)
    except Exception as e:
      return Response({"message":"invalid page number"})
    
  def post(self , request):
    data = request.data
    serailizer = PersonSerailizer(data=data)
    if serailizer.is_valid():
      serailizer.save()
      return Response({'message':'successfully created', 'data' :serailizer.validated_data}, status=status.HTTP_201_CREATED)
    return Response(serailizer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def put(self , request):
    data = request.data
    person = Person.objects.get(id = data['id'])
    serailizer = PersonSerailizer(person, data=data)
    if serailizer.is_valid():
      serailizer.save()
      return Response({'message':'successfully updated', 'data' :serailizer.validated_data}, status=status.HTTP_201_CREATED)
    return Response(serailizer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self , request):
    data = request.data
    person = Person.objects.get(id = data['id'])
    serailizer = PersonSerailizer(person, data=data , partial = True)
    if serailizer.is_valid():
      serailizer.save()
      return Response({'message':'successfully updated', 'data' :serailizer.validated_data}, status=status.HTTP_201_CREATED)
    return Response(serailizer.errors , status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self , request):
    data = request.data
    person = Person.objects.get(id = data['id'])
    person.delete()
    return Response({'message':f'successfully deleted {person.name}'}, status=status.HTTP_200_OK)
  
  

# ---------to create the user--------------
class RegisterUser(APIView):
  def post(self, request):
    data = request.data
    serializers = RegisterSerializer(data=data)
    if serializers.is_valid():
      serializers.save()
      return Response({'message':'user created successfully', 'data':serializers.validated_data }, status=status.HTTP_201_CREATED)
    else:
      return Response({'message':serializers.errors }, status=status.HTTP_400_BAD_REQUEST)
    

class LoginUser(APIView):
  def post(self, request):
    data = request.data
    serializers = LoginSerailizer(data= data)
    if serializers.is_valid():
      user = authenticate(username = serializers.data['username'] , password = serializers.data['password'])

      if user is not None:
        token , _ = Token.objects.get_or_create(user = user)
        return Response({'status':True,"message":f"successfully logged in {user.first_name}"} , status=status.HTTP_200_OK)
      
      if user is None:
        return Response({'status':False,"message":"invalid credentials"} , status=status.HTTP_400_BAD_REQUEST)
      
    
    return Response({'status':False , 'message':serializers.errors} , status=status.HTTP_400_BAD_REQUEST)

    
class PersonViewSet(viewsets.ModelViewSet):
  serializer_class = PersonSerailizer
  queryset= Person.objects.all()
  http_method_names = ['get','post']  # to allow specific methods
  
  def list(self, request):
    queryset = self.queryset
    search = request.GET.get('search')
    
    if search:
        queryset = queryset.filter(name__startswith=search)
    
    serializer = PersonSerailizer(queryset, many=True)
    return Response(serializer.data)

      
    
  
  
  