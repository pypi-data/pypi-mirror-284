# python_logger

Даний пакет розроблений для логування дій сервісу у структурі ELK.

## Опис функціоналу

### Класи

#### StructuredMessage

Клас StructuredMessage є обгорткою для формування одного запису логу.

##### init

| Назва параметру | Тип    | Опис                                                                                       |
|-----------------| ------ |--------------------------------------------------------------------------------------------|
| message          | String | Повідомлення. Буде записано у поле `message`                                               |
| **kwargs          | String | Інші рядки логу. Будуть записані у відповідне поле з такою самою назвою, яку буде передано |

Приклад виклику:

```python
from softpro_elk_grpc_logger import StructuredMessage

StructuredMessage("OK", function='Render', ip='127.0.0.1', level='INFO')
```

##### str

Обгортка для перетворення одного запису логу з `json` у рядок. Викликається автоматично при преведення типу даних до `str`.

### Функції

#### setup_logger

Функція створення логеру. Створена для спрощення роботи з модулем

##### Параметри

| Назва        | Тип    | Опис                                                                                           |  Значення за замовчуванням  |
|--------------|--------|------------------------------------------------------------------------------------------------|:---------------------------:|
| log_filename | String | Шлях до логу, або ім'я. Якщо передається ім'я - то лог створиться у директорії виклику скрипту |       structured.log        |

```python
from softpro_elk_grpc_logger import setup_logger

logger = setup_logger(log_filename='../test_log.log') # створює лог на директорію вище (за деревом) з назвою test_log

logger = setup_logger(log_filename='/your/directory/path/test_log.log') # створю лог за шляхом /your/directory/path з назвою test_log

logger = setup_logger(log_filename='test_log.log') # створю лог у директорії виклику скрипта з назвою test_log
```

## Встановлення модуля

### pip

```commandline
pip3 install softpro_elk_grpc_logger
```

### from git

```commandline
git clone https://git.softpro.ua/service/python_logger
pip3 install setuptools wheel
python3 /path/to/repo/setup.py sdist bdist_wheel
```

## Рекомендації

Рекомендовано використовувати virtualenv для локальної роботи з модулем