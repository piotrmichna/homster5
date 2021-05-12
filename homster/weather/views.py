import datetime

from django.shortcuts import render, redirect
from django.views import View

from config.models import CfgCommand
from weather.models import WeatherDaily, WeatherLong


class WeatherChartsView(View):
    def get(self, request):
        queryset = WeatherDaily.objects.all()
        weat_now = WeatherDaily.objects.order_by('time_m').last()
        return render(request, 'plot.html', {'ctx': queryset, 'wnow': weat_now})


class WeatherChartsDayView(View):
    def get(self, request):
        queryset = WeatherLong.objects.all()
        weat_now = WeatherDaily.objects.order_by('time_m').last()
        return render(request, 'plot_day.html', {'ctx': queryset, 'wnow': weat_now})


def get_day_stats(yy: int, mn: int, dy: int):
    try:
        mans_count = WeatherDaily.objects.filter(time_m__year=yy, time_m__month=mn, time_m__day=dy).order_by(
            'time_m').count()
    except WeatherDaily.DoesNotExist:
        return redirect('weather')
    if mans_count > 0:
        prob = CfgCommand.objects.get(name='sv_sns')
        prob_tim = datetime.timedelta(minutes=int(prob.value))
        mans = WeatherDaily.objects.filter(time_m__year=yy, time_m__month=mn, time_m__day=dy).order_by(
            'time_m')
        data = {
            'num': mans_count,
            'date': datetime.date(year=yy, month=mn, day=dy),
            'tmp': 0,
            'prs': 0,
            'hum': 0,
            'lig': 0,
            'rin': '00:00:00',
            'ngh_n': 0,
            'ngh_tmp': 0,
            'ngh_prs': 0,
            'ngh_hum': 0,
            'ngh_lig': 0,
            'day_start': None,
            'day_stop': None,
            'day_n': 0,
            'day_tmp': 0,
            'day_prs': 0,
            'day_hum': 0,
            'day_lig': 0,
        }
        n = 0
        tmp = 0
        prs = 0
        hum = 0
        lig = 0
        rin = datetime.datetime(1, 1, 1, 0, 0, 0, 0)
        for man in mans:
            tmp += man.temp_m
            prs += man.pres_m
            hum += man.humi_m
            lig += man.ligh_m
            if man.rain_m:
                rin += prob_tim
            n += 1
        if n > 0:
            data['tmp'] = round(tmp / n, 1)
            data['prs'] = round(prs / n, 1)
            data['hum'] = round(hum / n, 1)
            data['lig'] = round(lig / n, 1)
            while rin.day > 1:
                rin -= prob_tim
            data['rin'] = rin.strftime('%H:%M:%S')
        mans = WeatherDaily.objects.filter(time_m__year=yy, time_m__month=mn, time_m__day=dy).order_by('time_m')
        n = 0
        tmp = 0
        prs = 0
        hum = 0
        lig = 0
        for man in mans:
            if man.ligh_m >= 320:
                data['day_start'] = man.time_m
                break
            else:
                tmp += man.temp_m
                prs += man.pres_m
                hum += man.humi_m
                lig += man.ligh_m
                n += 1
        mans = WeatherDaily.objects.filter(time_m__year=yy, time_m__month=mn, time_m__day=dy).order_by('-time_m')
        for man in mans:
            if man.ligh_m >= 320:
                data['day_stop'] = man.time_m
                break
            else:
                tmp += man.temp_m
                prs += man.pres_m
                hum += man.humi_m
                lig += man.ligh_m
                n += 1
        if n > 0:
            data['ngh_n'] = n
            data['ngh_tmp'] = round(tmp / n, 1)
            data['ngh_prs'] = round(prs / n, 1)
            data['ngh_hum'] = round(hum / n, 1)
            data['ngh_lig'] = round(lig / n, 1)
        data['day_length'] = data['day_stop'] - data['day_start']

        n = 0
        tmp = 0
        prs = 0
        hum = 0
        lig = 0
        mans = WeatherDaily.objects.filter(time_m__gte=data['day_start'], time_m__lte=data['day_stop']).order_by(
            'time_m')
        for man in mans:
            tmp += man.temp_m
            prs += man.pres_m
            hum += man.humi_m
            lig += man.ligh_m
            n += 1
        if n > 0:
            data['day_n'] = n
            data['day_tmp'] = round(tmp / n, 1)
            data['day_prs'] = round(prs / n, 1)
            data['day_hum'] = round(hum / n, 1)
            data['day_lig'] = round(lig / n, 1)
        data['day_start'] = data['day_start'].time()
        data['day_stop'] = data['day_stop'].time()
        sec = data['day_length'].total_seconds()
        hr = int(sec // 3600)
        mn = int((sec % 3600) // 60)
        ss = int(sec % 60)
        data['day_length'] = datetime.time(hour=hr, minute=mn, second=ss)
        return data
    else:
        return None


class WeatherCreateDayView(View):
    def get(self, request, yy, mn, dy):
        date_now = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        date_del = date_now - datetime.timedelta(7)
        date_get = datetime.datetime(yy, mn, dy, 0, 0, 0, 0)
        data = []
        num = 0

        while date_get < date_now:
            yy = date_get.year
            mn = date_get.month
            dy = date_get.day
            date_to = datetime.datetime(yy, mn, dy, 23, 59, 59, 999999)
            try:
                mans = WeatherDaily.objects.filter(time_m__gt=date_get, time_m__lt=date_to).order_by('time_m')
            except WeatherDaily.DoesNotExist:
                # return redirect('weather')
                date_get = date_get + datetime.timedelta(1)
                continue

            if mans.count() > 0:
                dx = datetime.date(year=yy, month=mn, day=dy)
                is_stat = WeatherLong.objects.filter(date_m=dx).count()

                print(f'is_stat={is_stat}')
                if is_stat == 0:
                    date_get = datetime.datetime(yy, mn, dy, 0, 0, 0, 0)
                    datax = get_day_stats(yy, mn, dy)
                    print(f'len(datax)={len(datax)}')
                    data.append({'date': date_get, 'date_to': date_to, 'datax': datax, 'wyn': 'ok'})
                    wl = WeatherLong.objects.create(date_m=datax['date'], temp_m=datax['tmp'], pres_m=datax['prs'],
                                                    humi_m=datax['hum'], ligh_m=datax['lig'], rain_m=data['rin'],
                                                    time_day_start=datax['day_start'], time_day_stop=datax['day_stop'],
                                                    time_day=datax['day_length'], temp_day_m=datax['day_tmp'],
                                                    pres_day_m=datax['day_prs'], humi_day_m=datax['day_hum'],
                                                    ligh_day_m=datax['day_lig'], temp_night_m=datax['ngh_tmp'],
                                                    pres_night_m=datax['ngh_prs'], humi_night_m=datax['ngh_hum'],
                                                    ligh_night_m=datax['ngh_lig'])
                    wl.save()
                num += 1

            date_get = date_get + datetime.timedelta(1)

        WeatherDaily.objects.filter(time_m__lt=date_del).delete()
        return render(request, 'get_day_list.html', {'data': data, 'num': num})
