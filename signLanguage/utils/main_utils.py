import os
import sys
import yaml
import base64

from signLanguage.exception import SignException
from signLanguage.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise SignException(e, sys) from e
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) ->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            logging.info("Writing yaml file successfully")

    except Exception as e:
        raise SignException(e, sys)
    

def decodeImage(imgstring, filename: str):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImage(cropped_img_path: str):
    with open(cropped_img_path, 'rb') as f:
        imgdata = f.read()
        imgstring = base64.b64encode(imgdata)
        return imgstring