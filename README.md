# ingress-simple-planner
A simple planner for ingress intel player

## Requirements
* Python 3.2+
* matplotlib

其他见 requirements.txt

## 使用方法

1. 使用[这个插件](https://gist.github.com/OllieTerrance/8547503) 或其他插件导出当前界面的portal csv列表
2. 将代码中的BASE1,BASE2，END 改成你的底边两顶点，以及最外层field的顶点
3. 运行代码，复制产生的DRAW TOOLS 代码，导入进IITC

## Example

```
计算完成，路点总数7, 路点如下[舞, 电梯闸线崩了, 奔小康, 拉琴哥, 歌剧演员, 从长安街看人民大会堂, 天安门广场－远眺国家博物馆],总AP 35012
[{"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.902192, "lng": 116.383106}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.904013, "lng": 116.381945}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.904013, "lng": 116.381945}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.9037, "lng": 116.382978}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.9037, "lng": 116.382978}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.904182, "lng": 116.383475}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.904182, "lng": 116.383475}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.904365, "lng": 116.383637}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.904365, "lng": 116.383637}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.904919, "lng": 116.383889}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.904919, "lng": 116.383889}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.906247, "lng": 116.385555}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.906247, "lng": 116.385555}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.906222, "lng": 116.379735}, {"lat": 39.906444, "lng": 116.389697}]}, {"color": "#a24ac3", "type": "polyline", "latLngs": [{"lat": 39.902192, "lng": 116.383106}, {"lat": 39.906444, "lng": 116.389697}]}]
```

[!IITC结果](images/plan_result.png)