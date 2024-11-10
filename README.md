# Instant Language Translator

This project is a language translation tool designed for **real-time, instant translations** between various languages, using a graphical user interface (GUI) built with Python's Tkinter library. It enables users to select source and target languages, translate live or pre-recorded audio input, and view translations directly on the interface.

## Features

- **Real-time audio translation:** Capture live spoken input via a camera/microphone, detect the language, and translate it into a target language.
- **User-friendly GUI:** Select languages, view translations, and control translation settings easily.
- **Support for multiple languages:** Leverage extensive language support provided by the `googletrans` library.
- **Scalability:** The project is structured for easy addition of more translation features, such as text or image-based translation.

## Technology Stack

- **Python:** The primary programming language for backend processing and GUI design.
- **Tkinter:** For building a responsive and accessible GUI.
- **VolkSpeechRecognition:** To capture and process live spoken input.
- **googletrans:** For translation services, supporting various language pairs.
- **OpenCV:** For integrating live camera feeds (if needed for video-based translation).
  
## License

This project is licensed under the MIT License.

## Acknowledgments

- [Googletrans Library](https://py-googletrans.readthedocs.io/en/latest/) - Translation functionality.
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/) - For handling live audio input.

---
