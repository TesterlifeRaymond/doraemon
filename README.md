[![Build Status](https://travis-ci.org/TesterlifeRaymond/doraemon.svg?branch=master)](https://travis-ci.org/TesterlifeRaymond/doraemon)

#   这是一个自动生成测试用例的项目, 您可以通过如下方式使用他

> run in python3

1： 在case_file 路径下， 找到case.txt， 并按照uri/class_name/func_name/body/assert_key 的顺序进行编写case， 分隔符为3空格
2： case.txt录入完成后， 可直接运行run.py 进行测试， 测试完成后， 可在app/report路径查看测试结果

示例如下：

1: 编写测试case及基础数据（断言情况等）
![case.txt](https://raw.githubusercontent.com/TesterlifeRaymond/doraemon/master/img/case-txt.png)

2: 运行run文件后， 自动在`app/constructor/case`路径下生成case
![python3 run.py](https://raw.githubusercontent.com/TesterlifeRaymond/doraemon/master/img/created-testcase.png)

3: 当case 执行完成后， 会在`app/report`路径下生成`report.html`
![report.html](https://raw.githubusercontent.com/TesterlifeRaymond/doraemon/master/img/text-case-report.png)

4: 如果需要使用x-test 下游报表系统
![x-test](https://raw.githubusercontent.com/TesterlifeRaymond/doraemon/master/img/x-test.png)

`请参照 x-test wiki  http://api.apiapp.cc/static/wiki/index.html#id17 进行操作， 或查看 http://git.oschina.net/x-utest/xtest-python-demo`
