from rest_framework import serializers

from tests.models import Question, Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class TestsSerializer(serializers.ModelSerializer):
    test = TestSerializer(required=False)

    class Meta:
        model = Question
        fields = "__all__"
