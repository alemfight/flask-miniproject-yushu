from flask import Flask,current_app
app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 离线应用,单元测试

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()


# with改写
with app.app_context(): #上下文表达式
	a = current_app
	d = current_app.config['DEBUG']

'''
1.连接数据库
2.sql
3.释放资源(释放连接)
'''

# 文件读写
# try:
# 	f = open(r'D:\t.txt')
# 	print(f.read())
# finally:
# 	f.close()
# with open(r'') as f:
# 	print(f.read())

# 实现了上下文协议的对象使用with语句
# 上下文管理器
# __enter__ __exit__上下文协议

class MyResource:
	def __enter__(self):
		print('connect to resource')
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_tb:
			print('process exception')
		else:
			print('no exception')
		print('close resourece')
		return False


	def query(self):
		print('query data')

with MyResource() as resource:
	resource.query()