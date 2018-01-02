import socket
import sqlite3
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect((host,port))
print( 'Connected to', host)
print( 'Simple Text-Based-SNS!')

user_name = input('User name : ')
user_name_len = len(user_name)
s.send(user_name.encode('utf-8'))

print(s.recv(1024).decode('utf-8'))


def show_timeline():

    conn = sqlite3.connect('following_list({}).db'.format(user_name))
    curs = conn.cursor()

    ctr = 0
    result = ['dfadsfa','','','','','','','','','','','','','']
    for row in conn.execute("SELECT * FROM following_list"):
        result[ctr] = row[0]
        ctr+=1

    conn.commit()
    curs.close()
    conn.close()


    print('\nYour timeline:\n\n')

    con = sqlite3.connect('TBS.db')
    cs = con.cursor()

    i=0

    while i<ctr:
        for row in con.execute("SELECT * FROM user_timeline WHERE name = ? OR name = ? ORDER BY time DESC",(user_name,result[i])):
            print("<" + row[1] + "> by " + "'" + row[0] + "'")
            print(row[2])
            print(row[3])
            print('----')
        i+=1

    con.commit()
    cs.close()
    con.close()

show_timeline()

while True:



    action = input('\n\nWhat would you do (POST, DELETE, FOLLOW, UNFOLLOW, QUIT)? ')
    s.send(action.encode('utf-8'))


    if action == 'POST':
        print('Do not use same title!!!')
        title = input('Title: ')

        s.send(title.encode('utf-8'))
        content = input('Content: ')

        s.send(content.encode('utf-8'))

        time.sleep(0.1)
        show_timeline()

    elif action == 'DELETE':

        print("Your posted messages --- ('TITLE','CONTENT','TIME')\n")
        conn = sqlite3.connect('TBS.db')
        curs = conn.cursor()
        data = (user_name,)


        for row in curs.execute("SELECT * FROM user_timeline WHERE name = ?",data):

            print('# ' + '<' + row[1] + '> ' + row[3])


        print('...')

        delete_object = input('Which one do you want to delete? (*Choose by Title)\n ')
        s.send(delete_object.encode('utf-8'))
        print('\nThe message is successfully deleted!')

        time.sleep(0.1)

        conn.commit()
        curs.close()
        conn.close()
        show_timeline()

    elif action == 'FOLLOW':

        print('You can follow these users\n\n')
        conn = sqlite3.connect('user_list.db')
        curs = conn.cursor()
        data = (user_name,)
        curs.execute("SELECT * FROM user_list WHERE name!= ?",data)
        for row in curs:
            print(row[0])
        print('\n\n')
        follow_name = input('Whom do you want to follow? ')
        s.send(follow_name.encode('utf-8'))
        reason = (s.recv(1024)).decode('utf-8')
        print(reason)
        time.sleep(0.1)
        show_timeline()


    elif action == 'UNFOLLOW':
        print('You can unfollow these users\n\n')
        conn = sqlite3.connect('following_list({}).db'.format(user_name))
        curs = conn.cursor()
        curs.execute("SELECT * FROM following_list")
        for row in curs:
            print(row[0])
        print('\n\n')
        unfollow_name = input('Whom do you want to unfollow? ')
        s.send(unfollow_name.encode('utf-8'))
        because = (s.recv(1024)).decode('utf-8')
        print(because)
        time.sleep(0.1)
        show_timeline()


    elif action == 'QUIT':
        print('Goodbye!! See you next time~')
        break

    else:
        print('\nYou should input between "POST", "DELETE", "FOLLOW", "UNFOLLOW", "QUIT"')
