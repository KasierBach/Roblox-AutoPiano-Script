
import re
import os

def get_sheet_music():
    input_file = "sheetConversion.txt"
    if os.path.exists(input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                print(f"Reading sheet music from {input_file}...")
                return content
    
    print(f"Error: {input_file} not found or empty.")
    print(f"Please paste your sheet music into {input_file} and run this script again.")
    return None

def get_float_input(prompt, default_val):
    try:
        val = input(f"{prompt} (default {default_val}): ").strip()
        if not val:
            return default_val
        return float(val)
    except ValueError:
        print(f"Invalid input. Using default {default_val}")
        return default_val

def main():
    text = get_sheet_music()
    if not text:
        return

    tempo = get_float_input("Enter Tempo", 60.0)
    speed = get_float_input("Enter Playback Speed", 0.75)

    # Tokenize: Match [notes] OR single char OR dash OR pipe
    tokens = re.findall(r'\[[^\]]+\]|[^ \n\[\]]', text)

    output = [f"playback_speed={speed}", f"tempo={tempo}"]
    time = 0.0
    duration = 0.25

    for token in tokens:
        if token == '-' or token == '|':
            time += duration
        else:
            # It's a note or chord
            cleantoken = token.replace("[", "").replace("]", "")
            output.append(f"{time:.2f} {cleantoken}")
            time += duration

    with open("song.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    print(f"Successfully converted to song.txt (Tempo: {tempo}, Speed: {speed})")

if __name__ == "__main__":
    main()
