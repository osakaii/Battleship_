import json
from .models import ShipsArea, Game, User
from channels.db import database_sync_to_async
from .exceptions import ClientError
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.authtoken.models import Token
from settings import cursor


class BattleShipConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = "game_%s" % self.game_name
        self.user = self.scope["user"]
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content):
        command = content.get("command", None)
        try:
            if command == "ready":
                await self.ready_to_game()

            if command == "join":
                await self.join_to_game(
                    content["user_token"],
                    self.game_name)

            elif command == "leave":
                await self.leave_game()

            elif command == "make_shoot":

                await self.shoot(
                    content["place"],
                    content["user_token"],
                    self.game_name,
                )

        except ClientError as e:
            await self.send_json({
                "error": e.code
                })

    async def ready_to_game(self):
        await self.channel_layer.group_send(
                self.game_group_name, {
                    "type": "game.message",
                    "message": "Ready",
                })

    async def leave_game(self):
        await self.channel_layer.group_send(self.game_group_name, {
            "type": "game.message",
            "message": "Player leaved",
            })

    async def join_to_game(self, user_token, game_code):
        try:

            await self.join_game(user_token, game_code)
            await self.channel_layer.group_send(
                self.game_group_name, {
                    "type": "game.message",
                    "message": "Game started",
                })
        except:
            await self.send_json({"error": "by you maybe"})

    async def game_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
        }))

    @database_sync_to_async
    def join_game(self, user_token, game_code):
        try:
            game = Game.objects.get(game_code=int(str(game_code)))
            if game.user2 is not None:
                return {
                    'status': 'BAD',
                    'message': 'This game is fulled with players'
                }
            user_check = Token.objects.filter(key=user_token).values('user')
            user_id = [i['user'] for i in user_check][0]
            user = User.objects.get(id=int(str(user_id)))
            game.user2 = user
            game.save()
            return {
                    'status': 'Successfully found and added',
                    'game_code': f'{game_code}',
                    "error": 'no error',
                }
        except ClientError as e:
            return {
                    "status": "BAD",
                    "error": f'{e.code}',
                    'game_code': f'{game_code}'
                    }

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )

    async def shoot(self, place, player_token, game_code):
        shoot = await self.make_shoot(place, player_token, game_code)
        await self.channel_layer.group_send(
            self.game_group_name, {
                "type": "shoot.message",
                "message": "Shoot made",
                "info": shoot
            })

    async def shoot_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "info": event["info"]
        }))

    @database_sync_to_async
    def make_shoot(self, place, player_token, game_code):
        try:
            user_id = Token.objects.filter(key=player_token).values('user')
            id = [ i['user'] for i in user_id]
            user = User.objects.get(id=int(id[0]))
            try:
                check = Game.objects.filter(
                    game_code=int(game_code), user1=user).values('user2', 'user1')

                list = [i['user2'] for i in check]
                opponent_id = list[0]
                opponent = User.objects.get(id=opponent_id)

                list2 = [i['user1'] for i in check]
                i_id = list2[0]
                i = User.objects.get(id=i_id)

            except:
                game = Game.objects.filter(
                    game_code=int(game_code)).values('user1', 'user2')
                list = [i['user1'] for i in game]
                opponent_id = list[0]
                opponent = User.objects.get(id=opponent_id)

                list2 = [i['user1'] for i in game]
                i_id = list2[0]
                i = User.objects.get(id=i_id)

            area = ShipsArea.objects.filter(
                user=opponent, game_code=int(game_code)).values(str(place), 's_' + str(place))
            list_result = [i[str(place)] for i in area]
            result = list_result[0]
            check = [i['s_' + str(place)] for i in area]

            if bool(check[0]) == True:
                return {
                    "status": "Error",
                    "result": "The place is still shot",
                    "place": f"{place}"
                }
            else:
                cursor.execute(f"UPDATE app_shipsarea SET s_{place} = True WHERE game_code = {game_code} AND user_id = {opponent} ")
                postgres.commit()
                area = ShipsArea.objects.get(user=opponent, game_code=int(game_code))
                last = int(area.shot_sum)
                area = ShipsArea.objects.filter(user=opponent, game_code=int(game_code))
                area.update(shot_sum=last+1)
                area = ShipsArea.objects.get(user=opponent, game_code=int(game_code))
                if area.shot_sum == area.sh_sum:
                    return {
                            "status": "Success",
                            "result": "Game ended",
                            "message": f"{i} won"
                            }
                return {
                    "status": "OK",
                    "result": str(result),
                    "place": f"{place}",
                    "whom": f"{opponent_id}"
                }

        except ClientError as e:
            return {
                "status": "BAD",
                "error": str(e.code)
            }
