import vosk
import pyaudio
import json
import socket
import sys
from googletrans import Translator

selected_language = sys.argv[1]

# Vosk model and recognizer setup
model_path = selected_language
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)

# Google Translate setup
translator = Translator()

# Set up the socket server to send recognized text
host = 'localhost'
port = 65434

# Open audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=16384)  # Increased buffer size for better performance

# Track the last recognized final text
last_text = ""  # Variable to store the last recognized final text

# Set up socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    # Accept connection from client
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        print("Listening for speech. Say 'Terminate' to stop.")
        
        try:
            while True:
                try:
                    data = stream.read(4096, exception_on_overflow=False)
                    if rec.AcceptWaveform(data):
                        # Process the final result
                        result = json.loads(rec.Result())
                        recognized_text = result['text']

                        if recognized_text != last_text:  # Only send final text if it's different
                            # Translate the recognized text using Google Translate
                            try:
                                translated_text = translator.translate(recognized_text, src='auto', dest='en').text
                                if translated_text:  # Only send if translation is not None
                                    final_text = translated_text  # Get the translated text
                                    conn.sendall(final_text.encode('utf-8'))  # Send the final result
                                    print(f"Final: {final_text}")
                                    last_text = recognized_text  # Update last_text
                                else:
                                    print("Translation failed: Received empty response.")
                            except Exception as e:
                                print(f"Translation error: {e}")

                        # Check for "terminate" keyword after receiving final text
                        if "terminate" in recognized_text.lower():
                            print("\nTermination keyword detected. Stopping...")
                            break

                except OSError as e:
                    print(f"Input overflow: {e}")
                    continue  # Skip this iteration and try again

        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Stopping...")

# Clean up audio stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()
