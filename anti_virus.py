import requests
import json
import os
import tkinter as tk
from customtkinter import *

API_KEY = "4bdf5f7ee65b605d9ed28f673a0e83b1d25490566ebb493725c1065430ab4ed9"
url_scan = "https://www.virustotal.com/vtapi/v2/file/scan"

def print_dict_values(d):
    total_votes = d['data']['attributes']['total_votes']
    analysis_stats = d['data']['attributes']['last_analysis_stats']
    suspicious_count = analysis_stats['suspicious']
    if total_votes["malicious"] > 0:
        return "There is a virus for 100%"
    elif suspicious_count > 0:
        return "There is a virus not for 100%"
    return "There isn't a virus"

def post_request(file_path):
    with open(file_path, 'rb') as file:
        params = {'apikey': API_KEY}
        files = {'file': file}
        posted = requests.post(url_scan, files=files, params=params)
        info_posted = posted.json()
    if info_posted["response_code"] == 1:
        return info_posted["resource"]
    else:
        return None

def get_request(resource):
    url_report = f"https://www.virustotal.com/api/v3/files/{resource}"
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }
    response = requests.get(url_report, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        return "API limit reached. Please get a new API key."
    else:
        return f"Error: {response.status_code}"

def is_virus(file_path):
    if os.path.isfile(file_path):
        resource = post_request(file_path)
        if resource:
            response = get_request(resource)
            if isinstance(response, dict):
                result = print_dict_values(response)
                return result
            else:
                return response
        else:
            return "Failed to post request"
    else:
        return f"{file_path} is not a file."

def scan_directory(folder_path):
    results = []
    files = os.listdir(folder_path)
    for file in files:
        full_item_path = os.path.join(folder_path, file)
        if os.path.isfile(full_item_path):
            result = is_virus(full_item_path)
            results.append(f"File: {full_item_path}\nResult: {result}\n")
        elif os.path.isdir(full_item_path):
            subdir_results = scan_directory(full_item_path)
            results.extend(subdir_results)
    return results

def get_text():
    global path
    path = text_box.get("1.0", tk.END).strip()
    results = scan_directory(path)
    result_text.set("\n".join(results))

def enable_paste(event=None):
    try:
        text_box.event_generate('<<Paste>>')
    except tk.TclError:
        pass

win = CTk()

width_win = 700
height_win = 600

win.title("Antivirus Scanner")
win.geometry(f"{width_win}x{height_win}")

title_label = CTkLabel(
    master=win,
    text="Welcome to Antivirus Scanner",
    font=("Helvetica", 24, "bold"),
    text_color="black"
)

title_label.pack(side=tk.TOP, pady=20)

text_box = CTkTextbox(
    master=win,
    scrollbar_button_color="#000",
    corner_radius=16,
    border_color="#FFCC30",
    height=100,
    width=500
)

instruction_label = CTkLabel(
    master=win,
    text="Enter the path you want to check for viruses:",
    font=("Helvetica", 16),
    text_color="black"
)

instruction_label.pack(side=tk.TOP, pady=(20, 10))
text_box.pack(side=tk.TOP, pady=(0, 20))

button = CTkButton(
    master=win,
    text="Submit",
    command=get_text,
    width=200,
    height=40,
    corner_radius=20,
    font=("Helvetica", 16)
)

button.pack(side=tk.TOP, pady=(0, 20))

result_text = tk.StringVar()
result_label = CTkLabel(
    master=win,
    textvariable=result_text,
    font=("Helvetica", 14),
    text_color="black",
    wraplength=600,
    justify=tk.LEFT
)

result_label.pack(side=tk.TOP, pady=(10, 20))

# Enable paste shortcut (Ctrl+V)
text_box.bind("<Control-v>", enable_paste)

win.mainloop()