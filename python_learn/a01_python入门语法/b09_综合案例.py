# json和python的转换
# import json
#
# # python转json
# data = {"name": "张三", "age": 18}
# print(json.dumps(data, ensure_ascii=False))
# data = [
#     {"name": "张三", "age": 18},
#     {"name": "张三", "age": 18},
#     {"name": "张三", "age": 18},
# ]
# print(json.dumps(data, ensure_ascii=False))
#
# # json转python
# s = '{"name": "张三", "age": 18}'
# d = json.loads(s)
# print(type(d))
# print(d)
#
# s = '[{"name": "张三", "age": 18}, {"name": "张三", "age": 18}, {"name": "张三", "age": 18}]'
# d = json.loads(s)
# print(type(d))
# print(d)
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [300, 200, 100])

# 全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()
