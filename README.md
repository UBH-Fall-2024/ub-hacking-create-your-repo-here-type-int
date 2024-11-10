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
- **SpeechRecognition:** To capture and process live spoken input.
- **googletrans:** For translation services, supporting various language pairs.
- **OpenCV:** For integrating live camera feeds (if needed for video-based translation).
  
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/instant-language-translator.git
   cd instant-language-translator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. If you're on **macOS**, ensure compatibility by setting the environment variable:
   ```bash
   export TK_SILENCE_DEPRECATION=1
   ```

## Usage

1. Run the main script to start the application:
   ```bash
   python3 language_dropdown_GUI.py
   ```

2. On the GUI:
   - Select source and target languages using the dropdown menus.
   - Press **Translate** to process the live audio feed or uploaded audio file.
   - The translated text appears in the GUI interface.

## Code Structure

- `language_dropdown_GUI.py`: The main application script that initializes the GUI and manages the translation workflow.
- `face_detection_with_subtitles.py`: Script for managing subtitle display and integrating audio feeds (modify as needed for your system).
- `requirements.txt`: List of all dependencies needed to run the project.

## Contributing

1. Fork this repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add a feature description"
   git push origin feature-name
   ```
4. Submit a pull request to the main branch.

## Troubleshooting

- **macOS Issues with Tkinter**: If you encounter `Tcl_WaitForEvent` errors, ensure you’re running Python outside of Anaconda and use `pythonw` on macOS for GUI applications.
- **Translation Limitations**: The `googletrans` library has usage limits. For extensive use, consider upgrading to a paid API.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Googletrans Library](https://py-googletrans.readthedocs.io/en/latest/) - Translation functionality.
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/) - For handling live audio input.

---
