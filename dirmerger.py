import os
import sys
import time

# -------------------------------------------------------------------
# BLACKLIST MODE (default)
#   Skip items if they match these lists:
#     - excluded_files (relative paths)
#     - excluded_dirs (folder names)
#     - excluded_extensions (e.g. .txt, .md)
# -------------------------------------------------------------------
excluded_files = [
    'dir.txt',        # merged output file
    'result.json',
    'dirmerger.py',
    'readme.md'
]
excluded_dirs = [
    '__pycache__',
    '.history',
    '.idea',
    '.git',
    '.vscode'
]
excluded_extensions = ('.txt', '.md')  # skip any file ending with .txt or .md


# -------------------------------------------------------------------
# WHITELIST MODE (commented out)
#   If you want to ONLY allow certain items, use the allowed_* lists.
# -------------------------------------------------------------------
# allowed_files = [
#     # e.g. 'keepme.txt', 'somefolder/special.md'
# ]
# allowed_dirs = [
#     # e.g. 'somedirectory', 'another_folder'
# ]
# allowed_extensions = ('.txt', '.md')  # only .txt and .md are allowed


def scan_and_combine(directory, output_file):
    """
    Walks through 'directory', merging files into 'dir.txt'.
    
    By default (blacklist mode), it skips:
      - any file if its relative path is in excluded_files
      - any directory in excluded_dirs
      - any file if its extension is in excluded_extensions
    
    If switching to whitelist mode (uncomment the blocks below), 
    then it will only process items that appear in the allowed_* lists
    or have an extension from allowed_extensions.
    
    Returns:
      processed_files (int) - number of files merged
      skipped_files   (list) - which files were skipped
      total_size      (int)  - total bytes merged
      total_lines     (int)  - total line count
    """
    skipped_files = []
    processed_files = 0
    total_size = 0
    total_lines = 0

    # Open the output file
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(directory):
            # BLACKLIST for directories
            dirs[:] = [d for d in dirs if d not in excluded_dirs and not d.startswith('.')]

            # WHITELIST for directories (comment out the above if you enable this)
            # dirs[:] = [d for d in dirs if d in allowed_dirs]

            for f in files:
                relative_path = os.path.relpath(os.path.join(root, f), directory)

                # -----------------------------------------------------------
                # BLACKLIST approach for files:
                # -----------------------------------------------------------
                if relative_path in excluded_files:
                    skipped_files.append(relative_path)
                    continue
                
                # BLACKLIST approach for extensions
                _, ext = os.path.splitext(f.lower())
                if ext in excluded_extensions:
                    skipped_files.append(relative_path)
                    continue

                # -----------------------------------------------------------
                # WHITELIST approach for files (comment out BLACKLIST blocks above):
                # -----------------------------------------------------------
                # if relative_path not in allowed_files:
                #     skipped_files.append(relative_path)
                #     continue

                # WHITELIST approach for extensions
                # _, ext = os.path.splitext(f.lower())
                # if ext not in allowed_extensions:
                #     skipped_files.append(relative_path)
                #     continue
                # -----------------------------------------------------------

                # If not a normal file, skip
                full_path = os.path.join(root, f)
                if not os.path.isfile(full_path):
                    skipped_files.append(relative_path)
                    continue

                try:
                    with open(full_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        out.write(f"---\n{relative_path}:\n\n{content}\n\n")
                        processed_files += 1
                        total_size += len(content.encode('utf-8'))
                        total_lines += (content.count('\n') + 1) if content else 0
                except Exception:
                    skipped_files.append(relative_path)

    return processed_files, skipped_files, total_size, total_lines


def main():
    print("Processing...")
    start_time = time.time()

    directory = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(directory, 'dir.txt')

    try:
        processed, skipped, size_bytes, lines_count = scan_and_combine(directory, output_file)

        print("Processing completed")
        print(f"- Processed files: {processed}")
        print(f"- Skipped files: {len(skipped)} ({', '.join(skipped)})")
        print(f"- Total lines: {lines_count}")
        print(f"- Total size: {size_bytes / 1024:.2f} KB")

    except Exception as e:
        print(f"Critical error: {e}")
    finally:
        print(f"Time taken: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()