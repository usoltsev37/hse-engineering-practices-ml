# hse-engineering-practices-ml

### HW02

#### Установка пакетного менеджера Pip (уже установленно, он дефолтный)

#### Развертывание окружения
```
python -m venv ./gender-classifier-cnn/env
```
#### Сборка пакета
```
python setup.py sdist bdist_wheel
```
#### Загрузка пакета на pypi
```
twine upload --repository testpypi dist/*
```
#### Ссылка на пакет в pypi

https://test.pypi.org/project/gender-classifier-cnn-usoltsev37/0.0.1/

#### Установка пакета из pypi
```
pip install -i https://test.pypi.org/simple/ gender-classifier-cnn-usoltsev37==0.0.1
```
#### P.S. 
Попробывал ```poetry```, возникли проблемы с установкой библиотеки torch на mac, это решение мне не помогло https://github.com/python-poetry/poetry/issues/6409?ysclid=lar7tjjma6220333470

### Формтер, линтер и плагины

Я выбрал ```black```, ```isort``` и плагины для ```flake8```:
flake8-spellcheck
flake8-comprehensions 
flake8-docstrings
flake8-eradicate
flake8-builtins