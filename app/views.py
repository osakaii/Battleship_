from rest_framework import permissions, generics, views
from app.models import User, ShipsArea, Game
from app.serializers import (
    UserSerializer,
    CreateShipAreaSerializer,
    GameListSerializer,
    AreaShipListSerializer
)
from rest_framework import viewsets, response, status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
import random
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return response.Response(
                {
                    'Status': 'Success',
                    'Data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            raise ValidationError(
                {
                    'Status': 'Fail',
                    'Message': serializer.errors,
                    'Data': []
                }
            )


@api_view(['GET'])
def get_user_list(request):
    if request.method == 'GET':
        user_id = request.user
        users = User.objects.exclude(id=int(str(user_id)))
        users_set = []
        for i in users:
            users_set.append(int(str(i)))
        user_infos = []
        for i in users_set:
             users_ = User.objects.filter(id=i).values('id', 'username')
             for i in users_:
                 user_infos.append(
                     {'id': f'{i["id"]}',
                      'username': f'{i["username"]}'
                      })

        if not users.exists():
            raise ValidationError("problems with token")
        else:
            return response.Response(
                {
                    'users': user_infos
                },
                status=status.HTTP_200_OK
            )


class CreateShipArea(viewsets.ModelViewSet):
    queryset = ShipsArea.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']
    serializer_class = CreateShipAreaSerializer


@api_view(['GET'])
def start_game(request):
    if request.method == 'GET':
        user_id = request.user
        game_code = random.randint(10000, 100000)
        user = User.objects.get(id=int(str(user_id)))
        game = Game(user1=user, game_code=game_code)
        game.save()
        return response.Response(
                {
                    'message': "Successfully created",
                    'game_code': game_code
                },
                status=status.HTTP_200_OK
            )


class FindGame(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        game_code = request.data['game_code']
        try:
            game = Game.objects.get(game_code=int(str(game_code)))
            if game.user2 is not None:
                return response.Response({'message': 'This game is fulled with players'})
            user_id = request.user
            user = User.objects.get(id=int(str(user_id)))
            game.user2 = user
            game.save()
            return response.Response(
                 {
                     'message': 'Successfully found and added',
                     'game_code': game_code
                 },
                 status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return response.Response(
                {
                    'message': 'Error. There isnt any game with this game code',
                }, status=400
            )

class ListGameView(generics.ListAPIView):
    http_method_names = ['get']
    queryset = Game.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GameListSerializer


class ListAreView(generics.ListAPIView):
    http_method_names = ['get']
    queryset = ShipsArea.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AreaShipListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ['game_code']


@api_view(['GET'])
def get_current_area(request):
    if request.method == 'GET':
        user_id = request.user
        user = User.objects.get(id=int(str(user_id)))
        game_code = ShipsArea.objects.filter(user=user).last().game_code
        ship_areas = ShipsArea.objects.filter(game_code=int(game_code)).values(
             'user',
             'game_code',
             's_x1',   's_x2',   's_x3',   's_x4',   's_x5',
             's_x6',   's_x7',   's_x8',   's_x9',   's_x10',
             's_x11',  's_x12',  's_x13',  's_x14',  's_x15',
             's_x16',  's_x17',  's_x18',  's_x19',  's_x20',
             's_x21',  's_x22',  's_x23',  's_x24',  's_x25',

             'x1',   'x2',   'x3',   'x4',   'x5',
             'x6',   'x7',   'x8',   'x9',   'x10',
             'x11',  'x12',  'x13',  'x14',  'x15',
             'x16',  'x17',  'x18',  'x19',  'x20',
             'x21',  'x22',  'x23',  'x24',  'x25',
        )
        areas = []
        for i in ship_areas:
            areas.append(i)

        data1 = {}
        data2 = {}

        data1['user'] = areas[0]['user']
        data1['game_code'] = areas[0]['game_code']

        data2['user'] = areas[1]['user']
        data2['game_code'] = areas[1]['game_code']

        area_data1 =[]
        area_data2 = []

        areas[0].pop("user")
        areas[0].pop("game_code")
        areas[1].pop("user")
        areas[1].pop("game_code")

        count1 = 0
        count2 = 25
        for i in range(25):
            count1 += 1
            count2 += 1
            area_data1.append({
                'position': f'{"x"+ str(count1)}',
                'ship': f'{areas[0]["x" + str(count1)]}',
                'shot': f'{areas[0]["s_x" + str(count1)]}'
            })
            area_data2.append({
                'position': f'{"x" + str(count1)}',
                'ship': f'{areas[1]["x" + str(count1)]}',
                'shot': f'{areas[1]["s_x" + str(count1)]}'
            })

        return response.Response(
                {
                    'user1': {
                        'personal': data1,
                        'data': area_data1
                    },
                    'user2': {
                        'personal': data2,
                        'data': area_data2
                    },
                },
                status=status.HTTP_200_OK
            )
