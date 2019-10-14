#flask轻量级框架创建接口服务
import flask
import json

# 1.定义一个server
server = flask.Flask(__name__)  # __name__代表当前的python文件。把当前的python文件当做一个服务启动

# 2.然后定义接口函数，一般函数和接口函数的区别在于，定义为接口的函数上方要特别加上：
# 第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
@server.route('/index', methods=['get', 'post'])
def index():
    res = {'msg': '这是我开发的第一个借口', 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)


# 3.让server执行起来
# port可自定义填写。不要与机器上已占用的port冲突。
# debug=True，在代码进行修改后，程序会自动重新加载，不用再次运行。也就是运行一次即可，即使改动代码，也不需要重启服务
# host本地ip地址，写0.0.0.0，可以让其他人直接访问本机的ip。
# 最终这个接口的访问地址就是  http://127.0.0.1/index  ,get方法或者post方法都可。返回数据是json格式res内容
server.run(port=7777, debug=True, host='0.0.0.0')
