# Энергетическая модель информационной динамики
## Задача 2.1.4 - Интегрировать энергетический аспект в информационную динамику

**Дата создания:** Январь 2025  
**Статус:** ✅ ЗАВЕРШЕНО  
**Критический пробел:** Энергетика информационных процессов не была учтена в предыдущих моделях

---

## 🎯 Цель

Создать полную энергетическую модель информационной динамики, описывающую:
- Энергозатраты когнитивных процессов (ATP в нейронах)
- Энергетическое взаимодействие информационных компонентов
- Принципы энергетической эффективности в обработке информации
- Энергетические ограничения и затухание систем

---

## ⚡ Нейробиологические основы энергетики

### 1. Мозг как энергетическая система

**Базовые факты:**
- Мозг потребляет ~20% общей энергии организма
- Масса мозга ~2% от массы тела
- Потребление: ~20W в покое, до 25-30W при интенсивной работе
- Нейроны потребляют ~4.7×10⁻¹² cal/spike (глюкоза → ATP)

**Энергетические процессы:**
```python
class NeuralEnergyModel:
    """Модель энергопотребления нейронной сети"""
    
    def __init__(self):
        # Базовое потребление (в Джоулях)
        self.baseline_power = 20.0  # Вт (состояние покоя)
        self.max_power = 30.0       # Вт (максимальная нагрузка)
        
        # Энергия на spike нейрона
        self.energy_per_spike = 4.7e-12 * 4184  # Джоули (cal → J)
        
        # Энергия на синаптическую передачу
        self.energy_per_synapse = 1e-15  # Джоули
        
        # Эффективность обработки
        self.processing_efficiency = 0.25  # 25% (остальное - тепло)
    
    def calculate_processing_energy(
        self,
        neural_activity: float,      # [0,1] уровень нейронной активности
        cognitive_load: float,       # [0,∞] когнитивная нагрузка
        duration_seconds: float      # время обработки
    ) -> Dict[str, float]:
        """
        Расчет энергозатрат на обработку информации
        """
        # Дополнительная мощность сверх baseline
        additional_power = (self.max_power - self.baseline_power) * neural_activity
        
        # Коррекция на когнитивную нагрузку (перегрузка увеличивает потребление)
        load_multiplier = 1.0 + 0.5 * np.tanh(cognitive_load - 1.0)
        
        # Общая мощность
        total_power = (self.baseline_power + additional_power) * load_multiplier
        
        # Общая энергия
        total_energy = total_power * duration_seconds
        
        # Эффективная энергия (на полезную работу)
        useful_energy = total_energy * self.processing_efficiency
        
        # Тепловые потери
        heat_loss = total_energy * (1 - self.processing_efficiency)
        
        return {
            'total_energy_joules': total_energy,
            'useful_energy_joules': useful_energy,
            'heat_loss_joules': heat_loss,
            'power_watts': total_power,
            'efficiency': self.processing_efficiency,
            'load_multiplier': load_multiplier
        }
```

### 2. Энергетические типы когнитивных процессов

```python
class CognitiveEnergyProfile:
    """Энергетические профили различных когнитивных процессов"""
    
    ENERGY_PROFILES = {
        'attention_focus': {
            'base_power_factor': 1.2,      # 20% выше baseline
            'duration_efficiency': 0.9,    # Высокая эффективность
            'fatigue_rate': 0.05           # Медленное утомление
        },
        'working_memory': {
            'base_power_factor': 1.5,      # 50% выше baseline
            'duration_efficiency': 0.7,    # Средняя эффективность
            'fatigue_rate': 0.15          # Быстрое утомление
        },
        'long_term_retrieval': {
            'base_power_factor': 1.1,      # 10% выше baseline
            'duration_efficiency': 0.95,   # Очень эффективно
            'fatigue_rate': 0.02          # Очень медленное утомление
        },
        'complex_reasoning': {
            'base_power_factor': 1.8,      # 80% выше baseline
            'duration_efficiency': 0.6,    # Низкая эффективность
            'fatigue_rate': 0.25          # Очень быстрое утомление
        },
        'creative_thinking': {
            'base_power_factor': 1.4,      # 40% выше baseline
            'duration_efficiency': 0.5,    # Низкая эффективность (много "мусора")
            'fatigue_rate': 0.20          # Быстрое утомление
        },
        'automatic_processing': {
            'base_power_factor': 0.9,      # 10% ниже baseline
            'duration_efficiency': 0.98,   # Максимальная эффективность
            'fatigue_rate': 0.01          # Почти нет утомления
        }
    }
    
    def get_energy_cost(self, process_type: str, duration: float) -> float:
        """Получить энергетическую стоимость процесса"""
        if process_type not in self.ENERGY_PROFILES:
            process_type = 'working_memory'  # default
        
        profile = self.ENERGY_PROFILES[process_type]
        
        # Базовая стоимость
        base_cost = 20.0 * profile['base_power_factor'] * duration
        
        # Учет утомления (экспоненциальный рост)
        fatigue_penalty = 1.0 + profile['fatigue_rate'] * (np.exp(duration / 3600) - 1)
        
        # Корректировка на эффективность
        total_cost = base_cost * fatigue_penalty / profile['duration_efficiency']
        
        return total_cost
```

---

## ⚡ Энергетические аналоги электротехники

### 1. Информационная мощность

```python
def calculate_information_power(U_info: float, I_info: float, efficiency: float = 1.0) -> Dict[str, float]:
    """
    Информационная мощность по аналогии с электрической
    P = U × I
    """
    # Активная мощность (полезная работа)
    P_active = U_info * I_info * efficiency
    
    # Реактивная мощность (потери на реактивных элементах)
    P_reactive = U_info * I_info * (1 - efficiency)
    
    # Полная мощность
    P_apparent = U_info * I_info
    
    return {
        'active_power': P_active,           # Полезная информационная работа
        'reactive_power': P_reactive,       # Потери (тепло, помехи)
        'apparent_power': P_apparent,       # Общая информационная мощность
        'power_factor': efficiency          # Коэффициент мощности
    }

def information_energy_in_components(R_info: float, L_info: float, C_info: float, 
                                   I_info: float, U_info: float) -> Dict[str, float]:
    """
    Энергия, запасенная в информационных компонентах
    """
    # Энергия в резистивном элементе (рассеивается как тепло)
    E_resistive = I_info ** 2 * R_info  # Мгновенная мощность потерь
    
    # Энергия в индуктивном элементе (инерция, задержки)
    E_inductive = 0.5 * L_info * I_info ** 2
    
    # Энергия в емкостном элементе (накопленная информация)
    E_capacitive = 0.5 * C_info * U_info ** 2
    
    # Общая запасенная энергия
    E_stored = E_inductive + E_capacitive
    
    return {
        'resistive_loss': E_resistive,      # Потери (необратимые)
        'inductive_energy': E_inductive,    # Энергия инерции
        'capacitive_energy': E_capacitive,  # Энергия накопления
        'total_stored': E_stored            # Общая запасенная энергия
    }
```

### 2. Энергетический баланс информационной системы

```python
class InformationEnergyBalance:
    """Энергетический баланс информационной системы"""
    
    def __init__(self, neural_energy_model: NeuralEnergyModel):
        self.neural_model = neural_energy_model
        self.energy_history = []
    
    def energy_conservation_law(
        self,
        E_input: float,          # Входная энергия
        E_processing: float,     # Энергия обработки  
        E_stored: float,         # Запасенная энергия
        E_output: float,         # Выходная энергия
        E_loss: float            # Потери
    ) -> Dict[str, float]:
        """
        Закон сохранения энергии для информационной системы
        E_input = E_processing + E_stored + E_output + E_loss
        """
        
        # Проверка баланса
        E_total_consumption = E_processing + E_stored + E_output + E_loss
        energy_balance_error = abs(E_input - E_total_consumption)
        
        # Энергетическая эффективность
        useful_energy = E_output + E_stored  # Полезная энергия
        efficiency = useful_energy / E_input if E_input > 0 else 0
        
        # Потери в процентах
        loss_percentage = E_loss / E_input * 100 if E_input > 0 else 0
        
        return {
            'energy_balance_error': energy_balance_error,
            'efficiency_percent': efficiency * 100,
            'loss_percentage': loss_percentage,
            'useful_energy': useful_energy,
            'energy_conservation_valid': energy_balance_error < 0.01 * E_input
        }
    
    def cognitive_energy_budget(
        self,
        available_energy: float,     # Доступная энергия (Дж)
        task_demands: List[Dict],    # Список задач с требованиями
        time_window: float           # Временное окно (сек)
    ) -> Dict[str, any]:
        """
        Распределение энергетического бюджета между задачами
        """
        total_demand = sum(task['energy_cost'] for task in task_demands)
        
        if total_demand <= available_energy:
            # Достаточно энергии для всех задач
            allocation = task_demands.copy()
            remaining_energy = available_energy - total_demand
            
        else:
            # Нехватка энергии - нужна приоритизация
            # Сортировка по приоритету / энергопотреблению
            sorted_tasks = sorted(
                task_demands, 
                key=lambda x: x.get('priority', 1.0) / x['energy_cost'],
                reverse=True
            )
            
            allocation = []
            remaining_energy = available_energy
            
            for task in sorted_tasks:
                if task['energy_cost'] <= remaining_energy:
                    allocation.append(task)
                    remaining_energy -= task['energy_cost']
                else:
                    # Частичное выполнение, если возможно
                    if task.get('divisible', False):
                        partial_task = task.copy()
                        completion_ratio = remaining_energy / task['energy_cost']
                        partial_task['energy_cost'] = remaining_energy
                        partial_task['completion_ratio'] = completion_ratio
                        allocation.append(partial_task)
                        remaining_energy = 0
                    break
        
        return {
            'allocated_tasks': allocation,
            'remaining_energy': remaining_energy,
            'total_allocated': sum(task['energy_cost'] for task in allocation),
            'energy_deficit': max(0, total_demand - available_energy),
            'allocation_efficiency': sum(task['energy_cost'] for task in allocation) / available_energy
        }
```

---

## 🔄 Энергетическое расширение компонентов модели

### 1. Энергетический закон Ома

```python
def energetic_ohms_law(
    U_info: float,          # Информационное напряжение
    R_info: float,          # Информационное сопротивление
    L_info: float,          # Информационная индуктивность
    C_info: float,          # Информационная емкость
    frequency: float = 0,   # Частота (для AC анализа)
    time_duration: float = 1.0  # Длительность процесса
) -> Dict[str, float]:
    """
    Энергетический анализ информационной цепи
    """
    if frequency == 0:  # DC анализ
        I_info = U_info / R_info
        
        # Мгновенная мощность
        P_resistive = I_info ** 2 * R_info  # Потери в сопротивлении
        P_input = U_info * I_info            # Входная мощность
        
        # Энергия за время duration
        E_dissipated = P_resistive * time_duration  # Рассеянная энергия
        E_input_total = P_input * time_duration     # Общая входная энергия
        
        # Запасенная энергия (для C и L - ноль в DC)
        E_stored = 0
        
    else:  # AC анализ
        omega = 2 * np.pi * frequency
        
        # Импеданс
        Z_total = complex(R_info, omega * L_info - 1/(omega * C_info))
        I_info_complex = U_info / Z_total
        I_info = abs(I_info_complex)
        
        # Активная мощность (только резистивная часть)
        P_active = I_info ** 2 * R_info
        
        # Реактивная мощность
        X_total = omega * L_info - 1/(omega * C_info)  # Реактивное сопротивление
        P_reactive = I_info ** 2 * abs(X_total)
        
        # Полная мощность
        P_apparent = U_info * I_info
        
        # Энергия за период
        E_dissipated = P_active * time_duration
        E_reactive = P_reactive * time_duration  # Энергия колебаний
        
        # Запасенная энергия в реактивных элементах
        E_stored = 0.5 * L_info * I_info ** 2 + 0.5 * C_info * U_info ** 2
    
    return {
        'current': I_info,
        'active_power': P_active if frequency > 0 else P_resistive,
        'reactive_power': P_reactive if frequency > 0 else 0,
        'apparent_power': P_apparent if frequency > 0 else P_input,
        'energy_dissipated': E_dissipated,
        'energy_stored': E_stored,
        'power_factor': P_active / P_apparent if frequency > 0 and P_apparent > 0 else 1.0,
        'efficiency': (P_apparent - P_resistive) / P_apparent if P_apparent > 0 else 0
    }
```

### 2. Энергетические трансформаторы

```python
class EnergeticTransformer:
    """Энергетическая модель информационного трансформатора"""
    
    def __init__(self, transformation_ratio: float, efficiency: float = 0.9):
        self.k = transformation_ratio
        self.η = efficiency
        
    def transform_with_energy_analysis(
        self,
        U_input: float,
        I_input: float,
        cognitive_load: float = 1.0
    ) -> Dict[str, float]:
        """
        Трансформация с учетом энергетических потерь
        """
        # Входная мощность
        P_input = U_input * I_input
        
        # Идеальная трансформация
        U_output_ideal = self.k * U_input
        I_output_ideal = I_input / self.k
        P_output_ideal = U_output_ideal * I_output_ideal  # = P_input
        
        # Реальные потери
        # 1. Резистивные потери (когнитивное сопротивление)
        resistance_loss = P_input * (1 - self.η) * cognitive_load
        
        # 2. Потери на трансформацию (semantic drift, etc.)
        transformation_loss = P_input * 0.05 * (abs(self.k - 1.0))
        
        # 3. Потери на частоту (если трансформация меняет "частоту" информации)
        frequency_loss = P_input * 0.02 * (self.k ** 0.5)
        
        total_loss = resistance_loss + transformation_loss + frequency_loss
        
        # Реальная выходная мощность
        P_output_real = P_input - total_loss
        
        # Коэффициент полезного действия (реальный)
        efficiency_real = P_output_real / P_input if P_input > 0 else 0
        
        return {
            'U_output': U_output_ideal,
            'I_output': I_output_ideal,
            'P_input': P_input,
            'P_output_ideal': P_output_ideal,
            'P_output_real': P_output_real,
            'total_loss': total_loss,
            'resistance_loss': resistance_loss,
            'transformation_loss': transformation_loss,
            'frequency_loss': frequency_loss,
            'efficiency_ideal': self.η,
            'efficiency_real': efficiency_real,
            'energy_quality_factor': P_output_real / P_output_ideal
        }
```

### 3. Энергетическая емкость

```python
class EnergeticCapacitor:
    """Энергетическая модель информационной емкости"""
    
    def __init__(self, capacity: float, max_energy: float):
        self.C_info = capacity
        self.max_energy = max_energy  # Максимальная энергия хранения
        self.current_energy = 0
        self.current_voltage = 0
    
    def charge_with_energy_tracking(
        self,
        voltage_source: float,
        resistance: float,
        time_step: float,
        available_energy: float
    ) -> Dict[str, float]:
        """
        Зарядка с учетом энергетических ограничений
        """
        # Стандартный расчет RC зарядки
        RC_constant = resistance * self.C_info
        dU_dt = (voltage_source - self.current_voltage) / RC_constant
        
        # Требуемая энергия для зарядки
        voltage_increment = dU_dt * time_step
        new_voltage = self.current_voltage + voltage_increment
        
        # Энергия, необходимая для такого приращения
        energy_old = 0.5 * self.C_info * self.current_voltage ** 2
        energy_new = 0.5 * self.C_info * new_voltage ** 2
        energy_required = energy_new - energy_old
        
        # Проверка энергетических ограничений
        if energy_required <= available_energy and energy_new <= self.max_energy:
            # Достаточно энергии - нормальная зарядка
            self.current_voltage = new_voltage
            self.current_energy = energy_new
            energy_consumed = energy_required
            charging_efficiency = 1.0
        else:
            # Энергетические ограничения - замедленная зарядка
            available_voltage_increase = np.sqrt(
                2 * min(available_energy, self.max_energy - self.current_energy) / self.C_info + 
                self.current_voltage ** 2
            ) - self.current_voltage
            
            self.current_voltage += available_voltage_increase
            self.current_energy = 0.5 * self.C_info * self.current_voltage ** 2
            energy_consumed = available_energy
            charging_efficiency = available_voltage_increase / voltage_increment if voltage_increment > 0 else 0
        
        # Ток зарядки
        charging_current = (voltage_source - self.current_voltage) / resistance
        
        return {
            'voltage': self.current_voltage,
            'energy_stored': self.current_energy,
            'charging_current': charging_current,
            'energy_consumed': energy_consumed,
            'charging_efficiency': charging_efficiency,
            'energy_utilization': self.current_energy / self.max_energy,
            'voltage_increment': voltage_increment
        }
    
    def discharge_with_energy_recovery(
        self,
        resistance: float,
        time_step: float
    ) -> Dict[str, float]:
        """
        Разрядка с возможностью восстановления энергии
        """
        RC_constant = resistance * self.C_info
        decay_factor = np.exp(-time_step / RC_constant)
        
        # Энергия до разрядки
        energy_before = self.current_energy
        
        # Новое напряжение и энергия
        self.current_voltage *= decay_factor
        self.current_energy = 0.5 * self.C_info * self.current_voltage ** 2
        
        # Высвобожденная энергия
        energy_released = energy_before - self.current_energy
        
        # Часть энергии может быть "переработана" (consolidation to LTM)
        recyclable_energy = energy_released * 0.3  # 30% может быть сохранено
        lost_energy = energy_released * 0.7        # 70% теряется
        
        discharge_current = -self.current_voltage / resistance
        
        return {
            'voltage': self.current_voltage,
            'energy_stored': self.current_energy,
            'discharge_current': discharge_current,
            'energy_released': energy_released,
            'recyclable_energy': recyclable_energy,
            'lost_energy': lost_energy,
            'retention_factor': decay_factor,
            'energy_recovery_efficiency': recyclable_energy / energy_released if energy_released > 0 else 0
        }
```

---

## 🧠 Когнитивные энергетические паттерны

### 1. Энергетические режимы мозга

```python
class BrainEnergyModes:
    """Энергетические режимы работы мозга"""
    
    ENERGY_MODES = {
        'default_mode': {
            'power_consumption': 20.0,      # Вт
            'information_processing': 0.3,  # Относительная эффективность
            'attention_level': 0.2,
            'fatigue_rate': 0.01
        },
        'focused_attention': {
            'power_consumption': 24.0,
            'information_processing': 1.0,
            'attention_level': 0.9,
            'fatigue_rate': 0.15
        },
        'diffuse_thinking': {
            'power_consumption': 22.0,
            'information_processing': 0.6,
            'attention_level': 0.4,
            'fatigue_rate': 0.05
        },
        'flow_state': {
            'power_consumption': 25.0,
            'information_processing': 1.5,  # Повышенная эффективность
            'attention_level': 1.0,
            'fatigue_rate': 0.03           # Низкое утомление
        },
        'cognitive_overload': {
            'power_consumption': 28.0,
            'information_processing': 0.4,  # Снижение эффективности
            'attention_level': 0.6,
            'fatigue_rate': 0.4            # Быстрое утомление
        },
        'mental_fatigue': {
            'power_consumption': 18.0,
            'information_processing': 0.2,
            'attention_level': 0.1,
            'fatigue_rate': 0.02
        }
    }
    
    def transition_energy_cost(self, from_mode: str, to_mode: str) -> float:
        """
        Энергетическая стоимость переключения между режимами
        """
        mode_distances = {
            ('default_mode', 'focused_attention'): 2.0,
            ('focused_attention', 'flow_state'): 1.0,
            ('flow_state', 'cognitive_overload'): 3.0,
            ('cognitive_overload', 'mental_fatigue'): 0.5,
            ('mental_fatigue', 'default_mode'): 1.5,
            # Обратные переходы
            ('focused_attention', 'default_mode'): 1.0,
            ('flow_state', 'focused_attention'): 0.5,
            ('cognitive_overload', 'flow_state'): 4.0,
            ('mental_fatigue', 'cognitive_overload'): 2.0,
            ('default_mode', 'mental_fatigue'): 1.0
        }
        
        # Симметричные переходы, если не указаны явно
        transition_cost = mode_distances.get((from_mode, to_mode), 
                                           mode_distances.get((to_mode, from_mode), 2.0))
        
        return transition_cost
    
    def optimal_mode_sequence(
        self,
        task_sequence: List[Dict],
        total_time_budget: float,
        total_energy_budget: float
    ) -> Dict[str, any]:
        """
        Оптимальная последовательность энергетических режимов для задач
        """
        optimal_sequence = []
        current_energy = total_energy_budget
        current_time = 0
        current_mode = 'default_mode'
        
        for task in task_sequence:
            required_processing = task['complexity']
            available_time = min(task['max_duration'], total_time_budget - current_time)
            
            # Выбор оптимального режима для задачи
            best_mode = None
            best_efficiency = 0
            
            for mode_name, mode_props in self.ENERGY_MODES.items():
                # Энергетическая стоимость переключения
                switch_cost = self.transition_energy_cost(current_mode, mode_name)
                
                # Энергетическая стоимость выполнения задачи
                task_energy = mode_props['power_consumption'] * available_time + switch_cost
                
                if task_energy <= current_energy:
                    # Эффективность = обработка / энергозатраты
                    efficiency = (mode_props['information_processing'] * 
                                mode_props['attention_level']) / task_energy
                    
                    if efficiency > best_efficiency:
                        best_efficiency = efficiency
                        best_mode = mode_name
            
            if best_mode:
                # Выполнение задачи в оптимальном режиме
                switch_cost = self.transition_energy_cost(current_mode, best_mode)
                mode_props = self.ENERGY_MODES[best_mode]
                task_energy = mode_props['power_consumption'] * available_time + switch_cost
                
                optimal_sequence.append({
                    'task_id': task['id'],
                    'mode': best_mode,
                    'duration': available_time,
                    'energy_cost': task_energy,
                    'switch_cost': switch_cost,
                    'efficiency': best_efficiency
                })
                
                current_energy -= task_energy
                current_time += available_time
                current_mode = best_mode
            else:
                # Недостаточно энергии - задача пропускается или откладывается
                optimal_sequence.append({
                    'task_id': task['id'],
                    'mode': 'deferred',
                    'reason': 'insufficient_energy'
                })
        
        return {
            'sequence': optimal_sequence,
            'energy_utilized': total_energy_budget - current_energy,
            'time_utilized': current_time,
            'overall_efficiency': sum(s.get('efficiency', 0) for s in optimal_sequence) / len(optimal_sequence)
        }
```

### 2. Энергетическая усталость и восстановление

```python
class CognitiveFatigueModel:
    """Модель когнитивного утомления и восстановления"""
    
    def __init__(self, max_energy_capacity: float = 100.0):
        self.max_capacity = max_energy_capacity
        self.current_energy = max_energy_capacity
        self.fatigue_level = 0.0
        self.recovery_rate = 0.1  # % в минуту
        
    def energy_depletion(
        self,
        task_intensity: float,    # [0,1] интенсивность задачи
        duration_minutes: float,
        cognitive_load: float     # [0,∞] когнитивная нагрузка
    ) -> Dict[str, float]:
        """
        Истощение энергии при выполнении когнитивных задач
        """
        # Базовая скорость истощения
        base_depletion_rate = 2.0  # % в минуту при нормальной нагрузке
        
        # Модификация от интенсивности и нагрузки
        intensity_multiplier = 1.0 + 2.0 * task_intensity  # [1, 3]
        load_multiplier = 1.0 + 0.5 * np.tanh(cognitive_load - 1.0)  # [1, 1.5]
        
        # Общая скорость истощения
        depletion_rate = base_depletion_rate * intensity_multiplier * load_multiplier
        
        # Учет текущего уровня усталости (усталость ускоряет истощение)
        fatigue_penalty = 1.0 + 2.0 * self.fatigue_level
        
        total_depletion = depletion_rate * fatigue_penalty * duration_minutes
        
        # Обновление состояния
        energy_lost = min(total_depletion, self.current_energy)
        self.current_energy -= energy_lost
        self.fatigue_level = 1.0 - (self.current_energy / self.max_capacity)
        
        return {
            'energy_lost': energy_lost,
            'current_energy': self.current_energy,
            'fatigue_level': self.fatigue_level,
            'depletion_rate': depletion_rate,
            'fatigue_penalty': fatigue_penalty,
            'energy_percentage': self.current_energy / self.max_capacity * 100
        }
    
    def energy_recovery(
        self,
        rest_type: str,          # 'active_rest', 'passive_rest', 'sleep'
        duration_minutes: float
    ) -> Dict[str, float]:
        """
        Восстановление энергии через отдых
        """
        recovery_rates = {
            'active_rest': 0.05,      # 5% в минуту (легкая активность)
            'passive_rest': 0.1,      # 10% в минуту (медитация, расслабление)
            'sleep': 0.3,             # 30% в минуту (глубокий сон)
            'micro_break': 0.15       # 15% в минуту (короткие перерывы)
        }
        
        recovery_rate = recovery_rates.get(rest_type, 0.1)
        
        # Эффективность восстановления снижается при высокой усталости
        recovery_efficiency = 1.0 - 0.3 * self.fatigue_level
        
        effective_recovery_rate = recovery_rate * recovery_efficiency
        energy_recovered = effective_recovery_rate * duration_minutes
        
        # Обновление состояния
        self.current_energy = min(self.max_capacity, self.current_energy + energy_recovered)
        self.fatigue_level = 1.0 - (self.current_energy / self.max_capacity)
        
        return {
            'energy_recovered': energy_recovered,
            'current_energy': self.current_energy,
            'fatigue_level': self.fatigue_level,
            'recovery_efficiency': recovery_efficiency,
            'energy_percentage': self.current_energy / self.max_capacity * 100
        }
    
    def optimal_work_rest_cycle(
        self,
        total_work_duration: float,  # минуты
        task_intensity: float,       # [0,1]
        cognitive_load: float        # [0,∞]
    ) -> Dict[str, any]:
        """
        Оптимальный цикл работы и отдыха для максимальной продуктивности
        """
        cycles = []
        remaining_time = total_work_duration
        cycle_count = 0
        
        while remaining_time > 0 and self.current_energy > 20:  # Минимум 20% энергии
            cycle_count += 1
            
            # Оптимальная длительность работы (зависит от текущей энергии)
            optimal_work_time = min(
                25 * (self.current_energy / self.max_capacity),  # Pomodoro с коррекцией
                remaining_time
            )
            
            # Симуляция работы
            work_result = self.energy_depletion(task_intensity, optimal_work_time, cognitive_load)
            
            # Оптимальная длительность отдыха
            if cycle_count % 4 == 0:  # Длинный перерыв каждые 4 цикла
                rest_duration = 15
                rest_type = 'passive_rest'
            else:
                rest_duration = 5
                rest_type = 'micro_break'
            
            # Симуляция отдыха
            rest_result = self.energy_recovery(rest_type, rest_duration)
            
            cycles.append({
                'cycle': cycle_count,
                'work_duration': optimal_work_time,
                'rest_duration': rest_duration,
                'rest_type': rest_type,
                'energy_before_work': work_result['current_energy'] + work_result['energy_lost'],
                'energy_after_work': work_result['current_energy'],
                'energy_after_rest': rest_result['current_energy'],
                'productivity_score': optimal_work_time * (1 - work_result['fatigue_level'])
            })
            
            remaining_time -= optimal_work_time
        
        total_productivity = sum(cycle['productivity_score'] for cycle in cycles)
        
        return {
            'cycles': cycles,
            'total_cycles': cycle_count,
            'total_productivity': total_productivity,
            'average_productivity_per_cycle': total_productivity / cycle_count if cycle_count > 0 else 0,
            'final_energy_level': self.current_energy,
            'optimization_efficiency': total_productivity / total_work_duration
        }
```

---

## 📈 Интеграция с существующими моделями

### 1. Энергетический закон Ома (обновленный)

```python
def energetic_information_ohm_law(
    U_info: float,
    R_info: float,
    L_info: float,
    C_info: float,
    available_energy: float,    # Доступная энергия
    neural_efficiency: float = 0.25,  # Нейронная эффективность
    frequency: float = 0
) -> Dict[str, float]:
    """
    Энергетически ограниченный закон Ома для информации
    """
    # Стандартный расчет
    if frequency == 0:
        I_info_ideal = U_info / R_info
    else:
        omega = 2 * np.pi * frequency
        Z_total = complex(R_info, omega * L_info - 1/(omega * C_info))
        I_info_ideal = abs(U_info / Z_total)
    
    # Энергетические требования
    P_required = U_info * I_info_ideal  # Требуемая информационная мощность
    E_neural_required = P_required / neural_efficiency  # Требуемая нейронная энергия
    
    # Энергетические ограничения
    if E_neural_required <= available_energy:
        # Достаточно энергии - идеальная работа
        I_info_actual = I_info_ideal
        energy_utilization = E_neural_required / available_energy
        performance_factor = 1.0
    else:
        # Нехватка энергии - снижение производительности
        energy_utilization = 1.0
        performance_factor = available_energy / E_neural_required
        I_info_actual = I_info_ideal * performance_factor
    
    # Энергетические потери
    E_useful = I_info_actual * U_info * neural_efficiency
    E_heat_loss = (I_info_actual * U_info) * (1 - neural_efficiency)
    E_total_consumed = min(E_neural_required, available_energy)
    
    return {
        'current_ideal': I_info_ideal,
        'current_actual': I_info_actual,
        'performance_factor': performance_factor,
        'energy_utilization': energy_utilization,
        'energy_consumed': E_total_consumed,
        'useful_energy': E_useful,
        'heat_loss': E_heat_loss,
        'neural_efficiency': neural_efficiency,
        'energy_deficit': max(0, E_neural_required - available_energy)
    }
```

### 2. Энергетические трансформаторы (интеграция)

```python
def energetic_transformer_integration(
    transformer_chain: List[Dict],  # Цепь трансформаторов
    initial_energy: float,
    energy_budget: float
) -> Dict[str, any]:
    """
    Энергетический анализ цепи трансформаторов
    """
    current_energy = initial_energy
    transformation_results = []
    total_energy_loss = 0
    
    for i, transformer in enumerate(transformer_chain):
        # Энергетические требования трансформации
        complexity_factor = transformer.get('complexity', 1.0)
        base_energy_cost = 5.0 * complexity_factor  # Базовая стоимость
        
        if current_energy >= base_energy_cost:
            # Выполнение трансформации
            efficiency = transformer.get('efficiency', 0.9)
            actual_efficiency = efficiency * (current_energy / energy_budget)  # Снижение при истощении
            
            energy_consumed = base_energy_cost
            energy_output = energy_consumed * actual_efficiency
            energy_loss = energy_consumed * (1 - actual_efficiency)
            
            current_energy -= energy_consumed
            total_energy_loss += energy_loss
            
            transformation_results.append({
                'transformer_id': i,
                'type': transformer['type'],
                'energy_consumed': energy_consumed,
                'energy_output': energy_output,
                'efficiency': actual_efficiency,
                'energy_loss': energy_loss,
                'remaining_energy': current_energy
            })
        else:
            # Недостаток энергии - пропуск или частичная трансформация
            partial_efficiency = current_energy / base_energy_cost
            
            transformation_results.append({
                'transformer_id': i,
                'type': transformer['type'],
                'status': 'partial' if partial_efficiency > 0.3 else 'skipped',
                'partial_efficiency': partial_efficiency,
                'energy_deficit': base_energy_cost - current_energy
            })
            
            current_energy = 0  # Энергия исчерпана
            break
    
    return {
        'transformations': transformation_results,
        'total_energy_consumed': initial_energy - current_energy,
        'total_energy_loss': total_energy_loss,
        'remaining_energy': current_energy,
        'chain_efficiency': (initial_energy - total_energy_loss) / initial_energy if initial_energy > 0 else 0,
        'completion_rate': len([t for t in transformation_results if t.get('status') != 'skipped']) / len(transformer_chain)
    }
```

---

## 🔬 Экспериментальные предсказания

### Предсказание 1: Энергетическая эффективность vs когнитивная нагрузка
```python
def test_energy_efficiency_vs_load():
    """
    Тест: при увеличении когнитивной нагрузки энергетическая эффективность снижается
    """
    loads = np.linspace(0.5, 3.0, 20)
    efficiencies = []
    
    for load in loads:
        result = energetic_information_ohm_law(
            U_info=5.0, R_info=load, L_info=1.0, C_info=2.0,
            available_energy=100.0, neural_efficiency=0.25
        )
        efficiencies.append(result['neural_efficiency'] * result['performance_factor'])
    
    # Предсказание: обратная корреляция
    correlation = np.corrcoef(loads, efficiencies)[0,1]
    assert correlation < -0.8, "Эффективность должна снижаться с ростом нагрузки"
```

### Предсказание 2: Оптимальная частота работы
```python
def test_optimal_working_frequency():
    """
    Тест: существует оптимальная частота для минимального энергопотребления
    """
    frequencies = np.logspace(-2, 1, 50)  # 0.01 to 10 Hz
    energy_costs = []
    
    for freq in frequencies:
        result = energetic_information_ohm_law(
            U_info=5.0, R_info=2.0, L_info=1.0, C_info=1.0,
            available_energy=100.0, frequency=freq
        )
        energy_costs.append(result['energy_consumed'])
    
    # Предсказание: U-образная кривая с минимумом
    min_idx = np.argmin(energy_costs)
    assert 0 < min_idx < len(frequencies) - 1, "Должен быть внутренний минимум"
```

### Предсказание 3: Закон усталости
```python
def test_fatigue_law():
    """
    Тест: производительность экспоненциально снижается с истощением энергии
    """
    fatigue_model = CognitiveFatigueModel(100.0)
    performance_data = []
    
    for session in range(10):  # 10 сессий по 30 минут
        result = fatigue_model.energy_depletion(
            task_intensity=0.7, duration_minutes=30, cognitive_load=1.5
        )
        performance = result['current_energy'] / 100.0  # Нормализованная производительность
        performance_data.append(performance)
    
    # Предсказание: экспоненциальное снижение
    x = np.arange(len(performance_data))
    log_performance = np.log(np.array(performance_data) + 0.01)  # Избегаем log(0)
    slope, _ = np.polyfit(x, log_performance, 1)
    assert slope < -0.1, "Производительность должна экспоненциально снижаться"
```

---

## 🎯 Практические применения

### 1. Энергетически оптимизированное обучение
```python
def design_energy_optimal_curriculum(
    student_energy_profile: Dict,
    course_content: List[Dict],
    time_constraints: Dict
) -> Dict[str, any]:
    """
    Дизайн учебного плана с учетом энергетических ограничений
    """
    fatigue_model = CognitiveFatigueModel(student_energy_profile['max_capacity'])
    optimized_schedule = []
    
    for week in range(time_constraints['total_weeks']):
        weekly_schedule = []
        
        for day in range(5):  # Рабочие дни
            daily_energy = student_energy_profile['daily_energy_budget']
            fatigue_model.current_energy = daily_energy
            
            # Оптимальное распределение контента по дню
            day_result = fatigue_model.optimal_work_rest_cycle(
                total_work_duration=time_constraints['daily_study_hours'] * 60,
                task_intensity=0.7,
                cognitive_load=1.2
            )
            
            weekly_schedule.append({
                'day': day + 1,
                'cycles': day_result['cycles'],
                'productivity': day_result['total_productivity'],
                'energy_efficiency': day_result['optimization_efficiency']
            })
        
        optimized_schedule.append({
            'week': week + 1,
            'daily_schedules': weekly_schedule,
            'weekly_productivity': sum(day['productivity'] for day in weekly_schedule)
        })
    
    return {
        'schedule': optimized_schedule,
        'total_productivity': sum(week['weekly_productivity'] for week in optimized_schedule),
        'average_efficiency': np.mean([
            day['energy_efficiency'] 
            for week in optimized_schedule 
            for day in week['daily_schedules']
        ])
    }
```

### 2. Энергетический мониторинг интерфейсов
```python
def interface_energy_monitor(
    user_interactions: List[Dict],
    interface_elements: List[Dict]
) -> Dict[str, any]:
    """
    Мониторинг энергозатрат пользователя при работе с интерфейсом
    """
    total_energy_consumed = 0
    energy_per_element = {}
    efficiency_scores = []
    
    for interaction in user_interactions:
        element_id = interaction['element_id']
        interaction_type = interaction['type']
        duration = interaction['duration_seconds']
        
        # Энергетическая стоимость взаимодействия
        base_costs = {
            'click': 0.5,
            'type': 2.0,
            'read': 1.0,
            'search': 3.0,
            'navigate': 1.5
        }
        
        complexity_multiplier = interface_elements[element_id].get('complexity', 1.0)
        energy_cost = base_costs.get(interaction_type, 1.0) * complexity_multiplier * duration
        
        total_energy_consumed += energy_cost
        energy_per_element[element_id] = energy_per_element.get(element_id, 0) + energy_cost
        
        # Эффективность = достигнутая цель / энергозатраты
        goal_achieved = interaction.get('goal_achieved', 0.5)
        efficiency = goal_achieved / energy_cost if energy_cost > 0 else 0
        efficiency_scores.append(efficiency)
    
    # Рекомендации по оптимизации
    high_cost_elements = sorted(
        energy_per_element.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:5]
    
    recommendations = []
    for element_id, cost in high_cost_elements:
        if cost > np.mean(list(energy_per_element.values())) * 1.5:
            recommendations.append({
                'element_id': element_id,
                'current_cost': cost,
                'recommendation': 'simplify_interaction',
                'potential_saving': cost * 0.3  # 30% потенциальная экономия
            })
    
    return {
        'total_energy_consumed': total_energy_consumed,
        'average_efficiency': np.mean(efficiency_scores),
        'energy_per_element': energy_per_element,
        'high_cost_elements': high_cost_elements,
        'optimization_recommendations': recommendations,
        'estimated_energy_savings': sum(rec['potential_saving'] for rec in recommendations)
    }
```

---

## 📈 Валидационные критерии

### Количественные метрики:
1. **Корреляция с нейронными данными**: r > 0.7 между предсказанными и измеренными энергозатратами
2. **Закон сохранения энергии**: Погрешность баланса < 5%
3. **Эффективность модели**: Предсказание производительности ±15%
4. **Оптимизационная валидность**: Улучшение показателей на 20%+ при энергетической оптимизации

### Качественные критерии:
1. **Биологическая валидность**: Соответствие данным fMRI и PET
2. **Поведенческая валидность**: Предсказание паттернов усталости
3. **Эргономическая валидность**: Применимость в дизайне интерфейсов
4. **Образовательная валидность**: Улучшение результатов обучения

---

**Статус:** ✅ **ЗАДАЧА 2.1.4 ЗАВЕРШЕНА**

Создана полная энергетическая модель информационной динамики с:
- ✅ Нейробиологическими основами энергопотребления
- ✅ Энергетическими расширениями всех компонентов (R, L, C, трансформаторы)
- ✅ Моделями когнитивного утомления и восстановления
- ✅ Энергетическими режимами мозга и оптимизацией
- ✅ Экспериментальными предсказаниями
- ✅ Практическими применениями в образовании и UX
- ✅ Полной интеграцией с существующими моделями

**Критический пробел устранен!** Теперь модель информационной динамики имеет полную энергетическую основу! 🚀 