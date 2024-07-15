import json
##for find key:none,key:'',key:0,key:[],key:{}
def find_empty_values(json_data, path=""):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            new_path = f"{path}.{key}" if path else key
            find_empty_values(value, new_path)
    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            new_path = f"{path}[{index}]"
            find_empty_values(item, new_path)
    else:
        if not json_data:
            print(f"Key with empty value found at path: {path}")

#sort json[list]
def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    for i in range(len(sorted_list1)):
        if sorted_list1[i] != sorted_list2[i]:
            return False
    return True
  
#for diff json[list]
def print_diff_paths(data1, data2, path=""):
    for key in data1:
        new_path = f"{path}.{key}" if path else key
        if key in data2:
            if isinstance(data1[key], list) and isinstance(data2[key], list):
                if not compare_lists(data1[key], data2[key]):
                    print(f"Lists at path '{new_path}' are not consistent")
            elif data1[key] != data2[key]:
                print(f"Values at path '{new_path}' are different: {data1[key]} vs {data2[key]}")
        else:
            print(f"Key '{key}' is missing in the second JSON object")
          
#for diff json[list],strict mode
def compare_json(json1, json2, path=""):
    if isinstance(json1, dict) and isinstance(json2, dict):
        for key in set(json1.keys()).union(json2.keys()):
            new_path = f"{path}.{key}" if path else key
            if key not in json1:
                print(f"Key {new_path} is missing in the first JSON")
            elif key not in json2:
                print(f"Key {new_path} is missing in the second JSON")
            else:
                compare_json(json1[key], json2[key], new_path)
    elif isinstance(json1, list) and isinstance(json2, list):
        if len(json1) != len(json2):
            print(f"Lists at path {path} have different lengths")
        else:
            for i, (item1, item2) in enumerate(zip(json1, json2)):
                compare_json(item1, item2, f"{path}[{i}]")
    else:
        if json1 != json2:
            print(f"Values at path {path} are different: {json1} vs {json2}")
