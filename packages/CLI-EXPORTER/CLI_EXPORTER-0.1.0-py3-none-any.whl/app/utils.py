import pandas as pd
from docx import Document
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
import re
import os

def load_document(file_path):
    """
    Load a Word document from the specified file path.
    """
    return Document(file_path)

def extract_client_from_path(file_path, splice):
    """
    Extract the client name from the file path by finding the 'CLIENTS' directory and taking the next part.
    """
    # Normalize the file path to use consistent separators
    normalized_path = os.path.normpath(file_path)
    parts = normalized_path.split(os.sep)
    try:
        # Find the index of specified directory and get the next part
        for i, part in enumerate(parts):
            if part.upper() == splice and (i + 1) < len(parts):
                client_name = parts[i + 1]
                return client_name
        raise ValueError(splice + "not found in path or no subsequent part available")
    except (ValueError, IndexError) as e:
        print(f"Error extracting "+ splice + " name: {e}")  # Debugging output
        return None

def extract_data(doc):
    """
    Extract the Computer Name and Local Admin Username/Password from the tables in the Word document.
    Returns a tuple with the extracted data and any errors encountered.
    """
    computer_name = None
    local_admin_username = None
    local_admin_password = None
    errors = []
    delimiters = r"[ ]"

    for table in doc.tables:
        for row in table.rows:
            for i, cell in enumerate(row.cells):
                if "Computer Name" in cell.text:
                    try:
                        computer_name = row.cells[i + 1].text.strip()
                    except IndexError:
                        errors.append("Computer Name not found.")
                if "Notes/Comments" in cell.text:
                    try:
                        computer_name = row.cells[i + 1].text.strip()
                    except IndexError:
                        errors.append("No notes found.")
                if "Local Admin Username" in cell.text:
                    try:
                        complete_data = row.cells[i + 1].text.strip()
                        parts = complete_data.split()
                        if len(parts) >= 2:
                            local_admin_username = parts[0].strip()
                            local_admin_password = " ".join(parts[2:]).strip()
                        else:
                            local_admin_username = complete_data.strip()
                            local_admin_password = None

                        if local_admin_username.startswith(".\\"):
                            local_admin_username = local_admin_username[2:]

                        if local_admin_username.startswith("./"):
                            local_admin_username = local_admin_username[2:]
                        
                        if "/" in complete_data:
                            parts = complete_data.split("/", 1)
                        
                        # Validate the extracted username and password
                        if not local_admin_username:
                            errors.append("Invalid Local Admin Username format.")
                        if local_admin_password and not re.match(r'^[\w!@#$%^&*()_+=-]+$', local_admin_password):
                            errors.append("Invalid Local Admin Password format.")
                    except IndexError:
                        errors.append("Local Admin Username not found.")
                        
            if computer_name and local_admin_username:
                break
        if computer_name and local_admin_username:
            break
    
    return computer_name, local_admin_username, local_admin_password, errors, complete_data

def save_to_csv(data, file_path):
    """
    Save the aggregated data to a CSV file with the specified headers.
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

def get_file_paths():
    """
    Get the input file paths using file dialogs.
    """
    initial_dir = "O:\\CLIENTS\\"

    Tk().withdraw()  # Hide the main tkinter window

    input_docxs = askopenfilenames(title="Select the Word documents", filetypes=[("Word files", "*.docx")], initialdir=initial_dir)
    if not input_docxs:
        return None, None

    output_csv = asksaveasfilename(title="Save as", defaultextension=".csv", filetypes=[("CSV files", "*.csv")], initialdir=initial_dir)
    if not output_csv:
        return None, None

    return input_docxs, output_csv
