import PyPDF2
from gtts import gTTS
from multiprocessing import Process


# Определение функции для генерации аудио файла
def generate_audio(text, mp3_file):
    # Создание аудио из текста с помощью библиотеки gTTS
    audio = gTTS(text, lang="ru", slow=False)
    # Сохранение аудио в указанный файл
    audio.save(mp3_file)


# Определение функции для обработки PDF-файла
def process_pdf(pdf_file_path, text_file_path, mp3_file_path):
    # Открытие PDF-файла для чтения
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Инициализация переменной для хранения текста из PDF-файла
        text = ""
        # Цикл по всем страницам PDF-файла
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            # Добавление текста страницы к общему тексту
            text += page.extractText().replace('\n', ' ')

    # Запись текста в текстовый файл
    with open(text_file_path, 'w') as text_file:
        text_file.write(text)

    # Запуск процесса генерации аудио файла
    audio_process = Process(target=generate_audio, args=(text, mp3_file_path))
    audio_process.start()
    audio_process.join()


# Путь к PDF-файлу
pdf_file_path = 'internet.pdf'
# Путь к TXT-файлу
text_file_path = 'internet.txt'
# Путь к MP3-файлу
mp3_file_path = 'internet.mp3'

process_pdf(pdf_file_path, text_file_path, mp3_file_path)
