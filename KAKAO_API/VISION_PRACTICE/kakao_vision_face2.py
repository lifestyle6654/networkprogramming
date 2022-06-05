import requests
from PIL import Image, ImageFilter

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = '40d4689f5e3f8fdd29e87835d84e9879'

def detect_face(filename): # app_key와 이미지 파일을 POST로 전송하여 얼굴 검출을 수행
    headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
    files = {'image' : open(filename, 'rb')}
    rsp = requests.post(API_URL, headers=headers, files=files)
    return rsp.json() # 검출 결과를 딕셔너리로 변환하여 반환

def mosaic(filename, detection_result): # 모자이크 처리 함수
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width) # 반환되는 x, y, w, h값은
        y = int(face['y']*image.height) # 0~1.0 사이의 비율이므로
        w = int(face['w']*image.width) # 실제 크기를 곱해야
        h = int(face['h']*image.height) # 좌표값을 얻을 수 있음
        box = image.crop((x,y,x+w,y+h)) # 얼굴 부분 잘라내기
    # 모자이크 처리
        box = box.resize((20,20), Image.Resampling.NEAREST).resize((w,h), Image.Resampling.NEAREST)
        image.paste(box, (x,y,x+w,y+h)) # 모자이크 처리한 부분을 다시 붙이기

    return image

if __name__ == "__main__":
    IMAGE = 'myphoto.jpg' # 얼굴 검출할 이미지 파일
    detection_result = detect_face(IMAGE) # API를 이용하여 얼굴 검출
    image = mosaic(IMAGE, detection_result) # 검출한 얼굴을 모자이크 처리
    image.show() 