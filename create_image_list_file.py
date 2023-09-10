import os

data_set_ids = ['/m/02gsv','/m/0h8nh56','/m/06txfd','/m/0hgr9cc','/m/01b7fy', '/m/09rvlp4','/m/027lnzs','/m/0mcx2','/m/0hg7b','/m/02psk3p','/m/025xf_8','/m/030swj','/m/02x_6w','/m/050k8','/m/03nsht8','/m/0h8k552', '/m/0hgs8xl','/m/0h8kx8s','/m/0h8k5mc','/m/0169zh','/m/07cx4','/m/066zr','/m/024j5d', '/m/0c9sm1','/m/0n5v01m', '/m/0f828h', '/m/0h8mw0p', '/m/0hgryjx','/m/01sdgj', ' /m/03wcykg' ,'/m/06tlg8','/m/0h8jj5_','/m/02635ct']

train_bboxes_filename = os.path.join('.', 'train_data_mapping.csv')
validation_bboxes_filename = os.path.join('.', 'validation_data_mapping.csv')
test_bboxes_filename = os.path.join('.', 'test_data_mapping.csv')

image_list_file_path = os.path.join('.', 'image_list_file.csv')

image_list_file_list = []
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in data_set_ids and id not in image_list_file_list:
                image_list_file_list.append(id)
                with open(image_list_file_path, 'a') as fw:
                    fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], id))
            line = f.readline()

        f.close()
