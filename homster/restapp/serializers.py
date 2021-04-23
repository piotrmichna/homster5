from rest_framework import serializers

from config.models import CfgCommand
from items.models import GpioPinCfg
from programs.models import ProgPinCfg, ProgStartTime, ProgName
from weather.models import (WeatherDaily, WeatherLong, WeatherWeek)


class WeatherDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDaily
        fields = (
            'id',
            'time_m',
            'temp_m',
            'pres_m',
            'humi_m',
            'ligh_m',
        )


class WeatherLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherLong
        fields = (
            'id',
            'date_m',
            'temp_m',
            'pres_m',
            'humi_m',
            'ligh_m',
            'time_day_start',
            'time_day_stop',
            'temp_day_m',
            'pres_day_m',
            'humi_day_m',
            'ligh_day_m',
            'temp_night_m',
            'pres_night_m',
            'humi_night_m',
            'ligh_night_m',
        )


class WeatherWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherWeek
        fields = (
            'id',
            'date_m',
            'temp_m',
            'pres_m',
            'humi_m',
            'ligh_m',
            'time_day_start',
            'time_day_stop',
            'temp_day_m',
            'pres_day_m',
            'humi_day_m',
            'ligh_day_m',
            'temp_night_m',
            'pres_night_m',
            'humi_night_m',
            'ligh_night_m',
        )


class CfgWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CfgCommand
        fields = (
            'id',
            'description',
            'name',
            'value',
        )


class SyncCommandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CfgCommand
        fields = (
            'id',
            'name',
            'value',
        )


class GpioPinCfgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpioPinCfg
        fields = [
            'id',
            'buss_pin',
            'name',
            'description',
            'pin_board',
            'dir_out',
            'val',
            'val_default',
        ]


class ProgPinCfgSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='pin_cfg.name')
    pin_board = serializers.IntegerField(source='pin_cfg.pin_board')
    dir_out = serializers.BooleanField(source='pin_cfg.dir_out')
    val = serializers.IntegerField(source='pin_cfg.val')
    val_default = serializers.IntegerField(source='pin_cfg.val_default')

    class Meta:
        model = ProgPinCfg
        fields = [
            'id',
            'prog',
            'lp',
            'duration_sec',
            'stop_time',
            'parallel',
            'active',
            'pin_cfg',
            'name',
            'pin_board',
            'dir_out',
            'val',
            'val_default',
        ]


class ProgStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgStartTime
        fields = [
            'id',
            'name',
            'description',
            'day_delay',
            'start_time',
            'next_time',
            'running',
            'active',
            'prog',
        ]


class ProgramsCfgSerializer(serializers.ModelSerializer):
    progpin = ProgPinCfgSerializer(many=True, read_only=True)
    progstarts = ProgStartSerializer(many=True, read_only=True)

    class Meta:
        model = ProgName
        fields = [
            'id',
            'name',
            'description',
            'stop_run',
            'running',
            'active',
            'progpin',
            'progstarts',
        ]
