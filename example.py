from selenium import webdriver
import tesserocr
from PIL import Image

if __name__ == "__main__":
    #api = tesserocr.PyTessBaseAPI(path=r'C:\Program Files (x86)\Tesseract-OCR\tessdata')
    #browser = webdriver.Chrome()
    #browser = webdriver.Firefox()
    #browser = webdriver.PhantomJS(executable_path=r'E:\phantomjs\bin\phantomjs.exe')
    #browser.get('https:www.baidu.com')
    #print(browser.current_url)
    image = Image.open('image.png')
    print(tesserocr.image_to_text(image))
    print(tesserocr.file_to_text('image.png'))
