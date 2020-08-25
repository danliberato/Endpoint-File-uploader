import requests, os, json, io
from PIL import Image
from requests_toolbelt import MultipartEncoder

IMAGE_RESIZE_LARGE = 960
IMAGE_RESIZE_MEDIUM = 480
IMAGE_RESIZE_MINI = 160

token = ''
#base_url = 'http://localhost:8080'
metadata = {"metaTags": ["card"], "entitiesUuid": ["69f539b8-3610-4467-b070-ed05b830cb13"]}
login = {
        "username": "user",
        "password": "password"
        }


def upload_files_from_path(dirname):

    for filename in os.listdir(dirname):
        full_name = os.path.join(dirname, filename)
        if os.path.isdir(full_name):  # check if it's a directory
            print("entering..." + full_name)
            upload_files_from_path(full_name)
        else:
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".gif"):
                file_name = filename.split('.')[0]
                print("Uploading "+filename)
                upload_url = base_url + '/manager/products/supplier-number/' + file_name + '/files'
                p = '{"metaTags":["card"]}'

                files = {
                    'metadata': (None, p, 'application/json'),
                    'file': (filename, open(full_name, 'rb'), 'application/octet-stream')
                }
                headers = {
                    'Authorization': token
                }
                response = requests.post(upload_url, files=files, headers=headers)

                if r.status_code is not 200:
                    print("Fail while uploading" + filename)
                    print('MESSAGE = ', json.loads(response.text))
                    print('STATUS = ', response.status_code)
                    #quit(1)


if __name__ == '__main__':
    r = requests.post(base_url + '/login', data=json.dumps(login), headers={'Content-Type': 'application/json'})
    token = r.headers['authorization']
    upload_files_from_path(os.getcwd()+'/photos')
