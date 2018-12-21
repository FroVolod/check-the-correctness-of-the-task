from kuyruk import Kuyruk

import requests

from . import app
from .my_hash import file_hash


kuyruk = Kuyruk()

@kuyruk.task()
def echo(message):
    print ('##### ', message)

@kuyruk.task()
def task_check_version(filename, req_version):
    tests_folder = app.config['TESTS_FOLDER']
    files = None
    req_file = tests_folder / filename
    auth = ('admin', 'admin')

    if not req_file.exists():
        data = {"status": 404}
    else:
        
        version = file_hash(req_file)
        if version == req_version:
            data = {"status": 304}
        else:
            files={'files': open(req_file,'rb')}
            data = {"status": 200}
    
    url = app.config['BASE_URL'] + 'tests/' + filename
    res = requests.post(url, auth=auth, data=data, files=files)
    print ('########## ', res)
   