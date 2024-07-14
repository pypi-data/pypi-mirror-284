from collections import deque
import itertools

def get_run_id(project_name,file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.find(f"https://wandb.ai/jlbaker361/{project_name}/runs/")!=-1:
                run_id=line[line.rfind("/")+1:]
                return run_id.strip()
    print("couldn't find run id!")

def get_grouping_dict(project_name:str,file_path_format:str,key_value_dict:dict, grouping_keys:list)-> dict:
    assert all(key in key_value_dict for key in grouping_keys)
    grouping_keys.sort()
    relevant_values=[key_value_dict[key] for key in grouping_keys]
    combinations = ["_".join(t) for t in  list(itertools.product(*relevant_values))]
    grouping_dict={
        c:[] for c in combinations
    }

    print(grouping_dict)

    all_values=[]
    for k,v_list in key_value_dict.items():
        all_values.append([(k,v) for v in v_list])
    all_combinations=list(itertools.product(*all_values))
    all_combo_dicts=[
        {key:value for (key,value) in combination} for combination in all_combinations
    ]
    
    for combo_dict in all_combo_dicts:
        #print(combo_dict)
        file_path=file_path_format
        for key,value in combo_dict.items():
            file_path=file_path.replace("{"+key+"}",value)
        run_id=get_run_id(project_name,file_path)
        
        group_id="_".join([combo_dict[key] for key in grouping_keys])
        print(file_path,run_id,group_id)
        grouping_dict[group_id].append(run_id)
    
    return grouping_dict