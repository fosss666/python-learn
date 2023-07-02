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

# ================================折线图===========================================
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

"""
us_f = open("E:/fo的python学习/python_learn/a01_python入门语法/美国.txt", "r", encoding="UTF-8")
jp_f = open("E:/fo的python学习/python_learn/a01_python入门语法/日本.txt", "r", encoding="UTF-8")
in_f = open("E:/fo的python学习/python_learn/a01_python入门语法/印度.txt", "r", encoding="UTF-8")
us_data = us_f.read()
jp_data = jp_f.read()
in_data = in_f.read()

# 关闭文件
us_f.close()
jp_f.close()
in_f.close()

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
"""

# ================================地图===========================================
"""
# 读文件
f = open("E:/fo的python学习/python_learn/a01_python入门语法/疫情.txt", "r", encoding="UTF-8")
province_data_list = f.read()
# 关闭文件
f.close()

# 对数据进行处理
# 转为字典
province_dict_list = json.loads(province_data_list)
# 将省名和确诊数组装成字典封装在列表中
province_list = []
province_dict_list = province_dict_list["areaTree"][0]["children"]

for province_dict in province_dict_list:
    province = province_dict["name"]  # 省名
    if len(province_dict["name"]) <= 3:
        province = province + "省"
    confirm = province_dict["total"]["confirm"]  # 确诊人数
    m = (province, confirm)  # 封装为字典
    province_list.append(m)
# print(province_list)

# 生成地图
from pyecharts.charts import Map
from pyecharts.options import *

m = Map()
m.add("全国确诊人数图", province_list, maptype="china")

# 全局配置
m.set_global_opts(
    title_opts=TitleOpts(title="全国确诊人数图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)

m.render("全国确诊人数图.html")
"""

# ======================江苏省==========================
"""
# 读文件
f = open("E:/fo的python学习/python_learn/a01_python入门语法/疫情.txt", "r", encoding="UTF-8")
province_data_list = f.read()
# 关闭文件
f.close()

# 对数据进行处理
# 转为字典
province_dict_list = json.loads(province_data_list)
# 将市名和确诊数组装成字典封装在列表中
jiangsu_list = []
jiangsu_province_dict_list = province_dict_list["areaTree"][0]["children"][1]["children"]
for shi in jiangsu_province_dict_list:
    jiangsu_list.append((shi["name"] + "市", shi["total"]["confirm"]))
# print(jiangsu_list)

# 生成地图
from pyecharts.charts import Map
from pyecharts.options import *

m = Map()
m.add("江苏省各市确诊情况", jiangsu_list, maptype="江苏")

# 全局配置
m.set_global_opts(
    title_opts=TitleOpts(title="江苏省各市确诊情况", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "lable": "1~9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "lable": "10~99", "color": "#FFFF99"},
            {"min": 100, "max": 499, "lable": "100~499", "color": "#FF9966"},
            {"min": 500, "max": 999, "lable": "500~999", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "lable": "1000~9999", "color": "#CC3333"},
            {"min": 10000, "lable": "10000+", "color": "#990033"},
        ]
    )
)

m.render("江苏省各市确诊情况.html")
"""

# =========================柱状图==========================
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
# 基础柱状图
"""
bar = Bar()
bar.add_xaxis(["中国", "美国", "日本"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# 翻转x轴，y轴
bar.reversal_axis()

bar.render("基础柱状图.html")
"""
