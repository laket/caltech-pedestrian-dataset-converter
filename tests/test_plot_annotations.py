#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import glob
import sys
import cv as cv1
import cv2 as cv
from collections import defaultdict

annotations = json.load(open('data/annotations.json'))

out_dir = 'data/plots'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

root = "data/images"
img_fns = defaultdict(dict)
re_index = re.compile('_([0-9]+)\.jpg')

for set_name in sorted(os.listdir(root)):
    img_fns[set_name] = defaultdict(dict)
    path_set = os.path.join(root, set_name)

    for video_name in sorted(os.listdir(path_set)):
        img_fns[set_name][video_name] = []
        path_video = os.path.join(path_set, video_name)
        
        for fn in sorted(os.listdir(path_video)):
            n_frame = re_index.search(fn).group(1)
            fullpath = os.path.join(path_video, fn)
            img_fns[set_name][video_name].append((int(n_frame), fullpath))

n_objects = 0
for set_name in sorted(img_fns.keys()):
    for video_name in sorted(img_fns[set_name].keys()):
        wri = cv.VideoWriter(
            'data/plots/{}_{}.avi'.format(set_name, video_name),
            cv1.CV_FOURCC(*'XVID'), 30, (640, 480))

        if not wri.isOpened():
            print "can't create VideoWriter. configure opencv correctly."
            sys.exit(-1)
        
        for frame_i, fn in sorted(img_fns[set_name][video_name]):
            img = cv.imread(fn)

            if str(frame_i) in annotations[set_name][video_name]['frames']:
                data = annotations[set_name][
                    video_name]['frames'][str(frame_i)]

                for datum in data:
                    x, y, w, h = [int(v) for v in datum['pos']]
                    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                    n_objects += 1

                wri.write(img)

            #cv.imshow("test", img)
            #cv.waitKey(0)
        wri.release()
        print(set_name, video_name)
print(n_objects)
