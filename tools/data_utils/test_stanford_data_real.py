#!/usr/bin/env python3
"""
Quick test of Stanford behavioral data structure
"""

import pandas as pd
from pathlib import Path

def examine_events_file(file_path):
    """Examine structure of an events file"""
    print(f"\n📄 File: {file_path.name}")
    print(f"📏 Size: {file_path.stat().st_size / 1024:.1f} KB")
    
    try:
        df = pd.read_csv(file_path, sep='\t')
        print(f"📊 Shape: {df.shape}")
        print(f"📋 Columns: {list(df.columns)}")
        
        # Show first few rows
        print(f"\n🔍 First 3 rows:")
        print(df.head(3))
        
        # Basic statistics for numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            print(f"\n📈 Numeric summary:")
            print(df[numeric_cols].describe())
            
    except Exception as e:
        print(f"❌ Error reading file: {e}")

def main():
    print("🧪 Stanford Behavioral Data Test")
    print("=" * 40)
    
    # Test participant
    participant = "sub-s061"
    data_path = Path("data/ds004636-main")
    
    print(f"🧑 Testing participant: {participant}")
    
    # Check events files from both sessions
    events_files = []
    for session in ['ses-1', 'ses-2']:
        func_dir = data_path / participant / session / 'func'
        if func_dir.exists():
            events_files.extend(list(func_dir.glob('*_events.tsv')))
    
    print(f"📁 Found {len(events_files)} events files:")
    for file_path in sorted(events_files):
        task_name = file_path.name.split('_task-')[1].split('_')[0]
        print(f"  • {task_name}: {file_path.name}")
    
    # Examine each file
    for file_path in sorted(events_files)[:3]:  # First 3 files
        examine_events_file(file_path)
    
    print(f"\n✅ Stanford data structure test complete!")

if __name__ == "__main__":
    main() 