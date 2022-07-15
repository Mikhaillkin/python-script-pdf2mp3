from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path = 'test.pdf', language = 'en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('Allright! File exists')
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file = file_path, mode = 'rb')) as pdf:
            pages = [ page.extract_text() for page in pdf.pages ]

        text = ''.join(pages)
        text = text.replace('\n','')

        with open(f'{Path(file_path).name}.txt','w') as file:               # Создание текстового файла без переносов строки
            file.write(text)                                                # который будет записан в mp3 и будет зачитан

        my_audio = gTTS(text=text, lang = language, slow= False)            # Создание аудиодорожки спарсенного текста
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully\n---Have a good day!'
    else:
        return "File does not exist.Check the file path"



def main():
    tprint('PDF>>TO>>MP3', font = 'bulbhead')
    file_path = input("\nEnter an Absolute file path\n(for example: C:/Users/Terry/PycharmProjects/pdf_2_mp3/pdf_files/test.pdf): ")
    language = input("Choose language, for example 'en' or 'ru': ")

    print(pdf_to_mp3(file_path=file_path, language = language))


if __name__ == '__main__':
    main()