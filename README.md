<h1 align="center">🎥 YouTube Video & Audio Downloader</h1>

<p align="center">
  <b>A Clean, Fast & Feature-Rich Python GUI Tool for Downloading YouTube Videos & Audio with Style</b><br>
  🖥️ Built with Tkinter • 🎵 MP3 & HD Video Downloads • 🌗 Light/Dark Mode • 🧲 Drag & Drop • 📊 Progress Tracking
</p>

---

## 📌 Table of Contents

- [🚀 Overview](#-overview)
- [✨ Features](#-features)
- [🎯 Use Cases](#-use-cases)
- [🧠 Why This Project?](#-why-this-project)
- [🛠️ How It Works](#️-how-it-works)
- [🧩 Architecture](#-architecture)
- [⚙️ Installation](#️-installation)
- [📥 Usage Guide](#-usage-guide)
- [🖼️ UI Highlights](#️-ui-highlights)
- [💡 Planned Features](#-planned-features)
- [🧪 Testing](#-testing)
- [🔐 Security](#-security)
- [🧰 Tech Stack](#-tech-stack)
- [📦 Executable Packaging](#-executable-packaging)
- [👨‍💻 Contributing](#-contributing)
- [📜 License](#-license)
- [🌐 Connect With Me](#-connect-with-me)

---

## 🚀 Overview

**YouTube Video & Audio Downloader** is a sleek, beginner-friendly Python desktop app that lets users download videos from YouTube in various resolutions or extract clean MP3 audio. The app comes with a polished Tkinter GUI, real-time progress, and customizable themes.

---

## ✨ Features

✅ Download YouTube videos in **multiple resolutions** (360p, 720p, 1080p)  
✅ Extract **MP3 audio** with FFmpeg  
✅ Toggle between **Light & Dark mode**  
✅ View video metadata before download (title, length, thumbnail)  
✅ Monitor **real-time download progress**  
✅ Simple **drag-and-drop** YouTube link input  
✅ Cross-platform (Windows, macOS, Linux)

---

## 🎯 Use Cases

- 📚 Download lecture videos for offline study  
- 🎵 Extract audio from music videos for playlists  
- ✈️ Save videos for offline travel viewing  
- 🧘 Collect meditation/audiobooks in MP3  
- 📂 Back up useful YouTube content locally

---

## 🧠 Why This Project?

I built this as a **personal productivity tool** to simplify downloading content from YouTube without visiting spammy online websites or writing CLI commands. The goal: an elegant and secure app anyone can use — from beginners to developers.

---

## 🛠️ How It Works

```mermaid
graph TD
    A[User Enters URL] --> B{Validate Link}
    B -->|Valid| C[Fetch Video Info via yt-dlp]
    C --> D[Display Title, Resolutions]
    D --> E{User Choice}
    E -->|Video| F[Download in Chosen Resolution]
    E -->|Audio| G[Convert to MP3 via FFmpeg]
    F & G --> H[Show Progress]
    H --> I[Save File Locally]
