## English

Overview  
Three Python scripts for preparing data for processing by large language models (LLMs):  
1. pdf2txt.py — extracts text from `input.pdf` and saves it to a text file; can compare the extracted text to existing content and create a new file if differences are detected  
2. tgcutter.py — parses a Telegram chat or channel export (`result.json`), extracting message texts and summarizing statistics (e.g., total messages, empty messages, service messages)  
3. dirmerger.py — merges files into a single `dir.txt`, using a blacklist or whitelist approach for filenames, directories, and extensions  

Key Features  
- command-line interface only (no GUI)  
- error handling and notifications in the console  
- optional filtering of files by extensions or explicit exclusion lists  
- displays completion messages and processing statistics, including file sizes and line counts  

Additionally, consider exploring Cursor, Aider, and Cline — tools designed to simplify similar data preparation and processing tasks  

Usage  
1. Place the scripts (`pdf2txt.py`, `tgcutter.py`, `dirmerger.py`) in the same directory as your input files  
2. Run them individually with `python scriptname.py`  
3. Adjust settings (blacklist/whitelist, excluded directories, etc.) directly in the source code  

---

## Русский

Обзор  
Три Python-скрипта для подготовки данных перед отправкой в большие языковые модели (LLM):  
1. pdf2txt.py — извлекает текст из `input.pdf` и сохраняет его в текстовый файл; может сравнить извлечённый текст с уже имеющимся и создать новый файл, если найдены отличия  
2. tgcutter.py — парсит экспорт чата или канала Telegram (`result.json`), извлекая текст сообщений и рассчитывая статистику (общее количество сообщений, пустые сообщения, служебные сообщения)  
3. dirmerger.py — объединяет файлы в один `dir.txt`, используя чёрные или белые списки расширений, имён файлов и директорий  

Ключевые особенности  
- интерфейс командной строки (без графического интерфейса)  
- обработка ошибок и уведомления выводятся в консоль  
- возможность фильтровать файлы по расширениям или исключать их из обработки  
- вывод завершения и статистики, включая размер объединённых данных и количество строк  

Рекомендуется обратить внимание на инструменты Cursor, Aider и Cline — они упрощают аналогичные задачи по подготовке и обработке данных  

Использование  
1. Разместите скрипты (`pdf2txt.py`, `tgcutter.py`, `dirmerger.py`) в одной папке с входными файлами  
2. Запускайте их по отдельности командой `python scriptname.py`  
3. Настраивайте параметры (списки расширений, исключения и т. д.) в исходном коде  