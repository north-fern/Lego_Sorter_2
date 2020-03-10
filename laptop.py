import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import json, requests, time

Key = 'zZn5lZCJeeOQ1qhDOzO1QsJem8nFUTkSNL268RZGkY'

def imageProcess():
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open("testFile.jpg")
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    #turn the image into a numpy array
    image_array = np.asarray(image)
    # display the resized image
    image.show()
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    # run the inference
    prediction = model.predict(data)
    return prediction

def takeImage():
    im = cv2.VideoCapture(0)
    time.sleep(1)
    r,f = im.read()
    print(type(f))
    cv2.imwrite("testFile.jpg",f)
    im.release()
    return 

def SL_setup():
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":Key}
     return urlBase, headers
     
def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = requests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)         
          reply = 'failed'
     return reply

def Get_SL(Tag):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = requests.get(urlValue,headers=headers).text
          data = json.loads(value)
          #print(data)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result
     
def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          requests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e) 


takeImg = Get_SL("take_pic")
time.sleep(2)
print(takeImg)
takeImg = 1 

if takeImg == 1:
    img = takeImage()
    predic = imageProcess()
    print(predic)
    print(type(predic))
    legoCat = np.where(predic == max(predic))
    print("Lego Index is" + str(type(legoCat)))
    legoCat = legoCat + 1
    Put_SL("brick_type", "STRING", int2str(legoCat))







