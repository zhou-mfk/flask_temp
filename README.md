# Flask Template Project


This is a Template for Flask use Poetry manager python lib

python version is 3.11+

## Poetry

```shell
pip install poetry
# or

pipx install poetry

# install
cd your_project
poetry install

```

### pre-commit
use pre-commit check python code style.

```shell
pip install pre-commit
# or
pipx install pre-commit

# install
pre-commit install
```

**.pre-commit-config.yaml** is a config use pre-commit. you can read details from it.

- black 代码格式化工具
- isort 包导入顺序
- ruff python 语法检查
- mypy python 类型注解检查工具
- pytest 测试工具
- coverage 测试覆盖率

### chanage project name

**flask_temp** is a default name. your need change it

### flask command

your need edit wsgi.py file chanage your project name.

```shell
# in fish
set FALSK_APP wsgi.py
```

```shell
flask run
```
