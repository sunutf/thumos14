import os 
from scipy import io

#train_root = "/data/to_docker/datasets/THUMOS_frames/train"
#test_root  = "/data/to_docker/datasets/THUMOS_frames/test"

train_root = "/data/to_docker/datasets/THUMOS_frames/frames"
test_root  = "/data/to_docker/datasets/THUMOS_frames/frames"
train_mat = io.loadmat('validation_set.mat')
test_mat  = io.loadmat('test_set.mat')

train_l = train_mat['validation_videos'][0]
test_l  = test_mat['test_videos'][0]

# 1010 , video_name/ ... / label

#generate classInd.txt
class_l = []
if not os.path.exists('classInd.txt'):
    fo = open('class_ori.txt', 'r')
    f = open('classInd.txt', 'w')
    for line in fo.readlines():
        classlabel = line.split()[1]
        f.write("%s\n"%classlabel)
        class_l.append(classlabel)
    f.close()
    fo.close()
else:
    f = open('classInd.txt', 'r')
    for line in f.readlines():
        classlabel = line.strip()
        class_l.append(classlabel)
    f.close()

print(class_l)
#generate train_split.txt
f = open('thumos_train_split.txt', 'w')
for video in train_l :
    name = video[0][0]
    label = video[3][0]-1#class_l.index(video[2][0])+1
    
    second_label = video[4]
     
    path = os.path.join(train_root, name)
    duration = len(os.listdir(path))
    f.write("%s,%d,%d"%(name,duration,label))
    if len(second_label) != 0:
        second_label = video[5][0]-1#class_l.index(video[4][0])
        f.write(",%d"%second_label)
    f.write("\n")
f.close()
        

#generate val_split.txt
f = open('thumos_val_split.txt', 'w')
for video in test_l :
    name = video[0][0]
    label = video[3][0]-1#class_l.index(video[2][0])+1
    second_label = video[-2]
        
    path = os.path.join(test_root, name)
    duration = len(os.listdir(path))
    
    f.write("%s,%d,%d"%(name,duration,label))
    if len(second_label) != 0:
        second_label = video[-1][0]-1#class_l.index(video[-2][0])
        f.write(",%d"%second_label)
    f.write("\n")
f.close
