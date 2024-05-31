from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer , PostSerializer , QuizSerializer, CategorySerializer, UserDataSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Question, QuizCategory, CustomUser
import json as js
from .backfn import back


class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)  # Pass request.data directly
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json_data = serializer.data
                return Response(json_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class QuestionList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuizSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('id')  
        return Question.objects.filter(category_id=category_id)


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = QuizCategory.objects.all()
    serializer_class = CategorySerializer


class UserData(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserDataSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def backtest(request):
    try:
        data = request.data
        list = [[int(item) for item in sublist] for sublist in data]
        result_data = back(list)
        manipulated_data = {
            "data": result_data,
        }
        
        return JsonResponse(manipulated_data, status=status.HTTP_200_OK)
    except js.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



