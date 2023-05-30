## 环境

```bash
source ./venv/bin/activate
deactivate
```

## 依赖管理

```bash
pip install xlrd==1.2.0

pip freeze > requirements.txt

pip install -r requirements.txt
```

## 把 db-struct.py 打包成可执行文件

```bash
pip install pyinstaller

pyinstaller -w -F dbstruct.py && mv dist/dbstruct /usr/local/bin/dbstruct && rm -rf dist build dbstruct.spec

./dbstruct --env=IO --db=octopus --table=user
```