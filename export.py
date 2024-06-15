import os

# Define the directories to walk through and the output directory
input_directory = '.'
output_directory = './output'

# Walk through all directories
for root, dirs, files in os.walk(input_directory):
    md_file = [file for file in files if file.endswith('.md')]
    py_file = [file for file in files if file.endswith('.py')]
    
    # Make sure there is exactly one .md and .py file in the directory
    if len(md_file) == 1 and len(py_file) == 1:
        md_file = md_file[0]
        py_file = py_file[0]

        # Open the .md file and read its contents
        with open(os.path.join(root, md_file), 'r') as file:
            md_contents = file.read()
        
        # Open the .py file and read its contents
        with open(os.path.join(root, py_file), 'r') as file:
            py_contents = file.read()
        
        # Create a new markdown section called ## Code
        new_contents = md_contents + '\n\n## Code\n\n```python\n' + py_contents + '\n```\n'
        
        # Define the name and location of the output file
        output_file = os.path.join(output_directory, root) + ".md"

        print(output_file)
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)
        
        # Write the new contents to the output file
        with open(output_file, 'w') as file:
            file.write(new_contents)
