import os

# # Specify the directory path where the files are located
# directory_path = 'Nine Start Hegemon Body Arts p5'

# # Iterate through all files in the directory
# for filename in os.listdir('Nine Start Hegemon Body Arts p5'):
#     if filename.startswith('hapter'):
#         # Construct the full paths for the old and new file names
#         old_file_path = os.path.join(directory_path, filename)
#         new_file_path = os.path.join(directory_path, filename.replace('hapter', 'chapter', 1))
        
#         # Rename the file
#         os.rename(old_file_path, new_file_path)
#         print(f"Renamed '{old_file_path}' to '{new_file_path}'")



# Define the input and output file names
input_file = "chapterLinks NSHB New .txt"
output_file = "chapterLinks NSHB New x.txt"

# Read the lines from the input file and reverse them
with open(input_file, "r") as infile:
    lines = infile.readlines()
    reversed_lines = lines[::-1]  # Reverse the order of lines

# Write the reversed lines to the output file
with open(output_file, "w") as outfile:
    outfile.writelines(reversed_lines)

print(f"Reversed file created: {output_file}")