# A New Chapter, Fantasy Overhual Flags

This is a comprehensive list of all the flags used in the game. It is recommended to use the HTML file, as it includes detailed descriptions of each flag's purpose.

When launching the game please use `-debug -crash_data_log` to use the full development mode the game provides.

## Table of Content

* [Mapping](#list-mapping)
* [All State Flags](#list-state-flags)
* [All Country Flags](#list-country-flags)
* [All Global Flags](#list-global-flags)

## Mapping

# **Land Province Map Size Guidelines**
- Forest: Fightable 90~ Pixels

- Hills: Fightable 90~ Pixels

- Mountain: Fightable 100~ Pixels

- Plains: Fightable 80~ Pixels

- Farmlands: Fightable 70~ Pixels

- Urban: Minors 60-45~ Pixels

- Urban: Majors 30-20~ Pixels

- Jungle: Fightable 100~ Pixels

- Marsh: Fightable 90~ Pixels

- Desert: Fightable 120~ Pixels

- All Impassable provinces are double of what the terrain is. Example for plains is 160~ Pixels

# **Naval Province Map Size Guidlines**
Using Pdn I Gaussian blur'ed then erased 10x to get the distance from land starting from the land/sea map. Gaussian blur'ing direct 10, near 20, and deep 40. I start at the end of each layer. For Near I Median Blur 1x, well for Deep I median Blur 3x.

- Naval: Direct 1000-1500~ Pixels (Covers Coastal/Land)

- Naval: Near 2000-3000~ Pixels   (Covers 2-3~ Direct)

- Naval: Deep 4000-6000~ Pixels   (Covers 3-5~ Near)

- Naval: Waste(Remaining) 10000-16000~ Pixels

## State Flags

* [urbanized_state1](#urbanized_state1)
* [urbanized_state2](#urbanized_state2)
* [crisis_HHE_entrench_line_built](#crisis_HHE_entrench_line_built)
* [state_flag_HHE_industrialize_the_cities](#state_flag_HHE_industrialize_the_cities)
* [state_flag_HHE_pillar_economic](#state_flag_HHE_pillar_economic)

## Country Flags

* species.dwarf_openness
* species.dwarf_isolationism
* divine_right_coring_num0
* divine_right_coring_num1
* divine_right_coring_num2
* divine_right_coring_num3
* divine_right_coring_num4
* ai_action_navy_small
* ai_action_navy_medium
* ai_action_navy_large
* ai_action_air_small
* ai_action_air_medium
* ai_action_air_large
* ai_action_industry_capacity
* ai_action_industry_vacancy
* denied.ally_with_HHE
* denied.ally_with_OAK
* denied.ally_with_MRC
* accept.ally_with_HHE
* accept.ally_with_OAK
* accept.ally_with_MRC

## Global Flags

* Artificers.GlobalIronShortage
* Artificers.GlobalIronSurplus0
* Artificers.GlobalIronSurplus1
* Artificers.GlobalIronSurplus2
* grand_canal_purchase_processing
* death_of_deed
* reforms_from_deed
* elected_tradition
* elected_influencer
* elected_authority
* elected_warmonger
* elected_peoples_government
* HHE_central_government_agenda
* HHE_collapse_of_the_nation
* HHE_warmonger_civil_war_first
* HHE_warmonger_civil_war_final
* civilwar_victory_tradition
* civilwar_victory_influencer
* civilwar_victory_authority
* civilwar_victory_warmonger
* aborroas_is_lost
* concordia_is_lost