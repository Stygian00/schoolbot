# extract data from images using OCR and computer vision techniques
import cv2
import pytesseract
def extract_text_from_image(image_path):
    # read the image using OpenCV
    image = cv2.imread(image_path)
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply thresholding to get a binary image
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # use pytesseract to extract text from the binary image
    text = pytesseract.image_to_string(binary)
    return text

#im checking chreey pick command from feture_cli branch 
#add a new line to check the pull request
