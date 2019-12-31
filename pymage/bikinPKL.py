#!/usr/bin/python

import glob
import os
import pickle
from PIL import Image
from cari_ciri import PencariCiri

fe = PencariCiri()

for img_path in sorted(glob.glob('../media/img/*.jpg')):
    print(img_path)
    img = Image.open(img_path)  # pakai PIL image
    ciriciri = fe.ekstraksi(img)
    path_ciri = '../media/ciri/' + os.path.splitext(os.path.basename(img_path))[0] + '.pkl'
    pickle.dump(ciriciri, open(path_ciri, 'wb'))
