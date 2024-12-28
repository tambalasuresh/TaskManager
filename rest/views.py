
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from user.models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserRegisterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        json_data = request.data

        # Validate email format
        try:
            validate_email(json_data['email'])
        except ValidationError:
            return Response({"message": "Invalid email format."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if email already exists
        if CustomUser.objects.filter(email=json_data['email']).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if phone number already exists
        if CustomUser.objects.filter(phone_number=json_data['phone_number']).exists():
            return Response({"error": "Phone number already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the new user instance without sending an OTP
        user_instance = CustomUser(
            email=json_data['email'],
            name=json_data['name'],
            phone_number=json_data['phone_number'],
            is_active=True  # Set active if no verification needed
        )
        user_instance.set_password(json_data['password'])  # Set password securely
        user_instance.save()

        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id=None):
        # If no user_id is provided, use the authenticated user
        if user_id is None:
            user = request.user
        else:
            try:
                user = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the user data
        user_data = UserSerializer(user).data

        # Add address data if available
        user_data['addresses'] = AddressSerializers(user.addresses.all(), many=True).data

        return Response(user_data)

class GetAddresses(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        user = request.user  # Get the authenticated user

        # Retrieve all addresses for the user
        addresses = Address.objects.filter(user=user)

        # Serialize the addresses
        serialized_addresses = AddressSerializers(addresses, many=True).data

        return Response(serialized_addresses)


class PlayerApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all players
        player = Player.objects.all()

        # Serialize the players
        serialized_player = PlayerSerializer(player, many=True).data

        return Response(serialized_player)


class UserTeamApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id=None):
        if user_id:
            # Filter teams for the specified user if the user ID is provided
            user_teams = UserTeam.objects.filter(user_id=user_id)
        else:
            # Otherwise, filter teams for the authenticated user
            user_teams = UserTeam.objects.filter(user=request.user)

        serializer = UserTeamSerializer(user_teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,user_id = None):
        if user_id:
            user_question = Question.objects.filter(user_id=user_id)
        else:
            user_question = Question.objects.filter(user=request.user)

            serializer = QuestionSerializers(user_question,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)