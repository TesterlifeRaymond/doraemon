
[![Build Status](https://travis-ci.org/TesterlifeRaymond/doraemon.svg?branch=master)](https://travis-ci.org/TesterlifeRaymond/doraemon)

#   这是一个自动生成接口测试测试用例的项目, 您可以通过如下方式使用他

> run in python3
当你git clone 该项目后,可以通过如下命令配置你的环境

```python
>>> cd doraemon
>>> . venv/bin/activate
>>> pip3 install -r requirements.txt
```
## 测试用例的编写
-----------------
* 在根路径下找到cases路径
* 在cases路径下, 新增 `.json `尾缀的文件

* 如果是单个文件单个case, 可参考如下示例: `test_history_day.json`


```json
{
  "test_get_history_days": {
    "url": "http://api.juheapi.com/japi/toh",
    "params": "v=&month=&day=&key=1d39d53a70ebed87d5cabbc8b73b96e2",
    "method": "get",
    "desc": "测试历史上的今天接口, get请求",
    "assert": {
      "result": ["len", 0],
      "error_code": 10005
    }
  }
}
```

> 用字典包含字典的结构进行保存

> 在上面的示例中, {key: {...}}, 
* 文件名表示生成测试用例中的class的命名(以test开头,下划线分割多个单词)
* key表示测试方法名, 如果需要case有序执行, 可以将示例中: test_get_history_days 修改为`test_1_get_history_days`
* key对应的字典, 是这条case中所有的需要用到的参数, 目前支持结构体如下



key | value | Sample
------------ | -------------| ----------------
ResponseType| 验证返回结构体类型 | {"ResponseType": ["type", "dict"]}(支持字段类型验证)   
url | 对应接口地址 | http://api.juheapi.com/japi/toh
method | 请求方法 | get
desc | 测试报告对应的用例描述信息 |  测试历史上的今天接口, get请求
assert | 测试断言数据 | {"result": ["len", 0], "error_code": 10005}
params | get方法需要传递的数据 | v=&month=&day=&key=1d39d53a70ebed87d5cabbc8b73b96e2
data | post提交表单数据 | {"pno":1,"ps":30,"dtype":"json","key":"4beb9d77d2b95ce9bec6d8363ee5a620"}
json | post提交json数据 | {"pno":1,"ps":30,"dtype":"json","key":"4beb9d77d2b95ce9bec6d8363ee5a620"}
schema | 需要断言返回数据的结构体验证 | TODO
headers | 请求头信息 | {"User-Agent":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit\/537.36 (KHTML,like Gecko) Chrome\/63.0.3239.132 Safari\/537.36"}
cookies | 需要自定义cookies信息 | 字典类型的key value 键值对


## run.py
----------------
当你编写完成测试用例后, 可以通过以下命令运行测试
```python
python3 run.py
>>> Testing ...
```

run.py是一个可以接受外部传参的文件, 当你需要自定义`测试用例路径`/ `测试报告生成路径` / `测试用例的Pattern`时, 可以先通过 ```python3 run.py --help``` 来查看对应的入参后按需修改

```python
☁  doraemon [master] ⚡ python3 run.py --help
Usage: run.py [OPTIONS]

Options:
  --cases TEXT    case file path
  --pattern TEXT  get cases file pattern
  --report TEXT   generator report in path
  --help          Show this message and exit.
```

默认参数配置如下
```python
@click.option('--cases', default='src/testcases/', help="case file path")
@click.option('--pattern', default='*.py', help="get cases file pattern")
@click.option('--report', default='src/report/', help="generator report in path")
```

## 测试报告

当测试运行完成后, 可以通过进入src/report路径, 找到执行用例后生成的测试报告, 如下图:

![report.html](https://raw.githubusercontent.com/TesterlifeRaymond/doraemon/master/imgs/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.png)

--------------

如果大家在使用过程中, 发现任何问题可以提交issues 或直接给我发邮件`liujinjia@testerlife.com`
希望大家喜欢这个项目!

