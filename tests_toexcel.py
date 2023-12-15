import gspread
import pandas as pd
from gspread_formatting import *

# Authenticate with Google Sheets using credentials from 'credentials.json'
gc = gspread.oauth(credentials_filename='credentials.json')

# Open the Google Sheets workbook by name
sh = gc.open("temposTese")

# Read data from the text file
with open('log.txt', 'r') as file:
    data = file.read()

# Split the data into individual records based on the separator '--------------------------------------------------------------------------------------'
records = data.split('--------------------------------------------------------------------------------------')

# Initialize empty lists to store extracted information
file_sizes = []
msg_to_bc_bytes = []
search_bc_time = []
manifest_bytes = []
get_manifest_time = []
security_time = []
consumer_end2end_time = []

# Iterate over each record and extract information
for record in records:
    lines = record.strip().split('\n')

    for line in lines:
        if "Msg to BC bytes:" in line:
            msg_to_bc_bytes.append(int(line.split(":")[1].strip()))
        elif "SEARCH BC time:" in line:
            search_bc_time.append(int(line.split(":")[1].strip()))
        elif "MANIFEST BYTES:" in line:
            manifest_bytes.append(int(line.split(":")[1].strip()))
        elif "GET MANIFEST time:" in line:
            get_manifest_time.append(int(line.split(":")[1].strip()))
        elif "Security Time:" in line:
            security_time.append(int(line.split(":")[1].strip()))
        elif "consumer end2end time:" in line:
            consumer_end2end_time.append(int(line.split(":")[1].strip()))

# Create a DataFrame using the extracted information
df = pd.DataFrame({
    'Pesquisa BC': search_bc_time,
    'Get Manifest Time': get_manifest_time,
    'Security Time': security_time,
    'Consumer End2End Time': consumer_end2end_time,
    'Manifest (Bytes)': manifest_bytes,
    'Conversa Blockchain (bytes)': msg_to_bc_bytes
})

# Define cell formats
blue_format = cellFormat(
    backgroundColor=color(0, 3, 1),
    textFormat=textFormat(bold=True),
    horizontalAlignment='CENTER'
)

orange_format = cellFormat(
    backgroundColor=color(1, 0.7, 0),
    textFormat=textFormat(bold=True),
    horizontalAlignment='CENTER'
)

red_format = cellFormat(
    backgroundColor=color(1, 0, 0),
    textFormat=textFormat(bold=True),
    horizontalAlignment='CENTER'
)

# Apply cell formats to specific ranges
format_cell_range(sh.worksheet("Folha8"), 'A1:F1', blue_format)
format_cell_range(sh.worksheet("Folha8"), 'A2:F11', orange_format)
format_cell_range(sh.worksheet("Folha8"), 'A12:F12', red_format)

# Append the DataFrame to the worksheet
sh.worksheet("Folha8").append_table([df.columns.values.tolist()] + df.values.tolist())

# Write means in line A12:F12
mean_values = df.mean().tolist()
sh.worksheet("Folha8").update('A12', [mean_values])

