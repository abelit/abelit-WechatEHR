# abelit-WechatEHR

## setup.cfg
```yml
# setup.cfg
[metadata]
name = wechatehr
version = 1.0.0-alpha
url = https://github.com/abelit/abelit-WechatEHR
project_urls =
    Documentation = https://github.com/abelit/abelit-WechatEHR
    Code = https://github.com/abelit/abelit-WechatEHR
    Issue tracker = hhttps://github.com/abelit/abelit-WechatEHR/issues
license = BSD-3-Clause
license_files = file: LICENSE.rst
author = Abelit
author_email = ychenid@live.com
maintainer = Abelit
maintainer_email = ychenid@live.com
description = The basic wechat ehr program.
long_description = README.rst
long_description_content_type = text/x-rst
classifiers =
    Development Status :: 5 - Development/Alphas
    Environment :: Web Environment
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Operating System :: OS Independent
    Programming Language :: Python
    Topic :: Internet :: WWW/HTTP :: Dynamic Content

[options]
package_dir = wechatehr
packages = find:
include_package_data = true
python_requires = >= 3.5

[options.extras_require]
test = pytest

[options.packages.find]
where=wechatehr

[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source = wechatehr
```

## Run 

```bash
export FLASK_APP=wechatehr

flask run
```

##　API
```bash
curl  -X POST -H "Content-Type: application/json" -d '{"alias":"abelit1", "username":"chenying1", "surname":"cy1","email":"cycnenid@live.com","phone":"11285649896", "gender":"1","password":"123456"}' http://localhost:5000/api/v1/auth/register


# 用户登录获取access_token和refresh_token
curl  -X POST -H "Content-Type: application/json" -d '{"username":"chenying1","password":"123456"}' http://localhost:5000/api/v1/auth/login

# 结果
{
  "code": 200, 
  "data": [
    {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDgxNzAzMDcsInR5cGUiOiJhY2Nlc3MiLCJqdGkiOiIyM2Q1NTIwOC1mZWE5LTRhMWUtYjkxNi1hNzg1MmY2ZGNhZjkiLCJpZGVudGl0eSI6ImNoZW55aW5nMSIsImZyZXNoIjpmYWxzZSwiaWF0IjoxNjA4MTY2NzA3LCJuYmYiOjE2MDgxNjY3MDd9.a5Y2nHFenloSzXb2wR4fFzQq_xE-QG7MntDhllmCXUM", 
      "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDgyNTMxMDcsImp0aSI6Ijg5YTc2NGJiLTJjN2QtNDQ4OC04OTZkLTIzOGM3OWY1YTAyYyIsImlkZW50aXR5IjoiY2hlbnlpbmcxIiwidHlwZSI6InJlZnJlc2giLCJpYXQiOjE2MDgxNjY3MDcsIm5iZiI6MTYwODE2NjcwN30.Dh8xf5f5grocRFTl-v1KiN0leTkM6hf8__e8xHzavmQ"
    }
  ], 
  "msg": "get user successfully."
}

# 通过access_token获取信息
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDgxNzAzMDcsInR5cGUiOiJhY2Nlc3MiLCJqdGkiOiIyM2Q1NTIwOC1mZWE5LTRhMWUtYjkxNi1hNzg1MmY2ZGNhZjkiLCJpZGVudGl0eSI6ImNoZW55aW5nMSIsImZyZXNoIjpmYWxzZSwiaWF0IjoxNjA4MTY2NzA3LCJuYmYiOjE2MDgxNjY3MDd9.a5Y2nHFenloSzXb2wR4fFzQq_xE-QG7MntDhllmCXUM" -X GET http://localhost:5000/api/v1/auth/protected

#结果
{
  "logged_in_as": "chenying1"
}

# 通过refresh_token获取新的access_token
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDgyNTMxMDcsImp0aSI6Ijg5YTc2NGJiLTJjN2QtNDQ4OC04OTZkLTIzOGM3OWY1YTAyYyIsImlkZW50aXR5IjoiY2hlbnlpbmcxIiwidHlwZSI6InJlZnJlc2giLCJpYXQiOjE2MDgxNjY3MDcsIm5iZiI6MTYwODE2NjcwN30.Dh8xf5f5grocRFTl-v1KiN0leTkM6hf8__e8xHzavmQ" -X POST http://localhost:5000/api/v1/auth/refresh

# 结果
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDgxNzE5NTgsInR5cGUiOiJhY2Nlc3MiLCJqdGkiOiI0MjlmNzRjYy01YTUzLTQ4ODYtYTllNC1lZTk5MjIzMmE0MjMiLCJpZGVudGl0eSI6ImNoZW55aW5nMSIsImZyZXNoIjpmYWxzZSwiaWF0IjoxNjA4MTY4MzU4LCJuYmYiOjE2MDgxNjgzNTh9.r4WGASWmi5dsXIRhZyf93q2cvKiEmg1XmXvZoxOf2nE"
}

```

# custom status code

```python
# coding:utf-8

class RET:
    OK = "0"
    DBERR = "4001"
    NODATA = "4002"
    DATAEXIST = "4003"
    DATAERR = "4004"
    SESSIONERR = "4101"
    LOGINERR = "4102"
    PARAMERR = "4103"
    USERERR = "4104"
    ROLEERR = "4105"
    PWDERR = "4106"
    REQERR = "4201"
    IPERR = "4202"
    THIRDERR = "4301"
    IOERR = "4302"
    SERVERERR = "4500"
    UNKOWNERR = "4501"


error_map = {
    RET.OK: u"成功",
    RET.DBERR: u"数据库查询错误",
    RET.NODATA: u"无数据",
    RET.DATAEXIST: u"数据已存在",
    RET.DATAERR: u"数据错误",
    RET.SESSIONERR: u"用户未登录",
    RET.LOGINERR: u"用户登录失败",
    RET.PARAMERR: u"参数错误",
    RET.USERERR: u"用户不存在或未激活",
    RET.ROLEERR: u"用户身份错误",
    RET.PWDERR: u"密码错误",
    RET.REQERR: u"非法请求或请求次数受限",
    RET.IPERR: u"IP受限",
    RET.THIRDERR: u"第三方系统错误",
    RET.IOERR: u"文件读写错误",
    RET.SERVERERR: u"内部错误",
    RET.UNKOWNERR: u"未知错误",
}
```