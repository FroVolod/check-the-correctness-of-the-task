from flask import request, send_from_directory, abort

from .security import auth

from . import app
from .tasks import task_check_version
from .tasks import echo

storage = {}
print('&&&  ', storage)

@app.route('/tests/<filename>', methods=['POST','GET'])
@auth.login_required
def check_version(filename):
    print('???????????????  ', storage)
    if request.method == 'GET':
        if filename in storage:
            return storage[filename]
        req_version = request.headers.get('If-None-Match')
        task_check_version(filename, req_version)    
        return '[*] Task in queue\n'

    elif request.method == 'POST':
        print('*******  status: ', request.form.get('status'))
        #print('********  file:', request.files.get('files').read().decode('utf-8'))
        if request.files:
            storage[filename] = request.files.get('files').read()
        return '[#] Response'


@app.route('/tests/', methods=['POST'])
@auth.login_required
def test_echo():
    for i in range(3):
        message = "Hello Kuyruk " + str(i)
        echo(message)
        print('[*] ', message)
    return '[*] Task in queue\n'
    