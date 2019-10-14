# flask框架创建带参数接口服务

import flask
import json
server = flask.Flask(__name__)  # __name__代表当前的python文件。把当前的python文件当做一个服务启动


# 只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
@server.route('/reg', methods=['post'])
def reg():
    username = flask.request.values.get('username')
    passwd = flask.request.values.get('passwd')
    if username and passwd:
        msg = 'username,passwd分别为：%s,%s' % (username, passwd)
        res = {'msg': msg, 'msg_code': 1001}
    else:
        res = {'msg': '必填字段未填，请查看接口文档', 'msg_code': 1001}  # 1001表示必填接口未填
    return json.dumps(res, ensure_ascii=False)


server.run(port=7777, debug=True, host='0.0.0.0')
# 端口不写默认是5000.debug=True表示改了代码后不用重启，会自动帮你重启.host写0.0.0.0，别人就可以通过ip访问接口。否则就是127.0.0.1
