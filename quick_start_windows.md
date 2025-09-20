# Quick Start - Windows Setup

## ✅ Environment Ready!

**Conda environment**: `info-dynamics`
**Python path**: `C:\ProgramData\miniconda3\envs\info-dynamics\python.exe`
**Jupyter kernel**: "Information Dynamics"

## 🚀 How to Use:

### 1. Configure Cursor:
```
Ctrl+Shift+P → "Python: Select Interpreter"
Choose: C:\ProgramData\miniconda3\envs\info-dynamics\python.exe
```

### 2. Open Notebook:
```
File: analysis/notebooks/01_data_exploration_and_validation.ipynb
Kernel: "Information Dynamics"
```

### 3. Activate Environment (if needed):
```cmd
call C:\ProgramData\miniconda3\Scripts\activate.bat info-dynamics
```

### 4. Install Additional Packages:
```cmd
call C:\ProgramData\miniconda3\Scripts\activate.bat info-dynamics
pip install PACKAGE_NAME
```

## 📦 Installed Packages:
- ✅ pandas, numpy, scipy, matplotlib, seaborn
- ✅ scikit-learn 
- ✅ factor_analyzer
- ✅ jupyter, ipykernel

## 🔧 Troubleshooting:
- If kernel not visible → restart Cursor
- If import errors → run `install_packages.bat`
- If path issues → check Python interpreter setting 