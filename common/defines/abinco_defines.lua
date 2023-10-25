

NDefines.NCountry.POPULATION_YEARLY_GROWTH_BASE = 0.030
NDefines.NCountry.LOCAL_MANPOWER_ACCESSIBLE_NON_CORE_FACTOR = 0.08
NDefines.NCountry.WAR_SUPPORT_DEFENSIVE_WAR = 0.2
NDefines.NCountry.ARMY_IMPORTANCE_FACTOR = 10.0
NDefines.NCountry.TERRAIN_IMPORTANCE_FACTOR = 5.0
NDefines.NCountry.VICTORY_POINTS_IMPORTANCE_FACTOR = 5.0
NDefines.NCountry.BUILDING_IMPORTANCE_FACTOR = 1.0
NDefines.NCountry.RESOURCE_IMPORTANCE_FACTOR = 5.0
NDefines.NCountry.MAX_BOMBING_WAR_SUPPORT_IMPACT = -0.75
NDefines.NCountry.BASE_SURRENDER_LIMIT = 0.75

-----NDefines.NMilitary.HOURLY_ORG_MOVEMENT_IMPACT = -0.1 revert back if needed

NDefines.NMilitary.RECON_SKILL_IMPACT = 10
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 12
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 4
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 8

NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 2500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 1250
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 1750
NDefines.NMilitary.COMBAT_MINIMUM_TIME = 2

NDefines.NMilitary.LAND_COMBAT_STR_ARMOR_DEFLECTION_FACTOR = 0.6
NDefines.NMilitary.LAND_COMBAT_ORG_ARMOR_DEFLECTION_FACTOR = 0.8

NDefines.NMilitary.ARMY_LEADER_XP_GAIN_PER_UNIT_IN_COMBAT = 0.15 ---MOD was 2.0 should half the increase

NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_IMPACT = -0.50
NDefines.NMilitary.ANTI_AIR_TARGETTING_TO_CHANCE = 0.10
NDefines.NMilitary.TRAINING_MIN_STRENGTH = 0.2
NDefines.NMilitary.AIR_SUPPORT_BASE = 0.25
NDefines.NMilitary.PLAYER_ORDER_PLANNING_DECAY = 0.02

NDefines.NMilitary.COMBAT_STACKING_START = 10
NDefines.NMilitary.COMBAT_STACKING_EXTRA = 6
NDefines.NMilitary.COMBAT_STACKING_PENALTY = -0.08

NDefines.NMilitary.FRONT_MIN_PATH_TO_REDEPLOY = 4


NDefines.NMilitary.GARRISON_ORDER_ARMY_CAP_FACTOR = 4.0
NDefines.NMilitary.BASE_CAPTURE_EQUIPMENT_RATIO = 0.04
NDefines.NAir.AIR_WING_FLIGHT_SPEED_MULT = 0.04
NDefines.NAir.AIR_WING_MAX_STATS_ATTACK = 200
NDefines.NAir.AIR_WING_MAX_STATS_DEFENCE = 200
NDefines.NAir.AIR_WING_MAX_STATS_AGILITY = 200
NDefines.NAir.AIR_WING_MAX_STATS_SPEED = 2000
NDefines.NAir.AIR_WING_MAX_STATS_BOMBING = 200
NDefines.NAir.BIGGEST_AGILITY_FACTOR_DIFF = 5.0
NDefines.NMilitary.COMBAT_OVER_WIDTH_PENALTY = -1	-- #MOD -- was -1.5,			-- over combat width penalty per %.
--#this means that exactly matching the combat width matters even less now. (1% penalty per 1% over combat width)

NDefines.NAir.AIR_DEPLOYMENT_DAYS = 1	-- #MOD-- was 2,				-- Days to deploy one air wing
--# I hate this so much!

NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_TRUCK_DAMAGE_FACTOR = 0.35
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_FACTOR = 0.065
NDefines.NAI.LAND_COMBAT_ANTI_LOGISTICS_PER_ENEMY_ARMY = 5     -- Amount of CAS planes requested per enemy army for anti-logistics

NDefines.NNavy.ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE = 0.2	-- received air damage is calculated using following: 1 - ( (ship_anti_air + fleet_anti_air * SHIP_TO_FLEET_ANTI_AIR_RATIO )^ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE ) * ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE
NDefines.NNavy.ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE	= 0.15
NDefines.NNavy.MAX_ANTI_AIR_REDUCTION_EFFECT_ON_INCOMING_AIR_DAMAGE = 0.5	-- damage reduction for incoming air attacks is clamped to this value at maximum.

NDefines.NAir.ANTI_AIR_PLANE_DAMAGE_FACTOR = 0.5				-- Anti Air Gun Damage factor

NDefines.NAir.CAS_NIGHT_ATTACK_FACTOR = 0.5	-- #MOD-- was 0.1,			-- CAS damaged get multiplied by this in land combats at night
--#large buff to CAS. should result in 36% more CAS damage on average (1.5/1.1) (100% at day + 50% at night is 1.5 for mod, and 1.1 for vanilla)
--#also, CAS was apparently utter trash at night, which means that in timeszones with bad sortie timing, CAS was way weaker than elsewhere. Eastern France, Benelux, and Indian Ocean were such zones). This should now not matter anymore. Also, Land units get -50% at night, why would CAS get -90% instead?


NDefines.NNavy.ANTI_AIR_TARGETTING_TO_CHANCE = 0.5		-- Balancing value to convert averaged equipment stats (anti_air_targetting and naval_strike_agility) to probability chances of airplane being hit by navies AA.
NDefines.NNavy.ANTI_AIR_ATTACK_TO_AMOUNT = 0.005			-- Balancing value to convert equipment stat anti_air_attack to the random % value of airplanes being hit.
NDefines.NNavy.NAVAL_COMBAT_RESULT_TIMEOUT_YEARS = 24							-- after that many years we clear the naval combat results so they don't get stuck forever in the memory.
NDefines.NNavy.CONVOY_LOSS_HISTORY_TIMEOUT_MONTHS = 24					-- after this many months remove the history of lost convoys to not bloat savegames and memory since there is no way to see them anyway
NDefines.NNavy.NAVAL_COMBAT_AIR_CAPITAL_TARGET_SCORE = 50
NDefines.NNavy.NAVAL_COMBAT_AIR_CARRIER_TARGET_SCORE = 100
NDefines.NNavy.HIGHER_SHIP_RATIO_POSITIONING_PENALTY_FACTOR	= 0.75 -- if one side has more ships than the other that side will get this penalty for each +100% ship ratio it has
NDefines.NNavy.SUB_DETECTION_CHANCE_BASE_SPOTTING_EFFECT = 1.0			-- effect of base spotting for initial spotting of pure submarine forces. this along with next value is added together and rolled against a random to start spotting
NDefines.NNavy.SUB_DETECTION_CHANCE_SPOTTING_SPEED_EFFECT = 4.0				-- effect of spotting speed for initial spotting of pure submarine forces. this along with prev value is added together and rolled against a random to start spotting
NDefines.NNavy.SUB_DETECTION_CHANCE_BASE_SPOTTING_POW_EFFECT = 3.0	

NDefines.NNavy.AGGRESSION_SETTINGS_VALUES = { -- ships will use this values while deciding to attack enemies
		0,		-- do not engage
		1.0,	-- low
		1.5,	-- medium
		2.5,	-- high
		10000,	-- I am death incarnate!
	}
	
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR = 0.002			-- war score gained for every manpower killed when sinking a ship
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_PRODUCTION_COST_FACTOR = 0.01		-- war score gained for every IC of the sunk ship

NDefines.NNavy.EXPERIENCE_FACTOR_CARRIER_GAIN = 0.04							-- Xp gain by carrier ships in the combat
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_STR = 0.5					-- Balancing value to convert damage ( naval_strike_attack * hits ) to Strength reduction.
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_ORG = 0.75					-- Balancing value to convert damage ( naval_strike_attack * hits ) to Organisation reduction.
NDefines.NAir.NAVAL_STRIKE_CARRIER_MULTIPLIER = 30.0              -- damage bonus when planes are in naval combat where their carrier is present (and can thus sortie faster and more effectively)
NDefines.NAir.NAVAL_STRIKE_TARGETTING_TO_AMOUNT = 0.5			-- Balancing value to convert the naval_strike_targetting equipment stats to chances of how many airplanes managed to do successfull strike.

NDefines.NMilitary.WAR_SCORE_AIR_IC_LOSS_FACTOR = 0.008						-- war score gained for every IC of damage done to an enemy's air mission
NDefines.NMilitary.WAR_SCORE_LAND_DAMAGE_FACTOR = 0.01          				-- war score gained for every strengh damage done to an enemy's army
NDefines.NMilitary.WAR_SCORE_LAND_IC_LOSS_FACTOR = 0.008         				-- war score gained for every IC damage done to an enemy's army



--- speed ---
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_SPEED_IMPACT = -0.0 -- #MOD -- was -0.3,     -- effect on speed due to enemy air superiority
NDefines.NMilitary.COMBAT_MOVEMENT_SPEED = 0.8 -- #MOD -- was 0.33,	               -- speed reduction base modifier in combat

	--LAND_SPEED_MODIFIER = 0.05,                    -- basic speed control

	--RIVER_CROSSING_PENALTY = -0.3,                 -- small river crossing
	--RIVER_CROSSING_PENALTY_LARGE = -0.6,           -- large river crossing
	--RIVER_CROSSING_SPEED_PENALTY = -0.25,           -- small river crossing
	--RIVER_CROSSING_SPEED_PENALTY_LARGE = -0.5,     -- large river crossing


NDefines.NMilitary.FUEL_CAPACITY_DEFAULT_HOURS = 144 -- #MOD -- was 96,				-- default capacity if not specified

--- Tactics and Recon: ---
NDefines.NMilitary.INITIATIVE_PICK_COUNTER_ADVANTAGE_FACTOR  = 1.00 -- #MOD -- was 0.35, -- advantage per leader level for picking a counter
--#chance for picking the counter tactic if own recon is higher than enemy's.

	--RECON_SKILL_IMPACT = 5, -- how many skillpoints is a recon advantage worth when picking a tactic.
	--TACTIC_SWAP_FREQUENCEY = 12,                   -- hours between tactic swaps

--------------------------





	--BASE_CHANCE_TO_AVOID_HIT = 90,                 -- Base chance to avoid hit if defences left.
	--CHANCE_TO_AVOID_HIT_AT_NO_DEF = 60,	           -- chance to avoid hit if no defences left.
	--AMPHIBIOUS_INVADE_MOVEMENT_COST = 24.0,        -- total progress cost of movement while amphibious invading


	--BASE_FORT_PENALTY = -0.15, 					   -- fort penalty
	--MULTIPLE_COMBATS_PENALTY = -0.5,               -- defender penalty if attacked from multiple directions



---- Buffalo Additions
NDefines.NMilitary.DIG_IN_FACTOR = 0.01 -- 0.02						   -- bonus factor for each dug-in level
NDefines.NNavy.CARRIER_STACK_PENALTY = 8 -- The most efficient is 4 carriers in combat. 5+ brings the penalty to the amount of wings in battle.
NDefines.NNavy.ANTI_AIR_TARGETTING_TO_CHANCE = 0.07 -- Balancing value to convert averaged equipment stats (anti_air_targetting and naval_strike_agility) to probability chances of airplane being hit by navies AA.
NDefines.NNavy.ANTI_AIR_ATTACK_TO_AMOUNT = 0.005 -- Balancing value to convert equipment stat anti_air_attack to the random % value of airplanes being hit.

