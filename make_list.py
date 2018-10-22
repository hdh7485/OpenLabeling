import glob
files = glob.glob('./darknet181005/data/img/*.jpg')
with open('train.txt', 'w') as f:
    f.writelines(fn+'\n' for fn in files)
