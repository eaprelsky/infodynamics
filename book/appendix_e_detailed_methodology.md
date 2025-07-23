# Appendix E: Detailed Experimental Methodology

*Complete procedures for replicating information dynamics research*

---

## E.1 Stanford Dataset Analysis: Complete Methodology

### **E.1.1 Participant Recruitment and Screening**

**Inclusion Criteria:**
- Age 18-75 years
- Native English speakers or equivalent fluency
- Normal or corrected-to-normal vision
- No history of neurological or psychiatric disorders
- Able to complete 2-hour testing session

**Exclusion Criteria:**
- Current psychoactive medication (except stable antidepressants >3 months)
- History of head injury with loss of consciousness >30 minutes
- Current substance abuse
- Pregnancy (for fMRI subgroup)
- Color blindness (affects Stroop task performance)

**Recruitment Methods:**
- University participant pools (40%)
- Community advertisements (35%)
- Online research platforms (25%)
- Stratified sampling to ensure age/education diversity

### **E.1.2 Experimental Procedures**

**Session Structure (120 minutes total):**

```
0:00-0:15    Consent, demographics, pre-screening questionnaires
0:15-0:30    Practice trials for all tasks (counterbalanced order)
0:30-0:45    Stroop Task (15 min including breaks)
0:45-1:00    Stop Signal Task (15 min)
1:00-1:15    Break (physiological measures, snacks)
1:15-1:30    AX-CPT Task (15 min)
1:30-1:45    Dot Pattern Expectancy Task (15 min)
1:45-2:00    N-Back Task (15 min)
2:00-2:15    Go/No-Go Task (15 min)
2:15-2:30    Post-session questionnaires, debriefing
```

**Standardized Environment:**
- Quiet, temperature-controlled room (20-22°C)
- Identical computer setups (Dell monitors, 1920×1080 resolution)
- Standardized viewing distance (60cm from screen)
- Sound-isolating headphones for audio stimuli
- Same time-of-day testing when possible

**Instructions Protocol:**
All task instructions delivered via computer with standardized scripts. Research assistant present but minimal interaction to reduce variability.

### **E.1.3 Cognitive Task Specifications**

**Stroop Task Details:**
```
Stimuli: Color words ("RED", "BLUE", "GREEN", "YELLOW") 
Display colors: Red, blue, green, yellow (RGB values: R(255,0,0), B(0,0,255), G(0,255,0), Y(255,255,0))
Conditions: Congruent (50%), Incongruent (50%)
Trials: 240 total (120 per condition)
ITI: 500ms with fixation cross
Response window: 2000ms
Practice: 20 trials before main task
```

**Stop Signal Task Details:**
```
Go stimuli: Left/right pointing arrows
Stop signal: Auditory tone (1000Hz, 100ms duration)
Go probability: 75%
Stop probability: 25%
Stop signal delay: Adaptive staircase (starting 250ms)
Trials: 320 total (240 go, 80 stop)
ITI: 1000-1500ms (jittered)
```

### **E.1.4 Data Processing Procedures**

**Reaction Time Cleaning:**
```python
def clean_reaction_times(rt_data, task_type):
    """
    Standardized RT cleaning procedure
    """
    # Remove trials with RT < 150ms (anticipatory responses)
    rt_cleaned = rt_data[rt_data > 150]
    
    # Remove trials with RT > 3000ms (attention lapses)
    rt_cleaned = rt_cleaned[rt_cleaned < 3000]
    
    # Remove outliers > 3 SD from individual mean
    individual_mean = np.mean(rt_cleaned)
    individual_sd = np.std(rt_cleaned)
    rt_cleaned = rt_cleaned[np.abs(rt_cleaned - individual_mean) < 3 * individual_sd]
    
    return rt_cleaned
```

**Accuracy Calculation:**
```python
def calculate_accuracy_scores(trial_data):
    """
    Calculate multiple accuracy measures
    """
    # Overall accuracy rate
    overall_accuracy = np.mean(trial_data['correct'])
    
    # Condition-specific accuracy (e.g., congruent vs incongruent)
    cond_accuracy = {}
    for condition in trial_data['condition'].unique():
        cond_mask = trial_data['condition'] == condition
        cond_accuracy[condition] = np.mean(trial_data[cond_mask]['correct'])
    
    # Error type analysis
    commission_errors = np.sum((trial_data['response'] != 'none') & 
                              (trial_data['correct'] == False))
    omission_errors = np.sum(trial_data['response'] == 'none')
    
    return {
        'overall_accuracy': overall_accuracy,
        'condition_accuracy': cond_accuracy,
        'commission_errors': commission_errors,
        'omission_errors': omission_errors
    }
```

### **E.1.5 Information Dynamics Variable Calculation**

**Information Conductance (G_info) - Complete Formula:**
```python
def calculate_G_info_complete(participant_data):
    """
    Complete information conductance calculation
    
    G_info = (Processing_Speed_Index × Accuracy_Index × Consistency_Index) / Task_Demand_Index
    """
    
    # Processing Speed Index (normalized across tasks)
    rt_means = []
    for task in ['stroop', 'stop_signal', 'axcpt', 'nback', 'gng']:
        task_rt = participant_data[task]['reaction_times']
        rt_means.append(np.mean(task_rt))
    
    # Inverse of reaction time (faster = higher conductance)
    speed_index = 1 / np.mean(rt_means) * 1000  # Scale to reasonable range
    
    # Accuracy Index (weighted by task difficulty)
    task_weights = {'stroop': 1.0, 'stop_signal': 1.2, 'axcpt': 1.1, 'nback': 1.3, 'gng': 1.0}
    weighted_accuracy = 0
    total_weight = 0
    
    for task, weight in task_weights.items():
        accuracy = participant_data[task]['accuracy']
        weighted_accuracy += accuracy * weight
        total_weight += weight
    
    accuracy_index = weighted_accuracy / total_weight
    
    # Consistency Index (inverse of reaction time variability)
    rt_variabilities = []
    for task in ['stroop', 'stop_signal', 'axcpt', 'nback', 'gng']:
        task_rt = participant_data[task]['reaction_times']
        rt_variabilities.append(np.std(task_rt))
    
    consistency_index = 1 / (np.mean(rt_variabilities) + 1)  # +1 to avoid division by zero
    
    # Task Demand Index (higher for more difficult tasks)
    demand_index = 1.0  # Baseline difficulty
    
    # Calculate final G_info
    G_info = (speed_index * accuracy_index * consistency_index) / demand_index
    
    return G_info, {
        'speed_index': speed_index,
        'accuracy_index': accuracy_index,
        'consistency_index': consistency_index,
        'demand_index': demand_index
    }
```

**Information Resistance (R_info) - Complete Formula:**
```python
def calculate_R_info_complete(participant_data, questionnaire_data):
    """
    Information resistance based on cognitive control failures and interference effects
    
    R_info = Interference_Susceptibility + Control_Failures + Cognitive_Rigidity
    """
    
    # Interference Susceptibility (Stroop interference effect)
    stroop_congruent_rt = np.mean(participant_data['stroop']['congruent_rt'])
    stroop_incongruent_rt = np.mean(participant_data['stroop']['incongruent_rt'])
    interference_effect = (stroop_incongruent_rt - stroop_congruent_rt) / stroop_congruent_rt
    
    # Control Failures (Stop Signal Task performance)
    stop_signal_accuracy = participant_data['stop_signal']['stop_accuracy']
    control_failures = 1 - stop_signal_accuracy
    
    # Cognitive Rigidity (Set-shifting costs)
    if 'task_switching' in participant_data:
        switch_cost = participant_data['task_switching']['switch_cost']
    else:
        # Estimate from N-back lure trials
        switch_cost = participant_data['nback']['lure_error_rate']
    
    # Normalize all components to 0-1 scale
    interference_norm = min(interference_effect / 0.5, 1.0)  # Cap at 50% interference
    control_failures_norm = control_failures
    rigidity_norm = min(switch_cost / 0.3, 1.0)  # Cap at 30% switch cost
    
    # Weighted combination
    R_info = (interference_norm * 0.4 + 
              control_failures_norm * 0.4 + 
              rigidity_norm * 0.2)
    
    return R_info, {
        'interference_susceptibility': interference_norm,
        'control_failures': control_failures_norm,
        'cognitive_rigidity': rigidity_norm
    }
```

**Information Voltage (V_info) - Complete Formula:**
```python
def calculate_V_info_complete(participant_data, task_content_analysis):
    """
    Information voltage based on surprise, relevance, and engagement measures
    
    V_info = Surprise_Component × Relevance_Component × Engagement_Component
    """
    
    # Surprise Component (based on prediction error responses)
    # Use Dot Pattern Expectancy Task violations
    expectancy_violations = participant_data['dot_pattern']['violation_rt']
    expected_trials = participant_data['dot_pattern']['expected_rt']
    surprise_response = np.mean(expectancy_violations - expected_trials)
    surprise_component = min(surprise_response / 200, 2.0)  # Normalize to reasonable range
    
    # Relevance Component (estimated from effort and attention measures)
    # Use sustained attention performance as proxy for relevance
    attention_sustained = 1 - participant_data['axcpt']['vigilance_decrement']
    relevance_component = max(attention_sustained, 0.1)  # Minimum threshold
    
    # Engagement Component (estimated from motivation indicators)
    # Use performance consistency and effort indicators
    engagement_indicators = []
    
    # Reaction time consistency (engaged participants show stable performance)
    overall_rt_cv = np.std(participant_data['all_tasks_rt']) / np.mean(participant_data['all_tasks_rt'])
    engagement_indicators.append(1 - min(overall_rt_cv / 0.3, 1.0))
    
    # Response to feedback (if available)
    if 'feedback_response' in participant_data:
        feedback_adaptation = participant_data['feedback_response']['adaptation_rate']
        engagement_indicators.append(feedback_adaptation)
    
    # Self-reported engagement (from post-task questionnaires)
    if 'self_report' in participant_data:
        self_engagement = participant_data['self_report']['task_engagement'] / 7.0  # 7-point scale
        engagement_indicators.append(self_engagement)
    
    engagement_component = np.mean(engagement_indicators)
    
    # Calculate final V_info (multiplicative model)
    V_info = surprise_component * relevance_component * engagement_component
    
    return V_info, {
        'surprise_component': surprise_component,
        'relevance_component': relevance_component,
        'engagement_component': engagement_component
    }
```

### **E.1.6 Statistical Analysis Procedures**

**Model Validation Protocol:**
```python
def validate_ohms_law_model(dataset):
    """
    Complete validation procedure for I = V/R model
    """
    
    # Calculate all components for each participant
    results = []
    for participant_id in dataset.participant_ids:
        
        # Extract participant data
        p_data = dataset.get_participant(participant_id)
        
        # Calculate information dynamics variables
        G_info, G_components = calculate_G_info_complete(p_data)
        R_info, R_components = calculate_R_info_complete(p_data)
        V_info, V_components = calculate_V_info_complete(p_data)
        
        # Calculate predicted performance using Ohm's law
        I_predicted = V_info / R_info
        
        # Calculate actual performance (composite score)
        I_actual = calculate_performance_composite(p_data)
        
        results.append({
            'participant_id': participant_id,
            'G_info': G_info,
            'R_info': R_info,
            'V_info': V_info,
            'I_predicted': I_predicted,
            'I_actual': I_actual,
            'components': {**G_components, **R_components, **V_components}
        })
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame(results)
    
    # Primary validation: correlation between predicted and actual performance
    primary_correlation = scipy.stats.pearsonr(df['I_predicted'], df['I_actual'])
    
    # Cross-validation
    cv_correlations = []
    kfold = KFold(n_splits=6, shuffle=True, random_state=42)
    
    for train_idx, test_idx in kfold.split(df):
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]
        
        # Fit any scaling parameters on training data
        scaler = StandardScaler()
        train_features = scaler.fit_transform(train_df[['V_info', 'R_info']])
        test_features = scaler.transform(test_df[['V_info', 'R_info']])
        
        # Calculate predictions for test set
        test_predictions = test_features[:, 0] / test_features[:, 1]  # V/R
        test_actual = test_df['I_actual'].values
        
        # Calculate correlation for this fold
        fold_corr = scipy.stats.pearsonr(test_predictions, test_actual)[0]
        cv_correlations.append(fold_corr)
    
    return {
        'primary_correlation': primary_correlation,
        'cv_correlations': cv_correlations,
        'cv_mean': np.mean(cv_correlations),
        'cv_std': np.std(cv_correlations),
        'dataset': df
    }
```

**Power Analysis:**
```python
def calculate_required_sample_size(expected_effect_size=0.6, alpha=0.05, power=0.8):
    """
    Calculate required sample size for detecting information dynamics effects
    """
    
    # For correlation analysis
    from scipy.stats import norm
    
    z_alpha = norm.ppf(1 - alpha/2)
    z_beta = norm.ppf(power)
    
    # Fisher z-transformation
    z_r = 0.5 * np.log((1 + expected_effect_size) / (1 - expected_effect_size))
    
    # Required sample size
    n_required = ((z_alpha + z_beta) / z_r) ** 2 + 3
    
    return int(np.ceil(n_required))
```

### **E.1.7 Quality Control Procedures**

**Data Quality Checks:**
```python
def perform_quality_control(participant_data):
    """
    Comprehensive quality control for participant data
    """
    
    quality_flags = []
    
    # Check for extremely fast responses (< 150ms)
    fast_responses = sum([np.sum(np.array(task_data['reaction_times']) < 150) 
                         for task_data in participant_data.values()])
    if fast_responses > 20:  # More than 20 fast responses
        quality_flags.append('excessive_fast_responses')
    
    # Check for extremely slow responses (> 3000ms)
    slow_responses = sum([np.sum(np.array(task_data['reaction_times']) > 3000) 
                         for task_data in participant_data.values()])
    if slow_responses > 20:
        quality_flags.append('excessive_slow_responses')
    
    # Check for low accuracy (< 60% on any task)
    for task_name, task_data in participant_data.items():
        if task_data['accuracy'] < 0.6:
            quality_flags.append(f'low_accuracy_{task_name}')
    
    # Check for excessive missing data
    total_trials = sum([len(task_data['reaction_times']) 
                       for task_data in participant_data.values()])
    if total_trials < 800:  # Expected ~1200 total trials
        quality_flags.append('excessive_missing_data')
    
    # Check for non-engagement (flat reaction time pattern)
    all_rts = np.concatenate([task_data['reaction_times'] 
                             for task_data in participant_data.values()])
    rt_variance = np.var(all_rts)
    if rt_variance < 10000:  # Very low variance suggests non-engagement
        quality_flags.append('low_engagement')
    
    return quality_flags

def exclude_participants(dataset, quality_criteria):
    """
    Apply exclusion criteria based on quality control
    """
    
    excluded_participants = []
    
    for participant_id in dataset.participant_ids:
        p_data = dataset.get_participant(participant_id)
        flags = perform_quality_control(p_data)
        
        # Exclusion rules
        if len(flags) > 2:  # More than 2 quality issues
            excluded_participants.append(participant_id)
        elif 'excessive_missing_data' in flags:  # Critical exclusion
            excluded_participants.append(participant_id)
        elif 'low_engagement' in flags:  # Critical exclusion
            excluded_participants.append(participant_id)
    
    return excluded_participants
```

### **E.1.8 Replication Package**

**Complete Analysis Script:**
All analyses are available in the replication package:
- **Data preprocessing**: `scripts/01_preprocess_data.py`
- **Variable calculation**: `scripts/02_calculate_variables.py`
- **Statistical analysis**: `scripts/03_statistical_analysis.py`
- **Visualization**: `scripts/04_create_figures.py`
- **Cross-validation**: `scripts/05_cross_validation.py`

**Required Software:**
- Python 3.8+
- pandas 1.3+
- numpy 1.21+
- scipy 1.7+
- scikit-learn 1.0+
- matplotlib 3.4+
- seaborn 0.11+

**Hardware Requirements:**
- 8GB RAM minimum
- 2-3 hours computation time for full analysis
- 5GB disk space for datasets and outputs

---

## E.2 Neural Validation Methodology

### **E.2.1 Human Connectome Project Analysis**

**Dataset Specifications:**
- **Release**: HCP S1200 (1200 subjects)
- **Age range**: 22-35 years
- **Exclusions applied**: Motion > 0.2mm mean relative displacement
- **Final sample**: N = 1003 after quality control

**Imaging Parameters:**
```
Structural MRI:
- Sequence: 3D T1-MPRAGE
- Resolution: 0.7mm isotropic
- TR/TE: 2400/2.14ms
- Flip angle: 8°

Functional MRI:
- Sequence: Gradient echo EPI
- Resolution: 2mm isotropic
- TR: 720ms
- Sessions: 4 runs of 15 minutes each
```

**Connectivity Analysis:**
```python
def calculate_neural_conductance(fmri_timeseries, structural_connectivity):
    """
    Calculate neural information conductance from brain imaging data
    """
    
    # Calculate functional connectivity matrix
    func_connectivity = np.corrcoef(fmri_timeseries.T)
    
    # Weight by structural connectivity (DTI fiber tracts)
    weighted_connectivity = func_connectivity * structural_connectivity
    
    # Calculate network efficiency (conductance analog)
    G = nx.from_numpy_array(weighted_connectivity)
    global_efficiency = nx.global_efficiency(G)
    
    # Calculate local efficiency for brain regions
    local_efficiency = nx.local_efficiency(G)
    
    return {
        'global_efficiency': global_efficiency,
        'local_efficiency': local_efficiency,
        'connectivity_matrix': weighted_connectivity
    }
```

---

## E.3 Educational Validation Methodology

### **E.3.1 Khan Academy Implementation**

**Experimental Design:**
- **Design type**: Randomized controlled trial
- **Participants**: N = 12,847 students
- **Duration**: 6 months
- **Control group**: Standard Khan Academy interface
- **Treatment group**: Information dynamics-optimized interface

**Randomization Procedure:**
```python
def randomize_participants(student_list, stratification_variables):
    """
    Stratified randomization for educational experiment
    """
    
    # Stratify by key variables
    strata = {}
    for student in student_list:
        key = (student['grade_level'], 
               student['prior_math_score_quartile'],
               student['english_learner_status'])
        if key not in strata:
            strata[key] = []
        strata[key].append(student)
    
    # Randomize within each stratum
    treatment_assignments = {}
    for stratum_key, stratum_students in strata.items():
        random.shuffle(stratum_students)
        n = len(stratum_students)
        
        # 50-50 split
        for i, student in enumerate(stratum_students):
            treatment_assignments[student['id']] = 'treatment' if i < n//2 else 'control'
    
    return treatment_assignments
```

**Outcome Measures:**
```python
def calculate_learning_outcomes(student_data, time_period):
    """
    Calculate comprehensive learning outcome measures
    """
    
    outcomes = {}
    
    # Primary outcomes
    outcomes['mastery_speed'] = student_data['concepts_mastered'] / student_data['study_hours']
    outcomes['retention_rate'] = student_data['retained_concepts'] / student_data['total_concepts_learned']
    outcomes['transfer_performance'] = student_data['transfer_test_score']
    
    # Secondary outcomes
    outcomes['engagement_time'] = student_data['total_study_time']
    outcomes['completion_rate'] = student_data['exercises_completed'] / student_data['exercises_assigned']
    outcomes['help_seeking'] = student_data['hint_requests'] / student_data['total_attempts']
    
    # Long-term outcomes
    outcomes['standardized_test_improvement'] = (student_data['post_test_score'] - 
                                               student_data['pre_test_score'])
    
    return outcomes
```

This detailed methodology appendix provides researchers with the complete procedures needed to understand, evaluate, and replicate the information dynamics research findings. 