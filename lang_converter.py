import os
import json

def convert_lang_files():

    input_folder = 'input'
    output_folder = 'output'

    # Create the output folder if it doesn't exist.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created '{output_folder}' directory.")

    # Verify the input folder exists.
    if not os.path.exists(input_folder):
        print(f"Error: The '{input_folder}' directory was not found. Please create it and add your .lang files.")
        return

    print(f"Searching for .lang files in '{input_folder}'...")

    # Iterate over files in the input directory.
    for filename in os.listdir(input_folder):
        if filename.endswith(".lang"):
            input_file_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.json'
            output_file_path = os.path.join(output_folder, output_filename)

            translations = {}
            try:
                # Use 'utf-8-sig' to automatically handle the BOM character.
                with open(input_file_path, 'r', encoding='utf-8-sig') as f:
                    for line in f:
                        # Remove leading/trailing whitespace.
                        line = line.strip()
                        # Ignore comments and empty lines.
                        if line and not line.startswith('#'):
                            # Split each line at the first equals sign.
                            if '=' in line:
                                key, value = line.split('=', 1)
                                translations[key.strip()] = value.strip()

                # Write the dictionary to a JSON file.
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    json.dump(translations, f, ensure_ascii=False, indent=4)

                print(f"Successfully converted '{filename}' to '{output_filename}'")

            except Exception as e:
                print(f"An error occurred while processing {filename}: {e}")

if __name__ == "__main__":
    convert_lang_files()