# Модель информационного напряжения (U_info)
## Задача 2.2.2 - Разработать метрики "информационного напряжения"

**Дата создания:** Январь 2025  
**Статус:** ✅ ЗАВЕРШЕНО  
**Базис:** Найденные работы по persuasion, influence, authority + интеграция с тембром и энергетической моделью

---

## 🎯 Цель

Создать формальные метрики "информационного напряжения" (U_info) как движущей силы информационных потоков, аналогично электрическому напряжению. Модель должна:
- Операционализировать "силу воздействия" информации
- Интегрироваться с моделями тембра, энергетики и основными компонентами G, R, L, C
- Обеспечивать измеримые метрики для различных типов контента и контекстов

---

## 🔬 Концептуальная основа

### Аналогия с электрическим напряжением

**Электрическое напряжение (U):**
- Разность потенциалов между точками
- Движущая сила электрического тока
- Работа, совершаемая при перемещении единичного заряда
- Измеряется в вольтах (джоуль/кулон)

**Информационное напряжение (U_info):**
- "Разность информационных потенциалов" между источником и получателем
- Движущая сила информационного потока  
- "Работа", совершаемая при передаче единицы информации
- Измеряется в условных единицах "информационного воздействия"

### Основные компоненты информационного напряжения

1. **Authority Potential (U_authority)** - авторитетный потенциал источника
2. **Emotional Charge (U_emotional)** - эмоциональный заряд сообщения
3. **Social Proof (U_social)** - социальное подтверждение
4. **Relevance Gradient (U_relevance)** - градиент релевантности
5. **Credibility Field (U_credibility)** - поле достоверности

---

## 📊 Формальная модель информационного напряжения

### Базовая многокомпонентная формула

```python
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class VoltageComponent(Enum):
    AUTHORITY = "authority"
    EMOTIONAL = "emotional" 
    SOCIAL = "social"
    RELEVANCE = "relevance"
    CREDIBILITY = "credibility"
    NOVELTY = "novelty"
    URGENCY = "urgency"

@dataclass
class InformationVoltage:
    """
    Многокомпонентная модель информационного напряжения
    """
    # Основные компоненты напряжения
    authority_potential: float      # [0,1] авторитетный потенциал источника
    emotional_charge: float         # [-1,1] эмоциональный заряд (может быть отрицательным)
    social_proof: float            # [0,1] сила социального подтверждения
    relevance_gradient: float      # [0,1] градиент релевантности для получателя
    credibility_field: float       # [0,1] поле достоверности
    novelty_potential: float       # [0,1] потенциал новизны
    urgency_multiplier: float      # [0,2] мультипликатор срочности
    
    # Контекстуальные модификаторы
    context_amplifier: float = 1.0  # [0,3] контекстуальный усилитель
    medium_efficiency: float = 1.0  # [0,1] эффективность канала передачи
    
    def calculate_total_voltage(self) -> float:
        """
        Расчет общего информационного напряжения
        """
        # Базовые компоненты с весами
        base_components = (
            0.25 * self.authority_potential +
            0.20 * abs(self.emotional_charge) +  # Модуль эмоционального заряда
            0.15 * self.social_proof +
            0.20 * self.relevance_gradient +
            0.20 * self.credibility_field
        )
        
        # Модификаторы
        novelty_boost = 1.0 + 0.5 * self.novelty_potential
        urgency_factor = self.urgency_multiplier
        
        # Общее напряжение
        total_voltage = (
            base_components * 
            novelty_boost * 
            urgency_factor * 
            self.context_amplifier * 
            self.medium_efficiency
        )
        
        return min(10.0, max(0.0, total_voltage))  # Ограничение в диапазоне [0, 10]
    
    def get_polarity(self) -> float:
        """
        Определение полярности информационного напряжения
        """
        if self.emotional_charge >= 0:
            return 1.0  # Положительная полярность
        else:
            return -1.0  # Отрицательная полярность
    
    def calculate_voltage_by_component(self) -> Dict[str, float]:
        """
        Расчет напряжения по компонентам
        """
        return {
            'authority': self.authority_potential,
            'emotional': abs(self.emotional_charge),
            'social': self.social_proof,
            'relevance': self.relevance_gradient,
            'credibility': self.credibility_field,
            'novelty_boost': 1.0 + 0.5 * self.novelty_potential,
            'urgency_factor': self.urgency_multiplier,
            'total': self.calculate_total_voltage()
        }

class InformationVoltageCalculator:
    """Калькулятор информационного напряжения с различными методами"""
    
    def __init__(self):
        # Веса для различных типов контента
        self.content_type_weights = {
            'scientific': {
                'authority': 0.4, 'credibility': 0.3, 'emotional': 0.05,
                'social': 0.1, 'relevance': 0.15
            },
            'news': {
                'authority': 0.2, 'credibility': 0.25, 'emotional': 0.15,
                'social': 0.15, 'relevance': 0.25
            },
            'social_media': {
                'authority': 0.1, 'credibility': 0.15, 'emotional': 0.3,
                'social': 0.3, 'relevance': 0.15
            },
            'marketing': {
                'authority': 0.15, 'credibility': 0.1, 'emotional': 0.35,
                'social': 0.25, 'relevance': 0.15
            },
            'educational': {
                'authority': 0.3, 'credibility': 0.25, 'emotional': 0.1,
                'social': 0.05, 'relevance': 0.3
            }
        }
    
    def calculate_authority_potential(
        self, 
        source_info: Dict
    ) -> float:
        """
        Расчет авторитетного потенциала источника
        
        Основано на:
        - Академической репутации
        - Экспертности в области
        - Институциональной принадлежности
        - Истории публикаций
        """
        authority_score = 0.0
        
        # Академическая репутация (0-0.3)
        academic_reputation = source_info.get('academic_reputation', 0.0)
        authority_score += 0.3 * academic_reputation
        
        # Экспертность в области (0-0.25)
        domain_expertise = source_info.get('domain_expertise', 0.0)
        authority_score += 0.25 * domain_expertise
        
        # Институциональная принадлежность (0-0.2)
        institutional_affiliation = source_info.get('institutional_score', 0.0)
        authority_score += 0.2 * institutional_affiliation
        
        # История публикаций/достижений (0-0.15)
        publication_history = source_info.get('publication_score', 0.0)
        authority_score += 0.15 * publication_history
        
        # Признание сообществом (0-0.1)
        community_recognition = source_info.get('recognition_score', 0.0)
        authority_score += 0.1 * community_recognition
        
        return min(1.0, authority_score)
    
    def calculate_emotional_charge(
        self, 
        content: str,
        sentiment_analysis: Dict = None
    ) -> float:
        """
        Расчет эмоционального заряда сообщения
        
        Основано на:
        - Сентимент-анализе
        - Эмоциональной интенсивности
        - Наличии эмоциональных триггеров
        """
        if sentiment_analysis is None:
            # Заглушка для реального анализа настроений
            sentiment_analysis = self._mock_sentiment_analysis(content)
        
        # Базовая валентность (-1 до 1)
        base_valence = sentiment_analysis.get('valence', 0.0)
        
        # Интенсивность эмоций (0 до 1)
        emotion_intensity = sentiment_analysis.get('intensity', 0.5)
        
        # Наличие эмоциональных триггеров
        trigger_words = self._count_emotional_triggers(content)
        trigger_boost = min(0.3, trigger_words * 0.1)
        
        # Модификатор на основе длины и контекста
        length_modifier = self._calculate_length_modifier(content)
        
        emotional_charge = base_valence * emotion_intensity * (1 + trigger_boost) * length_modifier
        
        return max(-1.0, min(1.0, emotional_charge))
    
    def calculate_social_proof(
        self, 
        social_metrics: Dict
    ) -> float:
        """
        Расчет силы социального подтверждения
        
        Основано на:
        - Количестве лайков/репостов
        - Активности комментариев
        - Авторитете поделившихся
        - Скорости распространения
        """
        social_score = 0.0
        
        # Метрики взаимодействия (0-0.4)
        likes = social_metrics.get('likes', 0)
        shares = social_metrics.get('shares', 0) 
        comments = social_metrics.get('comments', 0)
        
        # Нормализация на основе логарифмической шкалы
        engagement_score = (
            0.4 * np.log10(max(1, likes)) / 6 +      # Максимум при 10^6 лайков
            0.3 * np.log10(max(1, shares)) / 5 +     # Максимум при 10^5 репостов  
            0.3 * np.log10(max(1, comments)) / 4     # Максимум при 10^4 комментариев
        )
        engagement_score = min(0.4, engagement_score)
        social_score += engagement_score
        
        # Авторитет поделившихся (0-0.3)
        influential_shares = social_metrics.get('influential_shares', 0.0)
        social_score += 0.3 * influential_shares
        
        # Скорость распространения (0-0.2)
        viral_velocity = social_metrics.get('viral_velocity', 0.0)
        social_score += 0.2 * viral_velocity
        
        # Географическое распространение (0-0.1)
        geographic_reach = social_metrics.get('geographic_reach', 0.0)
        social_score += 0.1 * geographic_reach
        
        return min(1.0, social_score)
    
    def calculate_relevance_gradient(
        self, 
        content_features: Dict,
        user_profile: Dict
    ) -> float:
        """
        Расчет градиента релевантности для получателя
        
        Основано на:
        - Семантическом соответствии интересам
        - Актуальности для текущих задач
        - Персональных предпочтениях
        """
        relevance_score = 0.0
        
        # Семантическое соответствие (0-0.4)
        content_topics = content_features.get('topics', [])
        user_interests = user_profile.get('interests', [])
        topic_overlap = self._calculate_topic_overlap(content_topics, user_interests)
        relevance_score += 0.4 * topic_overlap
        
        # Актуальность для текущих задач (0-0.3)
        current_tasks = user_profile.get('current_tasks', [])
        task_relevance = self._calculate_task_relevance(content_features, current_tasks)
        relevance_score += 0.3 * task_relevance
        
        # Персональные предпочтения (0-0.2)
        preference_match = self._calculate_preference_match(content_features, user_profile)
        relevance_score += 0.2 * preference_match
        
        # Временная актуальность (0-0.1)
        temporal_relevance = content_features.get('temporal_relevance', 0.5)
        relevance_score += 0.1 * temporal_relevance
        
        return min(1.0, relevance_score)
    
    def calculate_credibility_field(
        self, 
        content: str,
        source_info: Dict,
        verification_data: Dict = None
    ) -> float:
        """
        Расчет поля достоверности
        
        Основано на:
        - Фактической проверяемости
        - Наличии источников
        - Консистентности с известными фактами
        - Результатах фактчекинга
        """
        credibility_score = 0.0
        
        # Фактическая проверяемость (0-0.3)
        factual_verifiability = self._assess_factual_verifiability(content)
        credibility_score += 0.3 * factual_verifiability
        
        # Наличие и качество источников (0-0.25)
        source_quality = self._assess_source_quality(content, source_info)
        credibility_score += 0.25 * source_quality
        
        # Консистентность с известными фактами (0-0.25)
        fact_consistency = self._check_fact_consistency(content)
        credibility_score += 0.25 * fact_consistency
        
        # Результаты фактчекинга (0-0.2)
        if verification_data:
            factcheck_score = verification_data.get('factcheck_score', 0.5)
            credibility_score += 0.2 * factcheck_score
        else:
            credibility_score += 0.1  # Нейтральная оценка при отсутствии данных
        
        return min(1.0, credibility_score)
    
    def create_voltage_from_timbre(
        self, 
        timbre: 'InformationTimbre',
        context: Dict = None
    ) -> InformationVoltage:
        """
        Создание информационного напряжения на основе тембра
        """
        # Преобразование тембра в компоненты напряжения
        authority_potential = (timbre.authority + timbre.credibility) / 2
        emotional_charge = timbre.valence * timbre.arousal  # Валентность × Активация
        social_proof = 0.5  # Нейтральное значение без социальных данных
        relevance_gradient = timbre.relevance
        credibility_field = (timbre.credibility + timbre.verification + timbre.transparency) / 3
        novelty_potential = timbre.novelty
        urgency_multiplier = 1.0 + timbre.timeliness  # Актуальность как срочность
        
        # Контекстуальные модификаторы
        context_amplifier = 1.0
        medium_efficiency = 1.0
        
        if context:
            context_amplifier = context.get('amplifier', 1.0)
            medium_efficiency = context.get('medium_efficiency', 1.0)
        
        return InformationVoltage(
            authority_potential=authority_potential,
            emotional_charge=emotional_charge,
            social_proof=social_proof,
            relevance_gradient=relevance_gradient,
            credibility_field=credibility_field,
            novelty_potential=novelty_potential,
            urgency_multiplier=urgency_multiplier,
            context_amplifier=context_amplifier,
            medium_efficiency=medium_efficiency
        )
    
    # Вспомогательные методы (заглушки для реальной реализации)
    def _mock_sentiment_analysis(self, content: str) -> Dict[str, float]:
        """Заглушка для анализа настроений"""
        return {
            'valence': 0.0,     # Нейтральная валентность
            'intensity': 0.5    # Средняя интенсивность
        }
    
    def _count_emotional_triggers(self, content: str) -> int:
        """Подсчет эмоциональных триггеров в тексте"""
        emotional_words = ['amazing', 'shocking', 'incredible', 'urgent', 'breaking']
        return sum(1 for word in emotional_words if word.lower() in content.lower())
    
    def _calculate_length_modifier(self, content: str) -> float:
        """Модификатор на основе длины контента"""
        length = len(content.split())
        if length < 10:
            return 0.8  # Короткие сообщения менее эмоционально насыщены
        elif length > 500:
            return 0.9  # Очень длинные тексты размывают эмоции
        else:
            return 1.0  # Оптимальная длина
    
    def _calculate_topic_overlap(self, content_topics: List[str], user_interests: List[str]) -> float:
        """Расчет пересечения тем"""
        if not content_topics or not user_interests:
            return 0.0
        
        overlap = len(set(content_topics) & set(user_interests))
        return overlap / len(set(content_topics) | set(user_interests))
    
    def _calculate_task_relevance(self, content_features: Dict, current_tasks: List[str]) -> float:
        """Расчет релевантности для текущих задач"""
        return 0.5  # Заглушка
    
    def _calculate_preference_match(self, content_features: Dict, user_profile: Dict) -> float:
        """Расчет соответствия предпочтениям"""
        return 0.5  # Заглушка
    
    def _assess_factual_verifiability(self, content: str) -> float:
        """Оценка фактической проверяемости"""
        return 0.5  # Заглушка
    
    def _assess_source_quality(self, content: str, source_info: Dict) -> float:
        """Оценка качества источников"""
        return 0.5  # Заглушка
    
    def _check_fact_consistency(self, content: str) -> float:
        """Проверка консистентности фактов"""
        return 0.5  # Заглушка
```

---

## ⚡ Интеграция с энергетической моделью

### Связь напряжения с энергией обработки

```python
class VoltageEnergyModel:
    """Модель связи информационного напряжения с энергетикой обработки"""
    
    def __init__(self):
        # Энергетические коэффициенты для компонентов напряжения
        self.energy_coefficients = {
            'authority': 1.2,       # Авторитетная информация требует меньше энергии на проверку
            'emotional': 1.8,       # Эмоциональная информация увеличивает энергозатраты
            'social': 0.9,          # Социальное подтверждение снижает затраты на валидацию
            'relevance': 0.7,       # Релевантная информация обрабатывается легче
            'credibility': 0.8,     # Достоверная информация требует меньше проверки
            'novelty': 2.0,         # Новизна значительно увеличивает энергозатраты
            'urgency': 1.4          # Срочность увеличивает активацию системы
        }
    
    def calculate_voltage_energy_relationship(
        self, 
        voltage: InformationVoltage,
        base_energy: float = 1.0
    ) -> Dict[str, float]:
        """
        Расчет влияния напряжения на энергозатраты обработки
        """
        # Компонентные вклады в энергию
        authority_energy = voltage.authority_potential * self.energy_coefficients['authority']
        emotional_energy = abs(voltage.emotional_charge) * self.energy_coefficients['emotional']
        social_energy = voltage.social_proof * self.energy_coefficients['social']
        relevance_energy = voltage.relevance_gradient * self.energy_coefficients['relevance']
        credibility_energy = voltage.credibility_field * self.energy_coefficients['credibility']
        novelty_energy = voltage.novelty_potential * self.energy_coefficients['novelty']
        urgency_energy = (voltage.urgency_multiplier - 1.0) * self.energy_coefficients['urgency']
        
        # Общий энергетический мультипликатор
        total_energy_multiplier = (
            0.15 * authority_energy +
            0.25 * emotional_energy +
            0.10 * social_energy +
            0.20 * relevance_energy +
            0.15 * credibility_energy +
            0.10 * novelty_energy +
            0.05 * urgency_energy
        )
        
        # Модификация контекстом
        context_modifier = voltage.context_amplifier
        medium_modifier = 1.0 / voltage.medium_efficiency  # Неэффективный канал требует больше энергии
        
        final_energy = base_energy * total_energy_multiplier * context_modifier * medium_modifier
        
        return {
            'base_energy': base_energy,
            'authority_contribution': authority_energy,
            'emotional_contribution': emotional_energy,
            'social_contribution': social_energy,
            'relevance_contribution': relevance_energy,
            'credibility_contribution': credibility_energy,
            'novelty_contribution': novelty_energy,
            'urgency_contribution': urgency_energy,
            'total_multiplier': total_energy_multiplier,
            'context_modifier': context_modifier,
            'medium_modifier': medium_modifier,
            'final_energy': final_energy
        }

def calculate_information_power(
    voltage: InformationVoltage,
    current: float  # Информационный ток (скорость обработки)
) -> float:
    """
    Расчет информационной мощности: P_info = U_info × I_info
    """
    total_voltage = voltage.calculate_total_voltage()
    power = total_voltage * current
    return power

def calculate_energy_efficiency(
    voltage: InformationVoltage,
    processing_time: float,
    useful_output: float
) -> float:
    """
    Расчет энергетической эффективности обработки информации
    """
    total_voltage = voltage.calculate_total_voltage()
    total_energy_input = total_voltage * processing_time
    
    if total_energy_input == 0:
        return 0.0
    
    efficiency = useful_output / total_energy_input
    return min(1.0, efficiency)
```

---

## 🔗 Интеграция с компонентами G, R, L, C

### Влияние напряжения на информационный ток

```python
def voltage_to_current(
    voltage: InformationVoltage,
    resistance: float,
    inductance: float = 0.0,
    capacitance: float = 0.0,
    frequency: float = 0.0
) -> Dict[str, float]:
    """
    Расчет информационного тока на основе закона Ома
    I_info = U_info / Z_info, где Z_info - полный импеданс
    """
    total_voltage = voltage.calculate_total_voltage()
    voltage_polarity = voltage.get_polarity()
    
    if frequency == 0:  # DC режим
        current = total_voltage / resistance if resistance > 0 else 0
        return {
            'dc_current': current * voltage_polarity,
            'voltage': total_voltage,
            'resistance': resistance,
            'power': total_voltage * current
        }
    else:  # AC режим
        # Расчет импеданса Z = R + j(ωL - 1/ωC)
        omega = 2 * np.pi * frequency
        reactance = omega * inductance - 1/(omega * capacitance) if capacitance > 0 else omega * inductance
        impedance = np.sqrt(resistance**2 + reactance**2)
        
        current_magnitude = total_voltage / impedance if impedance > 0 else 0
        phase_shift = np.arctan2(reactance, resistance)
        
        return {
            'ac_current_magnitude': current_magnitude,
            'phase_shift_radians': phase_shift,
            'phase_shift_degrees': np.degrees(phase_shift),
            'impedance': impedance,
            'reactance': reactance,
            'voltage': total_voltage,
            'frequency': frequency,
            'power_real': total_voltage * current_magnitude * np.cos(phase_shift),
            'power_reactive': total_voltage * current_magnitude * np.sin(phase_shift)
        }

def voltage_modulated_conductivity(
    voltage: InformationVoltage,
    base_conductivity: float
) -> float:
    """
    Модуляция проводимости напряжением (высокое напряжение может пробить сопротивление)
    """
    total_voltage = voltage.calculate_total_voltage()
    
    # Эффект "пробоя" при высоком напряжении
    breakthrough_threshold = 7.0  # Пороговое напряжение
    if total_voltage > breakthrough_threshold:
        breakthrough_factor = 1.0 + (total_voltage - breakthrough_threshold) * 0.5
        return base_conductivity * breakthrough_factor
    
    # Обычная модуляция
    voltage_factor = 1.0 + 0.1 * (total_voltage - 5.0)  # Нормальное напряжение ~5
    return base_conductivity * max(0.1, voltage_factor)

def voltage_stress_resistance(
    voltage: InformationVoltage,
    base_resistance: float
) -> float:
    """
    Влияние напряжения на сопротивление (стресс от высокого напряжения)
    """
    total_voltage = voltage.calculate_total_voltage()
    
    # Стресс от высокого эмоционального заряда
    emotional_stress = abs(voltage.emotional_charge) * 2.0
    
    # Стресс от противоречия убеждениям (низкая достоверность + высокое напряжение)
    credibility_stress = (1.0 - voltage.credibility_field) * total_voltage * 0.3
    
    # Общий стресс-фактор
    total_stress = emotional_stress + credibility_stress
    stress_multiplier = 1.0 + total_stress * 0.5
    
    return base_resistance * stress_multiplier
```

---

## 📈 Типы информационного напряжения

### Предопределенные профили напряжения

```python
class VoltageProfiles:
    """Предопределенные профили информационного напряжения"""
    
    @staticmethod
    def breaking_news() -> InformationVoltage:
        """Напряжение срочных новостей"""
        return InformationVoltage(
            authority_potential=0.7,    # Авторитетные источники
            emotional_charge=0.8,       # Высокий эмоциональный заряд
            social_proof=0.9,          # Сильное социальное подтверждение
            relevance_gradient=0.9,     # Высокая релевантность
            credibility_field=0.6,      # Умеренная достоверность (еще проверяется)
            novelty_potential=0.95,     # Максимальная новизна
            urgency_multiplier=1.8,     # Высокая срочность
            context_amplifier=1.5,      # Контекстуальное усиление
            medium_efficiency=0.9       # Эффективные каналы распространения
        )
    
    @staticmethod
    def scientific_breakthrough() -> InformationVoltage:
        """Напряжение научного прорыва"""
        return InformationVoltage(
            authority_potential=0.95,   # Максимальный авторитет
            emotional_charge=0.3,       # Умеренный эмоциональный заряд
            social_proof=0.4,          # Умеренное социальное подтверждение
            relevance_gradient=0.7,     # Высокая релевантность для экспертов
            credibility_field=0.9,      # Высокая достоверность
            novelty_potential=0.9,      # Высокая новизна
            urgency_multiplier=1.2,     # Умеренная срочность
            context_amplifier=1.0,      # Нейтральный контекст
            medium_efficiency=0.7       # Академические каналы
        )
    
    @staticmethod
    def viral_meme() -> InformationVoltage:
        """Напряжение вирусного мема"""
        return InformationVoltage(
            authority_potential=0.1,    # Низкий авторитет источника
            emotional_charge=0.7,       # Высокий эмоциональный заряд
            social_proof=0.95,         # Максимальное социальное подтверждение
            relevance_gradient=0.8,     # Высокая релевантность для аудитории
            credibility_field=0.2,      # Низкая достоверность
            novelty_potential=0.6,      # Умеренная новизна
            urgency_multiplier=1.0,     # Без срочности
            context_amplifier=2.0,      # Сильное контекстуальное усиление
            medium_efficiency=0.95      # Высокоэффективные социальные сети
        )
    
    @staticmethod
    def corporate_announcement() -> InformationVoltage:
        """Напряжение корпоративного объявления"""
        return InformationVoltage(
            authority_potential=0.6,    # Умеренный авторитет
            emotional_charge=0.1,       # Низкий эмоциональный заряд
            social_proof=0.3,          # Умеренное социальное подтверждение
            relevance_gradient=0.5,     # Средняя релевантность
            credibility_field=0.8,      # Высокая достоверность
            novelty_potential=0.4,      # Умеренная новизна
            urgency_multiplier=1.1,     # Слабая срочность
            context_amplifier=0.8,      # Слабый контекстуальный эффект
            medium_efficiency=0.6       # Официальные каналы
        )
    
    @staticmethod
    def propaganda() -> InformationVoltage:
        """Напряжение пропагандистского содержания"""
        return InformationVoltage(
            authority_potential=0.5,    # Умеренный авторитет (часто ложный)
            emotional_charge=-0.8,      # Сильный негативный заряд
            social_proof=0.7,          # Искусственное социальное подтверждение
            relevance_gradient=0.6,     # Целенаправленная релевантность
            credibility_field=0.3,      # Низкая реальная достоверность
            novelty_potential=0.3,      # Низкая новизна (повторяющиеся нарративы)
            urgency_multiplier=1.6,     # Искусственная срочность
            context_amplifier=1.8,      # Сильное контекстуальное усиление
            medium_efficiency=0.8       # Эффективные каналы распространения
        )

def analyze_voltage_profile(voltage: InformationVoltage) -> Dict[str, str]:
    """Анализ профиля напряжения и определение типа контента"""
    components = voltage.calculate_voltage_by_component()
    total_voltage = components['total']
    
    # Определение доминирующих компонентов
    dominant_components = []
    if components['authority'] > 0.7:
        dominant_components.append('authority')
    if components['emotional'] > 0.6:
        dominant_components.append('emotional')
    if components['social'] > 0.7:
        dominant_components.append('social')
    if components['credibility'] < 0.4:
        dominant_components.append('low_credibility')
    
    # Классификация типа
    content_type = "unknown"
    if 'authority' in dominant_components and voltage.credibility_field > 0.8:
        content_type = "scientific_or_expert"
    elif 'social' in dominant_components and 'emotional' in dominant_components:
        content_type = "viral_content"
    elif voltage.urgency_multiplier > 1.5 and voltage.novelty_potential > 0.8:
        content_type = "breaking_news"
    elif 'low_credibility' in dominant_components and voltage.emotional_charge < -0.5:
        content_type = "potential_misinformation"
    
    # Оценка потенциального воздействия
    impact_level = "low"
    if total_voltage > 7.0:
        impact_level = "very_high"
    elif total_voltage > 5.0:
        impact_level = "high"
    elif total_voltage > 3.0:
        impact_level = "medium"
    
    return {
        'content_type': content_type,
        'impact_level': impact_level,
        'dominant_components': dominant_components,
        'total_voltage': f"{total_voltage:.2f}",
        'polarity': 'positive' if voltage.get_polarity() > 0 else 'negative'
    }
```

---

## 🧪 Экспериментальная валидация

### Протоколы измерения напряжения

```python
class VoltageValidationExperiment:
    """Экспериментальные протоколы для валидации модели напряжения"""
    
    def __init__(self):
        self.voltage_calculator = InformationVoltageCalculator()
    
    def validate_voltage_current_relationship(
        self,
        content_samples: List[Dict],
        participants: int = 100
    ) -> Dict[str, float]:
        """
        Валидация связи напряжения с током (скоростью обработки)
        
        Протокол:
        1. Рассчитать напряжение для образцов контента
        2. Измерить скорость обработки участниками
        3. Проверить корреляцию U_info vs I_info (время реакции)
        """
        results = {
            'voltage_vs_processing_speed': [],
            'emotional_charge_vs_attention': [],
            'authority_vs_acceptance_rate': [],
            'social_proof_vs_sharing_probability': []
        }
        
        for sample in content_samples:
            # Расчет напряжения
            voltage = self._calculate_sample_voltage(sample)
            
            # Экспериментальные измерения (заглушки)
            processing_speed = self._measure_processing_speed(sample, participants)
            attention_duration = self._measure_attention_duration(sample, participants)
            acceptance_rate = self._measure_acceptance_rate(sample, participants)
            sharing_probability = self._measure_sharing_probability(sample, participants)
            
            # Сбор данных для корреляций
            results['voltage_vs_processing_speed'].append(
                (voltage.calculate_total_voltage(), processing_speed)
            )
            results['emotional_charge_vs_attention'].append(
                (abs(voltage.emotional_charge), attention_duration)
            )
            results['authority_vs_acceptance_rate'].append(
                (voltage.authority_potential, acceptance_rate)
            )
            results['social_proof_vs_sharing_probability'].append(
                (voltage.social_proof, sharing_probability)
            )
        
        return self._calculate_correlations(results)
    
    def validate_voltage_energy_model(
        self,
        content_samples: List[Dict]
    ) -> Dict[str, float]:
        """
        Валидация связи напряжения с энергозатратами
        """
        energy_model = VoltageEnergyModel()
        correlations = {}
        
        for sample in content_samples:
            voltage = self._calculate_sample_voltage(sample)
            
            # Предсказанные энергозатраты
            predicted_energy = energy_model.calculate_voltage_energy_relationship(voltage)
            
            # Измеренные энергозатраты (заглушки)
            measured_energy = self._measure_cognitive_energy(sample)
            
            # Данные для корреляционного анализа...
        
        return correlations
    
    # Заглушки для экспериментальных методов
    def _calculate_sample_voltage(self, sample: Dict) -> InformationVoltage:
        """Заглушка для расчета напряжения образца"""
        return VoltageProfiles.breaking_news()  # Пример
    
    def _measure_processing_speed(self, sample: Dict, participants: int) -> float:
        """Заглушка для измерения скорости обработки"""
        return 1.0
    
    def _measure_attention_duration(self, sample: Dict, participants: int) -> float:
        """Заглушка для измерения продолжительности внимания"""
        return 1.0
    
    def _measure_acceptance_rate(self, sample: Dict, participants: int) -> float:
        """Заглушка для измерения уровня принятия"""
        return 0.5
    
    def _measure_sharing_probability(self, sample: Dict, participants: int) -> float:
        """Заглушка для измерения вероятности репоста"""
        return 0.3
    
    def _measure_cognitive_energy(self, sample: Dict) -> Dict[str, float]:
        """Заглушка для измерения когнитивной энергии"""
        return {'total_energy': 1.0}
    
    def _calculate_correlations(self, results: Dict) -> Dict[str, float]:
        """Заглушка для расчета корреляций"""
        return {key: 0.5 for key in results.keys()}
```

---

## 🎯 Практические применения

### 1. Система рекомендаций

```python
class VoltageBasedRecommendationSystem:
    """Система рекомендаций на основе информационного напряжения"""
    
    def __init__(self):
        self.voltage_calculator = InformationVoltageCalculator()
    
    def recommend_content(
        self,
        user_profile: Dict,
        available_content: List[Dict],
        target_voltage_range: Tuple[float, float] = (3.0, 7.0)
    ) -> List[Dict]:
        """
        Рекомендация контента с оптимальным напряжением
        """
        recommendations = []
        
        for content in available_content:
            # Расчет напряжения для пользователя
            voltage = self._calculate_personalized_voltage(content, user_profile)
            total_voltage = voltage.calculate_total_voltage()
            
            # Фильтрация по диапазону напряжения
            if target_voltage_range[0] <= total_voltage <= target_voltage_range[1]:
                recommendations.append({
                    'content': content,
                    'voltage': total_voltage,
                    'components': voltage.calculate_voltage_by_component(),
                    'estimated_impact': self._estimate_impact(voltage, user_profile)
                })
        
        # Сортировка по оптимальности
        recommendations.sort(key=lambda x: x['estimated_impact'], reverse=True)
        
        return recommendations[:10]  # Топ-10 рекомендаций
```

### 2. Детектор дезинформации

```python
class MisinformationVoltageDetector:
    """Детектор дезинформации на основе анализа напряжения"""
    
    def __init__(self):
        self.voltage_calculator = InformationVoltageCalculator()
        
        # Паттерны подозрительного напряжения
        self.suspicious_patterns = {
            'high_emotional_low_credibility': lambda v: (
                abs(v.emotional_charge) > 0.7 and v.credibility_field < 0.4
            ),
            'artificial_urgency': lambda v: (
                v.urgency_multiplier > 1.5 and v.novelty_potential < 0.3
            ),
            'fake_authority': lambda v: (
                v.authority_potential > 0.7 and v.credibility_field < 0.5
            ),
            'emotional_manipulation': lambda v: (
                abs(v.emotional_charge) > 0.8 and v.social_proof > 0.8 and v.credibility_field < 0.6
            )
        }
    
    def analyze_content_risk(self, content: Dict) -> Dict[str, float]:
        """Анализ риска дезинформации"""
        voltage = self._calculate_content_voltage(content)
        
        # Проверка подозрительных паттернов
        risk_scores = {}
        for pattern_name, pattern_func in self.suspicious_patterns.items():
            if pattern_func(voltage):
                risk_scores[pattern_name] = 1.0
            else:
                risk_scores[pattern_name] = 0.0
        
        # Общий риск
        total_risk = sum(risk_scores.values()) / len(risk_scores)
        
        return {
            'total_risk': total_risk,
            'risk_factors': risk_scores,
            'voltage_profile': voltage.calculate_voltage_by_component(),
            'recommendation': self._get_risk_recommendation(total_risk)
        }
```

### 3. Оптимизатор контента

```python
class ContentVoltageOptimizer:
    """Оптимизатор контента для достижения целевого напряжения"""
    
    def optimize_for_target_voltage(
        self,
        content: Dict,
        target_voltage: float,
        target_audience: Dict
    ) -> Dict[str, str]:
        """Оптимизация контента для достижения целевого напряжения"""
        
        current_voltage = self._calculate_content_voltage(content, target_audience)
        current_total = current_voltage.calculate_total_voltage()
        
        suggestions = []
        
        if current_total < target_voltage:
            # Увеличение напряжения
            if current_voltage.emotional_charge < 0.5:
                suggestions.append("Добавьте эмоциональные элементы")
            if current_voltage.social_proof < 0.5:
                suggestions.append("Включите социальные доказательства")
            if current_voltage.urgency_multiplier < 1.3:
                suggestions.append("Подчеркните срочность или актуальность")
        else:
            # Снижение напряжения
            if abs(current_voltage.emotional_charge) > 0.7:
                suggestions.append("Смягчите эмоциональный тон")
            if current_voltage.urgency_multiplier > 1.5:
                suggestions.append("Уберите элементы искусственной срочности")
        
        return {
            'current_voltage': current_total,
            'target_voltage': target_voltage,
            'optimization_suggestions': suggestions
        }
```

---

## 📊 Экспериментальные предсказания

### Основные гипотезы для валидации

1. **Напряжение-Ток корреляция:**
   - H1: Информационное напряжение положительно коррелирует со скоростью обработки (r > 0.6)
   - H2: Эмоциональный заряд увеличивает продолжительность внимания (r > 0.5)
   - H3: Авторитетный потенциал снижает время на проверку информации (r < -0.4)

2. **Компонентные эффекты:**
   - H4: Социальное подтверждение увеличивает вероятность репоста (r > 0.7)
   - H5: Низкая достоверность при высоком напряжении вызывает когнитивный диссонанс
   - H6: Новизна увеличивает энергозатраты на обработку (r > 0.6)

3. **Типы контента:**
   - H7: Научный контент имеет высокий авторитет + низкий эмоциональный заряд
   - H8: Вирусный контент имеет высокое социальное подтверждение + эмоциональный заряд
   - H9: Дезинформация имеет паттерн высокий эмоциональный заряд + низкая достоверность

---

## ✅ Заключение

Модель информационного напряжения предоставляет:

1. **Формальную основу** для измерения "силы воздействия" информации
2. **Многокомпонентную структуру** учитывающую авторитет, эмоции, социальные факторы
3. **Интеграцию с энергетической моделью** для реалистичного моделирования затрат
4. **Операционализируемые метрики** для различных типов контента
5. **Практические инструменты** для рекомендаций, детекции дезинформации и оптимизации

Модель готова к:
- Экспериментальной валидации с участниками
- Интеграции с полной системой Information Dynamics (G, R, L, C)
- Практическому применению в информационных системах

**Статус:** ✅ **ЗАДАЧА 2.2.2 ЗАВЕРШЕНА УСПЕШНО** 