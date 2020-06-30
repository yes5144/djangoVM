import json
import datetime
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
    if request.method == "POST":
        # print(request.POST.get(nid))
        commonIndexDir = request.POST.get("clientIndex")
        print("commonIndexDir", commonIndexDir)
        destDir = request.POST.get("destDir")
        print("destDir", destDir)
        commonClientDir = request.POST.get("clientPath")
        print("commonClientDir", commonClientDir)
        commonServerDir = request.POST.get("serverPath")
        print("commonServerDir", commonServerDir)
        res = models.Version.objects.filter(id=nid).values(
            "project", "zone", "version")
        print(type(res), res)
        today = datetime.datetime.now().strftime("%Y%m%d")
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
                destDir = "%s/%s/%s/%s" % (destDir, today, project, zone)
                if commonServerDir:
                    serverPack(commonServerDir, destDir, project, zone,
                               newVersion)
                if commonClientDir and commonIndexDir:
                    print('client pack')
                    projectIndexDir = "%s/%s/%s" % (commonIndexDir, project,
                                                    zone)
                    clientPack(projectIndexDir, commonClientDir, destDir,
                               project, zone, newVersion)
                if commonServerDir or commonClientDir:
                    models.Version.objects.filter(id=nid).update(
                        version=newVersion)

                msg = "%s - pack - succ" % nid
        else:
            msg = "no nid"
            print(msg)
        return JsonResponse({"name": msg})
