[![Build Status](https://github.com/wea-tools/wea-display-schema/workflows/CI/badge.svg)](https://github.com/wea-tools/wea-display-schema/actions)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

# wea-display-schema

wea-display Data-Model Objects

wea显示数据模型对象

## Installation

```console
pip install wea-display-schema
```

## QuickStart

```python
import wea_display_schema

```

## API Documentation

[Geometry Schema](https://wea-tools.github.io/wea-display-schema/geometry.html)

[Display Schema](https://wea-tools.github.io/wea-display-schema/display.html)

## Local Development

1. Clone this repo locally

```console
git clone git@github.com:wea-tools/wea-display-schema

# or

git clone https://github.com/wea-tools/wea-display-schema
```

2. Install dependencies:

```console
cd wea-display-schema
pip install -r dev-requirements.txt
pip install -r requirements.txt
```

3. Run Tests:

```console
python -m pytest tests/
```

4. Generate Documentation:

```python
python ./docs.py
```
