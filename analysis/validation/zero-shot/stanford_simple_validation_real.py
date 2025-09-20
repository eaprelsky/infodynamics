#!/usr/bin/env python3
"""
Simplified Stanford Information Dynamics Validation (no plotting dependencies)
Tests our theory on real cognitive data from 103 participants
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats

class SimpleStanfordValidator:
    
    def __init__(self, data_path="data/ds004636-main"):
        self.data_path = Path(data_path)
        print("🧠 Stanford Information Dynamics Validator (Simple)")
        print("=" * 50)
        
    def extract_stroop_metrics(self, participant_id, session='ses-2'):
        """Extract Stroop task metrics"""
        stroop_file = (self.data_path / participant_id / session / 'func' / 
                      f"{participant_id}_{session}_task-stroop_run-1_events.tsv")
        
        if not stroop_file.exists():
            return None
            
        try:
            df = pd.read_csv(stroop_file, sep='\t')
            
            # Filter valid trials
            valid_trials = df[(df['response_time'].notna()) & (df['response_time'] > 0)]
            
            if len(valid_trials) < 10:  # Need minimum trials
                return None
            
            # Extract metrics
            metrics = {}
            
            # Check if we have condition information
            if 'condition' in df.columns:
                congruent = valid_trials[valid_trials['condition'] == 'congruent']
                incongruent = valid_trials[valid_trials['condition'] == 'incongruent']
                
                if len(congruent) > 0 and len(incongruent) > 0:
                    metrics['congruent_rt'] = congruent['response_time'].mean()
                    metrics['incongruent_rt'] = incongruent['response_time'].mean()
                    metrics['stroop_effect'] = metrics['incongruent_rt'] - metrics['congruent_rt']
                    
                    if 'correct' in df.columns:
                        metrics['congruent_acc'] = congruent['correct'].mean()
                        metrics['incongruent_acc'] = incongruent['correct'].mean()
                        metrics['stroop_acc_cost'] = metrics['congruent_acc'] - metrics['incongruent_acc']
            
            # Overall metrics
            metrics['mean_rt'] = valid_trials['response_time'].mean()
            metrics['rt_variability'] = valid_trials['response_time'].std()
            
            if 'correct' in df.columns:
                metrics['overall_accuracy'] = valid_trials['correct'].mean()
            
            return metrics
            
        except Exception as e:
            print(f"  Error processing Stroop for {participant_id}: {e}")
            return None
    
    def extract_stop_signal_metrics(self, participant_id, session='ses-1'):
        """Extract Stop Signal task metrics"""
        stop_file = (self.data_path / participant_id / session / 'func' / 
                    f"{participant_id}_{session}_task-stopSignal_run-1_events.tsv")
        
        if not stop_file.exists():
            return None
            
        try:
            df = pd.read_csv(stop_file, sep='\t')
            
            # Filter valid trials
            valid_trials = df[df['response_time'].notna()]
            
            if len(valid_trials) < 10:
                return None
            
            metrics = {}
            
            # Go trials
            go_trials = valid_trials[valid_trials['trial_type'] == 'go']
            if len(go_trials) > 0:
                metrics['go_rt'] = go_trials['response_time'].mean()
                metrics['go_rt_std'] = go_trials['response_time'].std()
                
                if 'correct' in df.columns:
                    metrics['go_accuracy'] = go_trials['correct'].mean()
            
            # Stop trials
            stop_trials = valid_trials[valid_trials['trial_type'].str.contains('stop', case=False, na=False)]
            if len(stop_trials) > 0:
                if 'stopped' in df.columns:
                    metrics['stop_accuracy'] = stop_trials['stopped'].mean()
                elif 'correct' in df.columns:
                    metrics['stop_accuracy'] = stop_trials['correct'].mean()
                
                # Estimate SSRT if we have SS_delay
                if 'SS_delay' in df.columns and len(go_trials) > 0:
                    avg_ssd = stop_trials['SS_delay'].mean()
                    go_rt_mean = go_trials['response_time'].mean()
                    metrics['estimated_ssrt'] = go_rt_mean - avg_ssd
            
            return metrics
            
        except Exception as e:
            print(f"  Error processing Stop Signal for {participant_id}: {e}")
            return None
    
    def extract_dpx_metrics(self, participant_id, session='ses-2'):
        """Extract DPX task metrics (attention/context)"""
        dpx_file = (self.data_path / participant_id / session / 'func' / 
                   f"{participant_id}_{session}_task-DPX_run-1_events.tsv")
        
        if not dpx_file.exists():
            return None
            
        try:
            df = pd.read_csv(dpx_file, sep='\t')
            valid_trials = df[(df['response_time'].notna()) & (df['response_time'] > 0)]
            
            if len(valid_trials) < 10:
                return None
            
            metrics = {}
            metrics['mean_rt'] = valid_trials['response_time'].mean()
            metrics['rt_variability'] = valid_trials['response_time'].std()
            
            if 'correct' in df.columns:
                metrics['accuracy'] = valid_trials['correct'].mean()
            
            # Context processing if trial types available
            if 'trial_type' in df.columns:
                # AY trials typically test cognitive control
                ay_trials = valid_trials[valid_trials['trial_type'].str.contains('AY', case=False, na=False)]
                bx_trials = valid_trials[valid_trials['trial_type'].str.contains('BX', case=False, na=False)]
                
                if len(ay_trials) > 0 and len(bx_trials) > 0:
                    metrics['context_effect'] = ay_trials['response_time'].mean() - bx_trials['response_time'].mean()
            
            return metrics
            
        except Exception as e:
            print(f"  Error processing DPX for {participant_id}: {e}")
            return None
    
    def compute_information_dynamics(self, stroop_metrics, stop_metrics, dpx_metrics):
        """Compute Information Dynamics parameters from task metrics"""
        params = {}
        
        # G_info (Information Conductivity) - from DPX attention task
        if dpx_metrics:
            # Higher processing speed and accuracy = higher conductivity
            processing_speed = 1 / (dpx_metrics['mean_rt'] / 1000) if dpx_metrics['mean_rt'] > 0 else np.nan
            accuracy_factor = dpx_metrics.get('accuracy', 1.0)
            
            # Stability factor (lower variability = better conductivity)
            stability_factor = 1 / (1 + dpx_metrics.get('rt_variability', 0) / 1000)
            
            params['G_info'] = processing_speed * accuracy_factor * stability_factor
        else:
            params['G_info'] = np.nan
        
        # L_info (Information Inductance) - from Stroop interference
        if stroop_metrics and 'stroop_effect' in stroop_metrics:
            # Normalized interference effect
            baseline_rt = stroop_metrics['congruent_rt'] / 1000
            interference = stroop_metrics['stroop_effect'] / 1000
            
            if baseline_rt > 0:
                params['L_info'] = interference / baseline_rt  # Relative interference
            else:
                params['L_info'] = np.nan
        else:
            params['L_info'] = np.nan
        
        # T_eff (Transformation Efficiency) - from Stop Signal control
        if stop_metrics:
            # Efficiency from inhibition accuracy and response speed
            inhibition_accuracy = stop_metrics.get('stop_accuracy', 0)
            
            if 'go_rt' in stop_metrics and stop_metrics['go_rt'] > 0:
                response_speed = 1 / (stop_metrics['go_rt'] / 1000)
                
                # Control efficiency from SSRT
                control_factor = 1.0
                if 'estimated_ssrt' in stop_metrics and stop_metrics['estimated_ssrt'] > 0:
                    control_factor = 1 / (stop_metrics['estimated_ssrt'] / 1000)
                
                params['T_eff'] = inhibition_accuracy * response_speed * control_factor
            else:
                params['T_eff'] = np.nan
        else:
            params['T_eff'] = np.nan
        
        return params
    
    def validate_on_stanford_data(self):
        """Main validation using real Stanford data"""
        
        # Load participants
        participants_file = self.data_path / "participants.tsv"
        participants_df = pd.read_csv(participants_file, sep='\t')
        participants = participants_df['participant_id'].tolist()
        
        print(f"👥 Processing {len(participants)} participants...")
        
        # Process each participant
        results = []
        
        for i, participant_id in enumerate(participants):
            if i % 20 == 0:
                print(f"  Processing {i+1}/{len(participants)}: {participant_id}")
            
            # Extract metrics from each task
            stroop_metrics = self.extract_stroop_metrics(participant_id)
            stop_metrics = self.extract_stop_signal_metrics(participant_id)
            dpx_metrics = self.extract_dpx_metrics(participant_id)
            
            # Compute Information Dynamics parameters
            info_params = self.compute_information_dynamics(stroop_metrics, stop_metrics, dpx_metrics)
            
            # Collect results
            result = {
                'participant_id': participant_id,
                'G_info': info_params['G_info'],
                'L_info': info_params['L_info'], 
                'T_eff': info_params['T_eff']
            }
            
            # Add demographics
            participant_row = participants_df[participants_df['participant_id'] == participant_id]
            if len(participant_row) > 0:
                result['Age'] = participant_row['Age'].iloc[0]
                result['Gender'] = participant_row['Gender'].iloc[0]
            
            # Add task metrics for validation
            if stroop_metrics:
                result.update({f'stroop_{k}': v for k, v in stroop_metrics.items()})
            if stop_metrics:
                result.update({f'stop_{k}': v for k, v in stop_metrics.items()})
            if dpx_metrics:
                result.update({f'dpx_{k}': v for k, v in dpx_metrics.items()})
            
            results.append(result)
        
        # Create results DataFrame
        results_df = pd.DataFrame(results)
        
        # Summary statistics
        print(f"\n📊 VALIDATION RESULTS:")
        print(f"=" * 50)
        print(f"✓ Total participants: {len(results_df)}")
        
        for param in ['G_info', 'L_info', 'T_eff']:
            values = results_df[param].dropna()
            if len(values) > 0:
                print(f"✓ {param}: N={len(values)}, M={values.mean():.3f}, SD={values.std():.3f}")
                print(f"    Range: [{values.min():.3f}, {values.max():.3f}]")
            else:
                print(f"✗ {param}: No valid data")
        
        # Test correlations with age
        print(f"\n🧪 AGE CORRELATIONS:")
        for param in ['G_info', 'L_info', 'T_eff']:
            subset = results_df[[param, 'Age']].dropna()
            if len(subset) > 10:
                corr, p_val = stats.pearsonr(subset[param], subset['Age'])
                sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
                print(f"  {param} ~ Age: r={corr:.3f}, p={p_val:.3f} {sig}")
        
        # Test inter-parameter correlations
        print(f"\n🔗 PARAMETER CORRELATIONS:")
        params = ['G_info', 'L_info', 'T_eff']
        for i, param1 in enumerate(params):
            for param2 in params[i+1:]:
                subset = results_df[[param1, param2]].dropna()
                if len(subset) > 10:
                    corr, p_val = stats.pearsonr(subset[param1], subset[param2])
                    sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
                    print(f"  {param1} ~ {param2}: r={corr:.3f}, p={p_val:.3f} {sig}")
        
        # Save results
        output_path = Path('validation/stanford_real_results.csv')
        output_path.parent.mkdir(exist_ok=True)
        results_df.to_csv(output_path, index=False)
        
        print(f"\n💾 Results saved to: {output_path}")
        print(f"🎉 Real data validation complete!")
        
        return results_df

def main():
    validator = SimpleStanfordValidator()
    results = validator.validate_on_stanford_data()
    return results

if __name__ == "__main__":
    main() 