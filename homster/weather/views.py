from django.shortcuts import render, redirect
from django.views import View

from weather.models import WeatherDaily


class WeatherChartsView(View):
    def get(self, request):
        queryset = WeatherDaily.objects.all()
        return render(request, 'plot.html', {'ctx': queryset})


class WeatherCreateDayView(View):
    def get(self, request, yy, mn, dy):
        try:
            mans_count = WeatherDaily.objects.filter(time_m__year=yy, time_m__month=mn, time_m__day=dy).order_by(
                'time_m').count()
        except WeatherDaily.DoesNotExist:
            return redirect('weather')
        if mans_count > 0:
            mans = WeatherDaily.objects.filter(time_m__year=yy, time_m__month=mn, time_m__day=dy).order_by(
                'time_m')
        data = {
            'num':mans_count,
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
        for man in mans:
            if man.ligh_m > 2:
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
            if man.ligh_m > 2:
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
        n = 0
        tmp = 0
        prs = 0
        hum = 0
        lig = 0
        mans = WeatherDaily.objects.filter(time_m__gt=data['day_start'], time_m__lt=data['day_stop']).order_by('time_m')
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

        return render(request, 'get_day_data.html', {'data': data})
