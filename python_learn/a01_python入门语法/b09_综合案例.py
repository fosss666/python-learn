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
import json

# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
#
# line = Line()
# line.add_xaxis(["中国", "美国", "英国"])
# line.add_yaxis("GDP", [300, 200, 100])
#
# # 全局配置项
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
#
# line.render()

us_f = open("E:/fo的python学习/python_learn/a01_python入门语法/美国.txt", "r", encoding="UTF-8")
jp_f = open("E:/fo的python学习/python_learn/a01_python入门语法/日本.txt", "r", encoding="UTF-8")
in_f = open("E:/fo的python学习/python_learn/a01_python入门语法/印度.txt", "r", encoding="UTF-8")
us_data = us_f.read()
jp_data = jp_f.read()
in_data = in_f.read()
# 取出首尾不是json的数据
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]

# 转成字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(us)
# 取横纵坐标数据
us_trend = us_dict['data'][0]['trend']
jp_trend = jp_dict['data'][0]['trend']
in_trend = in_dict['data'][0]['trend']
# 取横纵坐标数据
us_x_data = us_trend['updateDate'][:314]
us_y_data = us_trend['list'][0]['data'][:314]
jp_x_data = jp_trend['updateDate'][:314]
jp_y_data = jp_trend['list'][0]['data'][:314]
in_x_data = in_trend['updateDate'][:314]
in_y_data = in_trend['list'][0]['data'][:314]

# print(x_data)
# print(y_data)

# 生成图表
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 配置
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美印日三国确诊人数表", pos_left="center", pos_bottom='1%')
)

line.render()
