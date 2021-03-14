#import gsmHat as GSM
import GSM
import time



def send_SMS(sender:str, receiver:str, message:str):
    # Send SMS
    gsm = GSM.GSMHat('/dev/ttyUSB0', 115200)
    Number = receiver
    Message = sender + " sent you the following message:\n\n" + message
    gsm.SMS_write(Number, Message)
    time.sleep(10)

def check_received_SMS():
    gsm = GSM.GSMHat('/dev/ttyUSB0', 115200)
    time.sleep(5)
    print(gsm.SMS_available())
    if gsm.SMS_available() > 0:
        number_messages = gsm.SMS_available()
        while number_messages != 0:
            new_sms = gsm.SMS_read()
            print("--------------------------------------------")
            print('Got new SMS from number %s' % new_sms.Sender)
            print('It was received at %s' % new_sms.Date)
            print('The message is: %s' % new_sms.Message)
            print("--------------------------------------------")
            number_messages -= 1
    time.sleep(5)

def get_location():
    from geopy.geocoders import Nominatim
    # Lets print some values
    gsm = GSM.GSMHat('/dev/ttyUSB0', 115200)
    time.sleep(5)
    GPSObj = gsm.GetActualGPS()
    time.sleep(5)
    GPS_Data = gsm.GPS_Data_List()
    for key in GPS_Data:
        print(key + ": " + GPS_Data[key])
    lat = GPS_Data['Latitude']
    lon = GPS_Data['Latitude']
    point = lon + "," + lat
    geolocator = Nominatim(user_agent="Pixel")
    location = geolocator.reverse(point)
    address = location.address
    print(address)



#send_SMS("Dora", "+353861645641", "See you later aligator!")
#check_received_SMS()
get_location() 

