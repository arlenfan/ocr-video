import easyocr


def readOCR(filename):
    reader = easyocr.Reader(['en'])
    output = reader.readtext(filename)

    x_arr = []
    y_arr = []
    w_arr = []
    h_arr = []
    text_arr = []
    type_arr = []
    for num, i in enumerate(output):
        b = i[0]
        x = float(b[0][0])
        x_ = b[1][0]
        y = float(b[0][1])
        y_ = b[2][1]
        w = float(x_ - x)
        h = float(y_ - y)
        #####
        x_arr.append(x)
        y_arr.append(y)
        w_arr.append(w)
        h_arr.append(h)
        text_arr.append(i[1])
        type_arr.append('u')

    send_to_frontend = {
        'x': x_arr,
        'y': y_arr,
        'w': w_arr,
        'h': h_arr,
        'text': text_arr,
        'type': type_arr
    }
    return send_to_frontend


import os

path = 'test_frames/'

for num, file in enumerate(os.listdir(path)):
    file_path = path + file
    result = readOCR(file_path)
    texts = result['text']
    print("File: ", num)
    print(file_path, texts)
