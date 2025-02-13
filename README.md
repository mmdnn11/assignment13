# Random Forest Classifier API

Этот проект представляет собой API для модели машинного обучения, построенной на основе алгоритма RandomForestClassifier. API создано с использованием FastAPI, MLflow для отслеживания экспериментов и Docker для контейнеризации.

## Структура проекта

```
random_forest_project/
│── app.py             # FastAPI сервер
│── train.py           # Обучение модели
│── model.joblib       # Сохранённая модель
│── Dockerfile         # Файл для контейнеризации
│── requirements.txt   # Зависимости проекта
│── README.md          # Описание проекта
│── mlruns/            # Логи MLflow
```

## Установка и запуск проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/mmdnn11/assignment13.git
cd assignment13
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Обучение модели
```bash
python3 train.py
```

### 4. Запуск FastAPI сервера
```bash
python3 -m uvicorn app:app --reload

```

После запуска сервер будет доступен по адресу: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. Запрос к API
Можно отправить POST-запрос с JSON-данными:
```json
{
  "feature1": 1.2,
  "feature2": 3.4,
  "feature3": 5.6
}
```
Используйте `curl` или Postman:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"feature1": 1.2, "feature2": 3.4, "feature3": 5.6}'
```

### 6. Запуск в Docker
```bash
docker build -t random_forest_api .
docker run -p 8000:8000 random_forest_api
```

## Отслеживание экспериментов в MLflow
Для просмотра метрик откройте MLflow UI:
```bash
mlflow ui
```
Затем откройте в браузере: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Автор
Kutubaeva Madina Bakytkyzy

