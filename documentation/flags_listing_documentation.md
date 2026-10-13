# A New Chapter, Fantasy Overhual Flags

This is a comprehensive list of all the flags used in the game. It is recommended to use the HTML file, as it includes detailed descriptions of each flag's purpose.

When launching the game please use `-debug -crash_data_log` to use the full development mode the game provides.

Regenerated 2026-10-13 from every flag command in `common`, `events` and `history`. Only the mod's own scripts are listed (files prefixed aNCFO, IRP, HHE, MRC, OAK, RoF, OCfA, LCfN, ECO, SEH, UIC, VNR, MJU, formable, and country history); imported mods such as BM, LAR, FAI, TALL and Vanilla.generic are left out. Each flag shows where it is set (with its timer if it has one), where it is checked, and where it is cleared. A written description appears only where one was hand written. Flags containing `@` are scoped per country (`name@TAG`).

## Table of Content

* [Mapping](#mapping)
* [State flags](#state-flags) (94)
* [Country flags](#country-flags) (211)
* [Global flags](#global-flags) (60)
* [Unit leader flags](#unit-leader-flags) (2)
* [Character flags](#character-flags) (0)
* [Checked but never set](#checked-but-never-set)

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

- Naval: Direct 1000-1250~ Pixels (Covers Coastal/Land)
- Naval: Near 2000-3000~ Pixels   (Covers 2-3~ Direct)
- Naval: Deep 5000-7000~ Pixels   (Covers 3-5~ Near)
- Naval: Waste(Remaining) 10000-16000~ Pixels

## State Flags

94 flags.

| Flag | Lifetime | Set | Checked | Cleared | Description |
|---|---|---|---|---|---|
| `bq_construction_complex` | Temporary, expires on its own | aNCFO.FAI_on_actions (on_action, 365 days) | aNCFO.FAI_on_actions (on_action) | none |  |
| `bq_oil_fired_generator` | Temporary, expires on its own | aNCFO.FAI_on_actions (on_action, 365 days) | aNCFO.FAI_on_actions (on_action) | none |  |
| `crisis_HHE_entrench_line_built` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none | marks that the state has already built entrenchments. |
| `HHE_civilwar_pillage_and_loot` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HHE_civilwar_recruited_militias` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `MJU_motorways_target` | Permanent marker, never cleared | MJU.national_branches (focus) | MJU.national_branches (focus) | none |  |
| `recruited_militias` | Set but never checked | aNCFO.scripted_effects (scripted effect) | none | none |  |
| `state_100_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_105_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_106_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_106_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_10_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_10_steel_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_10_steel_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_116_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_123_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_124_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_130_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_134_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_136_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_144_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_144_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_144_oil_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_148_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_149_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_149_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_149_oil_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_149_oil_developed_4` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_159_aluminium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_163_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_163_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_163_oil_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_163_oil_developed_4` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_184_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_184_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_189_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_189_steel_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_189_steel_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_190_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_190_steel_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_190_steel_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_19_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_19_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_19_oil_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_215_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_219_chromium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_219_chromium_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_219_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_241_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_242_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_242_tungsten_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_258_chromium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_258_chromium_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_258_chromium_developed_3` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_337_chromium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_341_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_341_tungsten_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_342_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_342_tungsten_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_343_coal_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_343_coal_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_343_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_343_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_344_chromium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_344_chromium_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_344_coal_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_344_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_406_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_421_coal_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_437_aluminium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_599_steel_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_748_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_748_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_77_aluminium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_79_aluminium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_81_aluminium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_841_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_846_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_846_oil_developed_2` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_84_aluminium_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_84_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_859_oil_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_86_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_87_tungsten_developed_1` | Permanent marker, never cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | none |  |
| `state_aluminium_is_developing` | Toggle, set then cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) |  |
| `state_chromium_is_developing` | Toggle, set then cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) |  |
| `state_coal_is_developing` | Toggle, set then cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) |  |
| `state_flag_HHE_industrialize_the_cities` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_decisions (decision) | HHE.Harmonainus_Imperious_decisions (decision) | none | marks that the state has already used industrialize. |
| `state_flag_HHE_pillar_economic` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_decisions (decision) | HHE.Harmonainus_Imperious_decisions (decision) | none | marks that the state has already used pillar_economic. |
| `state_oil_is_developing` | Toggle, set then cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) |  |
| `state_steel_is_developing` | Toggle, set then cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) |  |
| `state_tungsten_is_developing` | Toggle, set then cleared | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) | IRP.resource_prospecting (decision) |  |
| `urbanized_state_1` | Toggle, set then cleared | aNCFO.industries_dynamic_decisions (decision) | aNCFO.industries_dynamic_decisions (decision) | aNCFO.industries_dynamic_decisions (decision) |  |
| `urbanized_state_2` | Permanent marker, never cleared | aNCFO.industries_dynamic_decisions (decision) | aNCFO.industries_dynamic_decisions (decision) | none |  |

## Country Flags

211 flags.

| Flag | Lifetime | Set | Checked | Cleared | Description |
|---|---|---|---|---|---|
| `accept.ally_with_HHE` | Permanent marker, never cleared | aNCFO.Influence (event) | aNCFO.FAI_diplomacy (AI strategy) | none | States that said nation accpeted influence over sender. |
| `accept.ally_with_MRC` | Permanent marker, never cleared | aNCFO.Influence (event) | aNCFO.FAI_diplomacy (AI strategy); MRC.decisions (decision) | none | States that said nation accpeted influence over sender. |
| `accept.ally_with_OAK` | Permanent marker, never cleared | aNCFO.Influence (event) | aNCFO.FAI_diplomacy (AI strategy) | none | States that said nation accpeted influence over sender. |
| `ager_montis_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); AAV - Aavava (history); ABL - Arborlocus (history) (+55 more) | RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); RoF.scripted_triggers (trigger) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `ager_montis_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `aircraft_naval_effort_built` | Permanent marker, never cleared | HHE_subjects.national_branches (focus) | HHE_subjects.national_branches (focus) | none |  |
| `ALLOWED_FORMATION_OF_HARMONAINUS_IMPERIOUS` | Permanent marker, never cleared | IHS - Imperial Harmonainus State (history) | formable_nation_decisions (decision) | none |  |
| `aNCFO_railway_2419_to_7488` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_280_to_3826` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_280_to_8052` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_280_to_8238` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_2944_to_5401` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_3633_to_9324` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_7761_to_5358` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_7904_to_2419` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_7904_to_7761` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_8052_to_7915` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `aNCFO_railway_8238_to_7980` | Permanent marker, never cleared | aNCFO.FAI_workaround_railway (decision) | aNCFO.FAI_workaround_railway (decision) | none |  |
| `animaekin_religio` | Set but never checked | aNCFO.ideological_scripted_effects (scripted effect) | none | none |  |
| `animaekin_religion` | Toggle, set then cleared | RoF.scripted_effects (scripted effect) | RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); RoF.scripted_triggers (trigger) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `animaekin_religion_archived` | Permanent marker, never cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | none |  |
| `anti_authoritarianism_raids_failed` | Toggle, set then cleared | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) |  |
| `anti_pluralism_raids_failed` | Toggle, set then cleared | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) |  |
| `anti_semidemocracy_raids_failed` | Toggle, set then cleared | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) |  |
| `anti_theocratism_raids_failed` | Toggle, set then cleared | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) |  |
| `anti_unitism_raids_failed` | Toggle, set then cleared | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) | aNCFO.political_decisions (decision) |  |
| `aritifcers_decision_academia_faction_locked` | Permanent marker, never cleared | OAK.Artificers (event) | OAK.Artificers (event) | none |  |
| `aritifcers_decision_bureaucrats_faction_locked` | Permanent marker, never cleared | OAK.Artificers (event) | OAK.Artificers (event) | none |  |
| `aritifcers_decision_industrialist_faction_locked` | Permanent marker, never cleared | OAK.Artificers (event) | OAK.Artificers (event) | none |  |
| `aritifcers_decision_military_faction_locked` | Permanent marker, never cleared | OAK.Artificers (event) | OAK.Artificers (event) | none |  |
| `aritifcers_decision_populus_faction_locked` | Permanent marker, never cleared | OAK.Artificers (event) | OAK.Artificers (event) | none |  |
| `aritifcers_focus_attack_locked` | Set but never checked | OAK.national_branches (focus) | none | none |  |
| `aritifcers_focus_elites_locked` | Set but never checked | OAK.national_branches (focus) | none | none |  |
| `Artificers_iron_crisis_num0` | Permanent marker, never cleared | OAK.Artificers_decisions (decision) | OAK.Artificers_decisions (decision) | none |  |
| `Artificers_iron_crisis_num1` | Permanent marker, never cleared | OAK.Artificers_decisions (decision) | OAK.Artificers_decisions (decision) | none |  |
| `Artificers_iron_crisis_num2` | Permanent marker, never cleared | OAK.Artificers_decisions (decision) | OAK.Artificers_decisions (decision) | none |  |
| `Artificers_iron_crisis_num3` | Permanent marker, never cleared | OAK.Artificers_decisions (decision) | OAK.Artificers_decisions (decision) | none |  |
| `banned_authoritarianism_flag` | Set but never checked | aNCFO.political_decisions (decision) | none | none |  |
| `banned_pluralism_flag` | Set but never checked | aNCFO.political_decisions (decision) | none | none |  |
| `banned_semidemocracy_flag` | Set but never checked | aNCFO.political_decisions (decision) | none | none |  |
| `banned_theocratism_flag` | Set but never checked | aNCFO.political_decisions (decision) | none | none |  |
| `banned_unitism_flag` | Set but never checked | aNCFO.political_decisions (decision) | none | none |  |
| `bop_MJU_divert_resources_military` | Permanent marker, never cleared | MJU.decisions (decision) | MJU.decisions (decision) | none |  |
| `bop_MJU_focus_production_military` | Permanent marker, never cleared | MJU.decisions (decision) | MJU.decisions (decision) | none |  |
| `bop_MJU_strengthen_military` | Permanent marker, never cleared | MJU.decisions (decision) | MJU.decisions (decision) | none |  |
| `cco_HHE_neversurrender` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_decisions (decision) | HHE.Harmonainus_Imperious_decisions (decision) | none |  |
| `cco_neversurrender` | Permanent marker, never cleared | aNCFO.war_measures_decisions (decision) | aNCFO.war_measures_decisions (decision) | none |  |
| `coalition_with_communists` | Permanent marker, never cleared | aNCFO.ElectionEvents (event) | aNCFO.ElectionEvents (event) | none |  |
| `coalition_with_fascists` | Permanent marker, never cleared | aNCFO.ElectionEvents (event) | aNCFO.ElectionEvents (event) | none |  |
| `collapse_of_the_nation_civil_war_ignited` | Toggle, set then cleared | aNCFO.debug_decisions (decision); HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect) | HHE.civilwar_diplomacy (AI strategy); HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.scripted_triggers (trigger) | HHE.scripted_effects (scripted effect) |  |
| `collapse_of_the_nation_civil_war_local` | Toggle, set then cleared | aNCFO.debug_decisions (decision); HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect) | HHE.civilwar_diplomacy (AI strategy); HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.scripted_triggers (trigger) | HHE.scripted_effects (scripted effect) |  |
| `collapse_of_the_nation_civil_war_regional` | Toggle, set then cleared | aNCFO.debug_decisions (decision); HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect) | HHE.civilwar_diplomacy (AI strategy); HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.scripted_triggers (trigger) | HHE.scripted_effects (scripted effect) |  |
| `crisis_in_progress` | Toggle, set then cleared | aNCFO.Stability_Events (event) | aNCFO.crisis_decisions (decision); aNCFO.Stability_Events (event) | aNCFO.Stability_Events (event) |  |
| `crisis_solution_in_progress` | Toggle, set then cleared | aNCFO.Stability_Events (event) | aNCFO.crisis_decisions (decision); aNCFO.Stability_Events (event) | aNCFO.Stability_Events (event) |  |
| `denied.ally_with_HHE` | Permanent marker, never cleared | aNCFO.Influence (event) | none | none | Prevent second request from sender to ally with said nation. |
| `denied.ally_with_MRC` | Permanent marker, never cleared | aNCFO.Influence (event) | none | none | Prevent second request from sender to ally with said nation. |
| `denied.ally_with_OAK` | Permanent marker, never cleared | aNCFO.Influence (event) | none | none | Prevent second request from sender to ally with said nation. |
| `draft_dodging_resolved` | Temporary, expires on its own | aNCFO.Stability_Events (event, 90/180 days) | aNCFO.Stability_Events (event) | none |  |
| `emperor_personality_reli` | Set but never checked | aNCFO.ideological_scripted_effects (scripted effect) | none | none |  |
| `emperor_personality_religion` | Toggle, set then cleared | RoF.scripted_effects (scripted effect); EPC - Emperors Colonies (history); EPY - Emperors Empyrean (history); HIN - Hinozuku (history) | RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); RoF.scripted_triggers (trigger) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `emperor_personality_religion_archived` | Permanent marker, never cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | none |  |
| `ETF_collapse_of_the_nation_elven_tribes_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `ETF_collapse_of_the_nation_elven_tribes_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `fake_intel_template_created` | Permanent marker, never cleared | zz_debug_effects (scripted effect) | zz_debug_effects (scripted effect) | none |  |
| `form_harmonainus_imperious_center_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | HHE.civilwar_diplomacy (AI strategy); formable_nation_decisions (decision); HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action) | none |  |
| `form_harmonainus_imperious_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | HHE.civilwar_diplomacy (AI strategy); HHE.Imperium_fronts (AI strategy); formable_nation_decisions (decision); HHE.Harmonainus_Imperious_collapse_decisions (decision) (+2 more) | none |  |
| `form_harmonainus_imperious_west_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | HHE.civilwar_diplomacy (AI strategy); formable_nation_decisions (decision); HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action) | none |  |
| `form_kahnkermoy_kingdom_dwarf_forges_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_kahnkermoy_kingdom_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_new_mandate_over_empyrean_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_pearlin_duan_marian_federation_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_sanguis_river_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_united_vally_dwarf_forges_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `government_declined_communists` | Set but never checked | aNCFO.ElectionEvents (event) | none | none |  |
| `government_declined_fascists` | Set but never checked | aNCFO.ElectionEvents (event) | none | none |  |
| `gulf_trading_theories` | Permanent marker, never cleared | HHE_subjects.national_branches (focus) | aNCFO.industrial_concern (idea) | none |  |
| `harmonainism_collapse` | Set but never checked | aNCFO.NukeEvents (event) | none | none |  |
| `harmonainus_reformed_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); AGC - Argenti (history); AHM - Ahmyahar (history) (+40 more) | aNCFO.FAI_diplomacy (AI strategy); HHE.civilwar_diplomacy (AI strategy); MRC.diplomacy (AI strategy); RoF.map_modes (map_modes) (+3 more) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `harmonainus_reformed_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `harmonainus_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); CNO - Concordia (history); HAN - Harmonainus Anarchist (history) (+38 more) | aNCFO.FAI_diplomacy (AI strategy); HHE.civilwar_diplomacy (AI strategy); HHE.Imperium_diplomacy (AI strategy); MRC.diplomacy (AI strategy) (+8 more) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `harmonainus_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `has_clicked_emergency_factory_conversion_defensive` | Permanent marker, never cleared | aNCFO.war_measures_decisions (decision) | aNCFO.war_measures_decisions (decision) | none |  |
| `has_clicked_emergency_factory_conversion_offensive` | Permanent marker, never cleared | aNCFO.war_measures_decisions (decision) | aNCFO.war_measures_decisions (decision) | none |  |
| `hasdefensivepact@PREV` | Toggle, set then cleared | aNCFO_scripted_diplomatic_actions (diplomatic action) | none | aNCFO_scripted_diplomatic_actions (diplomatic action) |  |
| `hasdefensivepact@ROOT` | Toggle, set then cleared | aNCFO_scripted_diplomatic_actions (diplomatic action) | aNCFO_scripted_diplomatic_actions (diplomatic action) | aNCFO_scripted_diplomatic_actions (diplomatic action) |  |
| `HBB_collapse_of_the_nation_unity_front_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HBB_collapse_of_the_nation_unity_front_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HCR_collapse_of_the_nation_western_anarchist_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HCR_collapse_of_the_nation_western_anarchist_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HHE_accepts_intergration` | Set but never checked | HHE.Harmonainus_Imperious (event) | none | none |  |
| `HHE_AI_RANDOM_ACTIUS` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | HHE_strategy_plan (AI plan) | none |  |
| `HHE_AI_RANDOM_AUTHORITY` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | HHE_strategy_plan (AI plan) | none |  |
| `HHE_AI_RANDOM_INFLUENCER` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | HHE_strategy_plan (AI plan) | none |  |
| `HHE_AI_RANDOM_TRADITION` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | HHE_strategy_plan (AI plan) | none |  |
| `HHE_AI_RANDOM_UNITISM` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | HHE_strategy_plan (AI plan) | none |  |
| `HHE_AI_RANDOM_WARMONGER` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | HHE_strategy_plan (AI plan) | none |  |
| `HHE_collapse_of_the_nation_country_no_more_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.national_branches (focus); aNCFO.debug_on_actions (on_action) | none |  |
| `HHE_collapse_of_the_nation_country_no_more_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.national_branches (focus); aNCFO.debug_on_actions (on_action) | none |  |
| `HHE_collapse_of_the_nation_fire_river_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.civil_war_scripted_effects (scripted effect); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_fire_river_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_freedom_front_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.civil_war_scripted_effects (scripted effect); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_freedom_front_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_nobility_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_nobility_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_peoples_government_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); aNCFO.debug_on_actions (on_action); HHE.civil_war_scripted_effects (scripted effect); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_collapse_of_the_nation_peoples_government_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect); HHE.scripted_effects (scripted effect) | none |  |
| `HHE_demanded_outerlands` | Permanent marker, never cleared | HHE.national_branches (focus) | HHE.national_branches (focus) | none |  |
| `HHE_rejects_intergration` | Set but never checked | HHE.Harmonainus_Imperious (event) | none | none |  |
| `HHI_SUBJECTS_resource_storage_fuel` | Set but never checked | HHE_subjects.national_branches (focus) | none | none |  |
| `HLF_collapse_of_the_nation_confederacy_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HLF_collapse_of_the_nation_confederacy_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HLF_collapse_of_the_nation_junta_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect) | none |  |
| `HLF_collapse_of_the_nation_junta_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision); HHE.civil_war_scripted_effects (scripted effect) | none |  |
| `HST_collapse_of_the_nation_archaigan_people_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HST_collapse_of_the_nation_archaigan_people_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HTP_collapse_of_the_nation_free_sailors_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HTP_collapse_of_the_nation_free_sailors_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HUM_collapse_of_the_nation_dwarves_failed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `HUM_collapse_of_the_nation_dwarves_fixed` | Permanent marker, never cleared | HHE.Harmonainus_Imperious_collapse_decisions (decision) | HHE.Harmonainus_Imperious_collapse_decisions (decision) | none |  |
| `ideological_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); HAP - Harmonainus Archaigan People (history); HPG - Harmonainus Peoples Goverment (history); HUF - Harmonainus Unity Front (history) | RoF.map_modes (map_modes); aNCFO.on_actions (on_action); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) (+1 more) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `mining_operations` | Set but never checked | aNCFO.debug_decisions (decision); HHE.national_branches (focus); HHE_subjects.national_branches (focus) | none | none |  |
| `MJU_AI_RANDOM_NATIONALIST` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | MJU_strategy_plan (AI plan) | none |  |
| `MJU_AI_RANDOM_REFORM` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | MJU_strategy_plan (AI plan) | none |  |
| `MJU_AI_RANDOM_STATUS_QUO` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | MJU_strategy_plan (AI plan) | none |  |
| `MRC_AI_RANDOM_BLANACED` | Set but never checked | aNCFO.random_on_actions (on_action) | none | none |  |
| `MRC_AI_RANDOM_INTERVENTION` | Permanent marker, never cleared | aNCFO.random_on_actions (on_action) | MRC_strategy_plan (AI plan) | none |  |
| `MRC_AI_RANDOM_ISOLATION` | Set but never checked | aNCFO.random_on_actions (on_action) | none | none |  |
| `MRC_air_manufacturing_champion_accepted` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision) | none |  |
| `MRC_air_manufacturing_champion_accepted_flag` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision); aNCFO_tech_sharing_groups (technology_sharing) | none |  |
| `MRC_air_manufacturing_champion_declined_flag` | Set but never checked | MRC.Merchant_Republic (event) | none | none |  |
| `MRC_amc_actively_improving_flag` | Toggle, set then cleared | MRC.decisions (decision) | MRC.decisions (decision) | MRC.decisions (decision) |  |
| `MRC_amc_primary_champion_carrier_cas` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_carrier_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_carrier_naval` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_choosen_flag` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_decision_flag` | Permanent marker, never cleared | MRC.decisions (decision) | MRC.decisions (decision) | none |  |
| `MRC_amc_primary_champion_heavy_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision); MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger) (+1 more) | none |  |
| `MRC_amc_primary_champion_light_cas` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_light_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_light_naval` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_maritime_patrol` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_strategic_bomber` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_primary_champion_tactical` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_carrier_cas` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_carrier_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_carrier_naval` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_choosen_flag` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_decision_flag` | Permanent marker, never cleared | MRC.decisions (decision) | MRC.decisions (decision); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_heavy_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_light_cas` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_light_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_light_naval` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_maritime_patrol` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_strategic_bomber` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_secondary_champion_tactical` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_carrier_cas` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_carrier_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_carrier_naval` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_choosen_flag` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_decision_flag` | Permanent marker, never cleared | MRC.decisions (decision) | MRC.decisions (decision); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_heavy_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_light_cas` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_light_fighter` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_light_naval` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_maritime_patrol` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_strategic_bomber` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_amc_trinary_champion_tactical` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.scripted_effects (scripted effect); MRC.scripted_localisation (scripted_localisation); MRC.scripted_triggers (trigger); MRC.Merchant_Republic (event) | none |  |
| `MRC_blacklist_declined_champion_flag` | Toggle, set then cleared | MRC.decisions (decision) | MRC.decisions (decision); MRC.Merchant_Republic (event) | MRC.decisions (decision) |  |
| `MRC_blacklist_declined_triton_flag` | Toggle, set then cleared | MRC.decisions (decision) | MRC.decisions (decision); MRC.Merchant_Republic (event) | MRC.decisions (decision) |  |
| `MRC_expeditionary_experience_debug_flag` | Permanent marker, never cleared | MRC.decisions (decision) | MRC.decisions (decision) | none |  |
| `MRC_expeditionary_experience_received_flag` | Permanent marker, never cleared | MRC.decisions (decision); aNCFO.on_actions (on_action) | MRC.decisions (decision); aNCFO.on_actions (on_action) | none |  |
| `MRC_navy_manufacturing_triton_accepted` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision) | none |  |
| `MRC_navy_manufacturing_triton_accepted_flag` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.decisions (decision); aNCFO_tech_sharing_groups (technology_sharing) | none |  |
| `MRC_navy_manufacturing_triton_declined_flag` | Set but never checked | MRC.Merchant_Republic (event) | none | none |  |
| `MRC_negotiate_grand_canal` | Permanent marker, never cleared | MRC.national_branches (focus) | MRC.decisions (decision) | none |  |
| `MRC_nmt_actively_improving_flag` | Toggle, set then cleared | MRC.decisions (decision) | MRC.decisions (decision) | MRC.decisions (decision) |  |
| `MRC_transfer_merchant_ally_to_league_of_nations_ally` | Permanent marker, never cleared | MRC.decisions (decision) | MRC.decisions (decision) | none |  |
| `MTG_naval_treaty_abandoned` | Permanent marker, never cleared | VNR.naval_treaty_scripted_effects (scripted effect) | VNR.naval_treaty (decision) | none |  |
| `MTG_refused_naval_treaty` | Permanent marker, never cleared | VNR.naval_treaty (event) | VNR.naval_treaty (decision) | none |  |
| `MTG_second_london_treaty_signed` | Permanent marker, never cleared | VNR.naval_treaty (decision); VNR.naval_treaty (event) | VNR.naval_treaty (decision) | none |  |
| `mutiny_resolved` | Temporary, expires on its own | aNCFO.Stability_Events (event, 90/180 days) | aNCFO.Stability_Events (event) | none |  |
| `naval_effort_built` | Permanent marker, never cleared | MRC.national_branches (focus) | MRC.national_branches (focus) | none |  |
| `naval_effort_built1` | Permanent marker, never cleared | HHE_subjects.national_branches (focus) | HHE_subjects.national_branches (focus) | none |  |
| `naval_effort_built2` | Permanent marker, never cleared | HHE_subjects.national_branches (focus) | HHE_subjects.national_branches (focus) | none |  |
| `nihilism_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); COA - Commune of Artificers (history); NMR - Necromage Regna (history) (+2 more) | RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); RoF.scripted_triggers (trigger) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `nihilism_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `OAK_factions_unlocked_flag` | Set but never checked | OAK.Artificers_scripted_effects (scripted effect) | none | none |  |
| `object_attache_going_on` | Permanent marker, never cleared | aNCFO.foreign_decisions (decision) | aNCFO.foreign_decisions (decision) | none |  |
| `OCfA_allow_demobilization` | Set but never checked | OCfA.on_actions (on_action) | none | none |  |
| `OCfA_recent_demobilization` | Temporary, expires on its own | OCfA.decisions (decision, 365 days) | OCfA.scripted_effects (scripted effect) | none |  |
| `OCfA_wargoal_threat_either_way` | Toggle, set then cleared | OCfA.scripted_effects (scripted effect) | OCfA.decisions (decision) | OCfA.scripted_effects (scripted effect) |  |
| `OCfA_wargoal_threat_inbound` | Toggle, set then cleared | OCfA.scripted_effects (scripted effect) | OCfA.decisions (decision) | OCfA.scripted_effects (scripted effect) |  |
| `pullus_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); DTP - Deeltahai Principalty (history); HYP - Haymehshtat Principalty (history) (+7 more) | aNCFO._generic (idea); RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) (+1 more) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `pullus_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `racing_for_the_bomb` | Permanent marker, never cleared | aNCFO.political_decisions (decision) | none | none |  |
| `rebuilt_suez` | Set but never checked | aNCFO.special_projects_decisions (decision) | none | none |  |
| `secular_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); MAI - Aquilonoas Country (history); MOI - Orientoas Country (history) (+6 more) | HHE.civilwar_diplomacy (AI strategy); RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) (+1 more) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `secular_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `species.dwarf_openness` | Toggle, set then cleared | OAK.Artificers (event) | aNCFO.government_laws (idea) | OAK.Artificers_decisions (decision) | marks weather the dwarven state is open. |
| `strikes_resolved` | Temporary, expires on its own | aNCFO.Stability_Events (event, 90/180 days) | aNCFO.Stability_Events (event) | none |  |
| `thalassaus_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); LLA - Lataria (history) | RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); RoF.scripted_triggers (trigger) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `thalassaus_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |
| `urbanization_hidden` | Toggle, set then cleared | aNCFO.industries_dynamic_decisions (decision) | aNCFO.industries_dynamic_decisions (decision) | aNCFO.industries_dynamic_decisions (decision) |  |
| `war_justification_last_event_borderthreat` | Toggle, set then cleared | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) |  |
| `war_justification_last_event_generic` | Toggle, set then cleared | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) |  |
| `war_justification_last_event_mobilized` | Toggle, set then cleared | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) |  |
| `war_justification_last_event_neighbor` | Toggle, set then cleared | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) |  |
| `war_justification_last_event_political` | Toggle, set then cleared | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) | aNCFO.WarJustification (event) |  |
| `war_propaganda_campaign_running` | Toggle, set then cleared | aNCFO.propaganda_decisions (decision) | aNCFO.propaganda_decisions (decision) | aNCFO.propaganda_decisions (decision) |  |
| `yellow_reg_religion` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) | RoF.map_modes (map_modes); aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect); RoF.scripted_triggers (trigger) | aNCFO.ideological_scripted_effects (scripted effect); RoF.scripted_effects (scripted effect) |  |
| `yellow_reg_religion_archived` | Toggle, set then cleared | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) | aNCFO.ideological_scripted_effects (scripted effect) |  |

## Global Flags

60 flags.

| Flag | Lifetime | Set | Checked | Cleared | Description |
|---|---|---|---|---|---|
| `aborroas_is_lost` | Set but never checked | aNCFO.on_actions (on_action) | none | none | marks when the owner of the state is no longer the owner. |
| `aNCFO_enabled` | Set but never checked | aNCFO.on_actions (on_action) | none | none |  |
| `aritifcers_reconstruction_industry_completed` | Permanent marker, never cleared | OAK.national_branches (focus) | none | none |  |
| `Artificers.GlobalIronShortage` | Toggle, set then cleared | aNCFO.on_actions (on_action) | aNCFO.FAI_industry (AI strategy); HHE.Imperium_industry (AI strategy); MRC.industry (AI strategy); OAK.Artificers_categories (decision) (+1 more) | OAK.Artificers_scripted_effects (scripted effect) | marks that the Global Iron Shortage has happened caused by artificer civil war. |
| `Artificers.GlobalIronSurplus0` | Permanent marker, never cleared | OAK.Artificers_scripted_effects (scripted effect) | OAK.Artificers_scripted_effects (scripted effect) | none | counts that 3 nations and finish their mission tree to clear the debuff to all other nations whom have it. |
| `Artificers.GlobalIronSurplus1` | Permanent marker, never cleared | OAK.Artificers_scripted_effects (scripted effect) | OAK.Artificers_scripted_effects (scripted effect) | none | counts that 3 nations and finish their mission tree to clear the debuff to all other nations whom have it.. |
| `Artificers.GlobalIronSurplus2` | Permanent marker, never cleared | OAK.Artificers_scripted_effects (scripted effect) | OAK.Artificers_scripted_effects (scripted effect) | none | counts that 3 nations and finish their mission tree to clear the debuff to all other nations whom have it.. |
| `civilwar_victory_authority` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.scripted_triggers (trigger) | none | marks that HHE authority won the HHE civil war. |
| `civilwar_victory_influencer` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.scripted_triggers (trigger) | none | marks that HHE influencer won the HHE civil war. |
| `civilwar_victory_subject` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.scripted_triggers (trigger) | none |  |
| `civilwar_victory_tradition` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.scripted_triggers (trigger) | none | marks that HHE tradition won the HHE civil war. |
| `civilwar_victory_unitism` | Set but never checked | HHE.scripted_effects (scripted effect) | none | none |  |
| `civilwar_victory_warmonger` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.Imperium_diplomacy (AI strategy); HHE.scripted_triggers (trigger) | none | marks that HHE warmonger won the HHE civil war. |
| `concordia_is_lost` | Set but never checked | aNCFO.on_actions (on_action) | none | none | marks when the owner of the state is no longer the owner. |
| `death_of_actius` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.national_branches (focus) | none | marks the death of Actius. |
| `elected_authority` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.national_branches (focus); HHE_subjects.national_branches (focus); HHE.Harmonainus_Imperious (event) | none | marks that HHE authority leader is in power. |
| `elected_influencer` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.national_branches (focus); HHE_subjects.national_branches (focus); HHE.Harmonainus_Imperious (event) | none | marks that HHE influencer leader is in power. |
| `elected_tradition` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.national_branches (focus); HHE_subjects.national_branches (focus); HHE.Harmonainus_Imperious (event) | none | marks that HHE tradition leader is in power. |
| `elected_warmonger` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | formable_nation_decisions (decision); HHE.national_branches (focus); HHE_subjects.national_branches (focus); HHE.Harmonainus_Imperious (event) | none | marks that HHE warmonger leader is in power. |
| `fall_of_harmony_city_MJU` | Permanent marker, never cleared | aNCFO.NewsEvents (event) | aNCFO.NewsEvents (event) | none |  |
| `fall_of_harmony_city_MRC` | Permanent marker, never cleared | aNCFO.NewsEvents (event) | aNCFO.NewsEvents (event) | none |  |
| `fall_of_techcracia_HHE` | Permanent marker, never cleared | aNCFO.NewsEvents (event) | aNCFO.NewsEvents (event) | none |  |
| `form_artemum_oberflehkhuh_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_electrum_federation_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_kunstfertiger_artificers_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_united_vally1_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_united_vally2_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_united_vally3_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_united_vally4_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_UotPDMPF_federate_with_UFS_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_wum_high_kingdom_collab_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_wum_high_kingdom_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `form_wum_smithahaufast_flag` | Permanent marker, never cleared | formable_nation_decisions (decision) | formable_nation_decisions (decision) | none |  |
| `global_monthly_done` | Temporary, expires on its own | ECO.on_actions (on_action, 1 days) | ECO.on_actions (on_action) | none |  |
| `grand_canal_purchase_processing` | Toggle, set then cleared | MRC.decisions (decision) | MRC.decisions (decision) | MRC.Grand_Canal (event) | prevent any other purchasing processe of the grand canal. |
| `HHE_archardus_vladarus_failed_leader` | Permanent marker, never cleared | HHE_balance_of_power (balance of power) | HHE_balance_of_power (balance of power) | none |  |
| `HHE_central_government_agenda` | Permanent marker, never cleared | HHE.national_branches (focus) | HHE_subjects.national_branches (focus) | none | marks that HHE subjects can go down their political tree. |
| `HHE_collapse_of_the_nation` | Toggle, set then cleared | aNCFO.debug_decisions (decision); HHE.scripted_effects (scripted effect) | HHE.Imperium_diplomacy (AI strategy); formable_nation_decisions (decision); HHE.national_branches (focus); HHE_subjects.national_branches (focus) (+1 more) | aNCFO.debug_decisions (decision) | marks that HHE starting to collapse. |
| `HHE_lucas_actius_good_deeds` | Permanent marker, never cleared | HHE.national_branches (focus) | HHE_subjects.national_branches (focus) | none |  |
| `HHE_warmonger_civil_war_final` | Toggle, set then cleared | HHE.Harmonainus_Imperious (event) | HHE.civilwar_diplomacy (AI strategy); HHE.Imperium_army (AI strategy); HHE.Imperium_diplomacy (AI strategy); HHE.Imperium_fronts (AI strategy) (+6 more) | HHE.scripted_effects (scripted effect) | marks that the final stage of the HHE civil war starts. |
| `HHE_warmonger_civil_war_first` | Toggle, set then cleared | HHE.scripted_effects (scripted effect) | HHE.civilwar_diplomacy (AI strategy); HHE.Imperium_army (AI strategy); HHE.Imperium_diplomacy (AI strategy); HHE.Imperium_fronts (AI strategy) (+7 more) | HHE.scripted_effects (scripted effect) | marks that the first stage of the HHE civil war starts. |
| `HHI_SUBJECTS_firsts_of_many` | Permanent marker, never cleared | HHE.scripted_effects (scripted effect) | HHE.scripted_effects (scripted effect) | none |  |
| `is_LCfN_enabled` | Permanent marker, never cleared | LCfN.on_actions (on_action) | LCfN.scripted_triggers (trigger) | none |  |
| `is_OCfA_enabled` | Permanent marker, never cleared | OCfA.on_actions (on_action) | LCfN.scripted_effects (scripted effect); OCfA.scripted_triggers (trigger) | none |  |
| `is_OCfA_mobilization_scaling_rule_enabled` | Permanent marker, never cleared | OCfA.on_actions (on_action) | LCfN.scripted_effects (scripted effect) | none |  |
| `is_UIC_enabled` | Set but never checked | UIC.on_actions (on_action) | none | none |  |
| `LCfN_global_monthly_done` | Temporary, expires on its own | LCfN.on_actions (on_action, 1 days) | LCfN.on_actions (on_action) | none |  |
| `MJU_expand_mining_operations_flag` | Set but never checked | MJU.national_branches (focus) | none | none |  |
| `MJU_focus_oil_surveying_flag` | Set but never checked | MJU.national_branches (focus) | none | none |  |
| `MRC_civil_war_has_started` | Permanent marker, never cleared | MRC.Merchant_Republic (event) | MRC.diplomacy (AI strategy) | none |  |
| `MRC_most_serene_republic_of_insulae_completed` | Permanent marker, never cleared | MRC.national_branches (focus) | none | none |  |
| `MTG_naval_treaty_signatories` | Toggle, set then cleared | VNR.naval_treaty (decision); VNR.naval_treaty (event) | VNR.naval_treaty (decision); VNR.naval_treaty (event) | VNR.naval_treaty (decision) |  |
| `MTG_naval_treaty_violator` | Permanent marker, never cleared | VNR.naval_treaty (decision); VNR.naval_treaty (event) | VNR.naval_treaty (decision) | none |  |
| `news_genocide_HHI_SUBJECTS` | Permanent marker, never cleared | HHE.Harmonainus_Imperious (event) | HHE.Imperium_diplomacy (AI strategy) | none |  |
| `nova_laity_is_lost` | Set but never checked | aNCFO.on_actions (on_action) | none | none |  |
| `OCfA_global_monthly_done` | Temporary, expires on its own | OCfA.on_actions (on_action, 1 days) | OCfA.on_actions (on_action) | none |  |
| `OCfA_prevent_demobilization` | Temporary, expires on its own | OCfA.on_actions (on_action, 730 days) | OCfA.scripted_effects (scripted effect) | none |  |
| `principality_of_laity_is_lost` | Set but never checked | aNCFO.on_actions (on_action) | none | none |  |
| `regiusurbs_is_lost` | Set but never checked | aNCFO.on_actions (on_action) | none | none |  |
| `sinus_bay_is_lost` | Set but never checked | aNCFO.on_actions (on_action) | none | none |  |

## Unit leader Flags

2 flags.

| Flag | Lifetime | Set | Checked | Cleared | Description |
|---|---|---|---|---|---|
| `admiral_exp_boost_1` | Permanent marker, never cleared | _vnr_admirals (scripted effect) | _vnr_admirals (scripted effect) | none |  |
| `admiral_exp_boost_2` | Permanent marker, never cleared | _vnr_admirals (scripted effect) | _vnr_admirals (scripted effect) | none |  |

## Character Flags

0 flags.

| Flag | Lifetime | Set | Checked | Cleared | Description |
|---|---|---|---|---|---|

## Checked but never set

Tested with `has_*_flag` in the mod's own scripts, but no flag command sets it anywhere in the scanned folders, so the check is always false.

| Scope | Flag | Checked in | Old description |
|---|---|---|---|
| Country | `blew_up_suez` | aNCFO.special_projects_decisions (decision) |  |
| Country | `ignore_navy_micro_scripts` | aNCFO.FAI_fronts (AI strategy) |  |
| Country | `MRC_AI_RANDOM_NEUTRALITY` | MRC_strategy_plan (AI plan) |  |
| Country | `MRC_dev_theo` | MRC.national_branches (focus) |  |
| Country | `MRC_dev_unity` | MRC.national_branches (focus) |  |
| Country | `OAK_nsm_destroyed_flag` | OAK.scripted_localisation (scripted_localisation) |  |
| Country | `OAK_nsm_integrated_flag` | OAK.scripted_localisation (scripted_localisation) |  |
| Country | `prevent_women_army` | aNCFO.military_recruitment_laws (idea) |  |
| Country | `prevent_women_workers` | aNCFO.military_recruitment_laws (idea) |  |
| Country | `species.dwarf_isolationism` | aNCFO.government_laws (idea); aNCFO.on_actions (on_action) | marks weather the dwarven state is truely isolated. |
| Country | `unique_characters_flag` | aNCFO.scripted_triggers (trigger) |  |
| Country | `unique_ideologies_flag` | aNCFO.scripted_triggers (trigger) |  |
| Country | `unique_national_focus_flag` | aNCFO.scripted_triggers (trigger) |  |
| Global | `disabled.tyenren_alone_scripts` | aNCFO.FAI_diplomacy (AI strategy) |  |
| Global | `first_nuke_dropped` | aNCFO.political_decisions (decision) |  |
| Global | `form_sonnenvergen_smithahaufast_flag` | formable_nation_decisions (decision) |  |
| Global | `GRAND_CANAL_BLOCKED` | aNCFO.special_projects_decisions (decision) |  |
| Global | `harmonainism_collapse` | aNCFO.NukeEvents (event) |  |
| Global | `ignore_navy_micro_scripts_global` | aNCFO.FAI_fronts (AI strategy) |  |
| Global | `MTG_second_london_conference` | VNR.naval_treaty (decision); VNR.naval_treaty (event) |  |
| Global | `naval_tech_1946` | VNR.carriers (ai_equipment) |  |
| Global | `reforms_from_actius` | HHE.national_branches (focus) | marks that Actius did not die. |
