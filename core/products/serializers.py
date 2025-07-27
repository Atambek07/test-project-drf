from rest_framework import serializers
from . import models

class RegPopSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Register_Population
    fields = "__all__"
