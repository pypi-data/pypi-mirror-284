# coding=utf-8
import argparse
import os
import sys
import time

from qiyi_ctv_memory import snapshot_get, snapshot_summary, record_end, record_summary, record_start, snapshot_compare, \
    record_compare

if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-i', '--ip', help='device ip,if there is only one device please ignore this')
    argParser.add_argument('-p', '--pkgname',
                           help='package name,default is com.gitvdemo.video,if don`t change package name please '
                                'ignore this')
    argParser.add_argument('-t', '--target', help='target file')
    argParser.add_argument('-a', '--action', help='action to do')
    argParser.add_argument('-fi', '--fi', help='first input')
    argParser.add_argument('-si', '--si', help='second input')
    argParams = argParser.parse_args()
    package_name = "com.gitvdemo.video"
    cmd = "adb"
    if argParams.ip:
        cmd = cmd + " -s " + argParser.ip
    if argParams.pkgname:
        package_name = argParams.pkgname
    target = None
    if argParams.target:
        target = argParams.target
    if argParams.action:
        action = argParams.action
        if action == "ss":
            t = time.time()
            strTime = str(int(t))
            snapshot_path = os.path.join(os.getcwd(), "snapshot_" + strTime + ".txt")
            snapshot_get.pullSnapShot(cmd, package_name, snapshot_path)
            if os.path.exists(snapshot_path):
                snapshot_summary.snapshot_summary(snapshot_path, target)
        elif action == "sr":
            t = time.time()
            strTime = str(int(t))
            record_path = os.path.join(os.getcwd(), "record_" + strTime + ".txt")
            record_end.pullRecord(cmd, package_name, record_path)
            if os.path.exists(record_path):
                record_summary.record_summary(record_path, target)
        elif action == "rs":
            record_start.startRecrd(cmd, package_name)
        elif action == "cs":
            if argParams.fi and argParams.si and os.path.exists(argParams.fi) and os.path.exists(argParams.si):
                snapshot_compare.compare(argParams.fi, argParams.si, target)
            else:
                print("参数非法或文件不存在")
        elif action == "cr":
            if argParams.fi and argParams.si and os.path.exists(argParams.fi) and os.path.exists(argParams.si):
                record_compare.compare(argParams.fi, argParams.si, target)
            else:
                print("参数非法或文件不存在")