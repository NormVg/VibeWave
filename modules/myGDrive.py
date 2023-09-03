from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


permission = {
    'type': 'anyone',
    'value': None,
    'role': 'reader',
    'withLink': True
}
import os
gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# gauth.SaveCredentialsFile("cred.json")
gauth.LoadCredentialsFile("cred.json")

drive = GoogleDrive(gauth)


def upload_file(file):
    filee = drive.CreateFile({"parents":[{"id":'1OYdiWyPzTqdamyresLkRbetn9wC1xZFN'}]})
    filee.SetContentFile(file)
    file_name = os.path.basename(file)
    filee['title'] = file_name
    filee.Upload()
    filee.InsertPermission(permission)
    return filee['id']

def download_file(file , id=None):
    if not id:
        file_list = drive.ListFile({'q': "'1OYdiWyPzTqdamyresLkRbetn9wC1xZFN' in parents and trashed=false"}).GetList()
        for f in file_list:
            if file == f["title"]:
                id = f["id"]
                break
    # filee = drive.CreateFile({"id":id})
    # print('Downloading file %s from Google Drive' % filee['title'])
    # print(filee['alternateLink'])
    # file_name = os.path.basename(filee['title'])
    # filee.GetContentFile(file_name)
    # os.rename(file_name , f"static/cloud/{file_name}")
    link = f"https://www.googleapis.com/drive/v3/files/{id}?alt=media&key=AIzaSyBwi8dTMiaHUIy6mXuv0DmZyfuIkZqfO5A"
    return link

#https://www.googleapis.com/drive/v3/files/1K_c0NYWOWuuNX4rrIsHzZvtZkoSifWQm?alt=media&key=AIzaSyBwi8dTMiaHUIy6mXuv0DmZyfuIkZqfO5A
def create_file(name,data):
    file = drive.CreateFile({'title': name,"parents":[{"id":'1OYdiWyPzTqdamyresLkRbetn9wC1xZFN'}]}) 
    # drive.auth.service.permissions().create(fileId=file['id'], body=permission).execute()
    file.SetContentString(data) 
    file.Upload()
    file.InsertPermission(permission)

def get_file_list():
    audio_list = []
    file_list = drive.ListFile().GetList()
    for file1 in file_list:
        if file1['mimeType'] != 'application/vnd.google-apps.folder':
            audio_list.append({'title':file1['title'],"id":file1['id']})
    print(len(audio_list))
    return audio_list

