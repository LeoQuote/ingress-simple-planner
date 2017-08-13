# ingress-simple-planner
A simple planner for ingress intel player

## Requirements
* Python 3.2+
* matplotlib

其他见 requirements.txt

## 使用方法

1. 使用[这个插件](https://gist.github.com/OllieTerrance/8547503) 或其他插件导出当前界面的portal csv列表
2. 在csv 最上一行加上 
```
portal_name,lat,lon
```
3. 将代码中的BASE1,BASE2 改成你的底边两顶点的列表
4. 运行代码，复制产生的DRAW TOOLS 代码，导入进IITC
