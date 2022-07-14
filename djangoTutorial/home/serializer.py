from rest_framework import serializers
from .models import Todo
import re


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = ('create_at', 'update_at')

    def validate(self, data):
        if data.get('title'):
            string = data.get('title')
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(string) is None:
                raise serializers.ValidationError("title can not contain special character")
        return data