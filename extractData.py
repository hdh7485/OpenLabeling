import csv

def yolo_format(class_index, point_1, point_2, width, height):
    # YOLO wants everything normalized
    # Order: class x_center y_center x_width y_height
    x_center = (point_1[0] + point_2[0]) / float(2.0 * width)
    y_center = (point_1[1] + point_2[1]) / float(2.0 * height)
    x_width = float(abs(point_2[0] - point_1[0])) / width
    y_height = float(abs(point_2[1] - point_1[1])) / height
    return str(class_index) + " " + str(x_center) + " " + str(y_center) + " " + str(x_width) + " " + str(y_height)

def main():
    label = {'go':0, 'stop':1, 'warning':2}
    image_width, image_height = 1280, 960
    last_file_name = ''
    firstline = True
    with open('frameAnnotationsBOX.csv', 'r') as reader:
        for line in reader:
            if firstline:
                firstline = False
                continue
            fields = line.split(';')
            #data:filename, label, upper left corner x, y, lower right corner x, y
            data = [fields[0], fields[1], [int(fields[2]), int(fields[3])], [int(fields[4]), int(fields[5])]]
            
            file_name = 'yolo_labels/'+data[0][8:-3]+'txt'
            print(file_name)
            if last_file_name == data[0]:
                writer = open(file_name, 'a')
                if data[1] != 'go' and data[1] != 'stop' and data[1] != 'warning':
                    pass
                else:
                    yolo_data = yolo_format(label[data[1]], data[2], data[3], image_width, image_height)
                    print(yolo_data)
                    writer.write('\n'+yolo_data)
                writer.close()
            else:
                writer = open(file_name, 'w')
                if data[1] != 'go' and data[1] != 'stop' and data[1] != 'warning':
                    pass
                else:
                    yolo_data = yolo_format(label[data[1]], data[2], data[3], image_width, image_height)
                    print(yolo_data)
                    writer.write(yolo_data)
                writer.close()
            last_file_name = data[0]

if __name__ == '__main__':
    main()
