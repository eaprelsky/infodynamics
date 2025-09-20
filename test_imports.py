#!/usr/bin/env python3

print("Testing imports...")

try:
    import pandas, numpy, matplotlib, seaborn
    print("✅ Basic packages work!")
except ImportError as e:
    print(f"❌ Basic packages error: {e}")

try:
    import factor_analyzer
    print("✅ factor_analyzer works!")
except ImportError as e:
    print(f"❌ factor_analyzer error: {e}")

try:
    import jupyter
    print("✅ Jupyter works!")
except ImportError as e:
    print(f"❌ Jupyter error: {e}")

print(f"Python executable: {__import__('sys').executable}")
print("All tests completed!") 