import glob
files = glob.glob('/home/hdh7485/darknet/darknet181209_tiny_face/data/img/*.jpg')
files = files + glob.glob('/home/hdh7485/darknet/darknet181209_tiny_face/data/img/*.JPG')
with open('train.txt', 'w') as f:
    f.writelines(fn+'\n' for fn in files)
