# Модель информационной емкости
## Задача 2.1.3 - Формализовать понятие "информационной емкости"

**Дата создания:** Январь 2025  
**Статус:** ✅ ЗАВЕРШЕНО  
**Базируется на:** Working Memory Research (Miller, Baddeley), Cognitive Overload теории

---

## 🎯 Цель

Создать формальную математическую модель информационной емкости (C_info), описывающую способность когнитивных агентов накапливать, хранить и организовывать информацию по аналогии с электрическими конденсаторами.

---

## ⚡ Электротехническая аналогия

### Электрический конденсатор
В электротехнике конденсатор накапливает энергию в электрическом поле:

```
C = Q/V (емкость = заряд/напряжение)
E = ½CV² (накопленная энергия)
I = C × dV/dt (ток заряда/разряда)
X_C = 1/(ωC) (емкостное реактивное сопротивление)
```

**Свойства:**
- Накапливает заряд при подаче напряжения
- Сопротивляется изменению напряжения
- Создает фазовый сдвиг (-90° для идеального конденсатора)
- Высокое сопротивление на низких частотах, низкое - на высоких

### Информационный конденсатор
Аналогично накапливает информацию при подаче информационного напряжения:

```
C_info = Q_info/U_info (информационная емкость)
E_info = ½C_info×U_info² (накопленные знания)
I_info = C_info × dU_info/dt (скорость накопления/забывания)
X_C_info = 1/(ωC_info) (сопротивление изменению знаний)
```

---

## 🧠 Когнитивные основы информационной емкости

### 1. Working Memory Model (Baddeley, 2000)

**Компоненты рабочей памяти:**
- **Central Executive**: Контролирующая система, управление вниманием
- **Phonological Loop**: Вербальная и акустическая информация (~2 сек)
- **Visuospatial Sketchpad**: Визуально-пространственная информация (~4 элемента)
- **Episodic Buffer**: Интеграция информации из разных источников (~4 chunks)

**Ограничения емкости:**
```python
class WorkingMemoryCapacity:
    """Модель емкости рабочей памяти по Baddeley"""
    
    def __init__(self, individual_differences: Dict[str, float]):
        # Базовые емкости (Miller 7±2, Cowan ~4)
        self.phonological_capacity = individual_differences.get('verbal_span', 7) # chunks
        self.visuospatial_capacity = individual_differences.get('visual_span', 4) # elements
        self.episodic_buffer_capacity = individual_differences.get('integration_span', 4) # bindings
        self.executive_efficiency = individual_differences.get('executive_control', 1.0) # multiplier
    
    def total_capacity(self, task_type: str) -> float:
        """Общая емкость в зависимости от типа задачи"""
        if task_type == 'verbal':
            return self.phonological_capacity * self.executive_efficiency
        elif task_type == 'visual':
            return self.visuospatial_capacity * self.executive_efficiency
        elif task_type == 'complex':
            return min(
                self.phonological_capacity, 
                self.visuospatial_capacity,
                self.episodic_buffer_capacity
            ) * self.executive_efficiency
        else:
            return (self.phonological_capacity + self.visuospatial_capacity) / 2 * self.executive_efficiency
```

### 2. Long-Term Memory Capacity

**Типы долговременной памяти:**
- **Declarative Memory**: Факты и события (~10¹⁵ bits теоретически)
- **Procedural Memory**: Навыки и привычки
- **Semantic Memory**: Концептуальные знания и значения

**Факторы, влияющие на емкость:**
```python
def calculate_ltm_capacity(
    age: float,
    education_years: float,
    domain_expertise: float,
    general_intelligence: float,
    health_factors: float = 1.0
) -> float:
    """
    Оценка емкости долговременной памяти
    """
    # Базовая емкость (нормализованная)
    base_capacity = 1.0
    
    # Возрастные изменения (пик в 25-30 лет)
    if age <= 30:
        age_factor = 0.8 + 0.4 * (age / 30)
    else:
        age_factor = 1.2 - 0.01 * (age - 30)  # Постепенное снижение
    
    # Образовательный фактор
    education_factor = 1.0 + 0.05 * education_years
    
    # Экспертиза в домене
    expertise_factor = 1.0 + 2.0 * domain_expertise  # Экспоненциальный рост
    
    # Общий интеллект
    intelligence_factor = 0.5 + 0.5 * general_intelligence
    
    total_capacity = (
        base_capacity * 
        age_factor * 
        education_factor * 
        expertise_factor * 
        intelligence_factor * 
        health_factors
    )
    
    return max(0.1, total_capacity)
```

### 3. Motivation and Learning Drive

**Влияние мотивации на емкость:**
```python
class MotivationalCapacityModulation:
    """Модуляция емкости через мотивационные факторы"""
    
    def __init__(self):
        self.intrinsic_motivation_weight = 0.4
        self.extrinsic_motivation_weight = 0.3
        self.curiosity_weight = 0.2
        self.relevance_weight = 0.1
    
    def calculate_motivation_multiplier(
        self,
        intrinsic_interest: float,        # [0,1] внутренний интерес
        external_rewards: float,          # [0,1] внешние стимулы
        curiosity_level: float,           # [0,1] любознательность
        personal_relevance: float         # [0,1] личная релевантность
    ) -> float:
        """
        Мотивационный множитель емкости
        """
        motivation_score = (
            self.intrinsic_motivation_weight * intrinsic_interest +
            self.extrinsic_motivation_weight * external_rewards +
            self.curiosity_weight * curiosity_level +
            self.relevance_weight * personal_relevance
        )
        
        # Нелинейная функция активации (sigmoid)
        motivation_multiplier = 1 / (1 + np.exp(-5 * (motivation_score - 0.5)))
        
        return 0.5 + 1.5 * motivation_multiplier  # Диапазон [0.5, 2.0]
```

---

## 🧮 Математическая модель информационной емкости

### Базовая формула:
```
C_info = C_base × Memory_Factor × Motivation_Factor × Organization_Factor

где:
C_base = базовая когнитивная емкость индивида
Memory_Factor = f(WM_capacity, LTM_capacity, age, health)
Motivation_Factor = f(interest, relevance, curiosity, rewards)
Organization_Factor = f(categorization_skills, schema_strength, retrieval_efficiency)
```

### Детализированная модель:
```python
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class CognitiveProfile:
    """Когнитивный профиль индивида"""
    working_memory_span: float      # 2-12 chunks
    processing_speed: float         # 0.5-2.0 relative
    general_intelligence: float     # 0.5-2.0 relative  
    age: float                     # years
    education_years: float         # years
    domain_expertise: float        # 0-1 normalized
    health_status: float           # 0-1 normalized

@dataclass  
class MotivationalProfile:
    """Мотивационный профиль"""
    intrinsic_interest: float      # 0-1
    external_motivation: float     # 0-1
    curiosity_drive: float         # 0-1
    personal_relevance: float      # 0-1
    goal_orientation: float        # 0-1

@dataclass
class OrganizationalProfile:
    """Профиль организационных способностей"""
    categorization_skill: float    # 0-1
    pattern_recognition: float     # 0-1
    schema_strength: float         # 0-1
    retrieval_efficiency: float    # 0-1
    knowledge_integration: float   # 0-1

class InformationCapacityModel:
    """Полная модель информационной емкости"""
    
    def __init__(self):
        self.base_capacity = 7.0  # Miller's magic number
        
    def calculate_memory_factor(self, cognitive: CognitiveProfile) -> float:
        """Фактор памяти на основе когнитивных способностей"""
        
        # Working Memory component
        wm_normalized = cognitive.working_memory_span / 7.0  # Нормализация к Miller
        wm_factor = 0.8 + 0.4 * wm_normalized  # [0.8, 1.2]
        
        # Processing Speed component  
        speed_factor = 0.7 + 0.6 * cognitive.processing_speed  # [0.7, 1.9]
        
        # General Intelligence component
        g_factor = 0.6 + 0.8 * cognitive.general_intelligence  # [0.6, 1.4]
        
        # Age-related changes
        if cognitive.age <= 25:
            age_factor = 0.9 + 0.2 * (cognitive.age / 25)  # Развитие до пика
        elif cognitive.age <= 60:
            age_factor = 1.1 - 0.1 * ((cognitive.age - 25) / 35)  # Стабильность
        else:
            age_factor = 1.0 - 0.02 * (cognitive.age - 60)  # Постепенное снижение
        
        # Education multiplier
        education_factor = 1.0 + 0.03 * cognitive.education_years
        
        # Domain expertise (экспоненциальный эффект)
        expertise_factor = 1.0 + 3.0 * (cognitive.domain_expertise ** 2)
        
        # Health impact
        health_factor = 0.5 + 0.5 * cognitive.health_status
        
        memory_factor = (
            wm_factor * speed_factor * g_factor * 
            age_factor * education_factor * expertise_factor * health_factor
        ) ** 0.5  # Geometric mean для сглаживания
        
        return max(0.2, min(5.0, memory_factor))
    
    def calculate_motivation_factor(self, motivation: MotivationalProfile) -> float:
        """Мотивационный фактор емкости"""
        
        # Weighted combination of motivational components
        motivation_score = (
            0.4 * motivation.intrinsic_interest +
            0.2 * motivation.external_motivation +
            0.2 * motivation.curiosity_drive +
            0.15 * motivation.personal_relevance +
            0.05 * motivation.goal_orientation
        )
        
        # Sigmoid activation for non-linear effect
        # При низкой мотивации емкость серьезно снижается
        if motivation_score < 0.3:
            motivation_factor = 0.3 + 0.7 * (motivation_score / 0.3)
        else:
            motivation_factor = 1.0 + 1.5 * ((motivation_score - 0.3) / 0.7)
        
        return max(0.1, min(2.5, motivation_factor))
    
    def calculate_organization_factor(self, organization: OrganizationalProfile) -> float:
        """Фактор организационных способностей"""
        
        # Categorization skills - способность структурировать информацию
        categorization_effect = 1.0 + 0.5 * organization.categorization_skill
        
        # Pattern recognition - выявление закономерностей
        pattern_effect = 1.0 + 0.4 * organization.pattern_recognition
        
        # Schema strength - сила концептуальных схем
        schema_effect = 1.0 + 0.6 * organization.schema_strength
        
        # Retrieval efficiency - эффективность извлечения
        retrieval_effect = 1.0 + 0.3 * organization.retrieval_efficiency
        
        # Knowledge integration - интеграция знаний
        integration_effect = 1.0 + 0.7 * organization.knowledge_integration
        
        # Multiplicative model (все факторы важны)
        organization_factor = (
            categorization_effect * pattern_effect * schema_effect * 
            retrieval_effect * integration_effect
        ) ** 0.2  # Geometric mean
        
        return max(0.5, min(3.0, organization_factor))
    
    def calculate_total_capacity(
        self,
        cognitive: CognitiveProfile,
        motivation: MotivationalProfile, 
        organization: OrganizationalProfile,
        context_factors: Dict[str, float] = None
    ) -> Dict[str, float]:
        """
        Расчет общей информационной емкости
        """
        # Базовые факторы
        memory_factor = self.calculate_memory_factor(cognitive)
        motivation_factor = self.calculate_motivation_factor(motivation)
        organization_factor = self.calculate_organization_factor(organization)
        
        # Контекстуальные модификации
        context_multiplier = 1.0
        if context_factors:
            stress_level = context_factors.get('stress', 0.0)
            time_pressure = context_factors.get('time_pressure', 0.0)
            distractions = context_factors.get('distractions', 0.0)
            
            # Стресс снижает емкость нелинейно
            stress_effect = 1.0 - 0.5 * (stress_level ** 2)
            
            # Временное давление
            pressure_effect = 1.0 - 0.3 * time_pressure
            
            # Отвлечения
            distraction_effect = 1.0 - 0.4 * distractions
            
            context_multiplier = stress_effect * pressure_effect * distraction_effect
        
        # Итоговая емкость
        total_capacity = (
            self.base_capacity * 
            memory_factor * 
            motivation_factor * 
            organization_factor * 
            context_multiplier
        )
        
        return {
            'total_capacity': max(0.5, min(50.0, total_capacity)),
            'memory_factor': memory_factor,
            'motivation_factor': motivation_factor,
            'organization_factor': organization_factor,
            'context_multiplier': context_multiplier,
            'base_capacity': self.base_capacity
        }
```

---

## ⚡ Динамические свойства информационной емкости

### 1. Зарядка и разрядка информационного конденсатора

```python
class InformationCapacitor:
    """Модель информационного конденсатора"""
    
    def __init__(self, capacity: float, initial_charge: float = 0):
        self.C_info = capacity
        self.Q_info = initial_charge  # Накопленная информация
        self.U_info = initial_charge / capacity if capacity > 0 else 0
        
    def charge(self, voltage_source: float, resistance: float, time_step: float) -> Dict[str, float]:
        """
        Процесс зарядки информационного конденсатора
        Аналог RC-цепи: V_C(t) = V_source × (1 - e^(-t/RC))
        """
        RC_constant = resistance * self.C_info
        
        # Изменение напряжения на конденсаторе
        dU_dt = (voltage_source - self.U_info) / RC_constant
        self.U_info += dU_dt * time_step
        
        # Обновление заряда
        self.Q_info = self.C_info * self.U_info
        
        # Ток зарядки
        I_charging = (voltage_source - self.U_info) / resistance
        
        return {
            'voltage': self.U_info,
            'charge': self.Q_info,
            'current': I_charging,
            'time_constant': RC_constant,
            'charge_percentage': self.U_info / voltage_source if voltage_source > 0 else 0
        }
    
    def discharge(self, resistance: float, time_step: float) -> Dict[str, float]:
        """
        Процесс разрядки (забывание информации)
        V_C(t) = V_initial × e^(-t/RC)
        """
        RC_constant = resistance * self.C_info
        
        # Экспоненциальная разрядка
        decay_factor = np.exp(-time_step / RC_constant)
        self.U_info *= decay_factor
        self.Q_info = self.C_info * self.U_info
        
        # Ток разрядки
        I_discharge = -self.U_info / resistance
        
        return {
            'voltage': self.U_info,
            'charge': self.Q_info,
            'current': I_discharge,
            'retention_factor': decay_factor
        }
    
    def frequency_response(self, omega: float) -> complex:
        """
        Частотная характеристика информационного конденсатора
        Z_C = 1/(jωC)
        """
        if omega == 0:
            return complex(float('inf'), 0)  # DC блокировка
        else:
            return complex(0, -1 / (omega * self.C_info))
```

### 2. Кривые обучения и забывания

```python
def learning_curve_model(
    learning_sessions: List[Dict], 
    capacity_model: InformationCapacityModel,
    individual_profile: Tuple[CognitiveProfile, MotivationalProfile, OrganizationalProfile]
) -> Dict:
    """
    Модель кривой обучения с учетом информационной емкости
    """
    cognitive, motivation, organization = individual_profile
    
    # Расчет текущей емкости
    capacity_result = capacity_model.calculate_total_capacity(cognitive, motivation, organization)
    total_capacity = capacity_result['total_capacity']
    
    # Информационный конденсатор
    info_capacitor = InformationCapacitor(total_capacity)
    
    learning_progress = []
    cumulative_knowledge = 0
    
    for session in learning_sessions:
        information_voltage = session['content_quality']
        cognitive_resistance = session['difficulty'] / cognitive.processing_speed
        session_duration = session['duration_hours']
        
        # Процесс обучения (зарядка)
        for time_step in np.arange(0, session_duration, 0.1):  # 6-минутные интервалы
            charge_result = info_capacitor.charge(
                voltage_source=information_voltage,
                resistance=cognitive_resistance,
                time_step=0.1
            )
        
        # Межсессионное забывание
        if 'time_between_sessions' in session:
            forget_time = session['time_between_sessions']
            for time_step in np.arange(0, forget_time, 0.5):  # 30-минутные интервалы
                discharge_result = info_capacitor.discharge(
                    resistance=cognitive_resistance * 2,  # Сопротивление забыванию
                    time_step=0.5
                )
        
        learning_progress.append({
            'session': len(learning_progress) + 1,
            'accumulated_knowledge': info_capacitor.Q_info,
            'knowledge_voltage': info_capacitor.U_info,
            'capacity_utilization': info_capacitor.Q_info / total_capacity,
            'learning_efficiency': charge_result.get('charge_percentage', 0)
        })
    
    return {
        'learning_trajectory': learning_progress,
        'final_knowledge_level': info_capacitor.Q_info,
        'capacity_utilization': info_capacitor.Q_info / total_capacity,
        'optimal_capacity': total_capacity
    }

def forgetting_curve_ebbinghaus_extended(
    initial_knowledge: float,
    time_hours: np.ndarray,
    individual_resistance: float,
    rehearsal_schedule: List[float] = None
) -> np.ndarray:
    """
    Расширенная кривая забывания Эббингауза с информационной емкостью
    """
    # Базовая экспоненциальная модель забывания
    base_retention = initial_knowledge * np.exp(-time_hours / (individual_resistance * 24))
    
    # Эффект повторений (rehearsal)
    if rehearsal_schedule:
        retention_with_rehearsal = base_retention.copy()
        for rehearsal_time in rehearsal_schedule:
            # Найти ближайший временной индекс
            time_idx = np.argmin(np.abs(time_hours - rehearsal_time))
            
            # Бустинг памяти от повторения
            boost_factor = 1.5 * np.exp(-(time_hours[time_idx:] - rehearsal_time) / 12)
            retention_with_rehearsal[time_idx:] *= (1 + boost_factor)
        
        return np.minimum(retention_with_rehearsal, initial_knowledge)  # Cap at initial level
    
    return base_retention
```

---

## 🔬 Экспериментальные предсказания

### Предсказание 1: Емкостные эффекты в AC режиме
```python
def test_capacitive_frequency_effects():
    """
    Тест частотной зависимости информационной емкости
    """
    capacity = 5.0  # Информационная емкость
    frequencies = np.logspace(-2, 2, 50)  # 0.01 to 100 Hz
    
    impedances = []
    for freq in frequencies:
        omega = 2 * np.pi * freq
        Z_C = 1 / (1j * omega * capacity)
        impedances.append(abs(Z_C))
    
    # Предсказание: Высокое сопротивление на низких частотах
    assert impedances[0] > impedances[-1] * 100
    
    # Предсказание: Обратная зависимость от частоты
    log_freq = np.log10(frequencies)
    log_impedance = np.log10(impedances)
    slope, _ = np.polyfit(log_freq, log_impedance, 1)
    assert slope < -0.8  # Приближенно -1 для идеального конденсатора
```

### Предсказание 2: RC постоянная времени
```python
def test_information_time_constant():
    """
    Тест постоянной времени информационной RC-цепи
    """
    C_info = 10.0  # Информационная емкость
    R_info = 2.0   # Информационное сопротивление
    tau_expected = R_info * C_info  # 20.0
    
    # Симуляция зарядки
    capacitor = InformationCapacitor(C_info)
    time_steps = np.arange(0, 100, 0.1)
    voltages = []
    
    for t in time_steps:
        result = capacitor.charge(voltage_source=1.0, resistance=R_info, time_step=0.1)
        voltages.append(result['voltage'])
    
    # Найти время достижения 63.2% от максимального значения
    target_voltage = 0.632
    time_63_idx = np.argmin(np.abs(np.array(voltages) - target_voltage))
    tau_measured = time_steps[time_63_idx]
    
    # Предсказание: τ измеренное ≈ τ расчетное
    assert abs(tau_measured - tau_expected) < tau_expected * 0.1
```

### Предсказание 3: Кривая забывания
```python
def test_forgetting_curve_validation():
    """
    Валидация кривой забывания против данных Эббингауза
    """
    # Исторические данные Эббингауза (приблизительные)
    ebbinghaus_data = {
        'time_hours': [0, 1, 9, 24, 48, 144, 720],  # 0h, 1h, 9h, 1d, 2d, 6d, 30d
        'retention': [1.0, 0.56, 0.36, 0.33, 0.28, 0.25, 0.21]
    }
    
    # Наша модель
    time_array = np.array(ebbinghaus_data['time_hours'])
    modeled_retention = forgetting_curve_ebbinghaus_extended(
        initial_knowledge=1.0,
        time_hours=time_array,
        individual_resistance=1.2  # Подбираемый параметр
    )
    
    # Корреляция с историческими данными
    correlation = np.corrcoef(ebbinghaus_data['retention'], modeled_retention)[0,1]
    
    # Предсказание: Высокая корреляция с классическими данными
    assert correlation > 0.9
```

---

## 🎯 Практические применения

### 1. Адаптивные образовательные системы
```python
def adaptive_curriculum_design(
    student_profiles: List[Tuple[CognitiveProfile, MotivationalProfile, OrganizationalProfile]],
    course_material: Dict[str, any],
    learning_objectives: List[str]
) -> Dict[str, any]:
    """
    Дизайн адаптивного курса на основе информационной емкости студентов
    """
    capacity_model = InformationCapacityModel()
    optimized_curriculum = {}
    
    for student_id, (cognitive, motivation, organization) in enumerate(student_profiles):
        # Расчет индивидуальной емкости
        capacity_result = capacity_model.calculate_total_capacity(cognitive, motivation, organization)
        student_capacity = capacity_result['total_capacity']
        
        # Оптимизация объема материала
        max_info_per_session = student_capacity * 0.8  # 80% от максимума
        
        # Расчет оптимального расписания
        material_complexity = course_material['complexity_score']
        cognitive_resistance = material_complexity / cognitive.processing_speed
        
        # RC постоянная для планирования интервалов
        time_constant = cognitive_resistance * student_capacity
        optimal_interval = time_constant * 2.3  # 90% восстановления емкости
        
        optimized_curriculum[f'student_{student_id}'] = {
            'info_per_session': max_info_per_session,
            'session_interval_hours': optimal_interval,
            'total_sessions': len(learning_objectives),
            'personalized_difficulty': material_complexity * (cognitive.processing_speed ** 0.5),
            'motivation_boosters': design_motivation_interventions(motivation)
        }
    
    return optimized_curriculum

def design_motivation_interventions(motivation: MotivationalProfile) -> List[str]:
    """Дизайн мотивационных интервенций"""
    interventions = []
    
    if motivation.intrinsic_interest < 0.5:
        interventions.append("gamification_elements")
        interventions.append("curiosity_gaps")
    
    if motivation.external_motivation < 0.5:
        interventions.append("progress_badges")
        interventions.append("social_recognition")
    
    if motivation.personal_relevance < 0.5:
        interventions.append("real_world_applications")
        interventions.append("career_connections")
    
    return interventions
```

### 2. Информационная архитектура интерфейсов
```python
def design_information_interface(
    user_capacity_profile: Dict[str, float],
    content_hierarchy: Dict[str, any],
    interaction_goals: List[str]
) -> Dict[str, any]:
    """
    Дизайн интерфейса с учетом информационной емкости пользователя
    """
    user_capacity = user_capacity_profile['total_capacity']
    
    # Принципы дизайна на основе емкости
    design_principles = {
        'max_elements_per_screen': min(int(user_capacity * 0.6), 12),
        'information_hierarchy_levels': min(int(user_capacity * 0.3), 5),
        'cognitive_load_budget': user_capacity * 0.7,  # Оставляем резерв
        'chunking_strategy': 'hierarchical' if user_capacity > 10 else 'sequential'
    }
    
    # Адаптивная группировка контента
    content_chunks = []
    current_chunk_load = 0
    current_chunk = []
    
    for item in content_hierarchy['items']:
        item_complexity = item['cognitive_weight']
        
        if current_chunk_load + item_complexity <= design_principles['cognitive_load_budget']:
            current_chunk.append(item)
            current_chunk_load += item_complexity
        else:
            content_chunks.append(current_chunk)
            current_chunk = [item]
            current_chunk_load = item_complexity
    
    if current_chunk:
        content_chunks.append(current_chunk)
    
    return {
        'design_principles': design_principles,
        'content_organization': content_chunks,
        'estimated_cognitive_load': sum(chunk['cognitive_weight'] for chunk in content_chunks[0] if content_chunks),
        'capacity_utilization': (sum(chunk['cognitive_weight'] for chunk in content_chunks[0] if content_chunks) / user_capacity) if content_chunks else 0
    }
```

### 3. Корпоративное управление знаниями
```python
def corporate_knowledge_capacity_audit(
    employee_profiles: List[CognitiveProfile],
    knowledge_domains: List[str],
    information_flow_requirements: Dict[str, float]
) -> Dict[str, any]:
    """
    Аудит информационной емкости корпоративной системы
    """
    capacity_model = InformationCapacityModel()
    
    # Анализ емкости сотрудников
    total_capacity = 0
    capacity_distribution = []
    
    for profile in employee_profiles:
        # Используем средние значения для мотивации и организации
        avg_motivation = MotivationalProfile(0.7, 0.6, 0.6, 0.8, 0.7)
        avg_organization = OrganizationalProfile(0.6, 0.6, 0.6, 0.6, 0.6)
        
        employee_capacity = capacity_model.calculate_total_capacity(
            profile, avg_motivation, avg_organization
        )['total_capacity']
        
        total_capacity += employee_capacity
        capacity_distribution.append(employee_capacity)
    
    # Анализ узких мест
    required_capacity = sum(information_flow_requirements.values())
    capacity_surplus = total_capacity - required_capacity
    
    # Рекомендации по оптимизации
    recommendations = []
    
    if capacity_surplus < 0:
        recommendations.append("increase_team_size")
        recommendations.append("reduce_information_complexity")
        recommendations.append("implement_automation")
    
    elif capacity_surplus > total_capacity * 0.5:
        recommendations.append("increase_information_throughput")
        recommendations.append("add_complex_projects")
        recommendations.append("cross_training_opportunities")
    
    return {
        'total_organizational_capacity': total_capacity,
        'required_capacity': required_capacity,
        'capacity_utilization': required_capacity / total_capacity,
        'capacity_distribution': {
            'mean': np.mean(capacity_distribution),
            'std': np.std(capacity_distribution),
            'min': np.min(capacity_distribution),
            'max': np.max(capacity_distribution)
        },
        'recommendations': recommendations,
        'bottleneck_domains': [domain for domain, req in information_flow_requirements.items() 
                             if req > np.mean(capacity_distribution)]
    }
```

---

## 📈 Валидационные критерии

### Количественные метрики:
1. **Корреляция с WM тестами**: r > 0.7 между C_info и working memory span
2. **Временные константы**: RC модель должна предсказывать время обучения ±20%
3. **Кривые забывания**: Корреляция с данными Эббингауза > 0.85
4. **Частотные эффекты**: Обратная зависимость от частоты для AC компонента

### Качественные критерии:
1. **Нейронная валидность**: Соответствие активности гиппокампа и PFC
2. **Развитийная валидность**: Предсказание возрастных изменений
3. **Клиническая валидность**: Диагностика когнитивных нарушений
4. **Образовательная валидность**: Улучшение результатов обучения

---

## 🚀 Интеграция с законом Ома

### Полная RLC модель:
```python
def complete_information_circuit(
    U_source: float,
    R_info: float, 
    L_info: float,
    C_info: float,
    frequency: float = 0,
    time_domain: bool = False
) -> Dict[str, any]:
    """
    Полная модель информационной RLC цепи
    """
    omega = 2 * np.pi * frequency if frequency > 0 else 0
    
    if time_domain and frequency == 0:
        # Переходной процесс в RLC цепи
        # Характеристическое уравнение: s² + (R/L)s + 1/(LC) = 0
        discriminant = (R_info / L_info) ** 2 - 4 / (L_info * C_info)
        
        if discriminant > 0:
            # Апериодический режим
            s1 = (-R_info / L_info + np.sqrt(discriminant)) / 2
            s2 = (-R_info / L_info - np.sqrt(discriminant)) / 2
            response_type = "overdamped"
        elif discriminant == 0:
            # Критический режим
            s1 = s2 = -R_info / (2 * L_info)
            response_type = "critically_damped"
        else:
            # Колебательный режим
            alpha = R_info / (2 * L_info)
            omega_d = np.sqrt(1 / (L_info * C_info) - alpha ** 2)
            response_type = "underdamped"
            
        return {
            'response_type': response_type,
            'damping_factor': R_info / (2 * np.sqrt(L_info / C_info)),
            'natural_frequency': 1 / np.sqrt(L_info * C_info),
            'time_constant': 2 * L_info / R_info
        }
    
    else:
        # Частотный анализ
        Z_total = complex(R_info, omega * L_info - 1 / (omega * C_info) if omega > 0 else -float('inf'))
        
        if abs(Z_total) > 0:
            I_info = U_source / Z_total
            V_R = I_info * R_info
            V_L = I_info * complex(0, omega * L_info)
            V_C = I_info * complex(0, -1 / (omega * C_info)) if omega > 0 else 0
        else:
            I_info = V_R = V_L = V_C = 0
        
        return {
            'current': abs(I_info),
            'current_phase': np.angle(I_info),
            'impedance': abs(Z_total),
            'voltage_R': abs(V_R),
            'voltage_L': abs(V_L),
            'voltage_C': abs(V_C),
            'power_factor': np.cos(np.angle(Z_total)),
            'resonance': abs(omega * L_info - 1 / (omega * C_info)) < 0.1 * R_info
        }
```

---

**Статус:** ✅ **ЗАДАЧА 2.1.3 ЗАВЕРШЕНА**

Создана полная модель информационной емкости с:
- ✅ Когнитивными основами (Working Memory, LTM, мотивация, организация)
- ✅ Математической формализацией C_info с детальной операционализацией
- ✅ Динамическими свойствами (зарядка, разрядка, частотные эффекты)
- ✅ Моделями обучения и забывания
- ✅ Экспериментальными предсказаниями
- ✅ Практическими применениями в образовании, UX, корпорациях
- ✅ Полной интеграцией с RLC моделью информационных цепей

Готова к валидации и практическому применению! 🚀 