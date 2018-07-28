from flask import jsonify,request
from app.libs.Helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm
#蓝图 blueprint 蓝本
#视图函数 controller

@web.route('/book/search') #<>表示参数
def search():
    """
        q : 普通关键字 / ISBN
        page
    """
    q = request.args['q']
    #q至少要有一个字符,长度限制
    page = request.args['page']
    #正整数,最大值限制
    form = SearchForm(request.args)
    #验证层
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        #dict 序列化 API
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result),200,{'content-type':'application/json'}