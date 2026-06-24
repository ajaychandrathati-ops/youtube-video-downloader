from pytube import YouTube
import customtkinter as ctk
from tkinter import messagebox

# App Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Download Function
def download_video():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        status_label.configure(text="Fetching video...", text_color="yellow")
        app.update()

        yt = YouTube(url)

        title_label.configure(text=f"Title: {yt.title}")

        stream = yt.streams.get_highest_resolution()

        status_label.configure(text="Downloading...", text_color="orange")
        app.update()

        stream.download()

        status_label.configure(
            text="Download Completed Successfully!",
            text_color="green"
        )

    except Exception as e:
        status_label.configure(
            text=f"Error: {str(e)}",
            text_color="red"
        )

# Main Window
app = ctk.CTk()
app.title("YouTube Video Downloader")
app.geometry("600x400")

# Heading
heading = ctk.CTkLabel(
    app,
    text="YouTube Video Downloader",
    font=("Arial", 24, "bold")
)
heading.pack(pady=20)

# URL Entry
url_entry = ctk.CTkEntry(
    app,
    width=450,
    placeholder_text="Paste YouTube Video URL Here"
)
url_entry.pack(pady=10)

# Download Button
download_btn = ctk.CTkButton(
    app,
    text="Download Video",
    command=download_video,
    width=200
)
download_btn.pack(pady=20)

# Video Title
title_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 14)
)
title_label.pack(pady=10)

# Status Label
status_label = ctk.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 14)
)
status_label.pack(pady=10)

# Run App
app.mainloop()