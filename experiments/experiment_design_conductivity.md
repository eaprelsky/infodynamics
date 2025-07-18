# Экспериментальный дизайн: Валидация модели информационной проводимости
## Задача 3.1.1: Научно обоснованный протокол тестирования

**Дата разработки:** Январь 2025  
**Статус:** 🔬 В РАЗРАБОТКЕ  
**Основа:** Formal_model_conductivity.md + методологии Broadbent, Treisman, Posner

---

## 🎯 Цель исследования

Эмпирически валидировать математическую модель информационной проводимости:
```
G_info = k_ind × Relevance × (1 - Cognitive_Distance) × Attention_Focus × (1 - Cognitive_Load_Ratio)
```

### Основные гипотезы:
1. **H1:** G_info ∝ Personal_Relevance (r > 0.6)
2. **H2:** G_info ∝ 1/Cognitive_Load (r < -0.5)  
3. **H3:** G_info ∝ Attention_Focus (r > 0.7)
4. **H4:** Существует пороговый эффект при high emotional_charge

---

## 📊 Экспериментальный дизайн

### Общий подход: Mixed-methods factorial design
- **Within-subjects** для cognitive load manipulation
- **Between-subjects** для personality factors
- **Repeated measures** для reliability

### Участники:
- **N = 120** (power analysis: effect size d=0.5, α=0.05, power=0.8)
- Возраст: 18-35 лет (контроль нейропластичности)
- Исключения: ADHD, дислексия, нарушения внимания
- Балансировка по полу и образованию

---

## 🧪 Экспериментальные манипуляции

### 1. BASELINE ИЗМЕРЕНИЯ (30 мин)

#### A. Индивидуальные характеристики:
```python
# Измерительные инструменты:
personality_profile = {
    "big_five": NEO_PI_R_questionnaire(),  # Openness to Experience для k_ind
    "working_memory": n_back_task(levels=[2,3,4]),  # Capacity measurement  
    "processing_speed": symbol_digit_modalities_test(),
    "attention_control": attention_network_test()  # Posner ANT
}
```

#### B. Когнитивные способности:
- **Working Memory Capacity:** Automated Operation Span Task (Unsworth et al., 2005)
- **Attention Control:** Attention Network Test (Fan et al., 2002)
- **Processing Speed:** WAIS-IV Symbol Search + Coding

### 2. ОСНОВНОЙ ЭКСПЕРИМЕНТ (45 мин)

#### Дизайн: 3×3×2 factorial within-subjects
- **Factor 1:** Cognitive Load (Low/Medium/High)
- **Factor 2:** Personal Relevance (Low/Medium/High)  
- **Factor 3:** Emotional Charge (Neutral/High)

#### Процедура:

**Phase 1: Cognitive Load Manipulation**
```python
cognitive_load_conditions = {
    "low": {
        "primary_task": "simple_categorization",  # 2 categories
        "secondary_task": None,
        "target_accuracy": 0.95
    },
    "medium": {
        "primary_task": "complex_categorization",  # 4 categories
        "secondary_task": "digit_monitoring",  # Dual-task
        "target_accuracy": 0.85
    },
    "high": {
        "primary_task": "working_memory_updating",  # N-back
        "secondary_task": "visual_tracking",
        "target_accuracy": 0.75
    }
}
```

**Phase 2: Information Processing Task**
```python
information_stimuli = {
    "content_types": [
        "news_articles",      # 200-300 words
        "social_posts",       # 50-100 words  
        "academic_abstracts", # 150-250 words
        "advertisements"      # 30-50 words
    ],
    "relevance_manipulation": {
        "high": "participant_major/interests",
        "medium": "general_knowledge_topics", 
        "low": "unrelated_specialized_topics"
    },
    "emotional_manipulation": {
        "neutral": "factual_content",
        "high": "emotional_language + images"
    }
}
```

---

## 📏 Зависимые переменные (Operationalization)

### 1. ИНФОРМАЦИОННАЯ ПРОВОДИМОСТЬ (G_info)

#### A. Behavioral Measures:
```python
conductivity_metrics = {
    "processing_speed": {
        "reading_time": "time_to_complete_comprehension",
        "decision_time": "relevance_judgment_latency",
        "response_time": "categorization_speed"
    },
    "information_flow": {
        "recall_accuracy": "free_recall_percentage", 
        "recognition_hits": "signal_detection_d_prime",
        "transfer_efficiency": "analogical_reasoning_success"
    },
    "spreading_activation": {
        "semantic_priming": "related_concept_activation",
        "associative_breadth": "semantic_fluency_task",
        "integration_speed": "concept_mapping_time"
    }
}
```

#### B. Physiological Measures:
```python
physiological_indicators = {
    "eye_tracking": {
        "fixation_duration": "attention_allocation",
        "saccade_velocity": "cognitive_effort", 
        "pupil_dilation": "cognitive_load_index"
    },
    "eeg": {
        "p300_amplitude": "attention_engagement",
        "n400": "semantic_processing_effort",
        "alpha_suppression": "cognitive_activation"
    },
    "autonomic": {
        "heart_rate_variability": "cognitive_stress",
        "skin_conductance": "emotional_arousal"
    }
}
```

### 2. CONTROL MEASURES

#### Attention Focus (Treisman model):
- **Dichotic listening task** с target detection
- **Visual attention paradigm** с cued attention
- **Sustained attention response task** (SART)

#### Cognitive Load (Sweller CLT):
- **Subjective rating:** NASA-TLX scale
- **Physiological:** Pupil dilation, HRV  
- **Performance:** Dual-task accuracy

---

## 📈 Аналитический план

### 1. DESCRIPTIVE ANALYSIS
```python
# Проверка assumptions
normality_tests = ["shapiro_wilk", "kolmogorov_smirnov"]
outlier_detection = "modified_z_score > 3.5"
reliability_analysis = "cronbach_alpha > 0.7"
```

### 2. CONFIRMATORY ANALYSIS

#### Model Testing:
```python
# Основная модель регрессии
model_formula = """
G_info ~ k_individual * Personal_Relevance * (1 - Cognitive_Distance) * 
         Attention_Focus * (1 - Cognitive_Load_Ratio) + 
         random_effects(participant_id)
"""

# Hierarchical Linear Modeling (HLM)
hlm_structure = {
    "level_1": "within_subject_trials",
    "level_2": "between_subject_differences", 
    "random_effects": ["intercept", "cognitive_load_slope"]
}
```

#### Statistical Tests:
1. **Correlation Analysis:** Pearson/Spearman для основных предсказаний
2. **Multiple Regression:** Stepwise для model building
3. **Mixed-Effects ANOVA:** Repeated measures design
4. **Structural Equation Modeling:** Path analysis

### 3. EXPLORATORY ANALYSIS

#### Non-linear Effects:
```python
# Threshold detection
threshold_analysis = {
    "cognitive_load_threshold": "piecewise_regression",
    "emotional_saturation": "polynomial_fitting",
    "attention_switching_costs": "change_point_detection"
}
```

#### Individual Differences:
```python
# Clustering analysis
individual_profiles = {
    "high_conductivity": "openness + low_cognitive_load_sensitivity",
    "low_conductivity": "conscientiousness + high_load_sensitivity", 
    "variable_conductivity": "emotional_reactivity + context_dependence"
}
```

---

## ⚡ Экспериментальные предсказания

### 1. ОСНОВНЫЕ ЭФФЕКТЫ

| Предсказание | Операционализация | Ожидаемый эффект |
|-------------|------------------|------------------|
| **H1:** G ∝ Relevance | Recall accuracy vs. personal relevance rating | r > 0.6, p < 0.001 |
| **H2:** G ∝ 1/Load | Processing speed vs. dual-task accuracy | r < -0.5, p < 0.001 |  
| **H3:** G ∝ Focus | Information transfer vs. attention control | r > 0.7, p < 0.001 |
| **H4:** Threshold | Emotional content processing efficiency | Non-linear relationship |

### 2. INTERACTION EFFECTS

```python
interaction_predictions = {
    "load_x_relevance": {
        "high_load": "relevance_effect_reduced_by_50%",
        "low_load": "full_relevance_effect",
        "statistical_test": "2x3_interaction_p < 0.05"
    },
    "personality_x_emotional": {
        "high_openness": "stronger_emotional_conductivity",
        "low_openness": "weaker_emotional_effects", 
        "effect_size": "cohen_d > 0.5"
    }
}
```

### 3. PHYSIOLOGICAL CORRELATES

| Measure | Prediction | Validation |
|---------|------------|------------|
| **Pupil Dilation** | ∝ 1/G_info | r < -0.4 |
| **P300 Amplitude** | ∝ G_info | r > 0.5 |
| **Fixation Duration** | ∝ 1/G_info | r < -0.3 |
| **Alpha Suppression** | ∝ G_info | r > 0.4 |

---

## 🔄 Pilot Study Protocol

### Phase 0: Mini-experiment (N=20, 2 недели)

#### Goals:
1. Проверить feasibility процедур
2. Estimate effect sizes для power analysis
3. Refine stimulus materials
4. Test technical setup

#### Procedure:
```python
pilot_design = {
    "duration": "60_minutes_per_participant",
    "conditions": "2x2_reduced_design",  # Load × Relevance
    "measures": ["behavioral_only", "eye_tracking"],
    "analysis": "exploratory_correlation_analysis"
}
```

---

## 📋 Materials & Equipment

### Software:
- **E-Prime 3.0** - экспериментальное управление
- **Tobii Eye Tracker** - eye movement recording  
- **MATLAB + Psychtoolbox** - stimulus presentation
- **R + lavaan** - статистический анализ

### Stimuli Database:
```python
stimulus_materials = {
    "text_corpus": {
        "sources": ["wikipedia", "news_apis", "academic_databases"],
        "preprocessing": ["readability_control", "emotional_valence_rating"],
        "validation": "pilot_relevance_ratings"
    },
    "individual_profiling": {
        "interests_survey": "detailed_academic_career_interests",
        "personality_assessment": "NEO_PI_R + additional_scales",
        "cognitive_testing": "standardized_battery"
    }
}
```

---

## 🎯 Expected Outcomes

### Primary Results:
1. **Validated mathematical model** G_info с empirically derived parameters
2. **Effect size estimates** для всех key relationships
3. **Individual difference profiles** для personalization
4. **Physiological signatures** информационной проводимости

### Scientific Impact:
- **Theoretical:** Bridge между cognitive psychology и information theory
- **Methodological:** Новые measurement approaches для information processing
- **Applied:** Practical guidelines для UX design, education, social media

### Practical Applications:
```python
applications = {
    "educational_technology": "adaptive_content_difficulty",
    "user_interface_design": "cognitive_load_optimization", 
    "social_media_algorithms": "engagement_prediction",
    "information_design": "optimal_presentation_formats"
}
```

---

## ⏰ Timeline & Resources

### Schedule (8 недель):
- **Week 1-2:** Pilot study + refinements
- **Week 3-4:** Main data collection (N=120)
- **Week 5-6:** Data analysis + model fitting
- **Week 7-8:** Validation + replication mini-study

### Budget estimate:
- Participant compensation: $3,600 ($30 × 120)
- Equipment rental: $2,000 
- Software licenses: $1,500
- **Total:** ~$7,100

---

## 📊 Data Management Plan

### Data Collection:
```python
data_structure = {
    "participant_level": {
        "demographics": "age, gender, education, native_language",
        "personality": "big_five_scores + cognitive_abilities",
        "baseline_performance": "attention_working_memory_tests"
    },
    "trial_level": {
        "experimental_conditions": "load_relevance_emotional_factors",
        "behavioral_responses": "rt_accuracy_confidence_ratings",
        "physiological_data": "eye_tracking_eeg_autonomic"
    }
}
```

### Analysis Pipeline:
1. **Preprocessing:** Outlier removal, normalization, missing data handling
2. **Model fitting:** Hierarchical linear models with random effects
3. **Validation:** Cross-validation, bootstrap confidence intervals  
4. **Replication:** Independent validation sample (N=40)

---

**Статус:** ✅ **ЗАДАЧА 3.1.1 ЗАВЕРШЕНА**

**Основные достижения:**
- Создан comprehensive экспериментальный дизайн на основе классических методологий attention research
- Операционализированы все компоненты математической модели G_info
- Интегрированы behavioral, physiological, и individual difference measures
- Разработан статистический план для валидации теоретических предсказаний
- Предусмотрен pilot study для refinement процедур
- Определены четкие критерии успеха и practical applications

**Готовность к реализации:** 🚀 ВЫСОКАЯ 