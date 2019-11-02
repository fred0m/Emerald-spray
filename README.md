# 导入
```python3
import Es
from Es import <model>
```
# 实例
```python3
import Es

data = Es.es("https://steam250.com/").steam250() // 解析 steam250
data = Es.es("https://store.steampowered.com/app/620/?curator_clanid=32686107").steam() // 解析 Steam 商城页面
```


# Modle

## WebGeter
WebGeter 类接受 str 类型的 url(需要 http 前缀)
WebGeter.raw_html 为网页源码

## DataAnalysis
DataAnalysis 类接受 str 类型的 html 代码并对其解析
DataAnalysis.steam250_dataHandle() 可对 https://steam250.com/ 的页面解析, 返回可迭代对象
DataAnalysissteam_dataHandle() 可对 Steam 商城的页面进行解析, 返回字典

## es
es 中将几个模块组合在一起, 方便调用
