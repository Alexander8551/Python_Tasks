# Task5
- Скачайте и установите приложение orange.
- Выберите датасет титаника. 
- Посмотрите на все факторы и определите, какие оказывают большее влияние на таргет и почему.
- Обучите любую модель. Точность вашей модели должна быть больше 80.
- Вы можете менять параметры модели и датасет
- В качестве ответа должен быть ows файл(из программы orange) и текстовый документ, где вы указываете наиболее важные параметры и даете свое предположение, почему они являются наиболее важными 


# Solution
В этом датасете целевой переменной является `survived`, т.к. основная задача анализа этого датасета — предсказать, выживет пассажир или нет.

### Наиболее важные факторы:

1. *Пол (sex):* Женщины имели более высокие шансы на выживание.

2. *Класс пассажира (status):* Пассажиры первого класса имели больше шансов на выживание.

#### Предположения:

- Женщины и дети имели приоритет при спасении, что объясняет важность этих факторов.
- Социальный статус (`status`) также может влиять, так как пассажиры первого класса имели больше шансов на спасение.