from django.shortcuts import render
from django.views import View

from programs.models import ProgName, ProgStartTime


class ProgramslView(View):

    def get(self, request):
        try:
            progs = ProgName.objects.order_by('name')
        except ProgName.DoesNotExist:
            progs = {}

        pgs = {}
        if len(progs):

            for prog in progs:
                pgs[prog.id] = ProgStartTime.objects.filter(prog_id=prog.id).order_by('start_time')

        return render(request, 'programs.html', {'pgn': progs, 'pgs': pgs})
