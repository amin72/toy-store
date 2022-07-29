from rest_framework import serializers
from toy.models import Toy


class ToySerializer(serializers.Serializer):
    model = Toy
    fields = (
        'pk',
        'name',
        'description',
        'release_date',
        'toy_category',
        'was_included_in_home',
    )
