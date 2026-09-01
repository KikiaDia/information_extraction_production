def field_metrics(expected: dict, actual: dict):
    fields=list(expected)
    tp=sum(actual.get(k)==expected[k] for k in fields)
    precision=tp/max(1,sum(actual.get(k) is not None for k in fields))
    recall=tp/max(1,len(fields))
    f1=0 if precision+recall==0 else 2*precision*recall/(precision+recall)
    return {"precision":precision,"recall":recall,"f1":f1}
