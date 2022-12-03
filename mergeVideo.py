import os
import glob
import subprocess

mp4_list = glob.glob('./*.mp4')

list_file = 'mergeList.txt'
f = open(list_file, 'w')
for file in (mp4_list):
    f.write('file ' + '\'' + file + '\'\n')
f.close()
param = ' -f concat -safe 0 -i ' + list_file + ' -c copy ' + 'mergedFile' + '.mp4'
os.system('ffmpeg.exe' + param)      
