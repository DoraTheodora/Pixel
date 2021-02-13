
def takePictures():
    import cv2
    import os
    import time

    name = input("Your name: ");
    path = "photos/"+name
    os.mkdir(path)
    camera = cv2.VideoCapture(0);
    end = time.time() + 10 
    i = 0

    print("[INFO] Taking pictures")
    while(time.time() < end):
            ret, image = camera.read()
            i+=1
            cv2.imwrite('photos/'+name+'/'+str(i)+'.png', image)
    del(camera)
    training(name)

def  training(name:str):
    import cv2
    import pickle

    from imutils import paths
    import face_recognition

    print("[INFO] Starting training...")
    path = "photos/"
    encodings = pickle.loads(open("Cascades/encodings.pickle", "rb").read())

    imagePaths = list(paths.list_images(path))
    knownFaces = []
    knownNames = []

    for (i, imagePath) in enumerate(imagePaths):
        print("[INFO] processing images: " + imagePath)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownFaces.append(encoding)
            knownNames.append(name)
    print("[INFO] save encodings...")
    data = {"encodings": knownFaces, "names": knownNames}
    file = open("Cascades/encodings.pickle", "wb")
    file.write(pickle.dumps(data))
    file.close()

    #TODO: try with MIKE

   
    

          



takePictures()
#training()