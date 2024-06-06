from flask import Flask,request,session,url_for, redirect,render_template
from lib import search_data,check_data,add_data
import time,json

app=Flask(__name__) # __name__ 代表目前執行的模組
# 環境設定
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'mysecretkey'

#首頁
@app.route("/",methods=['GET'])
def index():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        return render_template('主頁.html', username=username)
    else:
        return render_template('主頁.html')


@app.route("/login",methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/login",methods=['POST'])
def verify():
    account = request.form.get('account')
    pwd = request.form.get('pwd')
    username = check_data(account,pwd)
    print(username)
    if (username == ''):
        return render_template('login.html',username = '帳號或密碼錯誤')
    else:
        session['username'] = username
        return redirect(url_for('index'))

@app.route("/contact",methods=['GET'])
def contect():
    return render_template('contact.html')

@app.route("/contact",methods=['POST'])
def input():
    # 以request.values的方法取得表單的值
    username = request.form.get('Name')
    account = request.form.get('Account')
    email = request.form.get('Email')
    pwd = request.form.get('Pwd')
    print(username)
    add_data(username,account,email,pwd)
    session['username'] = username
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# 跳轉到各縣市的介紹頁面
@app.route("/pic",methods=['GET'])
def pic():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        return render_template('景點圖觀賞.html', username=username)
    else:
        return render_template('景點圖觀賞.html')

# 新北	New Taipei City
@app.route("/NTPC",methods=['GET'])
def NTPC():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/新北.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('新北.html', says=dic , username = username)
    else:
        with open('static/txt/新北.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('新北.html', says=dic)

@app.route("/NTPC",methods=['POST'])
# post
def say_NTPC():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/新北.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/新北.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('新北.html', says = dic,username = username)
        else:
            with open('static/txt/新北.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('新北.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 台北	Taipei City
@app.route("/TPE",methods=['GET'])
def TPE():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/台北.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台北.html', says=dic , username=username)
    else:
        with open('static/txt/台北.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台北.html', says=dic)


@app.route("/TPE",methods=['POST'])
# post
def say_TPE():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/台北.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/台北.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('台北.html', says = dic,username = username)
        else:
            with open('static/txt/台北.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('台北.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 桃園	Taoyuan City
@app.route("/TYN",methods=['GET'])
def TYN():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/桃園.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('桃園.html', says=dic , username = username)
    else:
        with open('static/txt/桃園.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('桃園.html', says=dic)


@app.route("/TYN",methods=['POST'])
# post
def say_TYN():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/桃園.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/桃園.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('桃園.html', says = dic,username = username)
        else:
            with open('static/txt/桃園.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('桃園.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 新竹	Hsinchu County
@app.route("/HSZ",methods=['GET'])
def HSZ():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/新竹.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('新竹.html', says=dic , username = username)
    else:
        with open('static/txt/新竹.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('新竹.html', says=dic)


@app.route("/HSZ",methods=['POST'])
# post
def say_HSZ():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/新竹.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/新竹.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('新竹.html', says = dic,username = username)
        else:
            with open('static/txt/新竹.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('新竹.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 苗栗	Miaoli City
@app.route("/ZMI",methods=['GET'])
def ZMI():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/苗栗.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('苗栗.html', says=dic , username = username)
    else:
        with open('static/txt/苗栗.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('苗栗.html', says=dic)


@app.route("/ZMI",methods=['POST'])
# post
def say_ZMI():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/苗栗.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/苗栗.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('苗栗.html', says = dic,username = username)
        else:
            with open('static/txt/苗栗.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('苗栗.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 台中市	Taichung City
@app.route("/TXG",methods=['GET'])
def TXG():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/台中.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台中.html', says=dic , username = username)
    else:
        with open('static/txt/台中.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台中.html', says=dic)


@app.route("/TXG",methods=['POST'])
# post
def say_TXG():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/台中.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/台中.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('台中.html', says = dic,username = username)
        else:
            with open('static/txt/台中.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('台中.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))


# 彰化市	Changhua City
@app.route("/CHW",methods=['GET'])
def CHW():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/彰化.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('彰化.html', says=dic , username = username)
    else:
        with open('static/txt/彰化.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('彰化.html', says=dic)


@app.route("/CHW",methods=['POST'])
# post
def say_CHW():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/彰化.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/彰化.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('彰化.html', says = dic,username = username)
        else:
            with open('static/txt/彰化.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('彰化.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 南投市	Nantou City
@app.route("/NTC",methods=['GET'])
def NTC():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/南投.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('南投.html', says=dic , username = username)
    else:
        with open('static/txt/南投.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('南投.html', says=dic)


@app.route("/NTC",methods=['POST'])
# post
def say_NTC():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/南投.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/南投.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('南投.html', says = dic,username = username)
        else:
            with open('static/txt/南投.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('南投.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 雲林縣	Yunlin County
@app.route("/YUN",methods=['GET'])
def YUN():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/雲林.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('雲林.html', says=dic , username = username)
    else:
        with open('static/txt/雲林.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('雲林.html', says=dic)


@app.route("/YUN",methods=['POST'])
# post
def say_YUN():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/雲林.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/雲林.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('雲林.html', says = dic,username = username)
        else:
            with open('static/txt/雲林.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('雲林.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 嘉義縣	Chiayi County
@app.route("/CYI",methods=['GET'])
def CYI():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/嘉義.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('嘉義.html', says=dic , username = username)
    else:
        with open('static/txt/嘉義.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('嘉義.html', says=dic)


@app.route("/CYI",methods=['POST'])
# post
def say_CYI():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/嘉義.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/嘉義.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('嘉義.html', says = dic,username = username)
        else:
            with open('static/txt/嘉義.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('嘉義.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 台南市	Tainan City
@app.route("/TNN",methods=['GET'])
def TNN():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/台南.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台南.html', says=dic , username = username)
    else:
        with open('static/txt/台南.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台南.html', says=dic)


@app.route("/TNN",methods=['POST'])
# post
def say_TNN():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/台南.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/台南.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('台南.html', says = dic,username = username)
        else:
            with open('static/txt/台南.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('台南.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 高雄市	Kaohsiung City
@app.route("/KHH",methods=['GET'])
def KHH():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/高雄.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('高雄.html', says=dic , username = username)
    else:
        with open('static/txt/高雄.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('高雄.html', says=dic)


@app.route("/KHH",methods=['POST'])
# post
def say_KHH():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/高雄.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/高雄.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('高雄.html', says = dic,username = username)
        else:
            with open('static/txt/高雄.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('高雄.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 屏東縣	Pingtung County
@app.route("/PIF",methods=['GET'])
def PIF():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/屏東.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('屏東.html', says=dic , username = username)
    else:
        with open('static/txt/屏東.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('屏東.html', says=dic)


@app.route("/PIF",methods=['POST'])
# post
def say_PIF():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/屏東.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/屏東.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('屏東.html', says = dic,username = username)
        else:
            with open('static/txt/屏東.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('屏東.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 宜蘭縣	Yilan County
@app.route("/ILA",methods=['GET'])
def ILA():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/宜蘭.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('宜蘭.html', says=dic , username = username)
    else:
        with open('static/txt/宜蘭.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('宜蘭.html', says=dic)


@app.route("/ILA",methods=['POST'])
# post
def say_ILA():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/宜蘭.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/宜蘭.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('宜蘭.html', says = dic,username = username)
        else:
            with open('static/txt/宜蘭.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('宜蘭.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 花蓮縣	Hualien County
@app.route("/HUN",methods=['GET'])
def HUN():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/花蓮.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('花蓮.html', says=dic , username = username)
    else:
        with open('static/txt/花蓮.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('花蓮.html', says=dic)


@app.route("/HUN",methods=['POST'])
# post
def say_HUN():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/花蓮.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/花蓮.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('花蓮.html', says = dic,username = username)
        else:
            with open('static/txt/花蓮.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('花蓮.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 台東市	Taitung City
@app.route("/TTT",methods=['GET'])
def TTT():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/台東.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台東.html', says=dic , username = username)
    else:
        with open('static/txt/台東.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('台東.html', says=dic)


@app.route("/TTT",methods=['POST'])
# post
def say_TTT():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/台東.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/台東.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('台東.html', says = dic,username = username)
        else:
            with open('static/txt/台東.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('台東.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 澎湖縣	Penghu County
@app.route("/PEH",methods=['GET'])
def PEH():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/澎湖.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('澎湖.html', says=dic , username = username)
    else:
        with open('static/txt/澎湖.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('澎湖.html', says=dic)


@app.route("/PEH",methods=['POST'])
# post
def say_PEH():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/澎湖.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/澎湖.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('澎湖.html', says = dic,username = username)
        else:
            with open('static/txt/澎湖.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('澎湖.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 金門縣	Kinmen County
@app.route("/KNH",methods=['GET'])
def KNH():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/金門.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('金門.html', says=dic , username = username)
    else:
        with open('static/txt/金門.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('金門.html', says=dic)


@app.route("/KNH",methods=['POST'])
# post
def say_KNH():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/金門.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/金門.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('金門.html', says = dic,username = username)
        else:
            with open('static/txt/金門.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('金門.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))

# 馬祖	Matsu
@app.route("/MFK",methods=['GET'])
def MFK():
    if 'username' in session:
        # print(session['account'])
        username = session['username']
        with open('static/txt/馬祖.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('馬祖.html', says=dic , username = username)
    else:
        with open('static/txt/馬祖.json', 'r' ,encoding='UTF-8') as f:
            dic = []
            for i in json.load(f): 
                dic.append(i)
        return render_template('馬祖.html', says=dic)


@app.route("/MFK",methods=['POST'])
# post
def say_MFK():
    if 'username' in session:
        text = request.form.get('saying')
        username = session['username']
        if text is not None:
            username = session['username']
            with open('static/txt/馬祖.json', 'r',encoding='UTF-8' ) as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            user = session['username']
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            dic.append({"text": text,
                            "user": user,
                            "date": date})
            with open('static/txt/馬祖.json', 'w' ,encoding='UTF-8') as f:
                    json.dump(dic, f, ensure_ascii = False, indent=2)
            return render_template('馬祖.html', says = dic,username = username)
        else:
            with open('static/txt/馬祖.json', 'r' ,encoding='UTF-8') as f:
                dic = []
                for i in json.load(f): 
                    dic.append(i)
            return render_template('馬祖.html', says = dic,username = username)
    else:
        return redirect(url_for('login'))


if __name__=="__main__":  # 若直接執行本程式才啟動伺服器，若僅被呼叫則不啟動
    app.run(debug=True, host='0.0.0.0', port=80)