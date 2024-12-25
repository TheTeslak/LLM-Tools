import json
import os
import sys
import time
import itertools

def spinner():
    """Displays a rotating spinner in the main thread."""
    for char in itertools.cycle('-\\|/'):
        sys.stdout.write(f'\rProcessing {char}')
        sys.stdout.flush()
        time.sleep(0.1)

def extract_text_blocks(data):
    """
    Recursively collects text blocks and calculates statistics:
    total_messages, text_messages, empty_messages, service_messages, total_characters.
    """
    texts = []
    stats = {
        'total_messages': 0,
        'text_messages': 0,
        'empty_messages': 0,
        'service_messages': 0,
        'total_characters': 0
    }

    def recurse(obj):
        if isinstance(obj, dict):
            if 'type' in obj:
                stats['total_messages'] += 1
                if obj['type'] == 'message' and 'full_text' in obj:
                    val = obj['full_text']
                    if isinstance(val, str) and val.strip():
                        texts.append(f'{{ "{val}" }}')
                        stats['text_messages'] += 1
                        stats['total_characters'] += len(val.strip())
                    else:
                        stats['empty_messages'] += 1
                elif obj['type'] == 'service':
                    stats['service_messages'] += 1

            for value in obj.values():
                recurse(value)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)

    recurse(data)
    return texts, stats

def main():
    start_time = time.time()
    input_file = "result.json"
    output_file = "output.txt"

    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        print("Processing completed")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)

        text_blocks, stats = extract_text_blocks(data)

        # Save extracted blocks
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(",\n".join(text_blocks))

        # Print statistics
        print("\nProcessing completed:")
        print(f"- Total messages: {stats['total_messages']}")
        print(f"- Text messages: {stats['text_messages']}")
        print(f"- Empty messages: {stats['empty_messages']}")
        print(f"- Service messages: {stats['service_messages']}")
        print(f"- Total characters in text messages: {stats['total_characters']}")
        print(f"- Output: '{output_file}'")

    except json.JSONDecodeError:
        print("Error: The JSON file is invalid or empty.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Processing completed")
        print(f"Time taken: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()