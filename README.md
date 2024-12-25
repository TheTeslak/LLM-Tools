# README

## English

**Overview**  
This repository contains three Python scripts that handle text extraction and file merging:
1. **pdf2txt.py** — Extracts text from `input.pdf` and saves it to a text file, with options to check for identical content and produce a second output file if differences are detected.  
2. **tgcutter.py** — Parses a `result.json` file, extracting message texts and summarizing statistics (e.g., total messages, empty messages, etc.).  
3. **dirmerger.py** — Merges files into a single `dir.txt`, using either a blacklist or whitelist approach for filenames, directories, and/or extensions.

**Key Features**  
- Command-line interface only (no GUI).  
- Error handling and notifications in the console.  
- Optional filtering of files by extensions or explicit exclusion lists.  
- Prints completion messages and processing statistics, including file sizes and line counts.  

**Usage**  
1. Place the scripts (`pdf2txt.py`, `tgcutter.py`, `dirmerger.py`) in the same directory as your input files.  
2. Run them individually with `python scriptname.py`.  
3. Adjust any settings (blacklist/whitelist, excluded directories, etc.) directly in the source code.

---

## Русский

**Обзор**  
В этом репозитории находятся три Python-скрипта, которые занимаются извлечением текста и объединением файлов:
1. **pdf2txt.py** — Извлекает текст из `input.pdf` и сохраняет в текстовый файл; при необходимости сравнивает содержимое со старым файлом и создаёт новый при наличии изменений.  
2. **tgcutter.py** — Парсит файл `result.json`, извлекая текст сообщений и рассчитывая статистику (общее число сообщений, пустые сообщения, служебные, и т. д.).  
3. **dirmerger.py** — Объединяет файлы в один `dir.txt`, используя чёрный или белый список расширений, файлов и директорий.

**Ключевые особенности**  
- Интерфейс командной строки (без графического интерфейса).  
- Обработка ошибок и уведомления выводятся в консоль.  
- Возможность выбора фильтрации файлов по расширениям, а также исключения отдельных файлов/директорий.  
- Выводит сообщение о завершении и статистику, включая размер объединённых данных и количество строк.

**Использование**  
1. Разместите скрипты (`pdf2txt.py`, `tgcutter.py`, `dirmerger.py`) в одной папке с входными файлами.  
2. Запускайте их по отдельности командой `python scriptname.py`.  
3. Настраивайте нужные параметры (списки расширений, исключения, и т. д.) прямо в исходном коде.