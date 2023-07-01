# json和python的转换
import json

# python转json
data = {"name": "张三", "age": 18}
print(json.dumps(data, ensure_ascii=False))
data = [
    {"name": "张三", "age": 18},
    {"name": "张三", "age": 18},
    {"name": "张三", "age": 18},
]
print(json.dumps(data, ensure_ascii=False))

# json转python
s = '{"name": "张三", "age": 18}'
d = json.loads(s)
print(type(d))
print(d)

s = '[{"name": "张三", "age": 18}, {"name": "张三", "age": 18}, {"name": "张三", "age": 18}]'
d = json.loads(s)
print(type(d))
print(d)
