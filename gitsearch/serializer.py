from rest_framework import serializers
from .models import SavedGit

class GitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedGit