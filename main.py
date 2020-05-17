import cv2
import sys
from flask import Flask, render_template, Response
from modules.camera import VideoCamera
from flask_basicauth import BasicAuth
import time
import threading
from modules.tgbot import send_photo
from modules.gdrive import backup_to_drive

email_update_interval = 60  # time interval
video_camera = VideoCamera(flip=False)
object_classifier = cv2.CascadeClassifier("models/facial_recognition_model.xml")
#object_classifier = cv2.CascadeClassifier("models/haarcascade_fullbody.xml")  # classifier

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
            fr, frame, found_obj = video_camera.get_object(object_classifier)
            if found_obj and (time.time() - last_epoch) > email_update_interval:
                last_epoch = time.time()
                print("Sending message to TelegramBot...")

                print('\n-- saving image...')
                cv2.imwrite(filename='last_captured_image.jpg', img=fr)
                print('++ done.')

                print("\n-- sending photo...")
                send_photo()
                print("++ done.")

                print("\n-- backing up photo to drive...")
                backup_to_drive()
                print("++ done.")
                print("\n==> All done. Sending message completed!")
        except:
            print("Error sending message: ", sys.exc_info()[0])


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
    app.run(host='0.0.0.0', debug=False)
