from rest_framework.serializers import IntegerField, CharField, Serializer, ModelSerializer, HyperlinkedIdentityField
from notes.models import Note


# class NoteSerializer(Serializer):
#     id = IntegerField(read_only=True)
#     title = CharField(max_length=255, required=True)
#     text = CharField(required=False, allow_blank=True)
#
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#     def update(self, instace, validated_data):
#         instace.title = validated_data.get('title', instace.title)
#         instace.text = validated_data.get('text', instace.text)
#         instace.save()
#         return instace


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class ThinNoteSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='notes-detail')

    class Meta:
        model = Note
        fields = ('id', 'title', 'url')

