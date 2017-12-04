import json

dic1 = {'id': 'myid', 'pw': 'mypw', 'age': 23}

json.dump(dic1, open('dic1.json', 'w+'))

dumped_dic1 = json.dumps(dic1)

f = open('dic2.json', 'w+')
f.write(dumped_dic1)
f.close()