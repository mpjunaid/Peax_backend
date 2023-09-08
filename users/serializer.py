from rest_framework import serializers
from .models import User
from .models import Plant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # feilds = ['id','name','email','password']

        # fields = '__all__'
        exclude = [
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "is_staff",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"
