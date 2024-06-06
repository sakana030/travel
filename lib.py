import sqlite3
database = 'mydb.db'

def check_data(account,pwd):
    global database
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM member WHERE account LIKE '%{account}%';")
        data = cursor.fetchall()
        for i in data:
            return i[1]
        print('False')
        return ''
    except sqlite3.OperationalError:
        print("沒有資料！")
        return ''
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def search_data(idno,password):
    global database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM member WHERE idno LIKE '%{idno}%'")
    data = cursor.fetchall()
    data.sort()
    if cursor is not None:
            cursor.close()
    if conn is not None:
            conn.close()
    for i in data:
        if (i[len(i)-1] == password):
            return i
            
def add_data(username,account,email,pwd):
    global database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO member(username, account, email, pwd) VALUES (?, ?, ?, ?)", (username,account,email,pwd))
    conn.commit()
    if cursor is not None:
            cursor.close()
    if conn is not None:
            conn.close()
            
def update_data(username,account,email,password):
    global database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM member WHERE idno LIKE '%{idno}%'")
    data = cursor.fetchall()
    iid = data[0][0]
    cursor.execute('UPDATE member SET nm = ?, birth = ?,blood = ?,phone = ?,email = ?,idno = ?,pwd = ? WHERE iid = ?', (name,birth,blood,phone,email,idno,password, iid))
    cursor.execute(f"SELECT * FROM member WHERE iid LIKE '%{iid}%'")
    conn.commit()
    if cursor is not None:
            cursor.close()
    if conn is not None:
            conn.close()
# check_data('OO','123456')
# search_data('E125718562','aehcdsfg')
# update_data('阿柳','1968-02-01','UU','0968597976','davis1329@icloud.com','A123456789','123456')