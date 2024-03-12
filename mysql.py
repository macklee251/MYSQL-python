import pymysql.cursors

conn = pymysql.connect(
    host='localhost', 
    port=3306, 
    user="root", 
    password="sousa123",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)