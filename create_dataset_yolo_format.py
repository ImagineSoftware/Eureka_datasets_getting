import os
import shutil


DATA_ALL_DIR = os.path.join('.', 'data')

DATA_OUT_DIR = os.path.join('.', 'data_set/eureka')

for set_ in ['train/eureka', 'validation/eureka', 'test/eureka']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'images'),
                 os.path.join(DATA_OUT_DIR, set_, 'labels')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)

data_set_ids = ['/m/02gsv','/m/0h8nh56','/m/06txfd','/m/0hgr9cc','/m/01b7fy', '/m/09rvlp4','/m/027lnzs','/m/0mcx2','/m/0hg7b','/m/02psk3p','/m/025xf_8','/m/030swj','/m/02x_6w','/m/050k8','/m/03nsht8','/m/0h8k552', '/m/0hgs8xl','/m/0h8kx8s','/m/0h8k5mc','/m/0169zh','/m/07cx4','/m/066zr','/m/024j5d', '/m/0c9sm1','/m/0n5v01m', '/m/0f828h', '/m/0h8mw0p', '/m/0hgryjx','/m/01sdgj', ' /m/03wcykg' ,'/m/06tlg8','/m/0h8jj5_','/m/02635ct','/m/0cw2yv','/m/02zsn','/m/0dzct']

# /m/02gsv -> Diary
# '/m/0h8nh56' -> Conference phone
# '/m/06txfd' -> Headphone amplifier
# "/m/0hgr9cc" -> Headphone ear pad
# '/m/01b7fy' -> Headphones
# /m/09rvlp4 -> Ipad
# /m/027lnzs ->Iphone
# /m/0mcx2 -> Ipod
# /m/0hg7b -> Microphone
# /m/02psk3p -> Microphone preamplifier
# /m/025xf_8 -> Microphone stand
# /m/030swj -> Mobile device
# /m/02x_6w -> Mobile home
# /m/050k8 -> Mobile phone
# /m/03nsht8 -> Mobile phone accessories
# /m/0h8k552 -> Mobile phone battery
# /m/0hgs8xl -> Mobile phone car mount
# /m/0h8kx8s -> Mobile phone case
# /m/0h8k5mc -> Mobile phone charger
# /m/0169zh -> Smartphone
# /m/07cx4 -> Telephone
# /m/066zr -> Telephone card
# /m/024j5d -> Telephone operator
# /m/0c9sm1 -> Wireless microphone
# /m/0n5v01m -> Bag
# /m/0f828h -> Birkin bag
# /m/0h8mw0p -> Bowling ball bag
# /m/0hgryjx,Business bag
# /m/01sdgj,Business card
# /m/03wcykg -> Diaper bag
# /m/06tlg8,Duffel bag
# /m/0h8jj5_,Garment bag
# /m/02635ct,Gig bag
# /m/05zppz,Male person
# /m/02zsn,Female person
# /m/0dzct,Human face

train_bboxes_filename = os.path.join('.', 'train_data_mapping.csv')
validation_bboxes_filename = os.path.join('.', 'validation_data_mapping.csv')
test_bboxes_filename = os.path.join('.', 'test_data_mapping.csv')


for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'validation', 'test'][j]
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in data_set_ids:
                if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'eureka/images', '{}.jpg'.format(id))):
                    shutil.copy(os.path.join(DATA_ALL_DIR, '{}.jpg'.format(id)),
                                os.path.join(DATA_OUT_DIR, set_, 'eureka/images', '{}.jpg'.format(id)))
                with open(os.path.join(DATA_OUT_DIR, set_, 'eureka/labels', '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1
                    ix = data_set_ids.index(class_name)

                    f_ann.write('{} {} {} {} {}\n'.format(ix, xc, yc, w, h))
                    f_ann.close()

            line = f.readline()
