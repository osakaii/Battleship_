from rest_framework import serializers
from app.models import User, ShipsArea, Game


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input': 'password'}, write_only=True, default="null")
    class Meta:
        model = User
        ref_name = 'Registration for user'
        fields = (
            'username',
            'password',
        )

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()


class CreateShipAreaSerializer(serializers.Serializer):

    game_code = serializers.CharField()
    data = serializers.ListField()

    def save(self):
        game_code = self.validated_data['game_code']
        user = self.context['request'].user
        x1 = self.validated_data['data']
        all_x = []
        sh_sum = 0
        for i in x1:
            all_x.append(i['ship'])
            if i['ship']:
                sh_sum += 1

        p = ShipsArea(
              user=user,
              sh_sum=sh_sum,
              game_code=game_code,
              x1=bool(all_x[0]),
              x2=bool(all_x[1]),
              x3=bool(all_x[2]),
              x4=bool(all_x[3]),
              x5=bool(all_x[4]),
              x6=bool(all_x[5]),
              x7=bool(all_x[6]),
              x8=bool(all_x[7]),
              x9=bool(all_x[8]),
              x10=bool(all_x[9]),
              x11=bool(all_x[10]),
              x12=bool(all_x[11]),
              x13=bool(all_x[12]),
              x14=bool(all_x[13]),
              x15=bool(all_x[14]),
              x16=bool(all_x[15]),
              x17=bool(all_x[16]),
              x18=bool(all_x[17]),
              x19=bool(all_x[18]),
              x20=bool(all_x[19]),
              x21=bool(all_x[20]),
              x22=bool(all_x[21]),
              x23=bool(all_x[22]),
              x24=bool(all_x[23]),
              x25=bool(all_x[24]),
        )
        p.save()


class FindGameSerializer(serializers.Serializer):
    game_code = serializers.IntegerField()


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'user1',
            'user2',
            'game_code',
        )


class AreaShipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipsArea
        fields = '__all__'
