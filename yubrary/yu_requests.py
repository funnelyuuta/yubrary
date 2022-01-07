import requests


def yu_requests(url, cookie = None , bool = False):
    '''
    入力
    第一引数 URL 第二引数 cookie 第三引数 bool(クッキーを返すか？デフォは返さない)
    出力
    URLを投げるとBeautifulSoupに入れるテキストを第一引数
    別のページに飛ばされていないかをbool型(True=飛ばされていない)第二引数
    cookieを第三引数(入力で設定しなければNoneを返す)
    '''
    header = user_agent()
    res  = requests.get(url,cookies=cookie,headers=header)
    text = res.text
    urlcheck = url_check(res ,url)
    new_cookie = get_cookie(res,bool)
    if res.status_code != 200:
        raise YubraryError("ステータスコードが200じゃないよ")
    return text, urlcheck, new_cookie


def user_agent():
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    header = {'User-Agent': ua}
    return header


def url_check(res, url):
    if res.url != url:
        return False
    return True


def get_cookie(res, bool):
    if not bool:
        return None
    cookie = res.cookies.get_dict()
    return cookie


class YubraryError(Exception):
    pass
