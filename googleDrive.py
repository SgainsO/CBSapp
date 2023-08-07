from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive as Drive
import os

def authen():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("creds.txt")  # Creates local webserver and auto handles authentication.

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.LocalWebserverAuth()
    else:
        gauth.Authorize()
    drive = Drive(gauth)
    gauth.SaveCredentialsFile("creds.txt")
    return drive

def make_filelist(drive):
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    return fileList

def check_if_newfile_needed(drive, file_name):
    fileList = make_filelist(drive)
    for file in fileList:
        if (file['title'] == file_name):
            return False
    return True

def upload_file_to_drive(file_id, local_path):
    """Overwrites the existing Google drive file."""
    drive = authen()
    fileList = make_filelist(drive)
    print("ac")
    userBool = check_if_newfile_needed(drive, file_id)
    if userBool:
        update_file = drive.CreateFile({'title': file_id})
    else:
        for file in fileList:
            if (file['title'] == file_id):
                update_file = file

    update_file.SetContentFile(local_path)
    update_file.Upload()


#def download_drive_file(file_id, save_path, drive):
 #   """Downloads an existing Google drive file."""
 #   download_file = drive.CreateFile({'title': file_id})
  #  download_file.GetContentFile(save_path)


def totalUpload():
    print("ac")
    upload_file_to_drive("dates.txt", "dates.txt")
    upload_file_to_drive("comments.txt", "comments.txt")

def totalDownload():
    drive = authen()
   # if check_if_newfile_needed == True:
    #    make_placeholder()

    download_drive_file("dates.txt", "dates.txt", drive)
    download_drive_file("comments.txt", "comments.txt", drive)


def make_placeholder(drive):
    file1 = drive.CreateFile({'title:': 'dates.text'})
    file2 = drive.CreateFile({'title:': 'comments.text'})

    file1.SetContentFile("")
    file2.SetcontentFile("")


def download_drive_file(file_id, local_path, drive):
    """Overwrites the existing Google drive file."""
    fileList = make_filelist(drive)
    userBool = check_if_newfile_needed(drive, file_id)
    if userBool:
        d_file = drive.CreateFile({'title': file_id})
        print("Do not work")
    else:
        for file in fileList:
            if (file['title'] == file_id):
                d_file = file

    d_file.GetContentFile(local_path)

