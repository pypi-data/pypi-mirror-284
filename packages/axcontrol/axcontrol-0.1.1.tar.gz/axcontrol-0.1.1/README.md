# axcontrol - aubex control

This project is a Windows UI automation tool that provides users some helpers and tools and allows to generate Python code for UI interactions by simply clicking on elements in any application. It uses UI Automation to detect controls, highlights them in real-time, and generates corresponding Python code for interacting with these controls.

## Features

- Real-time control detection and highlighting
- Code generation for UI interactions
- Modular architecture for easy extension and maintenance

## Requirements

- Python 3.10+
- tkinter
- pyperclip
- uiautomation
- pynput

## Installation

`pip install axcontrol` 

## Project Structure

- `main.py`: The entry point of the application
- `gui.py`: GUI-related code
- `listeners/input.py`: Mouse and keyboard event handling
- `control_finder.py`: Control finding and highlighting logic
- `code_generator.py`: Code generation and file writing
- `clipboard_utils.py`: Clipboard-related functions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the APACHE2 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of the `uiautomation`, the other dependencies and of course the `Python community` for making `axcontrol` possible.