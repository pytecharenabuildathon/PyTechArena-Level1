def count_inventory(fruit_list: list[str]) -> dict[str , int]:
    d={}
    for x in fruit_list: d[x]=d.get(x,0)+1
    return "{" + ", ".join(f'"{k}": {v}' for k,v in d.items()) + "}"
print(count_inventory(input().split()))
