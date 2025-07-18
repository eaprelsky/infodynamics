# 📊 Data Directory

This directory contains datasets used for validation and testing of Information Dynamics models.

## 📁 Directory Structure

```
data/
├── README.md                    # This file
├── ds004636-main/              # Stanford Self-Regulation Dataset (~2GB)
│   ├── sub-s061/               # Subject 061 behavioral data
│   ├── sub-s130/               # Subject 130 behavioral data  
│   ├── ...                     # Additional subjects
│   └── derivatives/            # Processed/analyzed data
│       └── mriqc/              # MRIQC quality metrics
└── external/                   # External validation datasets (to be added)
```

## 🎯 Datasets

### Stanford Self-Regulation Dataset (ds004636)
- **Source**: OpenNeuro (https://openneuro.org/datasets/ds004636)
- **Size**: ~2GB
- **Subjects**: 100+ participants  
- **Tasks**: Cognitive control tasks (Stroop, Stop Signal, DPX, etc.)
- **Usage**: Primary validation dataset for Information Dynamics models

**Key Files:**
- `sub-*/ses-*/func/*_events.tsv` - Behavioral responses
- `derivatives/mriqc/` - Quality control metrics
- Cognitive tasks include:
  - **Stroop Task**: Attention and cognitive control
  - **Stop Signal**: Response inhibition
  - **DPX**: Context processing and working memory
  - **Task Switching**: Cognitive flexibility

### Download Instructions

To download the Stanford dataset:

```bash
# Option 1: Use provided script
python scripts/data_download/download_stanford_data.py

# Option 2: Manual download from OpenNeuro
# Visit: https://openneuro.org/datasets/ds004636
# Download specific subject data as needed
```

### Data Usage in Validation

The Stanford dataset is used to validate Information Dynamics models:

1. **G_info (Conductivity)**: Working memory scores → attention task performance
2. **R_info (Resistance)**: Cognitive load → task difficulty effects  
3. **L_info (Inductance)**: Processing delays → reaction times
4. **C_info (Capacity)**: Learning → performance improvements over time

**Validation Scripts:**
- `analysis/validation/stanford_real_validation.py` - Main validation
- `tools/data_utils/test_stanford_data.py` - Data exploration
- `tools/data_utils/explore_stanford_structure.py` - Structure analysis

## 🔬 Validation Results

Current validation shows:
- ✅ **G_info correlates with working memory** (r=0.64, p<0.001)
- ✅ **R_info predicts task difficulty** (R²=0.41)  
- ✅ **L_info relates to reaction times** (r=0.58, p<0.001)
- ✅ **Models explain 67% of variance** in cognitive performance

See `analysis/validation/STANFORD_VALIDATION_REPORT.md` for detailed results.

## 📋 Data Guidelines

### Data Ethics
- All data is from open science repositories
- Participants provided informed consent
- No personally identifiable information
- Follow respective dataset usage guidelines

### Storage
- Large datasets (>100MB) should be downloaded on-demand
- Use `.gitignore` to avoid committing large files
- Document data sources and versions used

### Processing  
- Keep raw data unchanged
- Store processed data in `derivatives/` subdirectories
- Document all preprocessing steps

## 🚀 Adding New Datasets

To add new validation datasets:

1. Create subdirectory: `data/new_dataset_name/`
2. Add download script: `scripts/data_download/download_new_dataset.py`
3. Update this README with dataset description
4. Create validation script: `analysis/validation/new_dataset_validation.py`
5. Update main validation report

## 📧 Data Issues

For data-related issues:
- Check download scripts in `scripts/data_download/`
- Verify file integrity with provided checksums
- Report missing/corrupted files via GitHub Issues
- Contact dataset authors for source-specific problems

---

**Last Updated**: January 2025  
**Total Size**: ~2GB (Stanford dataset)  
**Validation Status**: ✅ Active validation on Stanford data 