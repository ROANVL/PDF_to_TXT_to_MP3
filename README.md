# PDF_to_TXT_to_MP3

Этот скрипт использует модули PyPDF2, gTTS и multiprocessing для преобразования PDF-файла в текстовый и аудио-файлы.

PyPDF2 используется для чтения содержимого PDF-файла.
gTTS используется для генерации аудио из текста.
multiprocessing используется для запуска генерации аудио в отдельном процессе.

Процесс обработки PDF-файла включает следующие шаги:

    Открытие PDF-файла для чтения
    Извлечение текста из всех страниц PDF-файла
    Запись текста в текстовый файл
    Запуск процесса генерации аудио из текста

После завершения этого скрипта, у вас будут текстовый и аудио-файлы, соответствующие содержимому PDF-файла.
