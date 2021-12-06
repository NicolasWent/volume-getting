def compute_data(data):
    ret = {}
    for c in data:
        for t in data[c]:
            if t in ret:
                ret[t] += data[c][t]
            else:
                ret[t] = data[c][t]

    return ret
