import os , shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    print("Organising your files intro [ images - music - video -executable - archive - torrent - document - code - design files]")
    for filename in os.listdir(dir_path):
        # Check if files are code files
        if filename.lower().endswith((".py", ".php", ".html" , ".css" , ".js")):
            #Check if this file is Not The Script File itself
            if not __file__.endswith(filename):
                # If code folder doesnt exist then create
                dir_name = "code"
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                shutil.move(filename, dir_name)
                #os.remove(filename)

        # Check if files are images and you can add more extentions 
        elif filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")):
            # If images folder doesnt exist then create new folder
            dir_name = "images"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)

        # Check if files are music and you can add more extentions
        elif filename.lower().endswith((".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw")):
            # If music folder doesnt exist then create
            dir_name = "music"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)

        # Check if files are videos and you can add more extentions
        elif filename.lower().endswith((".webm", ".mp4")):
            # If video folder doesnt exist then create
            dir_name = "video"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)

        # Check if files are executables
        elif filename.lower().endswith((".exe", ".msi", ".deb" , "dmg")):
            # If executables folder doesnt exist then create
            dir_name = "executables"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)

        # Check if files are archive files
        elif filename.lower().endswith((".rar", ".tar" , ".zip" , ".gz")):
            # If archive folder doesnt exist then create
            dir_name = "archive"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)


        # Check if files are torrent files
        elif filename.lower().endswith((".torrent",)):
            # If torrent folder doesnt exist then create
            dir_name = "torrent"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)

        # Check if files are documents
        elif filename.lower().endswith((".txt", ".pdf", ".docx" , "doc")):
            # If documents folder doesnt exist then create
            dir_name = "design-files"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)


        # Check if files are design files
        elif filename.lower().endswith((".psd", ".ai")):
            # If desgin folder doesnt exist then create
            dir_name = "design-files"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(filename, dir_name)
            #os.remove(filename)


        # If file Doesn't Match any extension
        else :
            if os.path.isfile(filename):
                dir_name = "others"
                # If Others folder doesnt exist then create .
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                shutil.move(filename, dir_name)
                #os.remove(filename)'''



except Exception as e:
    print("Error happened ...... try again" , e)
print("Finished organising your files")