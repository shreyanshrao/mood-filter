import cv2
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import time

# Configure Edge browser path (update if needed)
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# Map detected emotions (from DeepFace) to Spotify playlist URIs
emotion_playlists = {
    'angry':    'spotify:playlist:7xNZil1utJmLE6bao8zy5V',   # Rock playlist
    'surprise': 'spotify:playlist:6jvSj3ZslXHAfgKqziNEbQ',   # Pop playlist
    'neutral':  'spotify:playlist:7EClwmhqu7mg4JvUI9z5DT',   # Classical playlist
    'sad':      'spotify:playlist:2sOMIgioNPngXojcOuR4tn',   # Blues playlist
    'happy':    'spotify:playlist:37i9dQZF1DWTwbZHrJRIgD'    # Electronic playlist
}

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR CLIENT ID HERE",  # Replace with your Spotify client ID
    client_secret="YOUR CLIENT SECRET HERE",  # Replace with your Spotify client secret
    redirect_uri="http://localhost:8888/callback",  # Make sure this matches your Spotify app settings
    scope="user-read-playback-state,user-modify-playback-state"
))

cap = cv2.VideoCapture(0)
current_emotion = None

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera frame not available")
            break

        try:
            # Analyze the frame for emotions
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            if results and len(results) > 0:
                dominant_emotion = results[0]['dominant_emotion']

                # Display detected emotion on screen
                cv2.putText(frame, dominant_emotion, (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Check if the emotion changed and play respective playlist
                if dominant_emotion != current_emotion and dominant_emotion.lower() in emotion_playlists:
                    playlist_uri = emotion_playlists[dominant_emotion.lower()]
                    try:
                        sp.start_playback(context_uri=playlist_uri)
                        print(f"Playing Spotify playlist for emotion: {dominant_emotion}")
                        current_emotion = dominant_emotion

                        # Prevent flickering or rapid switching of playlists
                        time.sleep(2)
                    except Exception as e:
                        print(f"Spotify playback error: {e}")

        except Exception as e:
            print(f"DeepFace error: {e}")

        cv2.imshow("Real-Time Emotion Detection & Spotify Player", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

# Optionally open a page in Edge after exit
webbrowser.get('edge').open("http://localhost:5000")
