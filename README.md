# To create for Eureka data Set
Need to download training dataset mapping [train](https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv)

Need to download validation dataset mapping [validation](https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv)

Need to download test dataset mapping [test](https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv)

After downloading those datasets

add those files in this folders

You can Create a vertual environment for this project

```
python3 -m venv venv
```

We need to Run 

```
python3 create_image_list_file.py
```

note: need to change file names in this file  `create_image_list_file.py`.

need to run to downloader.py

```
python3 downloader.py image_list_file.csv --download_folder=data
```

then we need to run

```
python3 create_dataset_yolo_format.py
```
