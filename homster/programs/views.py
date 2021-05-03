from datetime import datetime, time

from django.shortcuts import render, redirect
from django.views import View

from items.models import GpioPinCfg
from programs.models import ProgName, ProgStartTime, ProgPinCfg


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

    def post(self, request):
        act_id = request.POST.get('active_id')
        start_off_id = request.POST.get('start_off_id')
        delete_id = request.POST.get('delete_id')
        pr_active_id = request.POST.get('pr_active_id')

        err = ''
        if pr_active_id:
            pra = ProgName.objects.get(id=pr_active_id)
            if request.POST.get("pr_active_bool") == '1':
                pra.active = True
            else:
                pra.active = False
            pra.save()

        if delete_id:
            ProgStartTime.objects.get(id=delete_id).delete()
        if start_off_id:
            pst = ProgStartTime.objects.get(id=start_off_id)
            stim = datetime.now().replace(microsecond=0)
            stim = stim.time()
            stim = stim.strftime('%H:%M:%S')
            pst.stop_time = stim
            pst.running = False
            pst.save()
        if act_id:
            act_bool = request.POST.get('active_bool')
            st = ProgStartTime.objects.get(id=act_id)
            if str(act_bool) == '1':
                st.active = True
            else:
                st.active = False
            st.save()

        try:
            progs = ProgName.objects.order_by('name')
        except ProgName.DoesNotExist:
            progs = {}

        pgs = {}
        if len(progs):
            for prog in progs:
                pgs[prog.id] = ProgStartTime.objects.filter(prog_id=prog.id).order_by('start_time')

        return render(request, 'programs.html', {'pgn': progs, 'pgs': pgs, 'err': err})


class ProgramShowView(View):
    def get(self, request, pr_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}
        if prog:
            pgs = ProgStartTime.objects.filter(prog=prog).order_by('start_time')
            pgi = ProgPinCfg.objects.filter(prog=prog).order_by('lp')
        else:
            pgs = {}
            pgi = {}

        return render(request, 'program_show.html', {'prog': prog, 'pgs': pgs, 'pgi': pgi})

    def post(self, request, pr_id):
        name = request.POST.get('name')
        description = request.POST.get('description')
        active = request.POST.get('active')
        item_id = request.POST.get('active_id')
        active_bool = request.POST.get('active_bool')
        remove_id = request.POST.get('remove_id')
        if remove_id:
            ProgPinCfg.objects.get(id=remove_id).delete()
        if item_id:
            pin = ProgPinCfg.objects.get(id=item_id)
            pin.active = active_bool
            pin.save()
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}
        err = []
        if not name:
            err.append('Nazwa')
        if not description:
            description = None

        if not len(err):
            prog.name = name
            prog.description = description
            prog.active = active
            prog.save()
            return redirect('programs')
        pgs = ProgStartTime.objects.filter(prog=prog).order_by('start_time')
        pgi = ProgPinCfg.objects.filter(prog=prog).order_by('lp')
        return render(request, 'program_show.html', {'prog': prog, 'pgs': pgs, 'pgi': pgi, 'err': err})


class ProgramStartAddView(View):
    def get(self, request, pr_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = None

        if prog:
            vrs = {'tyt': f'Nowy start programu {prog.name}',
                   'name': '',
                   'description': '',
                   'day_delay': 0,
                   'start_time': time(hour=7, minute=0, second=0, microsecond=0),
                   'active': True}
            return render(request, 'program_start_add.html', {'prog': prog, 'vrs': vrs})
        else:
            return redirect('programs')

    def post(self, request, pr_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = None

        if prog:
            vrs = {'tyt': f'Nowy start programu {prog.name}',
                   'name': request.POST.get('name'),
                   'description': request.POST.get('description'),
                   'day_delay': int(request.POST.get('day_delay')),
                   'start_time': request.POST.get('start_time'),
                   'active': request.POST.get('active'),
                   'err': []
                   }
            if len(vrs['name']) == 0:
                vrs['err'].append('nazwa')
            if not isinstance(vrs['day_delay'], int):
                vrs['err'].append('dni przerwy')

            if len(vrs['err']) == 0:
                pst = ProgStartTime.objects.create(prog=prog,
                                                   name=vrs['name'],
                                                   description=vrs['description'],
                                                   day_delay=vrs['day_delay'],
                                                   start_time=vrs['start_time'],
                                                   stop_time='00:00:00',
                                                   active=vrs['active'])
                pst.save()
                return redirect('programs')
            else:
                return render(request, 'program_start_add.html', {'prog': prog, 'vrs': vrs})
        else:
            return redirect('programs')


class ProgramStartEditView(View):
    def get(self, request, pr_id, st_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = None
        try:
            prst = ProgStartTime.objects.get(id=st_id)
        except ProgName.DoesNotExist:
            prst = None
        if prog and prst:
            vrs = {'tyt': f'Edycja start programu {prog.name}',
                   'name': prst.name,
                   'description': prst.description,
                   'day_delay': prst.day_delay,
                   'start_time': prst.start_time,
                   'active': prst.active}
            return render(request, 'program_start_add.html', {'prog': prog, 'vrs': vrs})
        else:
            return redirect('programs')

    def post(self, request, pr_id, st_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = None
        try:
            prst = ProgStartTime.objects.get(id=st_id)
        except ProgName.DoesNotExist:
            prst = None

        if prog:
            vrs = {'tyt': f'Edycja start programu {prog.name}',
                   'name': request.POST.get('name'),
                   'description': request.POST.get('description'),
                   'day_delay': int(request.POST.get('day_delay')),
                   'start_time': request.POST.get('start_time'),
                   'active': request.POST.get('active'),
                   'err': []
                   }
            if len(vrs['name']) == 0:
                vrs['err'].append('nazwa')
            if not isinstance(vrs['day_delay'], int):
                vrs['err'].append('dni przerwy')

            if len(vrs['err']) == 0:
                prst.name = vrs['name']
                prst.description = vrs['description']
                prst.day_delay = vrs['day_delay']
                prst.start_time = vrs['start_time']
                prst.stop_time = '00:00:00'
                prst.active = vrs['active']
                prst.save()
                return redirect('programs')
            else:
                return render(request, 'program_start_add.html', {'prog': prog, 'vrs': vrs})
        else:
            return redirect('programs')


class ProgramItemsAddView(View):
    def get(self, request, pr_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}
            gpio = {}

        if prog:
            if ProgPinCfg.objects.filter(prog=prog).count():
                lp = ProgPinCfg.objects.filter(prog=prog).order_by('lp').last().lp
            else:
                lp = 0
            gpio = GpioPinCfg.objects.all().order_by('pin_board')
            vrs = {'tyt': 'Nowe urządzenie',
                   'lp': lp + 1,
                   'duration': '00:00:01',
                   'item': 0,
                   'parallel': False,
                   'active': True}

        return render(request, 'program_items_add.html', {'prog': prog, 'gpio': gpio, 'vrs': vrs})

    def post(self, request, pr_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}

        vrs = {'tyt': 'Nowe urządzenie',
               'lp': request.POST.get('lp'),
               'duration': request.POST.get('duration'),
               'item': GpioPinCfg.objects.get(id=int(request.POST.get('item'))),
               'parallel': request.POST.get('parallel'),
               'active': request.POST.get('active'),
               'err': [],
               }
        try:
            vrs['lp'] = int(vrs['lp'])
        except ValueError:
            vrs['err'].append('lp')
        if vrs['duration'] is None:
            vrs['err'].append('czas pracy')
        if vrs['parallel'] is None:
            vrs['err'].append('praca równoległa')
        if vrs['active'] is None:
            vrs['err'].append('dostępność')

        if prog and vrs['item'] and len(vrs['err']) == 0:
            it = ProgPinCfg.objects.create(prog=prog, pin_cfg=vrs['item'],
                                           lp=vrs['lp'], parallel=vrs['parallel'], active=vrs['active'])
            it.set_duration_sec(vrs['duration'])
            it.save()
            return redirect('program-edit', pr_id)
        else:
            gpio = GpioPinCfg.objects.all().order_by('pin_board')
            return render(request, 'program_items_add.html', {'prog': prog, 'gpio': gpio, 'vrs': vrs})


class ProgramItemsEditView(View):
    def get(self, request, pr_id, it_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}
            pin_prog = {}
        if prog:
            try:
                pin_prog = ProgPinCfg.objects.get(id=it_id)
            except ProgPinCfg.DoesNotExist:
                pin_prog = {}

        if pin_prog:
            gpio = GpioPinCfg.objects.all().order_by('pin_board')
            vrs = {'tyt': 'Edycja urządzenia',
                   'lp': pin_prog.lp,
                   'duration': pin_prog.duration_time,
                   'item': pin_prog.pin_cfg.id,
                   'parallel': pin_prog.parallel,
                   'active': pin_prog.active}
        return render(request, 'program_items_add.html', {'prog': prog, 'gpio': gpio, 'vrs': vrs})

    def post(self, request, pr_id, it_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}

        vrs = {'tyt': 'Nowe urządzenie',
               'lp': request.POST.get('lp'),
               'duration': request.POST.get('duration'),
               'item': GpioPinCfg.objects.get(id=int(request.POST.get('item'))),
               'parallel': request.POST.get('parallel'),
               'active': request.POST.get('active'),
               'err': [],
               }
        try:
            vrs['lp'] = int(vrs['lp'])
        except ValueError:
            vrs['err'].append('lp')
        if vrs['duration'] is None:
            vrs['err'].append('czas pracy')
        if vrs['parallel'] is None:
            vrs['err'].append('praca równoległa')
        if vrs['active'] is None:
            vrs['err'].append('dostępność')

        if prog and vrs['item'] and len(vrs['err']) == 0:
            it = ProgPinCfg.objects.get(id=it_id)
            it.pin_cfg = vrs['item']
            it.lp = vrs['lp']
            it.parallel = vrs['parallel']
            it.active = vrs['active']
            it.duration_time=vrs['duration']
            it.save()
            return redirect('program-edit', pr_id)
        else:
            gpio = GpioPinCfg.objects.all().order_by('pin_board')
            return render(request, 'program_items_add.html', {'prog': prog, 'gpio': gpio, 'vrs': vrs})


class ProgramRemoveView(View):
    def get(self, request, pr_id):
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}
        if prog:
            pgs = ProgStartTime.objects.filter(prog=prog).order_by('start_time')
        else:
            pgs = {}

        return render(request, 'program_remove.html', {'prog': prog, 'pgs': pgs})

    def post(self, request, pr_id):
        prof = request.POST.get('prof')
        try:
            prog = ProgName.objects.get(id=pr_id)
        except ProgName.DoesNotExist:
            prog = {}
        err = []
        if prof == 'jestem_pewien':
            ProgStartTime.objects.filter(prog_id=pr_id).delete()
            ProgPinCfg.objects.filter(prog_id=pr_id).delete()
            ProgName.objects.get(id=pr_id).delete()
            return redirect('programs')
        pgs = ProgStartTime.objects.filter(prog=prog).order_by('start_time')
        return render(request, 'program_remove.html', {'prog': prog, 'pgs': pgs})
