import sys
import os
current_file_path = os.path.abspath(__file__)

# Get the directory containing the currently executed Python file
current_directory = os.path.dirname(current_file_path)

sys.path.append(current_directory)

from claid_designer.claid_designer import CLAIDDesigner