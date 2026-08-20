# Improved Resource Prospecting -- generates common/decisions/IRP.resource_prospecting.txt
#
# Performance shape of the generated output (profiled 2026-08-02): there are ~77
# of these decisions and `available` is re-evaluated every tick for every visible
# one, which made them collectively the heaviest scripted block in the game --
# ~2.4 s of thread time each, and the `owns_or_subject_of` scripted trigger alone
# reached 27% of the run across 7.6M calls.
#
# Three things keep the generated blocks cheap. Preserve them when editing:
#
# 1. No ownership check in `available`. Per Wiki_Decision.txt, `available` is only
#    evaluated when `visible` was met, and `visible` already proves the state is
#    owned+controlled. Re-testing it in `available` was pure duplicated cost.
# 2. `visible` uses flat inline ownership triggers instead of the
#    `owns_or_subject_of` / `controls_or_subject_of` scripted triggers. Those wrap
#    their check in `custom_trigger_tooltip`, and a `visible` block never renders a
#    tooltip, so that wrapper plus the `owner`/`controller` scope change was wasted
#    work. The flat `is_owned_by = ROOT` short-circuits before any scope change in
#    the common case (your own state).
# 3. Cheap checks first, since triggers short-circuit in order: the state-flag test
#    leads `visible`, and the country-scope `has_tech` / factory count lead
#    `available`.
#
# `has_tech = excavation0` is NOT emitted per decision -- it lives on the
# `prospect_for_resources` category in common/decisions/categories/00_decision_categories.txt,
# so the engine tests it once instead of 77 times. That category is used only by
# this generated file. If a decision here ever needs to be visible without
# excavation0, that category gate has to move back in here.
import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DECISIONS_DIR = os.path.join(SCRIPT_DIR, '..', 'common', 'decisions')

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
    csv_file = os.path.join(SCRIPT_DIR, 'IRP.resource_prospecting.csv')
    output_file = os.path.join(DECISIONS_DIR, 'IRP.resource_prospecting.txt')

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

        # NOTE: this flag is deliberately NOT prefixed. It must match prev_flag
        # below (a tier-N decision requires the flag tier N-1 sets) and the flags
        # already written into existing save games. Adding an IRP_ prefix here
        # without changing prev_flag breaks every tier-2+ decision silently, and
        # changing both breaks saves.
        current_flag = f"state_{state_id}_{res_type}_developed_{tier}"
        prev_flag_cond = ""
        if tier > 1:
            prev_flag = f"state_{state_id}_{res_type}_developed_{tier-1}"
            prev_flag_cond = f"\n\t\t\t\thas_state_flag = {prev_flag}"

        block = f"""
\t{dec_id} = {{ # {res_type.capitalize()}
\t\tname = IRP_{res_type}
\t\ticon = {res_type}
\t\thighlight_states = {{
\t\t\thighlight_state_targets = {{
\t\t\t\tstate = {state_id}
\t\t\t}}
\t\t}}
\t\tvisible = {{
\t\t\t{state_id} = {{
\t\t\t\tNOT = {{ has_state_flag = {current_flag} }}{prev_flag_cond}
\t\t\t\tOR = {{
\t\t\t\t\tis_owned_by = ROOT
\t\t\t\t\towner = {{ is_subject_of = ROOT }}
\t\t\t\t}}
\t\t\t\tOR = {{
\t\t\t\t\tis_controlled_by = ROOT
\t\t\t\t\tcontroller = {{ is_subject_of = ROOT }}
\t\t\t\t}}
\t\t\t}}
\t\t}}
\t\tavailable = {{
\t\t\thas_tech = {tech}
\t\t\tnum_of_civilian_factories_available_for_projects > 4
\t\t\t{state_id} = {{
\t\t\t\tNOT = {{ has_state_flag = state_{res_type}_is_developing }}
\t\t\t}}
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
