#!/usr/bin/env python3
"""
Data Setup Script for Information Dynamics Project

This script helps new users and researchers set up the required datasets
for validation and experiments.

Usage:
    python setup_data.py               # Download all datasets
    python setup_data.py --stanford    # Download only Stanford dataset
    python setup_data.py --check       # Check existing data integrity
"""

import os
import sys
import subprocess
import hashlib
import argparse
from pathlib import Path

def check_data_integrity():
    """Check if required data files exist and are valid"""
    print("🔍 Checking data integrity...")
    
    required_files = [
        "data/ds004636-main/dataset_description.json",
        "data/ds004636-main.zip"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required data files present")
        return True

def download_stanford_data():
    """Download Stanford Self-Regulation Dataset"""
    print("📥 Downloading Stanford dataset...")
    
    script_path = "scripts/data_download/download_stanford_data.py"
    if Path(script_path).exists():
        try:
            result = subprocess.run([sys.executable, script_path], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Stanford dataset downloaded successfully")
                return True
            else:
                print(f"❌ Download failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Error running download script: {e}")
            return False
    else:
        print(f"❌ Download script not found: {script_path}")
        return False

def setup_directories():
    """Create necessary directories"""
    print("📁 Setting up directories...")
    
    directories = [
        "data/external",
        "data/temp",
        "analysis/outputs",
        "results"
    ]
    
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    print("✅ Directories created")

def display_info():
    """Display information about the project data setup"""
    print("""
🧠 Information Dynamics Project - Data Setup
============================================

This project uses external datasets for validation:

📊 Stanford Self-Regulation Dataset (ds004636)
   - Source: OpenNeuro (https://openneuro.org/datasets/ds004636)
   - Size: ~2GB
   - Purpose: Validate Information Dynamics models
   - Subjects: 100+ participants with cognitive task data

🔬 Usage in Validation:
   - G_info (Conductivity): Working memory → attention performance
   - R_info (Resistance): Cognitive load → task difficulty  
   - L_info (Inductance): Processing delays → reaction times
   - C_info (Capacity): Learning → performance improvements

📋 Next Steps:
   1. Run validation: python analysis/validation/stanford_real_validation.py
   2. Explore data: python tools/data_utils/explore_stanford_structure.py
   3. See results: analysis/validation/STANFORD_VALIDATION_REPORT.md

💡 Note: Data files are downloaded on-demand to keep git repository lightweight.
""")

def main():
    parser = argparse.ArgumentParser(description="Setup data for Information Dynamics project")
    parser.add_argument("--stanford", action="store_true", help="Download only Stanford dataset")
    parser.add_argument("--check", action="store_true", help="Check data integrity only")
    parser.add_argument("--info", action="store_true", help="Display project information")
    
    args = parser.parse_args()
    
    # Change to project root directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    if args.info:
        display_info()
        return
    
    if args.check:
        if check_data_integrity():
            print("🎉 Data setup is complete and valid!")
        else:
            print("⚠️  Some data files are missing. Run without --check to download.")
        return
    
    print("🚀 Setting up Information Dynamics project data...\n")
    
    # Setup directories
    setup_directories()
    
    # Download data
    if args.stanford or not args.check:
        if not download_stanford_data():
            print("❌ Failed to download Stanford dataset")
            sys.exit(1)
    
    # Final check
    if check_data_integrity():
        print("\n🎉 Data setup complete! You can now run validation experiments.")
        display_info()
    else:
        print("\n⚠️  Setup completed but some files may be missing.")

if __name__ == "__main__":
    main() 