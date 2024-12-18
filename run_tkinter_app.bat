@echo off
echo Starting Text Rewriter (Tkinter Version)...

:: Check if venv exists, if not create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

:: Install requirements if they haven't been installed
echo Checking/Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

:: Run the Tkinter app
echo Starting Tkinter application...
python src/tkinter_app.py

:: Keep the window open if there's an error
if errorlevel 1 (
    echo Error: Failed to start Tkinter application
    pause
    exit /b 1
)

:: Deactivate virtual environment
deactivate
