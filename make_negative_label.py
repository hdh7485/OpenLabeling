import glob
files = glob.glob('images/*.jpg')
for file_name in files:
    with open(file_name[:-3]+'txt', 'w') as f:
        pass
