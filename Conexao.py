import psycopg2

class Connection:
    
    def __init__(self):
        self.con, self.cur = self.conexaoDatabase()

    def conexaoDatabase(self):
        con = psycopg2.connect(host='{placeholder}',  
                                    port='{placeholder}',
                                    database='{placeholder}',
                                    user='{placeholder}', 
                                    password='{placeholder}')

        cur = con.cursor()
        return con, cur

    def insertData(self, data):
        sql = '''INSERT INTO {placeholder}
            ({placeholder}. {placeholder}. {placeholder}. {placeholder}. {placeholder}. {placeholder})
            VALUES (%s, %s, %s, %s, %s, %s, %s, to_timestamp(%s, 'DD "days" HH "hours'), %s, now()::timestamp)'''

        self.cur.execute(sql, data)
        self.con.commit()
        self.con.close()
