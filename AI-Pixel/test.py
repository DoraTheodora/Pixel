from gsmHat import GSMHat, SMS, GPS
import time



def send_SMS(sender:str, receiver:str, message:str):
    # Send SMS
    gsm = GSMHat('/dev/ttyUSB0', 115200)
    Number = receiver
    Message = sender + " sent you the following message:\n\n" + message
    gsm.SMS_write(Number, Message)
    time.sleep(10)

def check_received_SMS():
    gsm = GSMHat('/dev/ttyUSB0', 115200)
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

def get_location():
    # Lets print some values
    gsm = GSMHat('/dev/ttyUSB0', 115200)
    GPSObj = gsm.GetActualGPS()
    print('GNSS_status: %s' % str(GPSObj.GNSS_status))
    print('Fix_status: %s' % str(GPSObj.Fix_status))
    print('UTC: %s' % str(GPSObj.UTC))
    print('Latitude: %s' % str(GPSObj.Latitude))
    print('Longitude: %s' % str(GPSObj.Longitude))
    print('Altitude: %s' % str(GPSObj.Altitude))
    print('Speed: %s' % str(GPSObj.Speed))
    print('Course: %s' % str(GPSObj.Course))
    print('HDOP: %s' % str(GPSObj.HDOP))
    print('PDOP: %s' % str(GPSObj.PDOP))
    print('VDOP: %s' % str(GPSObj.VDOP))
    print('GPS_satellites: %s' % str(GPSObj.GPS_satellites))
    print('GNSS_satellites: %s' % str(GPSObj.GNSS_satellites))
    print('Signal: %s' % str(GPSObj.Signal))

#send_SMS("Dora", "+353861645641", "See you later aligator!")
#check_received_SMS()
get_location() 

