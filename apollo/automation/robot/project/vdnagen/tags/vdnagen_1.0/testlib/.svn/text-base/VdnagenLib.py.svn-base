import os
import sys
from robot.api import logger
from robot.api import *
from run_cmd import RunCmd
import re
import copy
import time
import random
from uuid import uuid1
from datetime import datetime
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class VdnagenLib:
    def __init__(self):
        pass
        
    def ingest_media_file(self, host, username, password, media_file):
        media_file = CI_SCRIPT_ROOT + "/" + media_file
        cmd = ["VDNAGen", "-s%s" % host, "-u%s" % username, "-p%s" % password, media_file, "-q"]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def generator_far_dna(self, media_file, dir_far):
        media_file = CI_SCRIPT_ROOT + '/' + media_file
        dir_far = CI_SCRIPT_ROOT + '/' + dir_far
        cmd = ["VDNAGen", "-TDNA", "%s" % media_file, "-o", "%s" % dir_far, "-q"]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def generator_far_media(self, media_file, dir_far):
        media_file = ' '.join(map(lambda s: CI_SCRIPT_ROOT + s, media_file.split(',')))
        dir_far = CI_SCRIPT_ROOT + '/' + dir_far
        cmd = ["VDNAGen", "-o", "%s" % dir_far, "%s" % media_file, "-q"]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def check_vdnagen_ver(self):
        cmd = ["VDNAGen", "-v"]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout[:-1]

    def generator_far(self,cmd, dir_far,media_file):
        source_file_name = CI_SCRIPT_ROOT + '/data/VDNAGen_data/source_file/' + media_file
        far_name = CI_SCRIPT_ROOT + '/data/VDNAGen_data/generator_far/' + dir_far
        cmd = [cmd, "-o" % source_file_name , "%s" % far_name, "-q"]
        process = RunCmd(" ".join(cmd))
        return process.stdout

    def generator_far_for_batch(self):
        r = []
        source_file_path = CI_SCRIPT_ROOT + '/data/VDNAGen_data/source_file'
        far_path = CI_SCRIPT_ROOT + '/data/VDNAGen_data/generator_far'
        for n in os.listdir(source_file_path):
            far_name = '.'.join(n.split('.')[:-1]) + '.far'
            cmd = ["VDNAGen", "-o" % (far_path + far_name), "%s" % (source_file_path + n), "-q"]
            process = RunCmd(" ".join(cmd))
            r.append(process.stdout)
        return r

    def parse_dna_status_result(self,data):
        #key_list = ['version is', 'Total length is', 'LENGTH=', 'VIDEO']
        keys_dict = {
            'LENGTH':('LENGTH=','''data[data.find('LENGTH=')+len('LENGTH='):].split('\\n')[0].strip()'''),
            'Total length is':('Total length is','''data[data.find('Total length is')+len('Total length is'):].split('s')[0].strip()'''),
            'version is':('version is','''data[data.find('version is')+len('version is'):].split(',')[0].strip()'''),
            'VIDEO':('VIDEO','''data[data.find('VIDEO')+len('VIDEO'):].split('\\n')[0].strip()''')
        }
        d = {}
        for k,v in keys_dict.items():
            if data.find(v[0]) < 0:
                d.setdefault(k,None)
            else:
                d.setdefault(k,str(eval(v[1])))
        return d

    def parse_ffmpeg_result(self, data):
        keys_dict = {
            'media_name':('Input','''data[data.find('Input')+len('Input'):].split('from')[1].strip().split(':\\n')[0][1:-1].split('/')[-1]'''),
            'video_codec':('Video','''data[data.find('Video:')+len('Video:'):].split(',')[0].strip().split(' ')[0]'''),
            'video_width':('Video','''data[data.find('Video')+len('Video'):].split(',')[2].strip().split('x')[0]'''),
            'video_height':('Video','''data[data.find('Video')+len('Video'):].split(',')[2].strip().split('x')[1].split(' ')[0]'''),
            'auido_codec':('Audio','''data[data.find('Audio:')+len('Audio:'):].split(',')[0].strip()'''),
            'auido_bit':('Audio','''data[data.find('Audio')+len('Audio'):].split(',')[1].strip().split(' ')[0]'''),
            'channels':('channels','''data[data.find('Audio')+len('Audio'):].split(',')[2].strip().split(' ')[0].strip()'''),
            'video_fps':('fps','''data[:data.find('fps')].strip().split(' ')[-1]''')
        }
        d = {}
        duration = data[data.find('Duration:')+len('Duration:'):].split('.')[0].strip()
        t = datetime.strptime(duration,"%H:%M:%S")
        sec = t.hour * 3600 +t.minute * 60 + t.second
        d.setdefault('Duration',str(sec))
        for k,v in keys_dict.items():
            if data.find(v[0]) < 0:
                d.setdefault(k,None)
            else:
                d.setdefault(k,str(eval(v[1])))
        return d



if __name__ == "__main__":
    vdnagen = VdnagenLib()
    d = '''LENGTH=60
VIDEO 60
File size is 71888
Start to analysize
From beginning to end
Header information:
	version is 2, length is 60, width is 1280, height is 720
	video_fps 29.970030
	video codec is 0
	video_bitrate is 0
	audio codec is 0
	audio audio_samplerate is 0
Total length is 60s
Total frame number 135259332
Valid frame number is 134716421, valid frame radio is 1.00
temporal complexity is 472
spatial complexity is 0'''
#    d='''ffmpeg version 0.8.10-4:0.8.10-0ubuntu0.12.04.1, Copyright (c) 2000-2013 the Libav developers
#  built on Feb  6 2014 20:59:08 with gcc 4.6.3
#*** THIS PROGRAM IS DEPRECATED ***
#This program is only provided for compatibility and will be removed in a future release. Please use avconv instead.
#[avi @ 0xa014aa0] max_analyze_duration reached
#Input #0, avi, from '/root/data/source_file/wmv1_wmav1_672x378.wmv':
#  Metadata:
#    encoder         : Lavf55.12.100
#  Duration: 00:00:05.10, start: 0.000000, bitrate: 1041 kb/s
#    Stream #0.0: Video: h264 (High), yuv420p, 640x480 [PAR 1:1 DAR 4:3], 29.97 fps, 29.97 tbr, 29.97 tbn, 59.94 tbc
#    Stream #0.1: Audio: mp3, 48000 Hz, 2 channels, stereo, s16, 195 kb/s
#At least one output file must be specified'''
#    d='''ffmpeg version 0.8.9-6:0.8.9-1, Copyright (c) 2000-2013 the Libav developers
#  built on Nov  3 2013 00:54:50 with gcc 4.7.2
#*** THIS PROGRAM IS DEPRECATED ***
#This program is only provided for compatibility and will be removed in a future release. Please use avconv instead.
#[mp3 @ 0x1c14b20] max_analyze_duration reached
#[mp3 @ 0x1c14b20] Estimating duration from bitrate, this may be inaccurate
#Input #0, mp3, from '/root/data/source_file/a.wav':
#  Duration: 00:04:13.68, start: 0.000000, bitrate: 24 kb/s
#    Stream #0.0: Audio: mp3, 11025 Hz, stereo, s16, 24 kb/s
#At least one output file must be specified
#'''
    #a = vdnagen.ingest_media_file("192.168.1.200", "maomao", "123", "data/media/c.flv")
    vdnagen.parse_dna_status_result(d)