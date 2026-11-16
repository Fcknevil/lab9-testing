# Лабораторная работа №9

GitHub Actions workflow для автоматического запуска pytest.

Локальная проверка:

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -v
```

Для запуска workflow нужно создать GitHub-репозиторий, загрузить содержимое этой папки и сделать push. Workflow находится в `.github/workflows/run-tests.yml`.
