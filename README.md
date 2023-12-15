# tosheets_script

A Python script designed to read data from a file and write it to a Google Sheets document. This script was specifically created to extract and organize results from tests conducted during my master's thesis.

## Overview

The script simplifies the process of transferring data from a text file (in this case, results from tests) to a Google Sheets document. It utilizes the `gspread` and `pandas` libraries for interacting with Google Sheets and managing data efficiently.

## How it Works

1. **Data Extraction**: The script reads test results from a text file (`log.txt`) and extracts relevant information.

2. **Data Organization**: The extracted data is organized into a pandas DataFrame, providing a structured representation.

3. **Google Sheets Integration**: The script connects to a Google Sheets document (`temposTese`) using OAuth credentials and writes the organized data to a specific worksheet (`Folha8`).

## Usage

1. Install the required dependencies:

   ```bash
   pip install gspread pandas gspread-formatting

2. Run the script:

   ```bash
   python tosheets_script.py
   
   ## Acknowledgments

- [gspread](https://github.com/burnash/gspread) - Google Sheets API for Python
- [pandas](https://pandas.pydata.org/) - Data manipulation and analysis library for Python
- [gspread-formatting](https://github.com/aiguofer/gspread-formatting) - Library for formatting cells in Google Sheets using gspread.

