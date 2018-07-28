from app import create_app

app = create_app()


if __name__=='__main__':
    #生产环境是用nginx+uwsgi
    #这里我们使用flask自带的服务器
    app.run(host='127.0.0.1',debug=app.config['DEBUG'],port=81)