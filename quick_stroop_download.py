#!/usr/bin/env python3
"""
Quick download of Stroop task event files for validation
"""

import requests
from pathlib import Path

def download_file(url, local_path):
    """Download a file if it exists"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"✓ Downloaded: {local_path} ({len(response.content)} bytes)")
            return True
        else:
            print(f"✗ Not found: {url} (HTTP {response.status_code})")
    except Exception as e:
        print(f"✗ Error downloading {url}: {e}")
    return False

def main():
    print("🎯 Quick Stroop Task Data Download")
    print("=" * 40)
    
    base_url = "https://s3.amazonaws.com/openneuro.org/ds004636"
    
    # Try first 5 participants
    test_participants = ["sub-s061", "sub-s130", "sub-s144", "sub-s172", "sub-s192"]
    
    # Different file types and locations to try
    file_patterns = [
        # Events files (most likely to contain behavioral data)
        "{participant}/func/{participant}_task-stroop_events.tsv",
        "{participant}/func/{participant}_task-stroop_bold.tsv", 
        "{participant}/func/{participant}_task-stroop_run-1_events.tsv",
        "{participant}/func/{participant}_task-stroop_run-01_events.tsv",
        
        # Behavioral files
        "{participant}/beh/{participant}_task-stroop_beh.tsv",
        "{participant}/beh/{participant}_task-stroop_events.tsv",
        
        # Session-based files
        "{participant}/ses-1/func/{participant}_ses-1_task-stroop_events.tsv",
        "{participant}/ses-01/func/{participant}_ses-01_task-stroop_events.tsv",
        
        # Direct in participant folder
        "{participant}/{participant}_task-stroop_events.tsv",
    ]
    
    downloaded_count = 0
    
    for participant in test_participants:
        print(f"\n🧪 Testing participant: {participant}")
        
        for pattern in file_patterns:
            file_path = pattern.format(participant=participant)
            url = f"{base_url}/{file_path}"
            local_path = f"stanford_data/{file_path}"
            
            if download_file(url, local_path):
                downloaded_count += 1
                
                # If we found one, also try other tasks for this participant
                other_tasks = ["ant", "stopsignal", "nback", "flanker"]
                for task in other_tasks:
                    alt_pattern = pattern.replace("stroop", task)
                    alt_path = alt_pattern.format(participant=participant)
                    alt_url = f"{base_url}/{alt_path}"
                    alt_local = f"stanford_data/{alt_path}"
                    download_file(alt_url, alt_local)
                
                break  # Found working pattern for this participant
    
    print(f"\n📊 Summary: Downloaded {downloaded_count} files")
    
    if downloaded_count > 0:
        print("🎉 Success! Found behavioral data files.")
        print("📂 Let's examine what we got:")
        
        stanford_dir = Path("stanford_data")
        for file_path in sorted(stanford_dir.rglob("*events.tsv")):
            size_kb = file_path.stat().st_size / 1024
            print(f"   • {file_path.relative_to(stanford_dir)} ({size_kb:.1f} KB)")
    else:
        print("❌ No behavioral event files found with this approach.")
        print("💡 Next steps:")
        print("   - The data might be in derivatives folder")
        print("   - Or available only through paper supplementary materials")
        print("   - Or we need different task names")

if __name__ == "__main__":
    main() 