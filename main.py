import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import os
import time

# Load emotion classification model
model = load_model('face_model.h5')

# Register Microsoft Edge browser
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# Map emotions to Spotify playlist URIs (must be spotify:playlist:...)
emotion_playlists = {
   'Angry': 'https://open.spotify.com/playlist/7xNZil1utJmLE6bao8zy5V',  # Rock Playlist
    'Surprised': 'https://open.spotify.com/playlist/6jvSj3ZslXHAfgKqziNEbQ',  # Pop Playlist
    'Neutral': 'https://open.spotify.com/playlist/7EClwmhqu7mg4JvUI9z5DT',  # Classical Playlist
    'Sad': 'https://open.spotify.com/playlist/2sOMIgioNPngXojcOuR4tn',  # Blues Playlist
    'Happy': 'https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD'      # Electronic
}

# Setup Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="1d923e7cc667477ab3f4ce15887358a6",
    client_secret="236d37e428904b8c9fb584081c10e70d",
    redirect_uri="http://127.0.0.1:8888/callback",  # make sure this is allowed in your Spotify dev app
    scope="user-read-playback-state,user-modify-playback-state"
))

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
current_emotion = None

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi_gray = roi_gray / 255.0
        roi_gray = np.expand_dims(roi_gray, axis=0)
        roi_gray = np.expand_dims(roi_gray, axis=-1)

        predictions = model.predict(roi_gray)
        max_index = int(np.argmax(predictions[0]))
        emotions = list(emotion_playlists.keys())
        emotion = emotions[max_index]

        # Show prediction
        cv2.putText(frame, emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h),
                      (255, 0, 0), 2)

        # Only act if emotion has changed
        if emotion != current_emotion:
            playlist_uri = emotion_playlists[emotion]
            try:
                print(f"Detected Emotion: {emotion} -> Playing {playlist_uri}")
                sp.start_playback(context_uri=playlist_uri)
                current_emotion = emotion

                # Open browser to Spotify Web Player (optional)
                webbrowser.get('edge').open("https://open.spotify.com")
            except Exception as e:
                print(f"Error starting playback: {e}")

    cv2.imshow('Mood Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
