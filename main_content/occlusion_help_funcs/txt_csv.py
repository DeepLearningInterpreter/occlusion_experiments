import cv2
import glob
import os
import pandas as pd
import xml.etree.ElementTree as ET

def string_to_words(text):
    last_space = 0
    cur_space = 0
    i = 0
    words = []
    for symbol in text:
        if symbol == ' ' or symbol == '\n':
            cur_space = i
            words.append(text[last_space:cur_space])
            last_space = cur_space + 1
        i += 1
    return words

def decimal_to_integer(number):
    i = 0
    for symbol in number:
        if symbol == '.':
            intStr = number[:i]
            break
        i += 1
    return intStr


def txt_to_csv(path):
    path_len = len(path)
    txt_list = []
    for txt_file in glob.glob(path + '/*.txt'):
        #import pdb; pdb.set_trace()
        file = open(txt_file)
        info = file.read()

        filename = txt_file[path_len+1:]
        filename = filename[:-3] + 'jpg'
        import pdb; pdb.set_trace()
        img = cv2.imread(filename)
        height = img.shape[0]
        width = img.shape[1]
        #label = 'pistol'

        wordlist = string_to_words(info)

        for i in range(int(len(wordlist)/5)):
            label = wordlist[i*5 + 0]
            x_min = decimal_to_integer(wordlist[i*5 + 1])
            y_min = decimal_to_integer(wordlist[i*5 + 2])
            x_max = decimal_to_integer(wordlist[i*5 + 3])
            y_max = decimal_to_integer(wordlist[i*5 + 4])

            if label == "Handgun":
                label = "pistol"

            value = (
                filename, y_min, x_min, y_max, x_max
            )
            txt_list.append(value)

    column_name = [
        'filename', 'ymin', 'xmin', 'ymax', 'xmax'
    ]
    df = pd.DataFrame(txt_list, columns = column_name)
    return df

def main():
    image_path = os.getcwd()
    txt_df = txt_to_csv(image_path)
    full_df = txt_df
    full_df.to_csv('directory/nameAndBB.csv', index=None)
    print('Successfully converted txt to csv.')

main()
