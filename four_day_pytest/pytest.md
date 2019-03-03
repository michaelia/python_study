#### 安装pytest
```
pip install -U pytest
```
#### 检查pytest是否有装
```
pytest --version
```

#### 创建第一个pytest例子

##### 如何运行pytest，在pycharm运行器上
1. File -> Settings -> Tools -> Python Integrated Tools,在 Default test runner 中选择 Pytes
2. 写有测试函数的文件中直接右键，会出现一个Run 'py.test' for project_name，直接点击即可运行自动化测试。

##### Pytest 测试样例规范
- 测试文件以 test_ 开头（以 _test 结尾也可以） 
- 测试类以 Test 开头，并且不能带有 init 方法
- 测试函数以 test_ 开头
- 断言使用基本的 assert 即可

##### 例子
```
func = lambda x :  x + 1
def test_answer():
    assert func(3) == 5
```
运行结果是
```
test_dome.py:6 (test_answer)
def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_dome.py:8: AssertionError
                                                           [100%]

=================================== FAILURES ===================================
_________________________________ test_answer __________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_dome.py:8: AssertionError
=========================== 1 failed in 0.14 seconds ===========================
Process finished with exit code 0
```
报告告诉原因是方法中返回是4，与期望值5不对应


#### 批量执行
    
pytest 遵循约定查找规则执行，即它执行当前路径（包括子目录）下的以test_ 开头或者 _test 结尾的python文件

pytest的约定规则：
- 如果执行命令中没有指定配置参数，则将会从testpath（如果配置了）或者当前的目录下寻找test_*.py 或者 *_test.py 文件收集test方法进行运行。
- 测试类以Test开头，并且不能带有 __init__ 方法
- 测试函数以test_开头
- 如果找不到测试文件，则执行unittest.TestCase的文件

执行命令参数配置例子：
```
tests/
|-- example
|   |-- test_example_01.py
|   |-- test_example_02.py
|   '-- test_example_03.py
|-- foobar
|   |-- test_foobar_01.py
|   |-- test_foobar_02.py
|   '-- test_foobar_03.py
'-- hello
    '-- world
        |-- test_world_01.py
        |-- test_world_02.py
        '-- test_world_03.py
```
如果执行命令中配置 --ignore=tests/foobar/test_foobar_03.py --ignore=tests/ hello/ 
则运行
```
collected 5 items
tests/example/test_example_01.py .
tests/example/test_example_02.py .
tests/example/test_example_03.py .
tests/foobar/test_foobar_01.py .
tests/foobar/test_foobar_02.py .
[ 20%]
[ 40%]
[ 60%]
[ 80%]
[100%]
========================= 5 passed in 0.02 seconds =========================
```
--ignore 支持模糊搜索配置，例如不执行01的测试case，则在命令中执行--ignore-glob='*_01.py' 

其他配置：
```
py.test test_fun.py   # 执行某个文件
py.test filepath      # 执行指定目录下
py.test test_mod.py::test_func #执行指定方法

```
可以查看更多的命令参数配置执行
```
py.test --fixtures
```



