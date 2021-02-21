 single 
def takePictures():
    """[This method takes pictures of the user in front of the mirror for 10 seconds]
    """
    import cv2
    import os
    import time
    import os.path

    from os import path

    name = input("Your name: ")
    folder_exists = True
    while folder_exists:
        if path.exists("Photos/"+name):
            name = input("The name is areleady used. Please insert another name: ")
        else:
            folder_exists = False
    path = "Photos/"+name
    os.mkdir(path)
    camera = cv2.VideoCapture(0);
    end = time.time() + 5 
    i = 0

    print("[INFO] Taking pictures")
    while(time.time() < end):
            ret, image = camera.read()
            i+=1
            cv2.imwrite('Photos/'+name+'/'+str(i)+'.png', image)
    del(camera)
    training(name)

def training(name:str):
    import cv2
    import pickle
    import face_recognition

    from imutils import paths

    print("[INFO] Starting training...")
    path = "Photos/"+name
    encodings = pickle.loads(open("Cascades/encodings.pickle", "rb").read())

    imagePaths = list(paths.list_images(path))
    knownFaces = []
    knownNames = []

    for (i, imagePath) in enumerate(imagePaths):
        print("[INFO] Processing images: " + imagePath)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownFaces.append(encoding)
            knownNames.append(name)
    print("[INFO] Save encodings...")
    data = {"encodings": knownFaces, "names": knownNames}
    file = open("Cascades/encodings.pickle", "wb")
    file.write(pickle.dumps(data))
    file.close()





          



takePictures()
#training()