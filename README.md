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
python3 -m pip --version

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
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
Используйте `curl` или Postman:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"sepal_length": 1.2, "sepal_width": 3.4, "petal_length": 5.6, "petal_width": 2.1}'

```

### 6. Запуск в Docker
```bash
docker build -t random_forest_api .
docker run -p 8000:8000 random_forest_api
```

## Отслеживание экспериментов в MLflow
Для просмотра метрик откройте MLflow UI:
```bash
python3 -m mlflow --version

```
Затем откройте в браузере: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Автор
Kutubaeva Madina Bakytkyzy

