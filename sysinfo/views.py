from django.http import HttpResponse
from django.template.context import RequestContext
from django.template.loader import get_template
import json

def home(request):
    template = get_template('index.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))


def get(request):
    core0 = request.GET.get('core0','0')
    core1 = request.GET.get('core1','0')
    core2 = request.GET.get('core2','0')
    core3 = request.GET.get('core3','0')
    core4 = request.GET.get('core4','0')
    core5 = request.GET.get('core5','0')
    core6 = request.GET.get('core6','0')
    core7 = request.GET.get('core7','0')
    file = open('sysinfofile.txt','wb')
    file.write(bytes(core0 + '\n', 'UTF-8'))
    file.write(bytes(core1 + '\n', 'UTF-8'))
    file.write(bytes(core2 + '\n', 'UTF-8'))
    file.write(bytes(core3 + '\n', 'UTF-8'))
    file.write(bytes(core4 + '\n', 'UTF-8'))
    file.write(bytes(core5 + '\n', 'UTF-8'))
    file.write(bytes(core6 + '\n', 'UTF-8'))
    file.write(bytes(core7 + '\n', 'UTF-8'))
    file.close()
    return HttpResponse(core0)
def servejson(request):
    cores = []
    with open('sysinfofile.txt', 'r+') as file:
        for line in file:
            cores.append(line[:-1])
    return HttpResponse(json.dumps(cores), content_type='application/json')

