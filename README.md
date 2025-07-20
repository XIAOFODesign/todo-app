# Todo App

A simple Windows todo application built with Python and Tkinter.

## Features
- Add and remove tasks
- Save tasks to JSON file
- Load tasks from JSON file
- Clear all tasks

## Requirements
- Python 3.13+
- Tkinter (usually included with Python)
- PyInstaller (for packaging)

## How to Run
1. Clone this repository
2. Run `python main.py`

## How to Package
1. Install PyInstaller: `pip install pyinstaller`
2. Run `pyinstaller --onefile --windowed main.py`
3. Find the executable in the `dist` folder