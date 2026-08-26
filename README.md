# Automation Tool 70

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

`automation-tool-70` is a high-performance, lightweight Python autoclicker designed for repetitive desktop workflows and gaming. It utilizes low-level system hooks to ensure precise click intervals and minimal CPU overhead.

## Features

*   **Configurable Click Rates:** Supports adjustable CPS (Clicks Per Second) ranging from 1 to 100+ with randomized delay emulation to bypass basic detection.
*   **Multi-Button Support:** Map automation triggers to Left, Right, or Middle mouse buttons independently.
*   **Global Hotkeys:** Start, pause, or terminate click sequences instantly using customizable global keyboard shortcuts (default: `F6` to toggle).
*   **Pattern Recording:** Record and replay custom mouse movement and clicking sequences for complex, multi-step tasks.

## Installation

Ensure you have Python 3.8 or higher installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-70.git
cd automation-tool-70
pip install -r requirements.txt
```

*Note: Linux users may need to install `python3-tk` and `python3-dev` prior to installing the dependencies for GUI and mouse hook support.*

## Usage

Run the main application script from your terminal:

```bash
python main.py
```

### Basic Command Line Usage

You can also run the core engine directly with custom arguments without launching the GUI:

```bash
python main.py --cps 15 --button left --hotkey F9
```

1. Launch the application.
2. Set your desired clicks per second in the configuration panel.
3. Hover your mouse over the target area.
4. Press `F6` to initiate the clicker, and press `F6` again to stop.

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes or bug fixes before submitting a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).