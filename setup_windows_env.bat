@echo off
echo Setting up Windows conda environment for Information Dynamics...

REM Activate conda environment
call C:\ProgramData\miniconda3\Scripts\activate.bat info-dynamics

REM Install additional packages via pip
pip install factor_analyzer psychopy mne

REM Install jupyter kernel
python -m ipykernel install --user --name info-dynamics --display-name "Information Dynamics (Windows)"

REM List installed packages
echo.
echo === Installed packages ===
conda list

echo.
echo === Environment setup complete! ===
echo Now you can:
echo 1. Open Cursor
echo 2. Press Ctrl+Shift+P
echo 3. Search "Python: Select Interpreter"
echo 4. Select: C:\ProgramData\miniconda3\envs\info-dynamics\python.exe

pause 