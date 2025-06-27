import os

def write_file(working_directory, file_path, content):
    # Resolve absolute path for working_directory
    working_directory = os.path.abspath(working_directory)
    
    # Check if file_path is absolute; if not, join with working_directory
    if not os.path.isabs(file_path):
        file_path = os.path.join(working_directory, file_path)
    
    # Resolve absolute path for file_path
    file_path = os.path.abspath(file_path)
    
    # Check if file_path is within working_directory using commonpath
    try:
        common_path = os.path.commonpath([working_directory, file_path])
        if common_path != working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except ValueError:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Create parent directories if they don't exist
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    except Exception as e:
        return f'Error: Failed to create directories for "{file_path}": {str(e)}'
    
    # Write (or overwrite) the file
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{file_path}": {str(e)}'