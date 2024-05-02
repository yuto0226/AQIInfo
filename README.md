# AQIInfo

## 虛擬環境

[參考資料：虛擬環境與套件](https://docs.python.org/zh-tw/3/tutorial/venv.html)

```zsh
venv/Scripts/activate   # 啟動虛擬環境
deactivate              # 停用虛擬環境
```

套件安裝

```zsh
python -m pip freeze > requirements.txt     # 凍結當前套件版本
python -m pip install -r requirements.txt   # 安裝需求套件
```
