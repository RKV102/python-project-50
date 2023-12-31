### Описание проекта

Проект посвящён разработке CLI-утилиты, которая сравнивает два поступающих в неё JSON-файла и показывает их совпадения и различия.
Если в первом файле есть ключи, которые отсутствуют во втором, то они будут помечены знаком «-», и, наоборот, если во втором файле находятся ключи, отсутствующие в первом файле, они будут помечены знаком «+». В случае, если оба файла содержат один и тот же ключ с разными значениями, сначала будет выведен ключ и значение из первого файла, а затем из второго.

### Как работать с программой

[![asciicast](https://asciinema.org/a/DIEZBakTBQ0GrmKflEYLhEJaT.svg)](https://asciinema.org/a/DIEZBakTBQ0GrmKflEYLhEJaT)

### Статус непрерывной интеграции:

[![Actions Status](https://github.com/RKV102/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RKV102/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/351625b2f9d5681b70da/maintainability)](https://codeclimate.com/github/RKV102/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/351625b2f9d5681b70da/test_coverage)](https://codeclimate.com/github/RKV102/python-project-50/test_coverage)