def solution(id):
    # 1
    id = id.lower()

    # 2
    for s in id:
        if not (s.islower() or s.isdigit() or s in ['-', '_', '.']):
            id = id.replace(s, "")

    # 3
    new_id = id[0]
    for i in range(1, len(id)):
        if not (id[i] == id[i-1] == '.'):
            new_id += id[i]

    # 4
    if new_id and new_id[0] == '.': new_id = new_id[1:]
    if new_id and new_id[-1] == '.': new_id = new_id[:-1]

    # 5
    if not new_id: new_id = 'a'

    # 6
    if len(new_id) >= 16: new_id = new_id[0:15]
    if new_id[-1] == '.': new_id = new_id[:-1]
    
    # 7
    if len(new_id) <= 2: new_id += new_id[-1] * (3-len(new_id))
    
    return new_id