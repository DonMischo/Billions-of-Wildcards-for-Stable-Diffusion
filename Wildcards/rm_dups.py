def remove_duplicates_and_sort(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    unique_phrases = list(set(lines))
    sorted_phrases = sorted(unique_phrases, key=str.lower)  # Case-insensitive sorting

    with open(output_file, 'w') as file:
        file.writelines(sorted_phrases)

# Example usage
input_file_path = 'realm.txt'  # Replace with your input file path
output_file_path = 'output_realm.txt'  # Replace with your output file path

remove_duplicates_and_sort(input_file_path, output_file_path)
