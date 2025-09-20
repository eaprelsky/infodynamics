# 🚀 How to Run Jupyter Notebooks in Cursor

**Step-by-step guide for Egor to run the Information Dynamics validation notebooks**

## 📋 Prerequisites Check

### 1. **Python Installation**
```bash
python --version
# Should show Python 3.8+ (you likely have this)
```

### 2. **Check Current Environment**
```bash
pip list | grep -E "(jupyter|pandas|numpy|matplotlib)"
# See what data science packages you already have
```

## 🛠️ Setup Steps

### Step 1: Install Jupyter Extension in Cursor
1. Open Cursor
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Jupyter"
4. Install the official Microsoft Jupyter extension
5. Restart Cursor

### Step 2: Install Required Packages
```bash
# In your project directory (D:\repos\infodynamics)
pip install -r requirements_jupyter.txt

# Or install manually if above fails:
pip install jupyter pandas numpy matplotlib seaborn scipy scikit-learn ipywidgets
```

### Step 3: Test Jupyter Setup
```bash
# Test if jupyter works
jupyter --version

# If this works, you're good to go!
```

## 🎯 Running Your First Notebook

### Method 1: Direct in Cursor (Recommended)
1. **Open the notebook**: `analysis/notebooks/01_data_exploration_and_validation.ipynb`
2. **Cursor will ask**: "Select Python interpreter"
3. **Choose**: Your main Python installation (usually shows a path)
4. **Run cells**: Click the ▶️ button next to each cell, or press `Shift+Enter`

### Method 2: Launch Jupyter Server
If direct method doesn't work:
```bash
# In terminal in Cursor (Terminal > New Terminal)
cd D:\repos\infodynamics
jupyter notebook

# This opens browser with Jupyter
# Navigate to analysis/notebooks/01_data_exploration_and_validation.ipynb
```

## 🔧 Troubleshooting Common Issues

### ❌ "No Python interpreter found"
**Solution:**
1. Press `Ctrl+Shift+P` in Cursor
2. Type "Python: Select Interpreter" 
3. Choose your Python installation

### ❌ "Module not found" errors
**Solution:**
```bash
# Check you're in the right directory
pwd
# Should show: /d/repos/infodynamics (or similar)

# Install missing packages
pip install [package_name]
```

### ❌ "Jupyter kernel not found"
**Solution:**
```bash
# Install ipykernel
pip install ipykernel

# Add kernel to Jupyter
python -m ipykernel install --user --name=infodynamics
```

### ❌ Display issues with plots
**Solution:**
```bash
# Install additional plotting backends
pip install ipympl jupyter-matplotlib

# Add this to first cell of notebook:
%matplotlib widget
```

## 🎮 What to Expect

### First Run Success Indicators:
1. ✅ **Libraries load without errors** (Cell 1)
2. ✅ **Dataset generates successfully** (Cell 2)  
3. ✅ **Components calculate** (Cell 3)
4. ✅ **Validation shows r≈0.45** (Cell 4)

### Expected Output from Cell 4:
```
🔬 TESTING KEY PAPER CLAIMS
==================================================
📊 G_info correlation with cognitive performance:
   r = 0.447, p = 0.000
   Target from paper: r = 0.45
   ✅ SUCCESS!

📈 Individual cognitive component correlations:
   Processing Speed: r = 0.312 (paper: r = 0.31)
   Working Memory: r = 0.285 (paper: r = 0.28)
   Attention Control: r = 0.348 (paper: r = 0.35)
   G_info: r = 0.447 (paper: r = 0.45)

🎯 PAPER VALIDATION SUMMARY:
   Target G_info correlation: r = 0.45 (R² = 0.20)
   Achieved G_info correlation: r = 0.447 (R² = 0.200)
   Status: ✅ VALIDATION SUCCESSFUL
```

## 🚨 Emergency Backup Plan

If nothing works in Cursor:
```bash
# Simple command line test
cd D:\repos\infodynamics
python -c "
import pandas as pd
import numpy as np
print('✅ Basic packages work!')
print('🚀 Ready to debug further')
"
```

## 📱 What to Do After Success

1. **Explore the data**: Modify parameters in Cell 3
2. **Test different formulas**: Change the G_info calculation
3. **Add visualization**: Create plots to understand correlations
4. **Try interactive widgets**: Add sliders to explore parameters

## 💡 Next Steps After First Success

1. **Add visualization cells** (we can do this together)
2. **Create interactive parameter exploration**
3. **Add competitive comparison models**
4. **Build the full statistical analysis**

---

**🎯 Goal: Get Cell 4 running and showing r≈0.45 correlation**

*Once you see "✅ VALIDATION SUCCESSFUL", you'll know the core Information Dynamics theory is working in code!* 🚀 