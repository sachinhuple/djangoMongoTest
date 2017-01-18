from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from TestDjangoProject.settings import DBNAME

connect(DBNAME)

class FileDetails(Document):
    fileName=StringField(max_length=60,required=True)
    filePath=StringField(max_length=200, required=True)
    fileType=StringField(max_length=50, required=True)
    author=StringField(max_length=100, required=True)





