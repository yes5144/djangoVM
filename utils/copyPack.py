import os
import shutil
import datetime

from .zipClass import mkZip

today = datetime.datetime.now().strftime("%Y%m%d")


def dirFormat(dirname):
    if not dirname.endswith('/'):
        return dirname + '/'
    return dirname


def serverPack(commonDir, destDir, project, zone, newversion):
    commonDir = dirFormat(commonDir)
    destDir = dirFormat(destDir)
    ## fightcross fightdynamic fightcenter login cross server
    for app in [
            "fightcross", "fightdynamic", "fightcenter", "login", "cross",
            "server"
    ]:
        newVersionDir = "%s_%s_%s_v%s_%s" % (project, zone, app, newversion,
                                             today)

        targetDir = destDir + newVersionDir
        if not os.path.exists(targetDir):
            try:
                os.makedirs(targetDir)
            except Exception as e:
                print(e)
        print("copy %s begin" % newVersionDir)
        if app == "cross":
            shutil.copy(commonDir + "crosscenterserver", targetDir)
            shutil.copytree(commonDir + "config", targetDir + "/config")
        if app == "login":
            shutil.copy(commonDir + "loginserver", targetDir)
        if app == "fightcenter":
            shutil.copy(commonDir + "fightcenterserver", targetDir)
            shutil.copy(commonDir + "mergeserver", targetDir)
            shutil.copytree(commonDir + "config", targetDir + "/config")
        if app == "server":
            shutil.copy(commonDir + "gameserver", targetDir)
            shutil.copy(commonDir + "gateserver", targetDir)
            shutil.copy(commonDir + "fightserver", targetDir)
            shutil.copytree(commonDir + "config", targetDir + "/config")

        if app in [
                "fightcross",
                "fightdynamic",
        ]:
            shutil.copy(commonDir + "fightserver", targetDir)
            shutil.copytree(commonDir + "config", targetDir + "/config")
        print("copy %s end" % newVersionDir)
        ## zip
        mkZip(targetDir)


def clientPack():
    pass


if __name__ == "__main__":
    commonDir = "J:/TTT/commonServer"
    destDir = "J:/pack2020"
    project = "nz"
    zone = "mlwx"
    newversion = "1.0.32.33"
    serverPack(commonDir, destDir, project, zone, newversion)