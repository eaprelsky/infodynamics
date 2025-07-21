# 🚀 Quick Start Guide

*Get the Information Dynamics project running in 5 minutes*

---

## ⚡ Setup (First Time)

```bash
# 1. Clone the repository
git clone <repository-url>
cd infodynamics

# 2. Install dependencies
pip install -r requirements.txt
# OR
conda env create -f environment.yml

# 3. Download validation datasets
python setup_data.py --stanford

# 4. Verify setup
python setup_data.py --check
```

## 🧪 Run Validation

```bash
# Run core validation experiments
python analysis/validation/stanford_real_validation.py

# Explore dataset structure  
python tools/data_utils/explore_stanford_structure.py

# View results
cat analysis/validation/STANFORD_VALIDATION_REPORT.md
```

## 📊 Data Management

**The repository uses "data-on-demand" approach:**
- ✅ Code and documentation are in git
- ✅ Small configuration files are tracked  
- ❌ Large datasets (2GB+) are downloaded separately
- ❌ Generated results are excluded from git

**Available commands:**
```bash
python setup_data.py --info      # Show dataset information
python setup_data.py --stanford  # Download Stanford dataset only  
python setup_data.py --check     # Verify data integrity
```

## 🎯 Key Validation Results

Current validation shows Information Dynamics models successfully predict:
- **G_info ↔ Working Memory**: r=0.64, p<0.001
- **R_info ↔ Task Difficulty**: R²=0.41  
- **L_info ↔ Reaction Times**: r=0.58, p<0.001
- **Overall Model Performance**: 67% variance explained

## 📁 Project Structure

```
infodynamics/
├── setup_data.py              # 🔧 Data setup script
├── infodynamics/              # 📦 Core models
├── analysis/validation/       # 🧪 Validation experiments  
├── data/                      # 📊 Datasets (downloaded)
├── scripts/data_download/     # ⬇️  Download scripts
└── book/                      # 📖 Documentation
```

## 🆘 Troubleshooting

**Git is slow?**
```bash
# Check if large files are tracked
git ls-files | wc -l  # Should be <1000, not 9000+

# If needed, clean up
python setup_data.py --check
```

**Data missing?**
```bash
# Re-download datasets
python setup_data.py --stanford
```

**Dependencies issues?**
```bash
# Check Python version (>=3.8)
python --version

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

## 🔗 Resources

- **Dataset Source**: [OpenNeuro ds004636](https://openneuro.org/datasets/ds004636)
- **Validation Report**: `analysis/validation/STANFORD_VALIDATION_REPORT.md`
- **Full Documentation**: `book/` directory
- **Mathematical Details**: `book/appendix_a_mathematical_derivations.md`

---

**Questions?** Check existing validation results or create an issue for support. 