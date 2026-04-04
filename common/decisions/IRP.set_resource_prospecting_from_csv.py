# Improved Resource Prospecting
import csv
import os

def determine_tier(decision_id, decisions_dict):
    req_id = decisions_dict[decision_id].get('Required_Decision_ID', '').strip()
    if not req_id:
        return 1
    return 1 + determine_tier(req_id, decisions_dict)

def get_base_id(decision_id, decisions_dict):
    req_id = decisions_dict[decision_id].get('Required_Decision_ID', '').strip()
    if not req_id:
        return decision_id
    return get_base_id(req_id, decisions_dict)

def generate_decisions():
    csv_file = 'IRP.resource_prospecting.csv'
    output_file = 'IRP.resource_prospecting.txt'
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    decisions = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            decisions[row['Decision_ID'].strip()] = row

    output = ["prospect_for_resources = {\n"]
    
    for dec_id, row in decisions.items():
        state_id = row['State_ID']
        res_type = row['Resource_Type']
        amount = row['Resource_Amount']
        tech = row['Required_Tech']
        tier = determine_tier(dec_id, decisions)
        base_id = get_base_id(dec_id, decisions)
        
        current_flag = f"state_{state_id}_{res_type}_developed_{tier}"
        prev_flag_cond = ""
        if tier > 1:
            prev_flag = f"state_{state_id}_{res_type}_developed_{tier-1}"
            prev_flag_cond = f"\n\t\t\t\thas_state_flag = {prev_flag}"
        
        name_line = f"\n\t\tname = {base_id}" if tier > 1 else ""

        block = f"""
\t{dec_id} = {{ # {res_type.capitalize()}
\t\t{name_line.strip()}
\t\tname = IRP_{res_type}
\t\ticon = {res_type}
\t\thighlight_states = {{
\t\t\thighlight_state_targets = {{
\t\t\t\tstate = {state_id}
\t\t\t}}
\t\t}}
\t\tvisible = {{
\t\t\t{state_id} = {{{prev_flag_cond}
\t\t\t\towns_or_subject_of = yes
\t\t\t\tcontrols_or_subject_of = yes
\t\t\t\tNOT = {{ has_state_flag = {current_flag} }}
\t\t\t}}
\t\t\thas_tech = excavation0
\t\t}}
\t\tavailable = {{
\t\t\t{state_id} = {{
\t\t\t\towns_or_subject_of = yes
\t\t\t\tcontrols_or_subject_of = yes
\t\t\t\tNOT = {{ has_state_flag = state_{res_type}_is_developing }}
\t\t\t}}
\t\t\thas_tech = {tech}
\t\t\tnum_of_civilian_factories_available_for_projects > 4
\t\t}}

\t\tfire_only_once = yes
\t\tcost = 25
\t\tdays_remove = 60
\t\tmodifier = {{ civilian_factory_use = 5 }}

\t\tcomplete_effect = {{
\t\t\t{state_id} = {{ set_state_flag = state_{res_type}_is_developing }}
\t\t}}

\t\tremove_effect = {{
\t\t\t{state_id} = {{
\t\t\t\tset_state_flag = {current_flag}
\t\t\t\tclr_state_flag = state_{res_type}_is_developing
\t\t\t\tadd_resource = {{ type = {res_type} amount = {amount} }}
\t\t\t}}
\t\t}}

\t\tai_will_do = {{
\t\t\tfactor = 1
\t\t\tmodifier = {{ factor = -100 do_save_political_power = yes }}
\t\t\tmodifier = {{ factor = 100 do_expand_{res_type} = yes }}
\t\t}}
\t}}
"""
        output.append(block.replace('\t\t\n', ''))

    output.append("\n}\n")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output)
    print(f"File {output_file} generated successfully.")

if __name__ == "__main__":
    generate_decisions()