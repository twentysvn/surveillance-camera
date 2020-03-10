import cv2
import sys
from mail import sendEmail
from flask import Flask, render_template, Response
from camera import VideoCamera
from flask_basicauth import BasicAuth
import time
import threading
import tgbot
from datetime import datetime
from tzlocal import get_localzone
import os

email_update_interval = 60  # interval
video_camera = VideoCamera(flip=False)
object_classifier = cv2.CascadeClassifier("models/haarcascade_fullbody.xml") # classifier
tz = get_localzone()


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'qodim'
app.config['BASIC_AUTH_PASSWORD'] = '12345'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
last_epoch = 0


def check_for_objects():
    global last_epoch
    while True:
        try:
            frame, found_obj = video_camera.get_object(object_classifier)
            if found_obj and (time.time() - last_epoch) > email_update_interval:
                last_epoch = time.time()
                print("Sending email...")
                sendEmail(frame)
                today = datetime.now(tz).strftime("%I:%M%p on %B %d, %Y")
                tgbot.send_message("Terdeteksi!!\n\n" + today)
                #cv2.imwrite('anyar.jpg', frame)
                #os.chdir('c:/')
                #image_dir = 'c:/anyar.jpg'
                # print(os.listdir(directory))

                #tgbot.send_photo(image_dir)
                print("done!")
        except:
            print("Error sending email: ", sys.exc_info()[0])


@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='127.0.0.1', debug=False)
