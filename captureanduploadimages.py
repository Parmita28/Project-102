import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time=time.time
        result=False
    return img_name
    print("Snapshot's taken")  
    videocaptureobject.release()  
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.BFEVELTe0Q1LX657cC6uD1x-80Qm8ZycjD_N4JG91wFanbSCthzp4F6IL0ZnhaQAxxg02Pg_UlfeNGrqfH5zbvENpaB02kKQnF0ocPICs98eLymGwfQg5pvmA94Ha7Pkfqix74s"
    file=img_name
    file_from=file    
    file_to="/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()