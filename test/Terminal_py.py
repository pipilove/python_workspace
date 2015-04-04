import os
if __name__ == "__main__":
    # pic_list = os.listdir('/media/E/mine/pythonworkspace/PatternRecog/FaceRecog/faces_extract')
    TrainNumber = os.system('cd ./faces_extract; ls | wc -l 1> /dev/null')-1
    print((type(TrainNumber)))
    print(TrainNumber)
    # print type(pic_list)
