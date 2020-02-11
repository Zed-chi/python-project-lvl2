from json import loads

def get_file_content(filepath):
    with open(filepath, "r") as f:
        return f.read()


a = loads(get_file_content("./a.json"))
b = loads(get_file_content("./b.json"))

diff_a = set(a.keys()).difference(set(b.keys()))
diff_b = set(b.keys()).difference(set(a.keys()))
common = set(a.keys()).intersection(set(b.keys()))
changed = []
unchanged = []
print(f"diff a {diff_a}")
print(f"diff b {diff_b}")
print(f"common {common}")

for k in common:
    if a[k] != b[k]:
        changed.append(k)
    else:
        unchanged.append(k)

print(f"changed {changed}")
print("{")
for k in unchanged:
    print(f"    {k}: {a[k]}")
for k in changed:
    print(f"  - {k}: {a[k]}")
    print(f"  + {k}: {b[k]}")
for k in diff_a:
    print(f"  - {k}: {a[k]}")
for k in diff_b:
    print(f"  + {k}: {b[k]}")
print("}")

    