# 制作发布压缩包步骤

"""
1、创建 setup.py
。setup.py 文件
"""
from distutils.core import setup
setup(name="hm_message",  # 包名
	version="1.0",  # 版本
	description="itheima's 发送和接收消息模块",  # 描述信息
	long_description="完整的发送和接收消息模块",  # 完整描述信息
	author="itheima",  # 作者
	author_email="itheima@itheima.com",  # 作者邮箱
	url="www.itheima",  # 主页
	py_modules=["hm_message.send_message",
				"hm_message.receive_message"])

"""
2、构建模块
"""
$ python3 setup.py build

"""
3、生成发布压缩包
"""
$ python3 setup.py sdist




# 安装模块
$ tar -zxvf hm_message-1.0.tar.gz

$ sudo python3 setup.py install 

# 卸载模块
$ cd /usr/local/lib/python3.5/dist-packages/
$ sudo rm -r hm_message*







