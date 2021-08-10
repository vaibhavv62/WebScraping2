import sqlite3
import ScrapData as sd

con = sqlite3.connect('faqs_database.db')
cur = con.cursor()

table_creation_query = "CREATE TABLE IF NOT EXISTS faqs_table (\
    question TEXT NOT NULL,\
    answer TEXT NOT NULL,\
    link TEXT NOT NULL\
        );"
cur.execute(table_creation_query)


parsed_data = sd.scrap_data()
# print(parsed_data[0],'\n\n',parsed_data[1],'\n\n',parsed_data[2])
for q,a,u in zip(parsed_data[0],parsed_data[1],parsed_data[2]):
    record_insertion_query = f'INSERT INTO faqs_table VALUES(\
        "{q}",\
        "{a}",\
        "{u}"\
        );'
    # print('Executing:\n',record_insertion_query,'\n\n')
    cur.execute(record_insertion_query)
print('Data stored in faqs_database.db/faqs_table')
con.commit()
con.close()