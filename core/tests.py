

# 测试用例：
# 输入的图片路径不存在时
# 图片路径中包含中文时（将filename采用gbk编码，就可支持中文路径）
# 图片元数据中包含中文字符时（目前可以显示。exiv2能提取Unicode字符，但是不会解码，直接显示会乱码，需要用python解码）
# 读取不存在的元数据时
# 写入不存在的元数据时
# 保存图片时，原图片被删除