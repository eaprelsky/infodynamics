# Настройка окружения: Информационная динамика

## Установка conda окружения (рекомендуется)

### 1. Создание окружения из файла
```bash
# Создать окружение из environment.yml
conda env create -f environment.yml

# Активировать окружение
conda activate info-dynamics
```

### 2. Альтернативная установка через conda
```bash
# Создать новое окружение
conda create -n info-dynamics python=3.11

# Активировать окружение
conda activate info-dynamics

# Установить основные пакеты
conda install -c conda-forge numpy pandas scipy matplotlib seaborn scikit-learn statsmodels

# Установить дополнительные пакеты
conda install -c conda-forge jupyter jupyterlab nltk spacy networkx plotly

# Установить пакеты через pip
pip install transformers sentence-transformers torch datasets wandb umap-learn hdbscan pymc arviz pingouin factor-analyzer
```

## Альтернативная установка через pip

### Для пользователей без conda:
```bash
# Создать виртуальное окружение
python -m venv info-dynamics-env

# Активировать окружение (Windows)
info-dynamics-env\Scripts\activate

# Активировать окружение (Linux/macOS)
source info-dynamics-env/bin/activate

# Установить зависимости
pip install -r requirements.txt
```

## Проверка установки

### Запустить тестовый скрипт:
```bash
python -c "
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import sklearn
import statsmodels.api as sm
print('✅ Все основные пакеты установлены успешно!')
print(f'NumPy: {np.__version__}')
print(f'Pandas: {pd.__version__}')
print(f'Matplotlib: {plt.matplotlib.__version__}')
print(f'Scikit-learn: {sklearn.__version__}')
"
```

## Дополнительные настройки

### Настройка Jupyter Lab:
```bash
# Установить расширения для JupyterLab
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Запустить JupyterLab
jupyter lab
```

### Настройка spaCy (для NLP анализа):
```bash
# Скачать языковые модели
python -m spacy download en_core_web_sm
python -m spacy download ru_core_news_sm
```

### Настройка NLTK (для text analysis):
```bash
python -c "
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
"
```

## Структура проекта

```
Информационная динамика/
├── environment.yml          # Conda окружение
├── requirements.txt         # Pip зависимости
├── SETUP.md                # Этот файл
├── analysis/               # Скрипты анализа данных
├── experiments/            # Экспериментальные дизайны
├── theory/                 # Теоретические модели
├── data/                   # Данные (создается автоматически)
├── results/                # Результаты анализов
└── notebooks/              # Jupyter notebooks
```

## Решение проблем

### Проблема с установкой PyTorch:
```bash
# Для GPU поддержки (опционально)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Только CPU версия
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Проблема с python-igraph:
```bash
# Для Windows может потребоваться дополнительная установка
conda install -c conda-forge python-igraph

# Или через pip с Visual Studio Build Tools
pip install python-igraph
```

### Проблема с памятью при установке:
```bash
# Увеличить лимит памяти для conda
conda config --set channel_priority flexible

# Установить пакеты по частям
conda install numpy pandas scipy
conda install matplotlib seaborn plotly
conda install scikit-learn statsmodels
```

## Запуск анализа

После установки окружения:

```bash
# Активировать окружение
conda activate info-dynamics

# Запустить валидацию модели проводимости
python simulation/analysis/hcp_conductivity_analysis_simulated.py

# Запустить JupyterLab для интерактивной работы
jupyter lab
```

## Деактивация окружения

```bash
# Деактивировать conda окружение
conda deactivate

# Удалить окружение (если нужно)
conda env remove -n info-dynamics
```

---

**Версия:** 1.0  
**Дата:** Январь 2025  
**Совместимость:** Python 3.11+, Windows/Linux/macOS 