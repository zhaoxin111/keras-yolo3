import os

def get_box(anno):
    ''''
    Row format: image_file_path box1 box2 ... boxN;
    Box format: x_min,y_min,x_max,y_max,class_id (no space).
    '''
    with open(anno,'r') as f:
        lines = f.readlines()
        boxs = ''
        for i in range(10,len(lines),5):
            line = lines[i]
            corrd = line.split(':')[1].replace(' ','')
            cord_min,cord_max = corrd.split('-')
            boxs = boxs+'{},{},{},{},1 '.format(cord_min.split(',')[0][1:],cord_min.split(',')[1][:-1],cord_max.split(',')[0][1:],cord_max.split(',')[1][:-2])
    return boxs[:-1]


def prepare_traintxt(root_path):
    anno_root = os.path.join(root_path, 'Annotation')
    img_root = os.path.join(root_path, 'PNGImages')
    annos = sorted(os.listdir(anno_root))
    imgs = sorted(os.listdir(img_root))

    save_file = '../model_data/PennFudanPed.txt'

    f = open(save_file,'w')
    for img, anno in zip(imgs,annos):
        box = get_box(os.path.join(anno_root,anno))
        line = os.path.join(img_root,img)+' '+box+'\n'
        f.write(line)
    f.close()

if __name__ == '__main__':
    prepare_traintxt(r'/mnt/raid3/home/zhaoxin/datasets/PennFudanPed/')
