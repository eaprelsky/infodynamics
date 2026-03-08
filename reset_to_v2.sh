#!/bin/bash
# Инфодинамика: обнуление репозитория, переход на v2
# Запускать из WSL: bash /mnt/d/repos/infodynamics/reset_to_v2.sh

set -e
cd /mnt/d/repos/infodynamics

echo "=== 1. Тег текущего состояния ==="
git add -A
git commit -m "pre-v2: сохранение текущего состояния перед обнулением" --allow-empty
git tag v1-archive -m "v1: электрическая аналогия, январь 2025"
echo "Тег v1-archive создан. Вернуться: git checkout v1-archive"

echo ""
echo "=== 2. Исправление структуры v2/ ==="
# Полный TERRITORY_MAP в theory/ (заменяем заглушку)
cp v2/TERRITORY_MAP.md v2/theory/TERRITORY_MAP.md
# RESEARCH_MAP в theory/
cp v2/RESEARCH_MAP_V2.md v2/theory/RESEARCH_MAP.md
# Убираем дубли из корня v2/
rm -f v2/MANIFESTO_V2.md
rm -f v2/TERRITORY_MAP.md
rm -f v2/RESEARCH_MAP_V2.md

echo ""
echo "=== 3. Удаление всего старого ==="
# Удаляем всё кроме .git/, v2/ и этого скрипта
find . -maxdepth 1 \
  ! -name '.' \
  ! -name '.git' \
  ! -name '.gitignore' \
  ! -name 'v2' \
  ! -name 'reset_to_v2.sh' \
  -exec rm -rf {} +

echo ""
echo "=== 4. Перемещение v2/ в корень ==="
cp -r v2/* .
cp -r v2/observations .
cp -r v2/theory .
cp -r v2/experiments .
rm -rf v2

echo ""
echo "=== 5. Новый .gitignore ==="
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.ipynb_checkpoints/
.DS_Store
*.egg-info/
.env
.venv/
reset_to_v2.sh
EOF

echo ""
echo "=== 6. Коммит ==="
rm -f reset_to_v2.sh
git add -A
git commit -m "v2 reset: наблюдения, карта территории, трансформация через масштабы

Обнуление репозитория. Электрическая аналогия сохранена в тег v1-archive.

Новая структура:
- observations/MANIFESTO.md: четыре наблюдения, критика v1, свойства информации
- theory/TERRITORY_MAP.md: пять масштабов, пять сквозных паттернов
- theory/RESEARCH_MAP.md: математические кандидаты (IB, Байес, Active Inference, IG)
- theory/TRANSFORMATION_ACROSS_SCALES.md: трансформация от нейрона до цивилизации

Центральная гипотеза: информация = событие, изменяющее модель мира агента."

echo ""
echo "=== ГОТОВО ==="
echo "Структура:"
find . -not -path './.git/*' -not -name '.git' | sort
echo ""
echo "Тег v1-archive сохранён. Чтобы посмотреть старый код: git show v1-archive:theory/ohms_law_information.md"
