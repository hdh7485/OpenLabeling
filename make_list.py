import glob
files = glob.glob('/home/hdh7485/darknet/darknet181102_tiny_negative/data/img/*.jpg')
with open('train.txt', 'w') as f:
    f.writelines(fn+'\n' for fn in files)
