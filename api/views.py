from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import NoteSerializer
from rest_framework import status
from api.models import Note

@api_view(["POST"])
def create_note(request):
    note = Note.objects.create(
        title=request.data['title'],
        body=request.data['body']
        )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_notes(request):
    notes = Note.objects.all().order_by('-created_at')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(["GET"])
def get_note(request,pk):
    try:
        note = Note.objects.get(pk=pk)
        note.delete()
    except Note.DoesNotExist:
        return Response({'message':'Note not found'}, status.HTTP_404_NOT_FOUND)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(["PUT"])
def update_note(request,pk):
    try:
        note = Note.objects.get(pk=pk)
        note.delete()
    except Note.DoesNotExist:
        return Response({'message':'Note not found'}, status.HTTP_404_NOT_FOUND)
    serializer = NoteSerializer(note, data=request.data)
    return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_note(request,pk):
    try:
        note = Note.objects.get(pk=pk)
        note.delete()
    except Note.DoesNotExist:
        return Response({'message':'Note not found'}, status.HTTP_404_NOT_FOUND)
    return Response({'message':'Note has been deleted'}, status.HTTP_204_NO_CONTENT)
    