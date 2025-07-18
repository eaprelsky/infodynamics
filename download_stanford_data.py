#!/usr/bin/env python3
"""
Download Stanford Self-Regulation Dataset (ds004636) from OpenNeuro
Focus on behavioral data for Information Dynamics validation
"""

import os
import requests
import json
from pathlib import Path
import urllib.request
from tqdm import tqdm
import time

def download_file(url, local_path, description=""):
    """Download a file with progress bar"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        with open(local_path, 'wb') as f, tqdm(
            desc=description,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                pbar.update(size)
        
        print(f"✓ Downloaded: {local_path}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return False

def main():
    """Download Stanford Self-Regulation Dataset behavioral data"""
    
    print("🧠 Downloading Stanford Self-Regulation Dataset (ds004636)")
    print("📊 Focus: Behavioral data for Information Dynamics validation")
    print("-" * 60)
    
    # Create base directory
    base_dir = Path("stanford_data")
    base_dir.mkdir(exist_ok=True)
    
    # OpenNeuro S3 base URL for ds004636
    base_url = "https://s3.amazonaws.com/openneuro.org/ds004636"
    
    # Key files to download for behavioral analysis
    files_to_download = [
        # Dataset description
        ("dataset_description.json", "Dataset metadata and description"),
        ("README", "Dataset README file"),
        ("participants.tsv", "Participant demographics and info"),
        
        # Behavioral data files (these contain the cognitive task results)
        ("sourcedata/behavioral_data/attention_network_task.csv", "Attention Network Task results"),
        ("sourcedata/behavioral_data/stop_signal_task.csv", "Stop Signal Task results"), 
        ("sourcedata/behavioral_data/stroop_task.csv", "Stroop Task results"),
        ("sourcedata/behavioral_data/spatial_working_memory.csv", "Working Memory Task results"),
        ("sourcedata/behavioral_data/cognitive_reflection_test.csv", "Cognitive Reflection Test"),
        ("sourcedata/behavioral_data/demographics.csv", "Detailed demographics"),
        ("sourcedata/behavioral_data/questionnaires.csv", "Psychological questionnaires"),
    ]
    
    # Alternative: Try to get the file list first
    print("🔍 Checking dataset structure...")
    
    # Download main files
    downloaded_count = 0
    failed_count = 0
    
    for filename, description in files_to_download:
        url = f"{base_url}/{filename}"
        local_path = base_dir / filename
        
        print(f"\n📥 {description}")
        if download_file(url, str(local_path), filename):
            downloaded_count += 1
        else:
            failed_count += 1
        
        # Be nice to the server
        time.sleep(0.5)
    
    print("\n" + "=" * 60)
    print(f"📊 Download Summary:")
    print(f"   ✓ Successfully downloaded: {downloaded_count} files")
    print(f"   ✗ Failed downloads: {failed_count} files")
    
    if downloaded_count > 0:
        print(f"\n📂 Data saved to: {base_dir.absolute()}")
        print("🔬 Ready for Information Dynamics validation!")
        
        # List what we actually got
        print("\n📋 Downloaded files:")
        for item in sorted(base_dir.rglob("*")):
            if item.is_file():
                size_mb = item.stat().st_size / (1024 * 1024)
                print(f"   • {item.relative_to(base_dir)} ({size_mb:.1f} MB)")
    else:
        print("\n❌ No files were downloaded successfully.")
        print("💡 This might be due to:")
        print("   - Network connectivity issues")
        print("   - OpenNeuro server problems")
        print("   - Dataset access restrictions")
        print("   - Incorrect file paths")
        
        print("\n🔄 Alternative: Manual download from https://openneuro.org/datasets/ds004636")

if __name__ == "__main__":
    main() 