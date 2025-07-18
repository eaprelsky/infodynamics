#!/usr/bin/env python3
"""
Download behavioral events files from Stanford Self-Regulation Dataset
These files contain trial-by-trial behavioral responses
"""

import requests
from pathlib import Path
import time
from tqdm import tqdm

def download_file(url, local_path):
    """Download a file if it exists"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
    except:
        pass
    return False

def main():
    print("🧠 Downloading Stanford Behavioral Events Data")
    print("📊 Target: Trial-by-trial cognitive task responses")
    print("=" * 60)
    
    # Read participants list
    participants = []
    with open("stanford_data/participants.tsv", 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:  # Skip header
            participant_id = line.strip().split('\t')[0]
            participants.append(participant_id)
    
    print(f"👥 Found {len(participants)} participants")
    
    # Stanford dataset base URL
    base_url = "https://s3.amazonaws.com/openneuro.org/ds004636"
    
    # Task names to try (based on the paper)
    tasks = [
        "stroop",        # Stroop task (confirmed to exist)
        "ant",           # Attention Network Task
        "stopsignal",    # Stop Signal Task
        "workingmemory", # Working Memory
        "nback",         # N-back task
        "flanker",       # Flanker task
        "cuedts",        # Cued Task Switching
        "threebytwo",    # Three by two task
        "spatialspan"    # Spatial span
    ]
    
    # Data types to try
    data_types = [
        "events",  # Trial-by-trial events (most important)
        "beh",     # Summary behavioral data
        "bold"     # fMRI events (contains behavioral timing)
    ]
    
    downloaded_files = []
    total_attempts = len(participants) * len(tasks) * len(data_types)
    
    print(f"🔍 Attempting to download {total_attempts} potential files...")
    print("⏱️  This may take a few minutes...")
    
    with tqdm(total=total_attempts, desc="Downloading") as pbar:
        for participant in participants:
            for task in tasks:
                for data_type in data_types:
                    # BIDS filename format
                    filename = f"{participant}_task-{task}_{data_type}.tsv"
                    
                    # Try different possible paths
                    possible_paths = [
                        f"{participant}/func/{filename}",  # Most common location
                        f"{participant}/beh/{filename}",   # Behavioral folder
                        f"{participant}/{filename}",       # Direct in participant folder
                    ]
                    
                    for path in possible_paths:
                        url = f"{base_url}/{path}"
                        local_path = f"stanford_data/{path}"
                        
                        if download_file(url, local_path):
                            downloaded_files.append((participant, task, data_type, path))
                            print(f"\n✓ {participant} - {task} - {data_type}")
                            break  # Found it, no need to try other paths
                    
                    pbar.update(1)
                    time.sleep(0.1)  # Be nice to the server
    
    print("\n" + "=" * 60)
    print("📊 Download Results:")
    print(f"✓ Successfully downloaded: {len(downloaded_files)} files")
    
    if downloaded_files:
        # Group by task type
        task_counts = {}
        for _, task, data_type, _ in downloaded_files:
            key = f"{task}_{data_type}"
            task_counts[key] = task_counts.get(key, 0) + 1
        
        print("\n📋 Files downloaded by task:")
        for task_type, count in sorted(task_counts.items()):
            print(f"   • {task_type}: {count} files")
        
        # Show sample file sizes
        print(f"\n📂 Sample downloaded files:")
        stanford_dir = Path("stanford_data")
        behavioral_files = list(stanford_dir.rglob("*_events.tsv")) + list(stanford_dir.rglob("*_beh.tsv"))
        
        for file_path in sorted(behavioral_files)[:10]:  # Show first 10
            size_kb = file_path.stat().st_size / 1024
            print(f"   • {file_path.relative_to(stanford_dir)} ({size_kb:.1f} KB)")
        
        if len(behavioral_files) > 10:
            print(f"   ... and {len(behavioral_files) - 10} more files")
        
        print(f"\n🔬 Ready for Information Dynamics validation!")
        print(f"📈 We now have real behavioral data from {len(set(p for p, _, _, _ in downloaded_files))} participants")
        
    else:
        print("\n❌ No behavioral files found.")
        print("💡 The behavioral data might be:")
        print("   - In a different file format")
        print("   - Processed and stored elsewhere")
        print("   - Available only in supplementary materials")
        print("   - Embedded in the imaging data")

if __name__ == "__main__":
    main() 