import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
from utils.copyPack import serverPack, clientPack

# Create your views here.


def index(request):
    data = {"name": "wkk", "msg": "welcome to djangoVM"}
    versions = models.Version.objects.all()
    return render(request, 'pack/index.html', {'versions': versions})


def index_json(request):
    return JsonResponse({"name": "channel"})


def pack(request, nid):
    print(type(nid), nid)
    if request.method == "GET":
        print(request.GET.get(nid))
        res = models.Version.objects.filter(id=nid).values(
            "project", "zone", "version")
        print(type(res), res)
        if res:
            for i in res:
                project = i['project']
                zone = i['zone']
                versionList = i['version'].split(".")
                versionList[-1] = str(int(versionList[-1]) + 1)
                newVersion = ".".join(versionList)
                print(i, project, zone, newVersion)

                ## fightcross fightdynamic fightcenter login cross server
                ## copy -> zip -> ftp
                commonDir = "J:/TTT/commonServer"
                destDir = "J:/pack2020"
                serverPack(commonDir, destDir, project, zone, newVersion)
                models.Version.objects.filter(id=nid).update(
                    version=newVersion)

                msg = "%s - pack - succ" % nid
        else:
            msg = "no nid"
            print(msg)
        return JsonResponse({"name": msg})
