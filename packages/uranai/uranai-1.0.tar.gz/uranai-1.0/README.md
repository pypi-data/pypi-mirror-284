# Pythonで今日の星座占い

## ```pip install Uranai```

## 必要なモジュール
- requests
- beautifulsoup4

#### example.py  
```py
from uranai import Uranai

u = Uranai(proxy = None)#一応プロキシ入れれるよ

print(u.do())#jsonで帰ってくるよ
```

### まじで簡単

made by こーた