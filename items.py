import sqlite3
import urllib.request
import time
import json

QUERY_DELAY = 3

conn = sqlite3.connect('rs.sqlite')

c = conn.cursor()

c.execute('''SELECT id, name FROM category''')

letters = ('%23', 'a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

categories = c.fetchall()

for category in categories:
    category_id = category[0]
    category_name = category[1]
    for letter in letters:
        page = 1
        while True:
            print('Category: ' + category_name + '(' + str(category_id) + '); Letter: ' + letter + '; Page: ' + str(page))
            url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category='
            url += str(category_id) + '&alpha=' + letter + '&page=' + str(page)
            for retry in range(3):
                try:
                    with urllib.request.urlopen(url) as f:
                        r = f.read().decode('utf-8', 'replace')
                    time.sleep(QUERY_DELAY)

                    j = json.loads(r)

                    break
                except(urllib.error.URLError):
                    print('!!! Could not retrieve ' + url + '; retry ' + str(retry))
                except(json.JSONDecodeError):
                    print('!!! Could not parse ' + url + 'response: trying again: ' + str(retry))

            if len(j['items']) == 0:
                print('No items found in ' + url)
                break

            for item in j['items']:
                current_price = item['current']['price']
                if isinstance(current_price, str):
                    current_price = current_price.strip().replace(',','')
                    if current_price.endswith('b'):
                        current_price = int(float(current_price[:-1]) * 1000000000)
                    elif current_price.endswith('m'):
                        current_price = int(float(current_price[:-1]) * 1000000)
                    elif current_price.endswith('k'):
                        current_price = int(float(current_price[:-1]) * 1000)
                    else:
                        current_price = int(current_price)

                c.execute('''SELECT id, current_price FROM item WHERE id = ?''', (item['id'],))
                rows = c.fetchall()

                if len(rows) == 0:
                    print('Inserting ' + item['name'])
                    c.execute('''INSERT INTO item (id, name, description, icon, icon_large, category, current_price, members) VALUES (?,?,?,?,?,?,?,?)''', (
                        item['id'],
                        item['name'],
                        item['description'],
                        item['icon'],
                        item['icon_large'],
                        category_id,
                        current_price,
                        item['members'] == 'true',
                    ))
                    conn.commit()
                elif rows[0][1] != current_price:
                    print('Updating ' + item['name'] + ' price from ' + str(rows[0][1]) + ' to ' + str(current_price))
                    c.execute('''UPDATE item SET current_price = ? WHERE id = ?''', (
                        current_price,
                        item['id'],
                    ))
                    conn.commit()
                else:
                    print('Skipping ' + item['name'])
            page = page + 1

conn.close()
