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


curl  -X POST -H "Content-Type: application/json" -d '{"username":"chenying1","password":"123456"}' http://localhost:5000/api/v1/auth/login

```
