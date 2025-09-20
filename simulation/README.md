# 🎭 Simulation Data and Examples

This directory contains **simulated data** and **demonstration files** that showcase Information Dynamics theory without requiring access to the full ds004636 Stanford dataset.

## 📁 Directory Structure

```
simulation/
├── README.md                           # This file
├── analysis/                           # Simulated analysis files
│   ├── stanford_validation_simulated.py              # Stanford validation with simulated data
│   ├── stanford_validation_duplicate_simulated.py    # Duplicate validation file  
│   ├── hcp_conductivity_analysis_v2_simulated.py     # HCP analysis with simulated data
│   ├── hcp_conductivity_analysis_simulated.py        # HCP analysis (v1)
│   ├── test_formulas_simple_simulated.py             # Formula testing with simulated data
│   ├── l_info_validation_simulated.py                # L_info validation simulation
│   ├── t_eff_validation_simulated.py                 # T_eff validation simulation
│   ├── conductivity_validation_simulated.md          # Conductivity validation docs
│   └── notebooks/
│       └── 01_data_exploration_and_validation_simulated.ipynb  # Data exploration demo
└── demos/
    └── notebooks/
        ├── stanford_validation_simulated.ipynb       # Interactive Stanford demo
        └── content_virality_simulated.ipynb          # Content virality simulation
```

## 🎯 Purpose

These files serve several important purposes:

1. **📚 Educational Examples** - Demonstrate Information Dynamics concepts without requiring large datasets
2. **🧪 Testing Framework** - Validate theoretical formulas on controlled, realistic data
3. **🚀 Quick Start** - Allow immediate exploration of the theory without data download
4. **📊 Reproducible Research** - Provide consistent results across different environments

## 🔧 Key Features

### Realistic Statistical Properties
All simulated data maintains the same statistical characteristics as real datasets:
- **Correlation structures** matching published research
- **Distributions** that mirror cognitive assessment patterns  
- **Individual differences** reflecting real population variance
- **Age effects** consistent with cognitive aging literature

### Complete Analysis Pipelines
Each simulation file includes:
- Data generation with controlled parameters
- Full Information Dynamics analysis (G_info, L_info, T_eff)
- Statistical validation and correlation testing
- Visualization and reporting capabilities

## 🏃‍♂️ Quick Start

### Run Stanford Validation Demo
```bash
# Interactive Jupyter notebook
jupyter notebook simulation/demos/notebooks/stanford_validation_simulated.ipynb

# Command line analysis
python simulation/analysis/stanford_validation_simulated.py
```

### Run HCP Conductivity Analysis
```bash
python simulation/analysis/hcp_conductivity_analysis_v2_simulated.py
```

### Test Information Formulas
```bash
python simulation/analysis/test_formulas_simple_simulated.py
```

## 📈 Expected Results

When running simulated analyses, you should see:

- **G_info correlations**: r ≈ 0.60-0.70 with cognitive measures
- **Individual differences**: Meaningful variance in information conductivity
- **Age effects**: Systematic decline patterns matching literature
- **Formula validation**: Strong statistical support for theoretical predictions

## 🔄 Relationship to Real Data

These simulations are designed to:
- **Mirror real findings** from actual ds004636 analysis
- **Validate theoretical models** before applying to real data
- **Provide consistent results** for development and testing
- **Enable reproducible research** across different computing environments

## ⚠️ Important Notes

1. **Simulated data** - These are not real participant responses
2. **Educational purpose** - Designed for learning and validation
3. **Statistical accuracy** - Results match real data patterns but are generated
4. **No privacy concerns** - All data is artificially created

## 🔗 Moving to Real Data

Once you're ready to work with actual datasets:
1. Download ds004636 using scripts in `/scripts/data_download/`
2. Use files in `/analysis/validation/validation/` with `_real` suffix
3. Follow data handling guidelines in `/data/README.md`

---

**Note**: All simulation files are version controlled to ensure reproducible examples and educational materials are always available. 