from django.shortcuts import render
from rest_framework import generics
from .serializers import CreateChatSerializer
from .models import Chat

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

'''
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                self.request.session['room_code'] = room.code
                return Response(RoomSerializer(room).data)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                self.request.session['room_code'] = room.code
                return Response(RoomSerializer(room).data)

        return Response({'Bad Request': 'Invalid data...'})


class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'


    def get(self, request, format=None):
        print(request.data.get("votes_to_skip"))
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data)
            return Response({'Room Not Found': 'Invalid Room Code.'})

        return Response({'Bad Request': 'Code paramater not found in request'})
'''

class SendMessage(APIView):
    serializer_class = CreateChatSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            chatId = request.data.get('chatId')
            author = request.data.get('author')
            content = request.data.get('content')

            chat = Chat(author=author, content=content, chatId=chatId)
            chat.save()
            return Response(CreateChatSerializer(chat).data)

        return Response({'Bad Request': 'Code paramater not found in request'})


class GetMessage(APIView):
    serializer_class = CreateChatSerializer
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()


        chatId = request.query_params.get('chatId')

        chats = Chat.objects.filter(chatId=chatId)

        data = []

        for i in range(len(chats)):
            data.append(CreateChatSerializer(chats[i]).data)

        return Response(data)

