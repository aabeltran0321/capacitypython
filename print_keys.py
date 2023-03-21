import json
filename = 'dataset.json'
f = open(filename)
data = json.load(f)
count = 0
for i,a in enumerate(list(data.keys())):
    bb = i%6
    if bb == 0 and i>1:
        count+=1
    print('<input type="submit" value="%s" name = "%s" style = "position: fixed; left: %spx; top: %spx;">' % (a,a.replace(" ","_"),(20+(350*count)),(80+(30*(i%6)))))