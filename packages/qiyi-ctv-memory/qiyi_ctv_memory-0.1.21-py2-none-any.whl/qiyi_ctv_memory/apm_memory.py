# -*- coding: utf-8 -*--
import argparse
import datetime
import subprocess

from qiyi_ctv_memory.Adb import Adb
from qiyi_ctv_memory.java import javaHeap


def parse_arguments():
    parser = argparse.ArgumentParser(description='argument')
    parser.add_argument('-c', '--categories', dest='CATEGORIES',  default='', help='what do you want to do?')
    parser.add_argument('-o', '--output',  dest='OUTPUT', default='', help='output path')
    parser.add_argument('-f', '--focus',  dest='FOCUS', default='', help='focus class')
    parser.add_argument('-m', '--mapping',  dest='MAPPING', default='', help='apk mapping file')
    args, unknown_args = parser.parse_known_args()
    return args, unknown_args

if __name__ == "__main__":
    args, unknown_args = parse_arguments()
    categories = args.CATEGORIES
    outputPath = args.OUTPUT
    if categories == 'native':
        command = ['python', 'native_memory.py'] + unknown_args
        result = subprocess.run(command, capture_output=True, text=True)
        pass
    else :
        adb = Adb()
        package_name = adb.get_current_package_name()
        now = datetime.datetime.now()
        # 格式化当前时间
        formatted_time = now.strftime("%Y.%m.%d-%H.%M.%S.%f")[:-3]
        hprof = javaHeap.dumpHprof(adb, package_name)
        hprof = javaHeap.pullHprof(adb, hprof, str(formatted_time), outputPath)
        mappingPath = args.MAPPING
        if categories == 'leak':
            javaHeap.parseLeak(hprof, outputPath, mappingPath, 'low')
        elif categories == 'javadetail':
            javaHeap.parseAll(hprof, outputPath, mappingPath, 'high')
        elif categories == 'focus':
            focus = args.FOCUS
            javaHeap.parseFocus(hprof, outputPath, mappingPath, focus)
        pass

