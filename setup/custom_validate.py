import os
import re
import sys
import shutil
import argparse
import setup_common

# Get the absolute path of the current file's directory (Kohua_SS project directory)
project_directory = os.path.dirname(os.path.abspath(__file__))

# Check if the "setup" directory is present in the project_directory
if "setup" in project_directory:
    # If the "setup" directory is present, move one level up to the parent directory
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project directory to the beginning of the Python search path
sys.path.insert(0, project_directory)
