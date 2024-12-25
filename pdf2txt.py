import os
import sys
import time
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Reads pages from a PDF and returns the combined text,
    plus page count, word count, and character count.
    """
    reader = PdfReader(pdf_path)
    page_count = len(reader.pages)
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text_parts.append(page_text)

    full_text = "\n".join(text_parts)
    words = full_text.split()
    return full_text, page_count, len(words), len(full_text)

def main():
    print("Processing...")
    start_time = time.time()

    input_pdf = "input.pdf"
    output_txt = "output.txt"

    if not os.path.exists(input_pdf):
        alt_inputs = [f for f in os.listdir() if f.startswith("input") and f != "input.pdf"]
        if alt_inputs:
            print(f"Found files: {alt_inputs} — cannot process them.")
        print("Error: Required file 'input.pdf' is missing.")
        print("Processing completed")
        return

    try:
        # Extract text data
        text_data, page_count, word_count, char_count = extract_text_from_pdf(input_pdf)

        if len(text_data.strip()) < 10:
            print("Warning: Extracted text is very short (<10 characters).")

        final_output = output_txt
        if os.path.exists(output_txt):
            with open(output_txt, 'r', encoding='utf-8') as old_file:
                if old_file.read().strip() == text_data.strip():
                    print(f"Content is identical. Overwriting '{output_txt}'.")
                else:
                    final_output = "output2.txt"
                    print(f"Content differs. Writing to '{final_output}'.")

        with open(final_output, 'w', encoding='utf-8') as out_file:
            out_file.write(text_data)

        print("\nText extracted successfully:")
        print(f"- Processed pages: {page_count}")
        print(f"- Total words: {word_count}")
        print(f"- Total characters: {char_count}")

    except Exception as e:
        print(f"\nError: {e}")
    finally:
        print("Processing completed")
        print(f"Time taken: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()