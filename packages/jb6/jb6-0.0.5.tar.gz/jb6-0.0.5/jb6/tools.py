# _*_ coding: utf-8 _/*_
import datetime
import os
import string
from zhon.hanzi import punctuation


def is_docker():
    path = '/proc/self/cgroup'
    return (os.path.exists('/.dockerenv') or
            os.path.isfile(path) and any('docker' in line for line in open(path)))


def filter_punctuations(text):
    for i in string.punctuation:
        text = text.replace(i, "")
    for i in punctuation:
        text = text.replace(i, "")
    return text
