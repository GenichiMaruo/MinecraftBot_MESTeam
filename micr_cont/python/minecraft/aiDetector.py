import sys
sys.path.append('.')
sys.path.append('./python/minecraft/')

from time import sleep
import cv2
import numpy as np
from PIL import ImageGrab
# import pytesseract

class AiDetector:
    def __init__(self) -> None:
        self.bbox = (20, 120, 900, 880)
        self.pos_box=(45, 20, 130, 45)
        self.margin = (0, -60)
        self.cascade_path = 'python/minecraft/data/cascade/cascade.xml'
        self.cascade = cv2.CascadeClassifier(self.cascade_path)


    def wright_txt(self, vector, max, white):
        f = open('tmp.txt', 'w', encoding='UTF-8')
        f.write(str(int(vector[0]*10))+'\n')
        f.write(str(int(vector[1]*10))+'\n')
        f.write(str(max)+'\n')
        f.write(white)
        f.close()


    def show_cascaded_image(self, img, white):
        #show cascaded image
        tmp_img = img
        cv2.putText(img,
                    text=white,
                    org=(60, 60),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.0,
                    color=(255, 0, 0),
                    thickness=2,
                    lineType=cv2.LINE_4)

        grayed = cv2.cvtColor(tmp_img, cv2.COLOR_BGR2GRAY)
        objs = self.cascade.detectMultiScale(grayed, 1.1, 5, minSize=(24, 24))
        #print(len(objs))
        max_box = [0, 0, 0, 0, 0]
        vector = [0, 0]
        for (x, y, w, h) in objs:
            if w + h + y > max_box[0] + max_box[2]:
                max_box = [w + h, x, y, w, h]
                vector = []
                vector.append(x + (w / 2) - (self.bbox[2] / 2) - self.margin[0])
                vector.append(y + (h / 2) - (self.bbox[3] / 2) - self.margin[1])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.line(img, (int(self.bbox[2]/2)+self.margin[0], int(self.bbox[3]/2) +
                    self.margin[1]), (int(x+(w/2)), int(y+(h/2))), (225, 225, 225), 1)
            cv2.putText(img,
                        text=str(vector[0])+','+str(vector[1]),
                        org=(x, y-10),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5,
                        color=(0, 255, 0),
                        thickness=1,
                        lineType=cv2.LINE_4)

        if len(objs) == 0:
            max_box = [0, 0, 0, 0, 0]
            vector = [0, 0]
        self.wright_txt(vector, max_box[0], white)
        cv2.rectangle(img, (max_box[1], max_box[2]), (max_box[1] +
                    max_box[3], max_box[2]+max_box[4]), (0, 65, 255), 2)
        pos_y = int((self.bbox[3]+(2*self.margin[1])) * ((100.0-float(white))/100.0))
        cv2.line(img, (int(int(self.bbox[2]/2)+40), pos_y), (int(int(self.bbox[2]/2)-40), pos_y), (0, 165, 225), 2)
        cv2.imshow('cockpit', img)
        cv2.moveWindow('cockpit', 1000, 0)


    def ground_ratio(self, frame: str):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        th, binary_img = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
        pixel = binary_img.size
        white = ("{0:.1f}".format(cv2.countNonZero(binary_img)/pixel*100))
        return white


    # def get_position(self):
    #     img = ImageGrab.grab(bbox=self.pos_box)
    #     number = pytesseract.image_to_string(img)
    #     print(number)


    def main(self):
        # capture = cv2.VideoCapture(0)
        while(True):
            # ret, frame = capture.read()
            frame = cv2.cvtColor(
                np.array(ImageGrab.grab(bbox=self.bbox)), cv2.COLOR_BGR2RGB)
            white = self.ground_ratio(frame)
            self.show_cascaded_image(frame, white)
            # self.get_position()
            # sleep(1.0/20.0)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    AiDetector().main()
