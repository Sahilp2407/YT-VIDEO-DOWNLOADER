import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pytube import YouTube
from threading import Thread
import logging
import os
import subprocess
import time
from urllib.error import HTTPError
from apify_client import ApifyClient # type: ignore

# Configure logging
logging.basicConfig(filename="app.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Apify Client
APIFY_API_TOKEN = "apify_api_uw70MRYQ2eJkjcCwGkyyNOyltOGFrS0viPoA"
# Ensure to verify the actor ID used below on the Apify platform
apify_client = ApifyClient(APIFY_API_TOKEN) 

# Create main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("600x500")

# Function to select download folder
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# Function to download video/audio
def download():
    url = url_entry.get()
    folder = folder_path.get()
    resolution = res_var.get()
    audio_only = audio_var.get()
    use_apify = apify_var.get()

    if not url or not folder:
        status_label.config(text="⚠️ Please enter a URL and select a folder!", fg="red")
        return

    def start_download():
        if use_apify:
            try:
                run_input = {
                    "startUrls": [{ "url": url }],
                    "mime": "video" if not audio_only else "audio",
                    "quality": "medium",
                    "proxy": { "useApifyProxy": True },
                    "maxRequestRetries": 3,
                }
                run = apify_client.actor("xOrNjsraTKK5C7SmE").call(run_input=run_input)
                for item in apify_client.dataset(run["defaultDatasetId"]).iterate_items():
                    print(item)
                status_label.config(text=f"✅ Download via Apify Complete!", fg="green")
                messagebox.showinfo("Success", "Download via Apify Completed Successfully!")
            except Exception as e:
                logging.error("Error occurred during Apify download", exc_info=True)
                status_label.config(text=f"⚠️ Error: {e}", fg="red")
                messagebox.showerror("Error", f"Download Failed! \n{e}")
        else:
            try:
                yt = YouTube(url)
                if audio_only:
                    stream = yt.streams.filter(only_audio=True).first()
                    file_type = "Audio"
                else:
                    stream = yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
                    file_type = "Video"
                if stream:
                    stream.download(folder)
                    status_label.config(text=f"✅ {file_type} Download Complete!", fg="green")
                    messagebox.showinfo("Success", f"{file_type} Downloaded Successfully!")
            except Exception as e:
                logging.error("Error occurred during Pytube download", exc_info=True)
                status_label.config(text=f"⚠️ Error: {e}", fg="red")
                messagebox.showerror("Error", f"Download Failed! \n{e}")
    
    download_thread = Thread(target=start_download)
    download_thread.start()

# Label & Entry for URL
tk.Label(root, text="YouTube Video URL:").grid(row=0, column=0)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2)

# Select Folder
tk.Label(root, text="Download Folder:").grid(row=1, column=0)
folder_path = tk.StringVar()
folder_entry = tk.Entry(root, textvariable=folder_path, width=40, state="readonly")
folder_entry.grid(row=1, column=1)
browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.grid(row=1, column=2)

# Dropdown for Resolution
tk.Label(root, text="Select Resolution:").grid(row=2, column=0)
res_options = ["1080p", "720p", "480p", "360p"]
res_var = tk.StringVar(value=res_options[1])
res_dropdown = ttk.Combobox(root, textvariable=res_var, values=res_options, state="readonly")
res_dropdown.grid(row=2, column=1)

# Checkbox for Audio Only
audio_var = tk.BooleanVar()
audio_check = tk.Checkbutton(root, text="Download Audio Only", variable=audio_var)
audio_check.grid(row=3, column=1)

# Checkbox for Apify option
apify_var = tk.BooleanVar()
apify_check = tk.Checkbutton(root, text="Use Apify for Download", variable=apify_var)
apify_check.grid(row=4, column=1)

# Download Button
download_button = tk.Button(root, text="Download", command=download)
download_button.grid(row=5, column=1)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=6, column=1)

root.mainloop()
