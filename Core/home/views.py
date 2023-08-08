from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['POST'])
def login(request):
  data = request.data
  serializer = LoginSerializer(data=data)
  if serializer.is_valid():
    return Response({'message':'Successfully Login'})
  return Response(serializer.error_messages)


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):
    personal_info = {
        'name': "Roman Humagain",
        'course': "BSC Hons",
        'Skills': ['python', 'django']
    }

    if request.method == "GET":
        search = request.GET.get('search')
        print(search)
        print("you Hit the get method")

    if request.method == "POST":
        data = request.data
        print("you Hit the post method")  # moved this line before the return statement
        return Response(data)

    return Response(personal_info)
  
  
@api_view(['GET', 'POST', 'PATCH', 'PUT' , 'DELETE'])
def StudentView(request):
  if request.method == 'GET':
    student = StudentInfo.objects.all()
    serializer = StudentSerailaizer(student , many = True)
    return Response(serializer.data)
  
  if request.method == "POST":
    data = request.data
    serializer = StudentSerailaizer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data)
    return Response(serializer.errors)
  
  if request.method == "PUT":
    data = request.data
    student = StudentInfo.objects.get(id = data['id'])
    serializer = StudentSerailaizer(student , data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data)
    return Response(serializer.errors)
  
  if request.method == "PATCH":
    data = request.data
    student = StudentInfo.objects.get(id = data['id'])
    serializer = StudentSerailaizer(student , data=data , partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data)
    return Response(serializer.errors)
  
  if request.method == 'DELETE':
    data = request.data
    student = StudentInfo.objects.get(id= data['id'])   
    student.delete()
    return Response({'message':f"successfully deleted {student.name}"}) 
  
  
  
# -------working with class based API------------

class StudentAPIView(APIView):
  def get(self,request):
    student = StudentInfo.objects.all()
    serializer = StudentSerailaizer(student , many = True)
    return Response(serializer.data)
  
  def post(self , request):
    data = request.data
    serializer = StudentSerailaizer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data)
    return Response(serializer.errors)
  
  def put(self , request):
    data = request.data
    student = StudentInfo.objects.get(id = data['id'])
    serializer = StudentSerailaizer(student , data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data)
    return Response(serializer.errors)
  
  def patch(self , request):
    data = request.data
    student = StudentInfo.objects.get(id = data['id'])
    serializer = StudentSerailaizer(student , data=data , partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data)
    return Response(serializer.errors)
    
  def delete(self , request):
    data = request.data
    student = StudentInfo.objects.get(id= data['id'])   
    student.delete()
    return Response({'message':f"successfully deleted {student.name}"})
  
  
  
  # -----using model view set----------------
  
class StudentViewSet(viewsets.ModelViewSet):
  serializer_class = StudentSerailaizer
  queryset = StudentInfo.objects.all()
  
  # to search the data
  def list(self, request):
    queryset = self.queryset
    search = request.GET.get('search')
    if search:
      queryset = queryset.filter(name__startswith = search)
      serializer = StudentSerailaizer(queryset , many = True)
      
      return Response({'status':200 , 'data':serializer.data})
    
    
    
# ---------for regestering into the User model-----------------

class RegisterUser(APIView):
  def post(self , request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(
                {'status': True, 'message': "User Created Successfully", 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
      return Response({'status': False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
# -----for login the user--------

class LoginView(APIView):
  
  def post(self , request):
    data = request.data
    serializer = LoginSerializer(data=data)
    
    if serializer.is_valid():
      user = authenticate(username = serializer.data['username'] , password = serializer.data['password'])
      
      if user is not None:
        token , _ = Token.objects.get_or_create(user = user)
        
      elif user is None:
        return Response({'status':False , 'message':serializer.errors} , status=status.HTTP_400_BAD_REQUEST)
        
        
      return Response({'status':True , 'message':f'Successfully Loggedin {user.first_name}', 'token':str(token)}, status=status.HTTP_200_OK )

    return Response({'status':False , 'message':serializer.errors} , status=status.HTTP_400_BAD_REQUEST)

  