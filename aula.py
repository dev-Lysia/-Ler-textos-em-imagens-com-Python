import pytesseract
import cv2

# passo 1 --> ler a imagem

imagem = cv2.imread("print_magalu.JPG")

# passo 2 --> extrair o texto

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)


