import os

def remove_spaces_from_filenames(folder_path):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Rename each file by removing leading and trailing spaces
    for filename in files:
        original_path = os.path.join(folder_path, filename)
        new_filename = filename.strip()
        new_path = os.path.join(folder_path, new_filename)

        if filename != new_filename:
            os.rename(original_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

    print("Space removal completed.")

# Specify the folder path here
folder_path = "/home/scelester/ProjectD/fetcher/STORAGE/Against the gods/Chapter_upto/"

# Call the function to remove spaces from filenames in the folder
remove_spaces_from_filenames(folder_path)
