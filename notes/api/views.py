# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer,UserSerializer
from .models import Note
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Gets a notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Get a particular note'
        },
        {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create a new note'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update a particular note'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete a particular note'
        },
    ]

    return Response(routes)


class RegisterUser(APIView):

    def post(self, request):

        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(username = serializer.data['username'])

            token_obj, _ = Token.objects.get_or_create(user = user)

            return Response({'payload' : serializer.data, 'token' : str(token_obj), 'message' : 'User has been registered'})

    
        return Response({'errors' : serializer.errors, 'message' : "User's information not correct"})



# get all notes

@api_view(['GET'])
def getNotes(request):

    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)


# get a particular note

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


# create a new note

@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(body=data['body'])

    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


# update a particular note

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# delete a particular note

@api_view(['DELETE'])
def deleteNote(request, pk):

    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response("Note has already deleted")


    note.delete()
    return Response('Node is deleted')