# 🎵 AI-Based Mood Filter 🎭

## Overview

**AI-Based Mood Filter** is a smart, interactive web application that detects your mood using your facial expressions or text input and instantly redirects you to a Spotify playlist that matches your emotion. Whether you're feeling 😠 *angry*, 😄 *happy*, 😢 *sad*, 😲 *surprised*, or 😕 *confused* — we've got a curated playlist ready for you!

## 🔥 Features

- 🎯 **Accurate Mood Detection** using AI (Facial Expression or Text Sentiment)
- 🎧 **Spotify Integration** — Get redirected to mood-specific playlists
- 💬 **Multiple Input Modes** — Use webcam or text box
- 🌐 **Web-based UI** — Simple, clean, and responsive interface
- 🧠 **Emotion Categories Supported**:
  - 😄 Happy
  - 😢 Sad
  - 😠 Angry
  - 😲 Surprise
  - 😕 Confused

## 🧰 Tech Stack

| Layer         | Tech Used                                      |
|---------------|------------------------------------------------|
| Backend       | Flask   |
| AI/ML Model   | TensorFlow / MediaPipe / OpenCV / Transformers |
| Mood Analysis | Facial Emotion Recognition / Text Sentiment    |
| APIs          | Spotify Web API                                |

## 🚀 How It Works

1. User provides input — either a selfie through webcam or a text message.
2. The AI model analyzes the mood from facial expressions or text sentiment.
3. Based on the detected emotion, the app maps it to a pre-defined Spotify playlist.
4. User is redirected to that playlist on Spotify.

## 🧪 Example Mood-Playlist Mapping

| Mood     | Playlist Link Example                                           |
|----------|-----------------------------------------------------------------|
| Happy    | [Happy Vibes](https://open.spotify.com/playlist/37) |
| Sad      | [Sad Songs](https://open.spotify.com/playlist/37i9dQZF)   |
| Angry    | [Anger Outlet](https://open.spotify.com/playlist/37i9dQZT7v)|
| Surprise | [Unexpected Hits](https://open.spotify.com/playlist/37iP7PZgoRCr1)|
| Confused | [Lo-Fi Beats](https://open.spotify.com/playlist/37i9duJkbcy) |

*(Note: You can update these playlist links with your own curated ones)*

## 🛠️ Installation

1. Clone the repository:
   
   git clone https://github.com/shreyanshrao/mood-filter.git
   cd mood-filter
