### 发送简单的请求

- 需求：通过requests向百度首页发送请求，获取百度首页的数据

```python
import requests
response = requests.get(url)
```

- response的常用方法：
  - response.text
  - response.content
  - response.status_code
  - response.request.headers
  - response.headers

### 判断请求是否成功

