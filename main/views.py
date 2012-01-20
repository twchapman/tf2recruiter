from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import Player, PlayerForm, Frag, FragForm

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/tf2recruiter/openid/')
    else:
        players = Player.objects.filter(is_looking=True)
        
        try:
            classes = request.GET['classes']
        except:
            classes = ''
        
        try:
            order = request.GET['order']
        except:
            order = ''
        
        if not classes == '':
            players_ = []
            for p in players:
                if classes in [c.name for c in p.classes.all()]:
                    players_.append(p)
            players = players_
            
        if not order == '':
            players = players.order_by(order)
            
        for p in players:
            p.cs = [c.name for c in p.classes.all()]
            p.fs = p.frags.all().count()
            if not p.user == request.user:
                p.f = p.frags.filter(fragger=request.user).count()
            else:
                p.f = 1
        
        return render_to_response('index.htm', {'user_':request.user, 'players':players}, context_instance=RequestContext(request))
        
def edit(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/tf2recruiter/openid/')
    
    try:
        player = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        player = Player()
    
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player.user=request.user
            player.alias = form.cleaned_data['alias']
            player.seasons = form.cleaned_data['seasons']
            days = ''
            for day in form.cleaned_data['days']:
                days = days + day
            player.days = days
            player.eseaid = form.cleaned_data['eseaid']
            es = ''
            for e in form.cleaned_data['esea']:
                es = es + e
            player.esea = es
            player.save()
            player.classes = form.cleaned_data['classes']
            player.save()
            return HttpResponseRedirect('/tf2recruiter/')
    else:
        form = PlayerForm(instance=player)

    return render_to_response('form.htm', { 'form': form, 'action':'/tf2recruiter/edit', 'user_':request.user}, context_instance=RequestContext(request))
    
def frag(request, pid=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/tf2recruiter/openid/')
        
    if not pid:
        return HttpResponseRedirect('/tf2recruiter/')
        
    try:
        player = Player.objects.get(pk=pid)
        player.frags.get(user=request.user)
    except Player.DoesNotExist:
        return HttpResponseRedirect('/tf2recruiter/')
    
    if request.method == 'POST':
        form = FragForm(request.POST, instance=player)
        if form.is_valid():
            frag = Frag(fragger=request.user, feedback=form.cleaned_data['feedback'])
            frag.save()
            player.frags.add(frag)
            return HttpResponseRedirect('/tf2recruiter/')
    else:
        form = PlayerForm(instance=player)

    return render_to_response('form.htm', { 'form': form, 'action':'/tf2recruiter/recommend/' + pid, 'user_':request.user}, context_instance=RequestContext(request))