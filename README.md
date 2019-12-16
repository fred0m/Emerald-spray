# V2.0.0更新
* 部分代码重写，增加detailsGeterFixed()方法
# V1.2.2更新
* 修复导入时可能遇到的错误
# V1.2.1更新
* 重写 WebGeter.py
* 修复部分bug
* 包名改为Es
* **去掉 steam250URLGeter 和 steamTop100URLGeter 在在构造时调用的dataHandle()方法，这意味着现在需要手动调用**
* 部分代码重构与逻辑优化

# 特别鸣谢
* Tsubasa

# Emerald-spray
方便的将steam商店页面信息解析出来，并可保存于本地

# 包含模块
* WebGeter
* DataAnalysis
* BugReporter

# 模块功能
## WebGeter
包含一个 WebGeter 类，需要一个接受一个string类型的url作为参数，例如你可以用如下方法调用：
```python
demo = WebGeter("https://fredom.ink")
```

**请注意，接受的url必须包含完整的协议头，也就是说，你不能省略http:// 或者 https:// 前缀**

接着你可以使用
```python
demo.raw_data
```

这是一个数据成员，类型为BeautifulSoup类，可以为下一个模块作为原始数据支持
## DataAnalysis
包含
* steam250URLGeter
* steamTop100URLGeter
* detailsDataGeter

**注意：在使用DataAnalysis时请使用DataAnalysis.\*来访问如你应该**
```
demo = DataAnalysis.steam250URLGeter()
```
**而不是**
```
demo = steam250URLGeter()
```
### steam250URLGeter
用于获取指定steam250.com页面的所有游戏的url、游戏名、和游戏评分

~~接受一个URL作为参数~~

接受BeautifulSoup类作为参数，也可使用 WebGeter 模块的 self.raw_data作为参数

有 dataHandle() 和 outputData() 两个方法

但通常只需要调用主动调用outputData()方法用于输出

~~dataHandle() 会自动调用~~

dataHandle()也需要调用主动调用

同时生成成员 self.data 类型为列表


### steamTop100URLGeter
用于获取指定steam游戏在线人数前100的所有游戏的url和游戏名

接受BeautifulSoup类作为参数，也可使用 WebGeter 模块的 self.raw_data作为参数

基本和 steam250URLGeter 使用方法一致~ 
dataHandle()也需要调用主动调用

### detailsDataGeter
用于获取steam商店页面详细信息，需要主动调用
detailsGeter()方法获取信息，

接受一个string类型的URL作为参数，会自动调用WebGeter 获取BeautifulSoup类用于解析,因此使用此模块请先导入WebGeter模块

也有一个outputData()方法用于输出文件

# 还是有不清楚的地方
建议直接阅读源码或者提交Issues

# BUG反馈
提交Issues
# 需要额外的模块支持
* BeautifulSoup4
* Requests

# 下载与使用
```language
git clone https://github.com/fred0m/Emerald-spray.git
```

或者

```language
pip install Emeraldspray
```

# 注意
* 导入模块请使用
```language
from Es import *
```
~~不要使用~~现在已经可以正常使用
```language
import Es
```
