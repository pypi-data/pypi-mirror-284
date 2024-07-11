# Различные утилиты которые лень писать каждый раз 

- `saver` (Предназначена для сохранения файлов)
- `ua` (Ротация юзер агентов. Мне не очень нравятся другие библиотеки)
- `repo` (Базовый репозиторий для crud операция а также фабрика через метакласс)
- `parsed` (Сохраняет в csv спарсенные и не удачно спарсенные файлы) 
- `proxy` (Менеджер для сервиса ротации прокси (самописного))


























## ProxyManager()

При активном использовании прокси во время парсинга возникает проблема постоянного перекидывания прокси из проекта в проект.  

Для использования данного модуля: необходимо развернуть АПИ на сервере. [использованное api](https://github.com/mangustik228/api_proxy)

Установка:
```bash
pip install mangust228
```
---


### Пример получения актуальных прокси:
```python
from mangust228 import ProxyManager

proxies = ProxyManager('your_token', 'your_url')
proxies.get('string') 
# [{http://user:pass@127.0.0.1:8000},...]
proxies.get('dict[str,str]')
# [{'server':'http://127.0.0.1:8000','username':'user','password':'pass'}, ...]
proxies.get('playwright')
# [{'proxy':{'server':'http://127.0.0.1:8000','username':'user','password':'pass'}},...]
```

---

### Пример получения списка всех прокси (включая просроченные)
```python
proxies = ProxyManager('your_token', 'your_url')
proxies.get_full()
```
Можно указать путь (только csv!), тогда результат будет сохранен в `csv` файл
```python
proxies.get_full('all_proxies.csv')
```
---

### Пример добавления прокси
```python
data = [{
    'server':'127.0.0.1',
    'port':8000,
    'username':'user',
    'password':'pass',
    'expire':'2023-12-31',
    'service':'example.service.com'
},...]
proxies = ProxyManager(token, url)
proxies.post(data=data)
```

Можно добавлять из файлов excel или csv
```python
proxies.post(path='example.csv')
```
---
### Пример удаления прокси
```python
proxies.delete(id)
```
---
### Пример изменения прокси
```python
data = {
    'id':1,
    'username':'John'
}
proxies.put(data)
```


## CaptchaAi()
Разгадывалка капчи с сервиса: captchaai.com [Документация](https://captchaai.com/api-docs.php)

На данный момент реализовано только разгадывание картинок.


Пример использования: 
```python
# sync
captcher = CaptchaAi(token)
result = captcher.solve_picture(image)

# async
captcher = CaptchaAi(token, async_=True)
result = await captcher.solve_picture(image)

```

Параметры которые можно передать при инициализации CaptchaAi(): 
- `token` токен который получаем от сервиса
- `async_` передаем, если надо вызывать в асинхронном коде
- `threads` сколько допустимо параллельно запросов(зависит от тарифа). В данный момент не реализовано.

Параметры метода solve_picture(): 
- `timeout` время между отправкой изображения на сервис и получения данных (default=5)
- `retries` сколько раз попытаться получить ответ от сервера(default=3)
- `phrase` см.документацию [link](https://captchaai.com/api-docs.php) 
- `regsense` см.документацию [link](https://captchaai.com/api-docs.php) 
- `numeric` см.документацию [link](https://captchaai.com/api-docs.php) 
- `calc` см.документацию [link](https://captchaai.com/api-docs.php) 
- `min_len` см.документацию [link](https://captchaai.com/api-docs.php) 
- `max_len` см.документацию [link](https://captchaai.com/api-docs.php) 
- `language` см.документацию [link](https://captchaai.com/api-docs.php) 
- `lang` см.документацию [link](https://captchaai.com/api-docs.php) 
Параметры `json` & `method` НЕ ПОДДЕРЖИВАЮТСЯ.