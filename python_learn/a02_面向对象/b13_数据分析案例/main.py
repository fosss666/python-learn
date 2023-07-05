"""    
    @author: fosss
    Date: 2023/7/5
    Time: 18:28
    Description:主类
"""
from data_define import Record
from file_define import TextFileReader, JsonFileReader

# 读取数据
f1 = TextFileReader("E:/fo的python学习/python_learn/a02_面向对象/b13_数据分析案例/2011年1月销售数据.txt")
f2 = JsonFileReader("E:/fo的python学习/python_learn/a02_面向对象/b13_数据分析案例/2011年2月销售数据JSON.txt")
jan_data = f1.read()
feb_data = f2.read()

# 合成一个数据
all_data = jan_data + feb_data
# 组装成{”时间“,”销售额“}
data_dict = {}
for record in all_data:
    if record.date in data_dict:
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 生成图表
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额（元）", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="销售额柱状图",pos_bottom="1%",pos_left="center")

)
bar.render("销售额柱状图.html")
