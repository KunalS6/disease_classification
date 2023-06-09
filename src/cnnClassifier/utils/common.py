import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path):
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load()



