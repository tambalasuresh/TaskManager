from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import *
from CreateTeam.models import *
from Question.models import *



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token['user_type'] = user.user_type
        # Add custom claims
        # token['first_name'] = user.first_name
        # token['main_package'] = list(user.main_package.values_list('id','name', flat=True))
        # ...


        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom claims
        refresh = self.get_token(self.user)
        print(data)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # data['user_type'] = self.user.user_type  # Add user type to the response

        return data



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password_confirm', 'name', 'profile_img', 'address', 'phone_number']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')  # Remove the password_confirm field
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()
        return user


class AddressSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Address
        fields = ['address_line1', 'address_line2', 'user', 'city', 'state', 'country', 'phone_number']


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializers(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'email', 'name', 'address']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'team_type', 'player_type', 'bowl_type','player_img']


class UserTeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    class Meta:
        model = UserTeam
        fields = ['id','user','team_name','players','match_date']


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question','answer_1','answer_2','answer_3','answer_4','correct_answer']
