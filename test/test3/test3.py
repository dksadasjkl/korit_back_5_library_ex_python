import pymysql
import pymysql.cursors

host = "localhost"
port = 3306
user = "admin"
password = "1234"
database = "book_db"

connection = pymysql.connect(
    host=host, 
    port=port, 
    user=user, 
    password=password, 
    database=database
)

bookDict = {
"bookName": "Hey, 파이썬! 생성형 AI 활용 앱 만들어 줘",
"author": "김한호, 최태온, 윤택한",
"publisher": "성안당"
}
cursur = connection.cursor(pymysql.cursors.DictCursor)
sql = f'''
insert into 
    book_tb
    values (0, 
    %s,
    %s,
    %s)
'''

cursur.execute(sql, (bookDict["bookName"], bookDict["author"], bookDict["publisher"]))
connection.commit()