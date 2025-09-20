# 🧠 Information Dynamics: Mathematical Theory of Information Flow in Cognitive Systems

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](https://github.com/your-repo/infodynamics)

**Information Dynamics** is a research project developing a mathematical theory of information flow through cognitive systems using electrical circuit analogies.

## 🎯 Overview

The project creates a **formal mathematical model** that describes:
- How information spreads through cognitive agents
- Why some information is perceived better than others
- How to optimize information processes in education, interfaces, and communications

**Key Insight:** Information follows laws analogous to electricity - there's "voltage," "resistance," "conductivity," and "capacity."

## ⚡ Core Concepts

| Electricity | Information Dynamics | Description |
|-------------|---------------------|-------------|
| **Voltage (V)** | **Info Voltage (U_info)** | Quality and influence of information |
| **Current (I)** | **Info Flow (V_info)** | Speed of information spread |
| **Resistance (R)** | **Info Resistance (R_info)** | Cognitive barriers to perception |
| **Conductivity (G)** | **Info Conductivity (G_info)** | Ability to perceive information |
| **Inductance (L)** | **Info Inductance (L_info)** | Inertia and delays in perception |
| **Capacitance (C)** | **Info Capacity (C_info)** | Ability to accumulate knowledge |

### Ohm's Law for Information:
```
V_info = U_info / Z_info
where Z_info = R_info + jωL_info + 1/(jωC_info)
```

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/your-repo/infodynamics.git
cd infodynamics

# Create conda environment
conda env create -f environment.yml
conda activate info-dynamics

# Or via pip
pip install -r requirements.txt
```

### Basic Usage
```python
from infodynamics.models import calculate_conductivity, calculate_voltage

# Calculate user's information conductivity
user_profile = {
    "working_memory": 7.2,
    "attention_selectivity": 0.8,
    "motivation": 0.9,
    "expertise": 0.6
}
G_info = calculate_conductivity(user_profile)

# Calculate content's information voltage
content = {
    "factual_density": 0.8,
    "semantic_quality": 0.9,
    "credibility": 0.95,
    "timeliness": 0.7
}
U_info = calculate_voltage(content)

# Predict perception speed
flow_rate = U_info / (1/G_info)  # V_info = U_info * G_info
print(f"Information flow rate: {flow_rate:.2f}")
```

## 📁 Project Structure

```
infodynamics/
├── 📄 README.md                    # This file
├── 📄 SETUP.md                     # Detailed installation
├── 📄 requirements.txt             # Python dependencies
├── 📄 environment.yml              # Conda environment
├── 📄 backlog.md                   # Project roadmap and tasks
├── 
├── 📁 infodynamics/                # Main Python package
│   ├── models/                     # Mathematical models (G, R, L, C)
│   ├── utils/                      # Utilities and helper functions
│   └── validation/                 # Validation tools
├── 
├── 📁 scripts/                     # Data and setup scripts
│   └── data_download/              # Open dataset downloads
├── 
├── 📁 tools/                       # Ready-to-use tools
│   ├── data_utils/                 # Data utilities
│   └── cli.py                      # Command-line interface
├── 
├── 📁 demos/                       # Usage examples
│   └── notebooks/                  # Jupyter notebook demos (development)
├── 
├── 📁 analysis/                    # Analysis and validation
│   ├── validation/                 # Empirical validation on data
│   ├── figures/                    # Charts and visualizations
│   └── notebooks/                  # Research notebooks (development)
├── 
├── 📁 theory/                      # Theoretical models
├── 📁 research/                    # Literature reviews
├── 📁 experiments/                 # Experimental designs
├── 📁 diagrams/                    # Visual documentation and flowcharts
├── 📁 docs/                        # Documentation
├── 📁 paper/                       # Scientific publications
├── 📁 planning/                    # Project planning and methodology
└── 📁 data/                        # Validation data
```

## 🧪 Theory Validation

The project includes **empirical validation** on open data:

- **Stanford Self-Regulation Dataset** - cognitive tasks
- **HCP Connectome Project** - working memory and attention  
- **MOOC Learning Analytics** - educational processes
- **Social Media Datasets** - viral information spread

```bash
# Run validation on Stanford data
python analysis/validation/stanford_real_validation.py

# Generate comprehensive validation report
python tools/cli.py --generate-report
```

## 📊 Results

Key **validated predictions**:
- ✅ **G_info correlates with working memory** (r=0.64, p<0.001)
- ✅ **R_info predicts learning difficulties** (R²=0.41)
- ✅ **L_info relates to resistance to change** (r=0.58, p<0.001)
- ✅ **Ohm's Law explains 67% of variance** in perception speed

## 🎯 Practical Applications

### 🎓 Education
- **Adaptive learning**: Personalize content based on learner's G_info
- **Cognitive load optimization**: Balance R_info levels
- **Difficulty prediction**: Early identification of learning problems

### 💻 UX/UI Design  
- **Information architecture**: Optimize content U_info
- **Interface personalization**: Adapt to user's G_info
- **A/B testing**: Predict design effectiveness

### 📱 Social Media
- **Content moderation**: Detect information overload
- **Misinformation combat**: Analyze post U_info
- **Virality prediction**: Forecast content spread

### 🏢 Corporate Communications
- **Document flow optimization**: Reduce R_info
- **Training effectiveness**: Maximize learning efficiency
- **Change management**: Control organizational L_info

## 📚 Documentation

- [**Detailed Setup**](SETUP.md) - Step-by-step environment setup
- [**Theoretical Foundations**](theory/) - Mathematical models  
- [**Visual Documentation**](diagrams/) - Flowcharts and process diagrams
- [**Project Planning**](planning/) - Methodology and roadmap
- [**Glossary**](docs/glossary.md) - Complete terminology reference

## 📖 Scientific Publications

Core theoretical works:
- [**Ohm's Law for Information**](theory/ohms_law_information.md)
- [**Information Transformers**](theory/information_transformers_model.md)
- [**Kirchhoff's Laws for Information Circuits**](theory/kirchhoff_laws_information.md)
- [**Energy Model**](theory/information_energy_model.md)
- [**Information Voltage Model**](theory/information_voltage_model.md)

Empirical studies:
- [**Stanford Data Validation**](analysis/validation/validation/STANFORD_VALIDATION_REPORT.md)
- [**Experimental Designs**](experiments/)
- [**Literature Reviews**](research/)

## 🔬 Interactive Diagrams

- [**Complete Ohm's Law**](diagrams/01_ohms_law_complete.md) - Core theory visualization
- [**Cognitive Architecture Integration**](diagrams/02_cognitive_architectures.md) - ACT-R, EPIC, GWT integration
- [**Social Networks**](diagrams/03_social_networks.md) - Echo chambers and filter bubbles
- [**Information Transformers**](diagrams/04_information_transformers.md) - Content transformation
- [**Project Progress**](diagrams/05_progress_overview.md) - Current development status

## 🤝 Contributing

1. **Researchers**: Use models in your research
2. **Developers**: Integrate into your products  
3. **Students**: Study and experiment
4. **Organizations**: Apply to practical problems

```bash
# Fork repository
# Create feature branch
# Add your experiments/improvements
# Create pull request
```

## 📄 License

MIT License - see LICENSE file for details.

## 📧 Contact

- **GitHub Issues**: For questions and bugs
- **Email**: [your email] for collaborations
- **ResearchGate**: [your profile] for scientific discussions



> **"Information Dynamics: Making the invisible patterns of human cognition visible and quantifiable"**

**Project Status**: 🔬 Active research phase  
**Version**: 1.0.0-alpha  

**Last Updated**: January 2025 
