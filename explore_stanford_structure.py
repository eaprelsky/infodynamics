#!/usr/bin/env python3
"""
Explore Stanford Self-Regulation Dataset structure to find behavioral data
"""

import requests
import json
from pathlib import Path

def check_url_exists(url):
    """Check if a URL exists without downloading"""
    try:
        response = requests.head(url)
        return response.status_code == 200
    except:
        return False

def download_if_exists(url, local_path):
    """Download file if it exists"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"✓ Found and downloaded: {local_path}")
            return True
    except:
        pass
    return False

def main():
    print("🔍 Exploring Stanford Dataset Structure")
    print("=" * 50)
    
    base_url = "https://s3.amazonaws.com/openneuro.org/ds004636"
    
    # Common BIDS files to check
    potential_files = [
        # Top level files
        "CHANGES",
        "README.md", 
        "README.txt",
        "task-*.json",
        
        # Phenotype data (behavioral)
        "phenotype/",
        "sourcedata/",
        "derivatives/",
        
        # Check if task files exist in subject folders
        "sub-s061/",
        "sub-s061/ses-1/",
        "sub-s061/ses-1/beh/",
        "sub-s061/beh/",
        "sub-s061/func/",
        
        # Task description files
        "task-ant_bold.json",
        "task-stroop_bold.json", 
        "task-stopsignal_bold.json",
        "task-workingmemory_bold.json",
    ]
    
    # Try to find task files for first participant
    participant = "sub-s061"
    sessions = ["", "ses-1/", "ses-01/", "ses-baseline/"]
    data_types = ["beh/", "func/", ""]
    
    print(f"\n🧪 Checking structure for participant: {participant}")
    
    found_files = []
    
    for session in sessions:
        for data_type in data_types:
            # Construct path
            path = f"{participant}/{session}{data_type}"
            full_path = f"{participant}/{session}{data_type}"
            
            # Try common task names from the research paper
            tasks = [
                "ant",  # Attention Network Task
                "stroop", 
                "stopsignal",
                "workingmemory", 
                "nback",
                "flanker",
                "cuedts",  # Cued Task Switching
                "threebytwo",
                "spatialspan"
            ]
            
            for task in tasks:
                # Try behavioral data files
                for ext in [".tsv", ".json", ".csv"]:
                    if data_type == "beh/":
                        filename = f"{participant}_{session.rstrip('/')}_task-{task}_beh{ext}"
                        if session == "":
                            filename = f"{participant}_task-{task}_beh{ext}"
                    else:
                        filename = f"{participant}_{session.rstrip('/')}_task-{task}_bold{ext}"
                        if session == "":
                            filename = f"{participant}_task-{task}_bold{ext}"
                    
                    url = f"{base_url}/{path}{filename}"
                    local_path = f"stanford_data/{path}{filename}"
                    
                    if download_if_exists(url, local_path):
                        found_files.append((path, filename))
    
    # Also try to download task description files
    print(f"\n📋 Checking for task description files...")
    task_descriptions = [
        "task-ant_bold.json",
        "task-stroop_bold.json", 
        "task-stopsignal_bold.json",
        "task-workingmemory_bold.json",
        "task-nback_bold.json",
        "task-flanker_bold.json"
    ]
    
    for task_file in task_descriptions:
        url = f"{base_url}/{task_file}"
        local_path = f"stanford_data/{task_file}"
        download_if_exists(url, local_path)
    
    # Try derivatives folder (where processed behavioral data often lives)
    print(f"\n📊 Checking derivatives folder...")
    derivatives_files = [
        "derivatives/behavioral/participants.tsv",
        "derivatives/behavioral/task-ant_summary.tsv",
        "derivatives/behavioral/task-stroop_summary.tsv",
        "derivatives/behavioral/group_behavioral_data.tsv",
        "derivatives/behavioral_data.csv",
        "derivatives/all_behavioral_data.csv"
    ]
    
    for deriv_file in derivatives_files:
        url = f"{base_url}/{deriv_file}"
        local_path = f"stanford_data/{deriv_file}"
        download_if_exists(url, local_path)
    
    print("\n" + "=" * 50)
    print("📁 Exploration Results:")
    
    if found_files:
        print(f"✓ Found {len(found_files)} behavioral data files!")
        for path, filename in found_files:
            print(f"   📄 {path}{filename}")
    else:
        print("❌ No behavioral data files found in standard locations")
        print("\n💡 The behavioral data might be:")
        print("   - In the derivatives folder (processed data)")
        print("   - Embedded in the fMRI event files")
        print("   - Available only through paper supplementary materials")
        print("   - In a different dataset format")
    
    # Show what we actually downloaded
    stanford_dir = Path("stanford_data")
    if stanford_dir.exists():
        print(f"\n📂 Currently downloaded:")
        for item in sorted(stanford_dir.rglob("*")):
            if item.is_file():
                size_kb = item.stat().st_size / 1024
                print(f"   • {item.relative_to(stanford_dir)} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main() 