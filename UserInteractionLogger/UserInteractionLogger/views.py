from django.http import HttpResponse
from django.template import loader
from UserInteractionLogger.models import User
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime


def login(request):
    # getting our templates
    template = loader.get_template('Login.html')
    user = User()
    user.title = 'Prit User'
    user.last_update = datetime.datetime.now()
    user.content = 'This is prit'
    # user.save()
    # rendering the templates in HttpResponse
    return HttpResponse(template.render())


def userprofile(request):
    # getting our templates
    template = loader.get_template('UserProfile.html')

    context = {
        'name': 'Prit Sheth',
        'stamp': 'today at 2',
    }
    users = User.objects
    # return render_to_response('UserProfile.html', {'Users': users},
    #                           context_instance=RequestContext(request))

    # rendering the template in HttpResponse
    # but this time passing the context and request
    # return HttpResponse(template.render(context, request))
#
# def validate_username(request):
#     username = request.GET.get('username', None)
#     data = {
#         'is_taken': User.objects.filter(username__iexact=username).exists()
#     }
#     return JsonResponse(data)

