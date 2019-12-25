import yaml

# 读取文件
with open("./value1.yaml", "r", encoding="utf-8") as f:
    # 加载yaml文件
    data = yaml.safe_load(f)

    print("data:{}".format(data))
    print("类型：{}".format(type(data.get("value7"))))
    print("类型：{}".format(type(data.get("value8"))))
    print("类型：{}".format(type(data.get("value9"))))
