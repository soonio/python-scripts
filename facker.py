import hashlib
import os
import random


files = os.listdir("./avatar")

uid = 900000

if os.path.exists('./users.sql'):
    os.remove('./users.sql')

f = open('./users.sql', mode='x')

f.writelines("INSERT INTO `user` (`id`, `name`, `phone`, `email`, `password`, `avatar`, `sex`, `status`, `notice`,`birth`, `times`, `prefix`, `country`, `nation`, `point`, `source`, `mode`, `expire`,`created`, `updated`, `deleted`) VALUES \n")

for x in files:
    m = hashlib.md5()
    m.update(x.encode('utf-8'))
    md5 = m.hexdigest()
    namie = x.split('.')
    sql = "({id}, '{name}', '{phone}', '{email}','', '{avatar}', {sex}, 1, 0, '', '', '', '', '', '0', 3, 'email', 0, 1, 1, 0),\n".format(
        id=uid,
        name=namie[0],
        phone='00-18888{uid}'.format(uid=uid),
        email='{uid}@faker_.com'.format(uid=uid),
        avatar='common/avatar/{md5}.{ext}'.format(md5=md5, ext=namie[1]),
        sex=random.randint(1, 2)
    )
    uid += 1
    f.writelines(sql)

f.close()
