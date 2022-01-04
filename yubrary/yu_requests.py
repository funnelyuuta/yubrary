import requests
def yu_requests(url, cookie = None , bool = False):
    '''
    入力
    第一引数 URL 第二引数 cookie 第三引数 bool(クッキーを返すか？デフォは返さない)
    出力
    URLを投げるとBeautifulSoupに入れるテキストを第一引数
    別のページに飛ばされていないかをbool型(True=飛ばされていない)第二引数
    ステータスコードの状態をbool型(True=ステータスコード200)第三引数
    cookieを第四引数(入力で設定しなければNoneを返す)
    '''
    header = user_agent()
    res  = requests.get(url,cookies=cookie,headers=header)
    text = res.text
    status = statuscode(res)
    urlcheck = url_check(res ,url)
    new_cookie = get_cookie(res,bool)

    return text, status, urlcheck, new_cookie  

def user_agent():
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    header = {'User-Agent': ua}
    return header

def statuscode(res):
    if res.status_code != 200:
        return False
    return True

def url_check(res, url):
    if res.url != url:
        return False
    return True

def get_cookie(res, bool):
    if not bool:
        return None
    cookie = res.cookies.get_dict()
    return cookie


