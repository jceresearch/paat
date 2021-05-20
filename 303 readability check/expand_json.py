# %%
import json

# %%
with open('rules.json') as json_file:
    data = json.load(json_file)

# %%
print(data[1])
# %%
data2=[]
for e in data:
    
    e["title"]=e["test_string"]
    data2.append(e)


# %%
with open('rule2.json', 'w') as fout:
    json.dump(data2, fout)

# %%
