import os
import shutil

#get files/folders from here
source = "/Users/Billy Kennedy-Carr/Downloads"
sourcefiles = os.listdir(source)

#file catagory directories
DestPathEXE = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/exetest"
DestPathZIP = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/ziptest"
DestPathIMG = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/imgtest"
DestPathDOCX = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/docxtest"
DestPathAUDIO = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/audiotest"
DestPathVIDEO = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/videotest"
DestPathPRESENTATION = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/presentationtest"
DestPathFOLDER = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/foldertest"
DestPathMODEL_ASSET = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/model_assettest"
DestPathHTML = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/htmltest"
DestPathMISC = "C:/Users/Billy Kennedy-Carr/Desktop/Downloads/misctest"

#arrays of catagories of file types
IMG = [".png", ".jpg", ".jpeg", ".jfif"]
DOC = [".docx",".doc", ".rtf", ".pdf"]
AUDIO = [".wav", ".mp3"]
VIDEO = [".mp4", ".mov", ".avi", ".flv", ".mpeg"]
ZIP = [".zip", ".rar"]
EXECUTABLE = [".exe", ".msi"]
MODEL_ASSET = [".blend", ".fbx", ".FBX"]
HTML = [".html", ".css", ".js"]

#moves file
for file in sourcefiles:
    if file.endswith(tuple(EXECUTABLE)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathEXE,file))
        print(file)
        print("succesfully moved {} to DestPathEXE".format(file))

    elif file.endswith(tuple(ZIP)):
            shutil.move(os.path.join(source,file), os.path.join(DestPathZIP,file))
            print("succesfully moved {} to DestPathZIP".format(file))

    elif file.endswith(tuple(IMG)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathIMG,file))
        print("succesfully moved {} to DestPathIMG".format(file))

    elif file.endswith(tuple(DOC)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathDOCX,file))
        print("succesfully moved {} to DestPathDOCX".format(file))

    elif file.endswith(tuple(AUDIO)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathAUDIO,file))
        print("succesfully moved {} to DestPathAUDIO".format(file))

    elif file.endswith(tuple(VIDEO)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathVIDEO,file))
        print("succesfully moved {} to DestPathVIDEO".format(file))

    elif file.endswith(".pptx"):
        shutil.move(os.path.join(source,file), os.path.join(DestPathPRESENTATION,file))
        print("succesfully moved {} to DestPathPRESENTATION".format(file))

    elif file.endswith(tuple(MODEL_ASSET)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathMODEL_ASSET,file))
        print("succesfully moved {} to DestPathMODEL_ASSET".format(file))

    elif file.endswith(tuple(HTML)):
        shutil.move(os.path.join(source,file), os.path.join(DestPathHTML,file))
        print("succesfully moved {} to DestPathHTML".format(file))

    else:
        shutil.move(os.path.join(source,file), os.path.join(DestPathMISC, file))
        print("succesfully moved {} to DestPathMISC".format(file))



#moves folders
for entry in os.listdir(source):
    if os.path.isdir(os.path.join(source, entry)):
        print(entry)
        shutil.move(os.path.join(source, entry), os.path.join(DestPathFOLDER, entry))
