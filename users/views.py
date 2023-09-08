from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from .serializer import UserSerializer
from .models import User
import jwt, datetime
from .models import Plant
from .serializer import PlantSerializer


# Create your views here.
class RegsiterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            "iat": datetime.datetime.utcnow(),
        }

        # token = jwt.encode(payload ,'peakseckey',algorithm='HS256').decode('utf-8')
        token = jwt.encode(payload, "peakseckey", algorithm="HS256")

        # return Response({
        #     'jwt': token
        # })
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}

        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Not logged in")

        try:
            payload = jwt.decode(token, "peakseckey", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Please loggin again")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response


class PlantsView(APIView):
    def get(self, request):
        queryset = Plant.objects.all()
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Not logged in")

        try:
            payload = jwt.decode(token, "peakseckey", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Please loggin again")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)
        plant_serlizer = PlantSerializer(queryset, many=True)
        return Response({"data": serializer.data, "objects": plant_serlizer.data})


class PlantAdd(APIView):
    def post(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Not logged in")

        try:
            payload = jwt.decode(token, "peakseckey", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Please log in again")

        user = User.objects.filter(id=payload["id"]).first()

        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Plant added successfully"})
        else:
            raise ValidationError(serializer.errors)


class PlantEditWithID(APIView):
    def put(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Not logged in")

        try:
            payload = jwt.decode(token, "peakseckey", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Please log in again")

        user = User.objects.filter(id=payload["id"]).first()

        try:
            plant_id = request.data["id"]
            plant = Plant.objects.get(pk=plant_id)
        except Plant.DoesNotExist:
            raise NotFound("Plant not found")

        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Plant updated successfully"})
        else:
            return Response(serializer.errors, status=400)
