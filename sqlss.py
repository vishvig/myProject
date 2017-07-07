import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='..\user_manage.log',
                    filemode='a')


####   CREATE TABLE    #########
class dbs:

    def create_table(self,db_name,json):
        try:
            str=''
            conn = sqlite3.connect('..\{0}'.format(db_name))
            for i in range (0,len(json['schema'])):
                        if i != 0:
                            str=str+','+json['schema'][i]['field']+' '+json['schema'][i]['type']
                        else :
                            str = str + json['schema'][i]['field'] + ' ' + json['schema'][i]['type']
            sql='create table {0}  ({1})'.format(json['table_name'],str,json['primary_key'])
            #print sql
            if True: #pragma:no cover
                conn.execute(sql)
                conn.commit()
                return "created"
        except sqlite3.OperationalError:#pragma :no cover
                    logging.error("ERROR: operational error in "+json['table_name']+" creation")
                    return "operational"
        except:#pragma: no cover
            logging.error("ERROR:error occured")
            return "error"

    def insert(self,db_name, json):#pragma :no cover
        try:

            conn = sqlite3.connect('..\{0}'.format(db_name))

            for i in range(0, len(json['data'])):
                field = ''
                values = ''
                for j in range(0, len(json['schema'])):
                    for k in range(0, len(json['data'][i])):
                        if json['schema'][j]['field'] == json['data'][i][k]['field']:

                            if k != 0:
                                field = field + ',' + json['data'][i][k]['field']
                                values = values + ',' + '"' + json['data'][i][k]['value'] + '"'
                            else:
                                field = field + json['data'][i][k]['field']
                                values = values + '"' + json['data'][i][k]['value'] + '"'

                sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(json['table_name'], field, values)
                print sql
                conn.cursor().execute(sql, json)
                conn.commit()
            return "inserted"
        except sqlite3.IntegrityError:
            conn.rollback()
            logging.error(" ERROR: duplicate primary key")
            return "duplicate for primary key"
        except:
            logging.error(" ERROR:in insertion")
            return "error"

