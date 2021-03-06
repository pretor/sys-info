from django.http import HttpResponse
from django.template.context import RequestContext
from django.template.loader import get_template
import json
import os

def home(request):
    template = get_template('index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def get(request):
    listCorePercentage = request.GET.getlist('cpu[]', 0)
    cpuBrand = request.GET.get('cpubrand', 0)
    memoryPercent = request.GET.get('memorypercent', 0)
    memoryTotal = request.GET.get('memorytotal', 0)
    gpuName = request.GET.get('gpuname', 0)
    cpuTempCores = request.GET.getlist('cputempcores[]', 0)
    platform = request.GET.get('platform', 0)
    platformRelease = request.GET.get('platformrelease', 0)
    platformName = request.GET.get('platformname', 0)
    file = open('files/' + cpuBrand +'.txt', 'wb')
    cpuInfo = {'cores': listCorePercentage,
               'cpubrand': cpuBrand,
               'memorypercent': memoryPercent,
               'memorytotal': memoryTotal,
               'gpuname': gpuName,
               'cputempcores': cpuTempCores,
               'platform': platform,
               'platformrelease': platformRelease,
               'platformname': platformName}
    file.write(bytes(json.dumps(cpuInfo), 'UTF-8'))
    file.close()
    return HttpResponse(json.dumps(cpuInfo))


def servejson(request):
    sysInfos = []
    for filename in os.listdir('files'):
        file = open('files/'+filename, 'r+')
        sysInfos.append(json.loads(file.read()))
        file.close()
    jsonFromFile = json.dumps(sysInfos)
    return HttpResponse(jsonFromFile, content_type='application/json')



