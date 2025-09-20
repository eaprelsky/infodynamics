#!/usr/bin/env python3
"""
Simple formula testing script for G_info optimization
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from scipy.optimize import minimize
import warnings
warnings.filterwarnings('ignore')

def load_simulated_data():
    """Load simulated HCP-like data"""
    np.random.seed(42)
    n_subjects = 1200
    
    # Generate realistic data
    ages = np.clip(np.random.normal(28.5, 6.2, n_subjects), 17, 40)
    
    # Cognitive abilities
    working_memory = np.random.normal(0, 1, n_subjects)
    processing_speed = np.random.normal(0, 1, n_subjects)
    intelligence = 0.6 * working_memory + 0.4 * processing_speed + np.random.normal(0, 0.5, n_subjects)
    
    # Information conductivity components
    k_individual = 0.5 * intelligence + np.random.normal(0, 0.3, n_subjects)
    attention_focus = 0.7 * working_memory + np.random.normal(0, 0.4, n_subjects)
    cognitive_load_ratio = np.clip(0.3 + 0.4 * (1 - processing_speed) + np.random.normal(0, 0.2, n_subjects), 0.1, 0.9)
    
    # Target variable with true relationships
    cognitive_performance = (
        0.6 * k_individual + 
        0.4 * attention_focus + 
        0.3 * (1 - cognitive_load_ratio) +
        0.2 * k_individual * attention_focus +
        np.random.normal(0, 0.3, n_subjects)
    )
    
    return pd.DataFrame({
        'k_individual': k_individual,
        'attention_focus': attention_focus,
        'cognitive_load_ratio': cognitive_load_ratio,
        'cognitive_performance': cognitive_performance
    })

def standardize_data(data):
    """Standardize the data"""
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    
    vars_to_scale = ['k_individual', 'attention_focus', 'cognitive_load_ratio', 'cognitive_performance']
    for var in vars_to_scale:
        data[f'{var}_scaled'] = scaler.fit_transform(data[[var]])
    
    return data

def test_formulas(data):
    """Test different G_info formulas"""
    k = data['k_individual_scaled'].values
    a = data['attention_focus_scaled'].values  
    l = data['cognitive_load_ratio_scaled'].values
    y = data['cognitive_performance_scaled'].values
    
    results = {}
    
    # 1. Original multiplicative formula
    print("1. Original Formula: G = k × attention × (1-load)")
    g_original = k * a * (1 - l)
    r_orig, p_orig = pearsonr(g_original, y)
    results['original'] = {'correlation': r_orig, 'r_squared': r_orig**2}
    print(f"   Correlation: r = {r_orig:.3f}, R² = {r_orig**2:.3f}")
    
    # 2. Additive formula
    print("\n2. Additive Formula: G = k + attention + (1-load)")
    g_additive = k + a + (1 - l)
    r_add, p_add = pearsonr(g_additive, y)
    results['additive'] = {'correlation': r_add, 'r_squared': r_add**2}
    print(f"   Correlation: r = {r_add:.3f}, R² = {r_add**2:.3f}")
    
    # 3. Weighted linear combination
    print("\n3. Weighted Formula: G = w₁×k + w₂×attention + w₃×(1-load)")
    
    def weighted_objective(weights):
        w1, w2, w3 = weights
        g_weighted = w1 * k + w2 * a + w3 * (1 - l)
        return -pearsonr(g_weighted, y)[0]
    
    result = minimize(weighted_objective, x0=[1, 1, 1], method='BFGS')
    w_opt = result.x
    g_weighted = w_opt[0] * k + w_opt[1] * a + w_opt[2] * (1 - l)
    r_weight, p_weight = pearsonr(g_weighted, y)
    
    results['weighted'] = {
        'correlation': r_weight, 
        'r_squared': r_weight**2,
        'weights': w_opt
    }
    print(f"   Optimal weights: w₁={w_opt[0]:.3f}, w₂={w_opt[1]:.3f}, w₃={w_opt[2]:.3f}")
    print(f"   Correlation: r = {r_weight:.3f}, R² = {r_weight**2:.3f}")
    
    # 4. Interaction formula
    print("\n4. Interaction Formula: G = k + attention + (1-load) + k×attention")
    g_interaction = k + a + (1 - l) + k*a
    r_int, p_int = pearsonr(g_interaction, y)
    results['interaction'] = {'correlation': r_int, 'r_squared': r_int**2}
    print(f"   Correlation: r = {r_int:.3f}, R² = {r_int**2:.3f}")
    
    return results

def main():
    """Main analysis"""
    print("=" * 60)
    print("G_INFO FORMULA OPTIMIZATION TEST")
    print("=" * 60)
    
    # Load and prepare data
    print("Loading simulated data...")
    data = load_simulated_data()
    data = standardize_data(data)
    print(f"Dataset: {len(data)} subjects")
    
    # Test formulas
    print(f"\nTesting alternative G_info formulas:")
    print("-" * 40)
    
    results = test_formulas(data)
    
    # Summary
    print(f"\n" + "=" * 60)
    print("FORMULA COMPARISON SUMMARY")
    print("=" * 60)
    
    original_r2 = results['original']['r_squared']
    print(f"Original formula R²: {original_r2:.3f}")
    
    for name, result in results.items():
        if name != 'original':
            improvement = 100 * (result['r_squared'] - original_r2)
            print(f"{name.capitalize():12} R²: {result['r_squared']:.3f} ({improvement:+.1f}% improvement)")
    
    # Best formula
    best_formula = max(results.keys(), key=lambda x: results[x]['r_squared'])
    best_improvement = 100 * (results[best_formula]['r_squared'] - original_r2)
    
    print(f"\n🏆 BEST FORMULA: {best_formula}")
    print(f"   Improvement: +{best_improvement:.1f}%")
    
    if best_formula == 'weighted':
        weights = results['weighted']['weights'] 
        print(f"   Optimal formula: G = {weights[0]:.2f}×k + {weights[1]:.2f}×attention + {weights[2]:.2f}×(1-load)")
    
    return results

if __name__ == "__main__":
    results = main() 