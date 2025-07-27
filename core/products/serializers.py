from rest_framework import serializers
from . import models

class Reg_Pop_Serializer(serializers.ModelSerializer):
  class Meta:
    model = models.Register_Population
    fields = "__all__"
