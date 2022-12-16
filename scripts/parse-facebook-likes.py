import re

with open('page-follows.html', 'r') as file:
    target_string = file.read()

    result = re.findall(r"href=\"/(\d+)\">(.*?)</a>", target_string, re.DOTALL)

    print('"Personal Link","Name"')

    for res in result:
        id = res[0]
        name = res[1].replace("\n", "")
        name = re.sub("\s+", " ", name)

        print('https://www.facebook.com/'+id+',\"'+name+'\"')
