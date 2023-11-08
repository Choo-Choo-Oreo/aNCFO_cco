-- aNCFO Defines
	NDefines.NGame.START_DATE = "1924.1.1.12"
	NDefines.NGame.END_DATE = "1949.1.1.1"
	NDefines.NGame.MAP_SCALE_PIXEL_TO_KM = 7.8254
	NDefines.NGame.HANDS_OFF_START_TAG = "LLA"
	NDefines.NBuildings.MAX_SHARED_SLOTS = 55
	NDefines.NCountry.MIN_STABILITY = -1.0
	NDefines.NCountry.MAX_STABILITY = 1.0
	NDefines.NCountry.MIN_WAR_SUPPORT = -1.0
	NDefines.NCountry.MAX_WAR_SUPPORT = 1.0

-- NRM Defines
	NDefines.NProduction.DEFAULT_MAX_NAV_FACTORIES_PER_LINE = 6 -- Was 3 changed to 6
	NDefines.NProduction.CAPITAL_SHIP_MAX_NAV_FACTORIES_PER_LINE = 6 -- Was 3 changed to 6
	NDefines.NProduction.CONVOY_MAX_NAV_FACTORIES_PER_LINE = 9
	NDefines.NProduction.BASE_FACTORY_SPEED_NAV = 4.15
	NDefines.NProduction.EQUIPMENT_MODULE_ADD_XP_COST = 3.0
	NDefines.NProduction.EQUIPMENT_MODULE_REPLACE_XP_COST = 3.0
	NDefines.NProduction.EQUIPMENT_MODULE_CONVERT_XP_COST = 2.0
	NDefines.NProduction.EQUIPMENT_MODULE_REMOVE_XP_COST = 1.0
	NDefines.NProduction.MIN_NAVAL_EQUIPMENT_CONVERSION_IC_COST_FACTOR = 0.1

	NDefines.NAir.DISRUPTION_FACTOR_CARRIER = 8

	NDefines.NNavy.MAX_SUBMARINES_PER_AUTO_TASK_FORCE = 10
	NDefines.NNavy.BEST_CAPITALS_TO_SCREENS_RATIO = 0.34
	NDefines.NNavy.COMBAT_MIN_HIT_CHANCE = 0.01
	NDefines.NNavy.COMBAT_EVASION_TO_HIT_CHANCE_TORPEDO_MULT = 40.0
	NDefines.NNavy.COMBAT_DAMAGE_RANDOMNESS = 0.4
	NDefines.NNavy.COMBAT_TORPEDO_CRITICAL_CHANCE = 0.25
	NDefines.NNavy.COMBAT_DAMAGE_TO_STR_FACTOR = 1.2
	NDefines.NNavy.COMBAT_DAMAGE_TO_ORG_FACTOR = 1.8
	NDefines.NNavy.COMBAT_RETREAT_DECISION_CHANCE = 0.3
	NDefines.NNavy.COMBAT_CRITICAL_DAMAGE_MULT = 3.0
	NDefines.NNavy.COMBAT_ARMOR_PIERCING_CRITICAL_BONUS = 0.5
	NDefines.NNavy.COMBAT_ARMOR_PIERCING_DAMAGE_REDUCTION = -0.9
	NDefines.NNavy.REPAIR_AND_RETURN_PRIO_LOW = 0.5
	NDefines.NNavy.REPAIR_AND_RETURN_PRIO_MEDIUM = 0.7
	NDefines.NNavy.REPAIR_AND_RETURN_PRIO_HIGH = 0.9
	NDefines.NNavy.REPAIR_AND_RETURN_PRIO_LOW_COMBAT = 0.4
	NDefines.NNavy.REPAIR_AND_RETURN_PRIO_MEDIUM_COMBAT = 0.6
	NDefines.NNavy.REPAIR_AND_RETURN_PRIO_HIGH_COMBAT = 0.8
	NDefines.NNavy.REPAIR_AND_RETURN_AMOUNT_SHIPS_LOW = 0.4
	NDefines.NNavy.REPAIR_AND_RETURN_AMOUNT_SHIPS_MEDIUM = 0.6
	NDefines.NNavy.REPAIR_AND_RETURN_UNIT_DYING_STR = 0.35
	NDefines.NNavy.NAVY_EXPENSIVE_IC = 8000
	NDefines.NNavy.MISSION_MAX_REGIONS = 5
	NDefines.NNavy.EXPERIENCE_FACTOR_CARRIER_GAIN = 0.075
	NDefines.NNavy.ANTI_AIR_TARGETTING_TO_CHANCE = 0.1
	NDefines.NNavy.BASE_CARRIER_SORTIE_EFFICIENCY = 0.4
	NDefines.NNavy.CONVOY_ATTACK_BASE_FACTOR = 0.10
	NDefines.NNavy.CARRIER_STACK_PENALTY = 6
	NDefines.NNavy.CARRIER_STACK_PENALTY_EFFECT = 0.1
	NDefines.NNavy.ENEMY_AIR_SUPERIORITY_IMPACT = -0.9
	NDefines.NNavy.DECRYPTION_SPOTTING_BONUS = 0.15
	NDefines.NNavy.MANPOWER_LOSS_RATIO_ON_STR_LOSS = 0.4
	NDefines.NNavy.CAPITAL_ONLY_COMBAT_ACTIVATE_TIME = 8
	NDefines.NNavy.ALL_SHIPS_ACTIVATE_TIME = 12
	NDefines.NNavy.ON_BASE_FUEL_COST = 0.01
	NDefines.NNavy.FUEL_COST_MULT = 0.20
	NDefines.NNavy.AGGRESION_MULTIPLIER_FOR_COMBAT = 1.25
	NDefines.NNavy.AGGRESSION_MAX_ARMOR_EFFICIENCY = 1.25
	NDefines.NNavy.AGGRESSION_HEAVY_GUN_EFFICIENCY_ON_LIGHT_SHIPS = 0.3
	NDefines.NNavy.AGGRESSION_TORPEDO_EFFICIENCY_ON_LIGHT_SHIPS = 0.2
	NDefines.NNavy.AGGRESSION_LIGHT_GUN_EFFICIENCY_ON_HEAVY_SHIPS = 0.15
	NDefines.NNavy.AGGRESSION_TORPEDO_EFFICIENCY_ON_HEAVY_SHIPS = 1.0
	NDefines.NNavy.SUPREMACY_PER_SHIP_BASE = 10.0
	NDefines.NNavy.NAVAL_MINES_SWEEPERS_REDUCTION_ON_PENALTY_EFFECT = 2.5
	NDefines.NNavy.NAVAL_MINES_INTEL_DIFF_FACTOR = 0.2
	NDefines.NNavy.NAVAL_MINES_NAVAL_SUPREMACY_FACTOR = 0.5
	NDefines.NNavy.NAVAL_MINES_ACCIDENT_CRITICAL_HIT_CHANCES = 0.1
	NDefines.NNavy.NAVAL_MINES_ACCIDENT_STRENGTH_LOSS = 20.0
	NDefines.NNavy.NAVAL_MINES_ACCIDENT_ORG_LOSS_FACTOR = 0.8
	NDefines.NNavy.SPOTTING_ENEMY_SPOTTING_MULTIPLIER_FOR_RUNNING_AWAY = 0.8
	NDefines.NNavy.SPOTTING_SPEED_MULT_FOR_CATCHING_UP = 0.25
	NDefines.NNavy.BASE_ESCAPE_SPEED = 0.01
	NDefines.NNavy.SPEED_TO_ESCAPE_SPEED = 1.5
	NDefines.NNavy.ESCAPE_SPEED_PER_COMBAT_DAY = 0.2
	NDefines.NNavy.MAX_ESCAPE_SPEED_FROM_COMBAT_DURATION = 0.3
	NDefines.NNavy.ESCAPE_SPEED_SUB_BASE = 0.05
	NDefines.NNavy.ESCAPE_SPEED_HIDDEN_SUB = 0.20
	NDefines.NNavy.CONVOY_DETECTION_CHANCE_BASE = 4.17
	NDefines.NNavy.BASE_SPOTTING_EFFECT_FOR_INITIAL_CONVOY_SPOTTING = 0.35
	NDefines.NNavy.SPOTTING_SPEED_EFFECT_FOR_INITIAL_CONVOY_SPOTTING = 1.20
	NDefines.NNavy.UNIT_TRANSFER_DETECTION_CHANCE_BASE = 25.02
	NDefines.NNavy.BASE_SPOTTING_EFFECT_FOR_INITIAL_UNIT_TRANSFER_SPOTTING = 10.0
	NDefines.NNavy.SPOTTING_SPEED_EFFECT_FOR_INITIAL_UNIT_TRANSFER_SPOTTING = 20.0
	NDefines.NNavy.RELATIVE_SURFACE_DETECTION_TO_POSITIONING_FACTOR = 0.1
	NDefines.NNavy.MAX_POSITIONING_BONUS_FROM_SURFACE_DETECTION = 0.0
	NDefines.NNavy.HIGHER_SHIP_RATIO_POSITIONING_PENALTY_FACTOR = 0.4
	NDefines.NNavy.MAX_POSITIONING_PENALTY_FROM_HIGHER_SHIP_RATIO = 0.8
	NDefines.NNavy.POSITIONING_PENALTY_HOURLY_DECAY_FOR_NEWLY_JOINED_SHIPS = 0.005
	NDefines.NNavy.DAMAGE_PENALTY_ON_MINIMUM_POSITIONING = 0.75
	NDefines.NNavy.AA_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING = 0.6
	NDefines.NNavy.MAX_ANTI_AIR_REDUCTION_EFFECT_ON_INCOMING_AIR_DAMAGE = 0.75
	NDefines.NNavy.SCREEN_RATIO_FOR_FULL_SCREENING_FOR_CAPITALS = 3.0
	NDefines.NNavy.HEAVY_GUN_ATTACK_TO_SHORE_BOMBARDMENT = 0.06
	NDefines.NNavy.LIGHT_GUN_ATTACK_TO_SHORE_BOMBARDMENT = 0.04
	NDefines.NNavy.GUN_HIT_PROFILES = { -- hit profiles for guns, if target ih profile is lower the gun will have lower accuracy
			80.0,	-- big guns
			120.0,	-- torpedos
			50.0,	-- small guns
		}
	NDefines.NNavy.DEPTH_CHARGES_HIT_CHANCE_MULT = 0.8
	NDefines.NNavy.DEPTH_CHARGES_DAMAGE_MULT = 1.0
	NDefines.NNavy.DEPTH_CHARGE_STAT_FOR_SHIP_TO_BE_SUB_HUNTER = 10
	NDefines.NNavy.SUB_DETECTION_STAT_FOR_SHIP_TO_BE_SUB_HUNTER = 4
	NDefines.NNavy.CONVOY_DEFENSE_MAX_CONVOY_TO_SHIP_RATIO = 2.0
	NDefines.NNavy.CONVOY_DEFENSE_MAX_REGION_TO_TASKFORCE_RATIO	= 3.0
	NDefines.NNavy.SUBMARINE_REVEAL_BASE_CHANCE = 15
	NDefines.NNavy.SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE = 0.2
	NDefines.NNavy.COMBAT_RESULT_PRIORITY_DAY_TO_LIVE = { 										-- the game will delete the combat results after some duration depending on its importance
			14, 
			60, 
			180,
		}

	NDefines.NAI.PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL = 0.02
	NDefines.NAI.PRODUCTION_CARRIER_PLANE_BUFFER_RATIO = 2.0
	NDefines.NAI.MAX_FUEL_CONSUMPTION_RATIO_FOR_NAVY_TRAINING = 0.4
	NDefines.NAI.MAX_FULLY_TRAINED_SHIP_RATIO_FOR_TRAINING = 1.0
	NDefines.NAI.REFIT_SHIP_RELUCTANCE = 500
	NDefines.NAI.REFIT_SHIP_PERCENTAGE_OF_FORCES = 0.0
	NDefines.NAI.MAX_CARRIER_OVERFILL = 1.05
	NDefines.NAI.SUB_TASKFORCE_MAX_SHIP_COUNT = 6
	NDefines.NAI.SCREEN_TASKFORCE_MAX_SHIP_COUNT = 8
	NDefines.NAI.MIN_CAPITALS_FOR_CARRIER_TASKFORCE = 4
	NDefines.NAI.CAPITALS_TO_CARRIER_RATIO = 1.5
	NDefines.NAI.SCREENS_TO_CAPITAL_RATIO = 4.0

-- Production Defines
	--------------------------------------------------------------------------------------------------------------
	-- INDUSTRIAL PRODUCTION
	--------------------------------------------------------------------------------------------------------------

	NDefines.NProduction.BASE_FACTORY_SPEED_MIL = 6.75
	NDefines.NProduction.BASE_FACTORY_SPEED_NAV = 5
	NDefines.NProduction.MAX_CIV_FACTORIES_PER_LINE = 10
	NDefines.NProduction.BASE_FACTORY_START_EFFICIENCY_FACTOR = 7.5
	NDefines.NProduction.BASE_FACTORY_EFFICIENCY_GAIN = 0.75

	--------------------------------------------------------------------------------------------------------------
	-- REPLENISHMENT and UPKEEP MECHANICS
	--------------------------------------------------------------------------------------------------------------

	NDefines.NMilitary.UNIT_UPKEEP_ATTRITION = 0.01 							--Constant attrition value applied to armies.

	--------------------------------------------------------------------------------------------------------------
	-- FUEL CONSUMPTION BALANCE
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAir.FUEL_COST_MULT = 0.2625
	NDefines.NMilitary.ARMY_FUEL_COST_MULT = 0.375
	NDefines.NNavy.FUEL_COST_MULT = 0.05

-- Timestamp Defines
	-- Spot Optimizations--------------------------------------------------------------------------------------
	NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 100
	NDefines.NGame.LAG_DAYS_FOR_PAUSE = 60
	NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 36
	NDefines.NGame.GAME_SPEED_SECONDS = { 0.35, 0.15, 0.1, 0.035, 0.0 }
	NDefines.NFocus.MAX_SAVED_FOCUS_PROGRESS = 30

	Nlua = {

	NTopbar = {
		GAME_SPEED_LIMIT = 0,	-- Unlocks Speed to match as much as the proccessor can handle
		GAME_SPEED_STEPS = 5,	-- DONT CHANGE -- Deals with graphics and speed settings
		GAME_SPEED_ONE = 1,	-- DONT CHANGE --
		GAME_SPEED_TWO = 2,	-- DONT CHANGE --
		GAME_SPEED_THREE = 3,	-- DONT CHANGE --
		GAME_SPEED_FOUR = 4,	-- DONT CHANGE --
		GAME_SPEED_FIVE = 5,	-- DONT CHANGE --
		}
	}

-- Abinco Defines
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

-- BMT Defines
	---- Military additions
	NDefines.NMilitary.DIVISION_SIZE_FOR_XP = 4                    -- how many battalions should a division have to count as a full divisions when calculating XP stuff
	NDefines.NMilitary.SPOTTING_QUALITY_DROP_HOURS = 3  	-- Each X hours the intel quality drops after unit was spotted.
	NDefines.NMilitary.MIN_SUPPLY_CONSUMPTION = 0.03 					-- minimum value of supply consumption that a unit can get
	NDefines.NMilitary.UNIT_EXPERIENCE_PER_COMBAT_HOUR = 0.00033 
	NDefines.NMilitary.UNIT_EXPERIENCE_SCALE = 0.30 
	NDefines.NMilitary.UNIT_EXPERIENCE_PER_TRAINING_DAY = 0.00270 
	NDefines.NMilitary.TRAINING_MAX_LEVEL = 4 
	NDefines.NMilitary.DEPLOY_TRAINING_MAX_LEVEL = 2 
	NDefines.NMilitary.TRAINING_EXPERIENCE_SCALE = 62.0 
	NDefines.NMilitary.TRAINING_ORG = 0.33 
	NDefines.NMilitary.ARMY_EXP_BASE_LEVEL = 3 
	NDefines.NMilitary.EXPERIENCE_COMBAT_FACTOR = 0.15 
	NDefines.NMilitary.UNIT_EXP_LEVELS = { 0.137,  0.225,  0.374,  0.452,  0.573,  0.681,  0.765,  0.879,  0.999 } 		-- Experience needed to progress to the next level
	NDefines.NMilitary.EXPEDITIONARY_FIELD_EXPERIENCE_SCALE = 0.66 		-- reduction factor in Xp from expeditionary forces
	NDefines.NMilitary.LEADER_EXPERIENCE_SCALE = 0.87 	
	NDefines.NMilitary.EXPERIENCE_LOSS_FACTOR = 0.17                  -- percentage of experienced solders who die when manpower is removed
	NDefines.NMilitary.EQUIPMENT_COMBAT_LOSS_FACTOR = 0.8 	 	       -- % of equipment lost to strength ratio in combat  so some % is returned if below 1
	NDefines.NMilitary.TRAINING_ATTRITION = 0.033 		  			   -- amount of extra attrition from being in training
	NDefines.NMilitary.REINFORCE_CHANCE = 0.033                  	   -- base chance to join combat from back line when empty
	NDefines.NMilitary.SPEED_REINFORCEMENT_BONUS = 0.011               -- chance to join combat bonus by each 100% larger than infantry base (up to 200%)
	NDefines.NMilitary.FLANKED_PROVINCES_COUNT = 3 					-- Attacker has to attack from that many provinces for the attack to be considered as flanking
	NDefines.NMilitary.MIN_DIVISION_DEPLOYMENT_TRAINING = 0.30 			-- Min level of division training	
	NDefines.NMilitary.FIELD_MARSHAL_ARMY_BONUS_RATIO = 0.7            -- ratio to apply regular bonuses FM bonuses to armies
	NDefines.NMilitary.FIELD_MARSHAL_XP_RATIO = 0.7					-- xp gain ratio for army group leaders
	NDefines.NMilitary.PARACHUTE_FAILED_EQUIPMENT_DIV = 30.0		   -- When the transport plane was shot down, we drop unit with almost NONE equipment
	NDefines.NMilitary.PARACHUTE_FAILED_MANPOWER_DIV = 60.0		   -- When the transport plane was shot down, we drop unit with almost NONE manpower
	NDefines.NMilitary.PARACHUTE_FAILED_STR_DIV = 7.0			   -- When the transport plane was shot down, we drop unit with almost NONE strenght
	NDefines.NMilitary.PARACHUTE_DISRUPTED_EQUIPMENT_DIV = 1.1   -- When the transport plane was hit, we drop unit with reduced equipment. Penalty is higher as more hits was received (and AA guns was in the state).
	NDefines.NMilitary.PARACHUTE_DISRUPTED_MANPOWER_DIV = 1.7	       -- When the transport plane was hit, we drop unit with reduced manpower. Penalty is higher as more hits was received (and AA guns was in the state).
	NDefines.NMilitary.PARACHUTE_DISRUPTED_STR_DIV = 2.1			   -- When the transport plane was hit, we drop unit with reduced strength. Penalty is higher as more hits was received (and AA guns was in the state).
	NDefines.NMilitary.PARACHUTE_PENALTY_RANDOMNESS = 0.3			   -- Random factor for str,manpower,eq penalties.
	NDefines.NMilitary.PARACHUTE_DISRUPTED_AA_PENALTY = 1            -- How much the Air defence in the state (from AA buildings level * air_defence) is scaled to affect overall disruption (equipment,manpower,str).
	NDefines.NMilitary.PARACHUTE_COMPLETE_ORG = 0.8				   -- Organisation value (in %) after unit being dropped, regardless if failed, disrupted, or successful.
	NDefines.NMilitary.PARACHUTE_ORG_REGAIN_PENALTY_DURATION = 72   -- penalty in org regain after being parachuted. Value is in hours.
	NDefines.NMilitary.PARACHUTE_ORG_REGAIN_PENALTY_MULT = -0.8	
	NDefines.NMilitary.LOW_SUPPLY = 0.8

	NDefines.NMilitary.UNIT_LEADER_ASSIGN_TRAIT_COST = 10.0 					-- cost to assign a new trait to a unit leader

-- Frontline Ai Defines
	--Hello, if you're looking to put this in a modpack, ask and link, but jokes on you, it's compatible in theory with literally every mod so you shouldn't have to put it in a modpack!						
			
	NDefines.NAI.GARRISON_FRACTION = 0.1					-- How large part of a front should always be holding the line rather than advancing at the enemy
		
	NDefines.NAI.DIPLOMACY_REJECTED_WAIT_MONTHS_BASE = 1	-- AI will not repeat offers until at least this time has passed, and at most the double
		
	NDefines.NAI.MIN_INVASION_PLAN_VALUE_TO_EXECUTE	 = 0.0	-- AI will typically avoid carrying out a plan it below this value (0.0 is considered balanced).

	NDefines.NAI.ENTRENCHMENT_WEIGHT = 4.0					-- AI should favour units with less entrenchment when assigning units around.

	NDefines.NAI.UNIT_ASSIGNMENT_TERRAIN_IMPORTANCE = 20.0	--- diminshed by 4x because of Greece-- Terrain score for units are multiplied by this when the AI is deciding which front they should be assigned to
		
	NDefines.NAI.SEND_VOLUNTEER_EVAL_BASE_DISTANCE = 175.0  -- How far away it will evaluate sending volunteers if not a major power
	NDefines.NAI.SEND_VOLUNTEER_EVAL_MAJOER_POWER = 1.0 	-- How willing major powers are to send volunteers.
	NDefines.NAI.SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR = 0.9 -- How much AI containment factors into its evaluation of sending volunteers.

	---NDefines.NAI.PLAN_ACTIVATION_SUPERIORITY_AGGRO = 10 --default 1.0		-- How aggressive a country is in activating a plan based on how superiour their force is.
		--planning

	NDefines.NAI.PLAN_VALUE_TO_EXECUTE = 0.0	---0.15			-- AI will typically avoid carrying out a plan it below this value (0.0 is considered balanced).

	NDefines.NAI.MIN_PLAN_VALUE_TO_MICRO_INACTIVE = 0.0 --default 0.2				-- The AI will not consider members of groups which plan is not activated AND evaluates lower than this.
		
	NDefines.NAI.MAX_UNITS_FACTOR_AREA_ORDER = 1.5 --- 2.0 --default 1.0					-- Factor for max number of units to assign to area defense orders
	NDefines.NAI.DESIRED_UNITS_FACTOR_AREA_ORDER = 0.75	--default^			-- Factor for desired number of units to assign to area defense orders
	NDefines.NAI.MIN_UNITS_FACTOR_AREA_ORDER = 0.5	--default^^				-- Factor for min number of units to assign to area defense orders

	NDefines.NAI.MAX_UNITS_FACTOR_FRONT_ORDER = 5.0	---MOD was 3.0 --default 1.5			-- Factor for max number of units to assign to area front orders
	NDefines.NAI.DESIRED_UNITS_FACTOR_FRONT_ORDER = 4.0	--MOD was 3.0 --default ^			-- Factor for desired number of units to assign to area front orders
	NDefines.NAI.MIN_UNITS_FACTOR_FRONT_ORDER = 3.0	--MOD was 2.0--default 1.0			-- Factor for min number of units to assign to area front orders

	NDefines.NAI.MAX_UNITS_FACTOR_INVASION_ORDER = 2.0	--MOD was 1.5 --default 1.0	-- Factor for max number of units to assign to naval invasion orders
	NDefines.NAI.DESIRED_UNITS_FACTOR_INVASION_ORDER = 1.5	--MOD was 1.0 --default ^		-- Factor for desired number of units to assign to naval invasion orders
	NDefines.NAI.MIN_UNITS_FACTOR_INVASION_ORDER = 1.0	--default ^^			-- Factor for min number of units to assign to naval invasion orders

	NDefines.NAI.FRONT_UNITS_CAP_FACTOR = 10.0 ----15.0 mad test here too 		--default 15.0				-- A factor applied to total front size and supply use. Primarily effects small fronts
	NDefines.NAI.MAX_DIST_PORT_RUSH = 25.0	--default 20.0			-- If a unit is in enemy territory with no supply it will consider nearby ports within this distance.
		
	NDefines.NAI.MIN_FIELD_STRENGTH_TO_BUILD_UNITS = 0.7	--default 0.7		-- Cancel unit production if below this to get resources out to units in the field
	NDefines.NAI.MIN_MANPOWER_TO_BUILD_UNITS = 0.7	--default 0.7				-- Cancel unit production if below this to get resources out to units in the field

	NDefines.NMilitary.PLAN_SPREAD_ATTACK_WEIGHT = 300 -- 1.0 -- (was 12.0)	-- The higher the value, the less it should crowd provinces with multiple attacks.		#WICHTIG
	NDefines.NMilitary.PLAN_MIN_AUTOMATED_EMPTY_POCKET_SIZE = 20		-- (was 2) -- The battle plan system will only automatically attack provinces in pockets that has no resistance and are no bigger than these many provinces

	NDefines.NMilitary.FRONTLINE_EXPANSION_FACTOR = 0.0 -- #MOD was 0.0 remove if problematic -- was 0.6,				-- When attacking along a frontline, how much should units spread out as they advance. 0.0 means head (more or less) directly to the drawn frontline, with no distractions

	NDefines.NAI.MAIN_ENEMY_FRONT_IMPORTANCE = 20.0			-- How much extra focus the AI should put on who it considers to be its current main enemy.
	NDefines.NAI.EASY_TARGET_FRONT_IMPORTANCE = 7.5 --MOD was 10.0			-- How much extra focus the AI should put on who it considers to be the easiest target.
			
	NDefines.NAI.AI_FRONT_MOVEMENT_FACTOR_FOR_READY = 0.2	-- If less than this fraction of units on a front is moving, AI sees it as ready for action	

	--------------------------------------------------------------------------------------------------------------
	-- RESEARCH
	--------------------------------------------------------------------------------------------------------------

	--------------------------------------------------------------------------------------------------------------
	-- DESIGNS
	--------------------------------------------------------------------------------------------------------------

	---------------

	NDefines.NAI.REFIT_SHIP_RELUCTANCE = 5000							-- How often to consider refitting to new equipment variants for ships in the field
	NDefines.NAI.REFIT_SHIP_PERCENTAGE_OF_FORCES = 0.30				-- How big part of the navy that should be considered for refitting

	NDefines.NAI.DIVISION_DESIGN_MANPOWER_WEIGHT = 0 --0.005
	NDefines.NAI.DIVISION_DESIGN_STOCKPILE_WEIGHT = 0 --0.01
	NDefines.NAI.DIVISION_DESIGN_COMBAT_WIDTH_TARGET_WEIGHT = -10000 -- -200	        -- This score is reduced the farther the width is from the target width (if set)

	NDefines.NAI.UPGRADE_PERCENTAGE_OF_FORCES = 0.25 --0.1
	NDefines.NAI.UPGRADES_DEFICIT_LIMIT_DAYS = 365 --50                 -- Ai will avoid upgrading units in the field to new templates if it takes longer than this to fullfill their equipment need
	NDefines.NAI.DIVISION_MATCH_ROLE_BOOST_FACTOR = 1.0 -- 0.600 --1.2                 -- When finding closest matching existing template to a target template, boost the score by this much if the template also has the correct role -- It is clamped to 1.000 we cant have 0.600

	--------------------------------------------------------------------------------------------------------------
	-- DIVISION PRODUCTION
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.MANPOWER_RATIO_REQUIRED_TO_PRIO_MOBILIZATION_LAW = 0.4		-- percentage of manpower in field is desired to be buffered for AI when it has upcoming wars or already at war. if it has less manpower, it will prio manpower laws

	NDefines.NAI.DEPLOY_MIN_TRAINING_SURRENDER_FACTOR = 0.5		-- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime while surrender progress is higher than 0 
	NDefines.NAI.DEPLOY_MIN_EQUIPMENT_SURRENDER_FACTOR = 0.8	-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime while surrender progress is higher than 0 
	NDefines.NAI.DEPLOY_MIN_TRAINING_PEACE_FACTOR = 0.4		-- Required percentage of training (1.0 = 100%) for AI to deploy unit in peacetime
	NDefines.NAI.DEPLOY_MIN_EQUIPMENT_PEACE_FACTOR = 0.9	-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in peacetime
	NDefines.NAI.DEPLOY_MIN_TRAINING_WAR_FACTOR = 0.9		-- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
	NDefines.NAI.DEPLOY_MIN_EQUIPMENT_WAR_FACTOR = 0.9		-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
	NDefines.NAI.DEPLOY_MIN_EQUIPMENT_CAP_DEPLOY_FACTOR = 0.85 -- If training is capped by equipment deficit and we have reached that cap, deploy unit anyway if percentage is above this (reinforce in field instead).

	--------------------------------------------------------------------------------------------------------------
	-- EQUIPMENT PRODUCTION
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.PRODUCTION_EQUIPMENT_SURPLUS_FACTOR = 1 -- [0.4] -- Base value for how much of currently used equipment the AI will at least strive to have in stock


	NDefines.NAI.SHIPS_PRODUCTION_BASE_COST = 1
	NDefines.NAI.NEEDED_NAVAL_FACTORIES_EXPENSIVE_SHIP_BONUS = 1000
	NDefines.NAI.PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL = 0.001 -- temp fix
	---NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_EXPENSIVE = 0.01
	---NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_CHEAP = 0.01

	NDefines.NAI.NAVAL_DOCKYARDS_SHIP_FACTOR = 1000			-- The extent to which number of dockyards play into amount of sips a nation wants
	NDefines.NAI.NAVAL_BASES_SHIP_FACTOR = 1000				-- The extent to which number of naval bases play into amount of sips a nation wants
	NDefines.NAI.NAVAL_STATES_SHIP_FACTOR = 1000			-- The extent to which number of states play into amount of sips a nation wants

	--------------------------------------------------------------------------------------------------------------
	-- FUEL
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_ARMY_MAX_CONSUMPTION = 365  -- AI will try to buffer at least this amount of days on max consumption, will trade if necesarry and will go into fuel saving mode/aggresive mode using this buffer 
	NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_AIR_MAX_CONSUMPTION  = 365  -- AI will try to buffer at least this amount of days on max consumption, will trade if necesarry and will go into fuel saving mode/aggresive mode using this buffer
	NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_NAVY_MAX_CONSUMPTION = 365  -- AI will try to buffer at least this amount of days on max consumption, will trade if necesarry and will go into fuel saving mode/aggresive mode using this buffer

	--------------------------------------------------------------------------------------------------------------
	-- DIPLOMACY
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.DIPLOMACY_SEND_MAX_FACTION = 0.75


	NDefines.NAI.GENERATE_WARGOAL_THREAT_BASELINE = 0.6

	NDefines.NAI.LENDLEASE_FRACTION_OF_PRODUCTION = 0.25 --0.5
	NDefines.NAI.LENDLEASE_FRACTION_OF_STOCKPILE = 0.125 --0.25

	--------------------------------------------------------------------------------------------------------------
	-- PP
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.NEW_LEADER_EXTRA_PP_FACTOR = 1 --2.0								 -- Country must have at least this many times extra PP to get new admirals or army leaders

	NDefines.NAI.DIPLOMACY_IMPROVE_RELATION_COST_FACTOR = 7.0                       -- Desire to boost relations subtracts the cost multiplied by this

	NDefines.NAI.COMMAND_POWER_BEFORE_SPEND_ON_TRAITS = 65.0

	--------------------------------------------------------------------------------------------------------------
	-- LAND AI
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.MIN_AI_UNITS_PER_TILE_FOR_STANDARD_COHESION = 2.0	-- How many units should we have for each tile along a front in order to switch to standard cohesion (less moving around)
	NDefines.NAI.MIN_FRONT_SIZE_TO_CONSIDER_STANDARD_COHESION = 2000	-- How long should fronts be before we consider switching to standard cohesion (under this, standard cohesion fronts will switch back to relaxed)

	NDefines.NAI.ASSIGN_TANKS_TO_WAR_FRONT = 8.0 --4.0
	NDefines.NAI.ASSIGN_TANKS_TO_NON_WAR_FRONT = 0.2 --0.4

	NDefines.NMilitary.PLAN_EXECUTE_RUSH = -1000									-- When looking for an attach target, this score limit is required in the battle plan to consider province for attack
	NDefines.NMilitary.PLAN_EXECUTE_CAREFUL_LIMIT = 10

	NDefines.NAI.FALLBACK_LOSING_FACTOR = 0.0 					                    -- The lower this number  the longer the AI will hold the line before sending them to the fallback line

	NDefines.NAI.HOUR_BAD_COMBAT_REEVALUATE = 72                                 	-- if we are in combat for this amount and it goes shitty then try skipping it

	NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_LOW = 0.85							-- Minimum org % for a unit to actively attack an enemy unit when executing a plan
	NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_LOW = 0.85						-- Minimum strength for a unit to actively attack an enemy unit when executing a plan

	NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_MED = 0.65							-- (LOW,MED,HIGH) corresponds to the plan execution agressiveness level.
	NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_MED = 0.65	

	NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_HIGH = 0.5		
	NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_HIGH = 0.5	

	NDefines.NAI.PLAN_FACTION_STRONG_TO_EXECUTE = 0.65 --0.80	0.60		        -- % or more of units in an order to consider ececuting the plan
	NDefines.NAI.ORG_UNIT_STRONG = 0.75												-- Organization % for unit to be considered strong
	NDefines.NAI.STR_UNIT_STRONG = 0.75												-- Strength (equipment) % for unit to be considered strong

	NDefines.NAI.PLAN_FACTION_NORMAL_TO_EXECUTE = 0.65
	NDefines.NAI.ORG_UNIT_NORMAL = 0.6 --6												-- Organization % for unit to be considered normal
	NDefines.NAI.STR_UNIT_NORMAL = 0.6 --6												-- Strength (equipment) % for unit to be considered normal

	NDefines.NAI.PLAN_FACTION_WEAK_TO_ABORT = 0.5 --0.50		0.65		        -- % or more of units in an order to consider ececuting the plan
	NDefines.NAI.ORG_UNIT_WEAK = 0.35 --0.45												-- Organization % for unit to be considered weak
	NDefines.NAI.STR_UNIT_WEAK = 0.4 --0.45												-- Strength (equipment) % for unit to be considered weak

	NDefines.NAI.PLAN_AVG_PREPARATION_TO_EXECUTE = 0.4				            -- % or more average plan preparation before executing


	NDefines.NAI.PLAN_ACTIVATION_MAJOR_WEIGHT_FACTOR = 1		                    -- AI countries will hold on activating plans if stronger countries have plans in the same location. Majors count extra (value of 1 will negate this)
	NDefines.NAI.PLAN_ACTIVATION_PLAYER_WEIGHT_FACTOR = 1 		                -- AI countries will hold on activating plans if player controlled countries have plans in the same location. Majors count extra (value of 1 will negate this)

	NDefines.NAI.PLAN_MIN_SIZE_FOR_FALLBACK = 5000					                -- A country with less provinces than this will not draw fallback plans  but rather station their troops along the front


	-- these are all 3 numbers for min, desired, max unit need weights for area defense
	NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_VP_WEIGHT = { 1.0, 1.0, 1.0 }
	NDefines.NAI.AREA_DEFENSE_CAPITAL_VP_WEIGHT = { 0.0, 1.5, 2.0 }
	NDefines.NAI.AREA_DEFENSE_HOME_VP_WEIGHT = { 0.0, 0.75, 1.0 }
	NDefines.NAI.AREA_DEFENSE_OTHER_VP_WEIGHT = { 0.0, 0.5, 1.0 }

	NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_COAST_WEIGHT = { 0.0, 0.0, 0.0 }
	NDefines.NAI.AREA_DEFENSE_CAPITAL_COAST_WEIGHT = { 0.0, 0.3, 1.0 }
	NDefines.NAI.AREA_DEFENSE_HOME_COAST_WEIGHT = { 0.0, 0.2, 0.75 }
	NDefines.NAI.AREA_DEFENSE_OTHER_COAST_WEIGHT = { 0.0, 0.0, 0.0 }

	NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_BASE_WEIGHT = { 0.0, 0.0, 0.0 }
	NDefines.NAI.AREA_DEFENSE_CAPITAL_BASE_WEIGHT = { 0.5, 1.5, 1.5 }
	NDefines.NAI.AREA_DEFENSE_HOME_BASE_WEIGHT = { 0.5, 1.5, 1.5 }
	NDefines.NAI.AREA_DEFENSE_OTHER_BASE_WEIGHT = { 0.5, 1.0, 1.0 }
		
	--------------------------------------------------------------------------------------------------------------
	-- NAVY AI
	--------------------------------------------------------------------------------------------------------------

	NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING = 0.10 -- maximum ratio of screens forces to be used in mine sweeping

	NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO_MAX_MINES = 250 -- highest mines for highest prio for mine missions

	NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_MINE_LAYING = 0.05 -- maximum ratio of screens forces to be used in mine laying


	NDefines.NAI.MISSING_CONVOYS_BOOST_FACTOR = 0.0


	NDefines.NAI.CAPITAL_TASKFORCE_MAX_CAPITAL_COUNT = 6 		-- optimum capital count for capital taskforces
	NDefines.NAI.SCREEN_TASKFORCE_MAX_SHIP_COUNT = 8			-- optimum screen count for screen taskforces
	NDefines.NAI.SUB_TASKFORCE_MAX_SHIP_COUNT = 10 				-- optimum sub count for sub taskforces



	NDefines.NAI.MIN_NAVAL_MISSION_PRIO_TO_ASSIGN = {  -- priorities for regions to get assigned to a mission
		0, -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
		200, -- PATROL		
		200, -- STRIKE FORCE 
		200, -- CONVOY RAIDING
		100, -- CONVOY ESCORT
		200, -- MINES PLANTING	
		100, -- MINES SWEEPING	
		0, -- TRAIN
		0, -- RESERVE_FLEET
		100, -- NAVAL INVASION SUPPORT
	}

	NDefines.NAI.HIGH_PRIO_NAVAL_MISSION_SCORES = {  -- priorities for regions to get assigned to a mission
		0, -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
		3800, -- PATROL - 100000	
		1000, -- STRIKE FORCE 
		4000, -- CONVOY RAIDING ---test to see if UK block Ethiopia was 1500
		3000, -- CONVOY ESCORT - 1000
		600, -- MINES PLANTING	
		300, -- MINES SWEEPING	
		0, -- TRAIN
		0, -- RESERVE_FLEET
		1000, -- NAVAL INVASION SUPPORT
	}

	NDefines.NAI.MAX_MISSION_PER_TASKFORCE = {  -- max mission region/taskforce ratio
		0, -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
		1.5, -- PATROL		
		6, -- STRIKE FORCE 
		6, -- CONVOY RAIDING ---test to see if UK block Ethiopia was 1.5
		2, -- CONVOY ESCORT
		2, -- MINES PLANTING
		2, -- MINES SWEEPING
		0, -- TRAIN
		0, -- RESERVE_FLEET
		10, -- NAVAL INVASION SUPPORT
	}

	-------------------------
	-- naval invasions
	-------------------------


	---NDefines.NAI.ENEMY_NAVY_STRENGTH_DONT_BOTHER = 3							-- If the enemy has a navy at least these many times stronger that the own, don't bother invading
	---NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE = 0 --0.08			-- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend.
	---NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE_DEFENSIVE = 0 --0.4	-- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend, but while being a defensive country.


	NDefines.NAI.INVASION_DISTANCE_RANDOMNESS = 600	---more long naval invasions test delete if problematic								-- This higher the value the more unpredictable the invasions. Compares to actual map distance in pixels.
	NDefines.NAI.INVASION_COASTAL_PROVS_PER_ORDER = 12 --24								-- AI will consider one extra invasion per number of provinces stated here (num orders = total coast / this)


	NDefines.NAI.MAX_INVASION_SIZE = 20 --24									-- max invasion group size


	-------------------------
	-- convoy escorts
	-------------------------


	NDefines.NAI.REGION_THREAT_LEVEL_TO_BLOCK_REGION = 25 * 200		-- How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY ) so the AI will decide to mark the region as avoid
	NDefines.NAI.REGION_CONVOY_DANGER_DAILY_DECAY = 2				-- When convoys are sunk it generates threat in the region which the AI uses to prio nalval missions

	NDefines.NAI.CONVOY_ESCORT_MUL_FROM_NO_CONVOYS = 0 -- score multiplier when no convoys are around


	NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MIN = 0.40 --0.20 -- maximum ratio of all screen-ships forces to be used in convoy defense (increases up to max as AI loses convoys).
	NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX = 0.6 --0.70 -- maximum ratio of all screen-ships forces to be used in convoy defense (increases up to max as AI loses convoys).

	NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX_CONVOY_THREAT = 500 -- 1500 -- AI will increase screen assignment for escort missions as threate increases


	--------------------------------------------------------------------------------------------------------------
	-- AIR AI
	--------------------------------------------------------------------------------------------------------------


	NDefines.NAI.MAX_FUEL_CONSUMPTION_RATIO_FOR_AIR_TRAINING = 1


	-------------------------
	-- Land combat
	-------------------------


	NDefines.NAI.LAND_COMBAT_OUR_COMBATS_AIR_IMPORTANCE = 1000		-- Strategic importance of our armies in the combats


	-------------------------
	-- Defense
	-------------------------

	NDefines.NAI.LAND_DEFENSE_FIGHERS_PER_PLANE = 1				-- Amount of air superiority planes requested per enemy plane
	NDefines.NAI.LAND_DEFENSE_INTERSEPTORS_PER_BOMBERS = 1		-- Amount of air interceptor planes requested per enemy bomber


	NDefines.NAI.LAND_DEFENSE_CIVIL_FACTORY_IMPORTANCE = 800 -- 50			-- Strategic importance of civil factories
	NDefines.NAI.LAND_DEFENSE_MILITARY_FACTORY_IMPORTANCE = 880 -- 70		-- Strategic importance of military factories
	NDefines.NAI.LAND_DEFENSE_NAVAL_FACTORY_IMPORTANCE = 420 -- 30			-- Strategic importance of naval factories


	-------------------------
	-- Str bombing
	-------------------------

	NDefines.NAI.STR_BOMB_PLANES_PER_CIV_FACTORY = 200				-- Amount of planes requested per enemy civ factory
	NDefines.NAI.STR_BOMB_PLANES_PER_MIL_FACTORY = 205				-- Amount of planes requested per enemy military factory
	NDefines.NAI.STR_BOMB_PLANES_PER_NAV_FACTORY = 105				-- Amount of planes requested per enemy naval factory
	NDefines.NAI.STR_BOMB_PLANES_PER_SUPPLY_HUB = 30                 -- Amount of planes requested per enemy supply node
	NDefines.NAI.STR_BOMB_MIN_EXCORT_PLANES = 200					-- Min amount of planes requested to excort operations
		
	-------------------------
	-- Naval air
	-------------------------


	NDefines.NAI.NAVAL_STRIKE_PLANES_PER_SHIP = 40					-- Amount of bombers requested per enemy ship

	NDefines.NAI.NAVAL_SHIP_AIR_IMPORTANCE = 10000 --2.0					-- Naval ship air importance

	NDefines.NAI.NAVAL_IMPORTANCE_SCALE = 2 --0.65						-- Naval total importance scale (every naval score get's multiplied by it)


	NDefines.NAI.NAVAL_PATROL_PLANES_PER_SHIP_PATROLLING = 20 --10.0		-- Amount of naval patrol planes per ship on a patrol mission
	NDefines.NAI.NAVAL_PATROL_PLANES_PER_SHIP_RAIDING = 40 --10.0		-- Amount of naval patrol planes per ship on a convoy raid mission
	NDefines.NAI.NAVAL_PATROL_PLANES_PER_SHIP_ESCORTING = 20 --10.0		-- Amount of naval patrol planes per ship on a convoy escort mission


	--- Land Defines
	NDefines.NMilitary.PLAN_EXECUTE_BALANCED_LIMIT = -10.0			-- When looking for an attach target, this score limit ---is required in the battle plan to consider province for attack suggested define by SensitiveDannyBoi
	NDefines.NMilitary.PLAN_PORVINCE_PORT_BASE_IMPORTANCE = 18.0		-- Added importance for area defense province with a port
	NDefines.NMilitary.PLAN_PORVINCE_PORT_LEVEL_FACTOR = 0.5			-- Bonus factor for port level
	NDefines.NAI.AREA_DEFENSE_CIVIL_WAR_IMPORTANCE = 5.0				-- Area defense order importance value when a country is in a civil war as target or revolter. vanilla 10000 lolwut?? am I missing something here :
	NDefines.NMilitary.PLAN_PORVINCE_RESISTANCE_BASE_IMPORTANCE = 150.0 -- Used when calculating the calue of defense area provinces for the battle plan system (factored by resistance level) vanilla 10.0
	NDefines.NMilitary.PLAN_PROVINCE_LOW_VP_IMPORTANCE_FRONT = 1.0    -- Used when calculating the calue of fronts in the battle plan system vanilla 2.0


	--- Navy Defines
	NDefines.NAI.ESTIMATED_CONVOYS_PER_DIVISION = 18			-- Not always correct, but mainly used to make sure AI does not go crazy vanilla 6
	---NDefines.NAI.MAX_DISTANCE_NAVAL_INVASION = 100.0				-- AI is extremely unwilling to plan naval invasions above this naval distance limit. van 250 this value is multiplied by 15.92 I think for the actual km distance, aka 250 ='s almost 4k km.
	NDefines.NAI.NAVY_PREFERED_MAX_SIZE = 50
	NDefines.NAI.RESEARCH_NAVAL_DOCTRINE_NEED_GAIN_FACTOR = 0.075 -- Multiplies value based on relative naval industry size / country size.
	NDefines.NAI.NAVAL_MISSION_INVASION_BASE = 30000					-- Base score for region with naval invasion (modified dynamically by prioritizing orders)

	--- Diplo Defines
	NDefines.NDiplomacy.NAP_UNBREAKABLE_MONTHS = 18                    -- NAPS cannot be broken for this many months
	NDefines.NDiplomacy.NAP_BREAK_FORCE_BALANCE_1 = 5.0              	-- 2-1 brigades along the border required to break NAP
	NDefines.NDiplomacy.NAP_BREAK_FORCE_BALANCE_2 = 1.0              	-- 1-1 brigades along the border required to break NAP
	NDefines.NDiplomacy.NAP_BREAK_FORCE_BALANCE_3 = 0.5 
	NDefines.NAI.MAX_VOLUNTEER_ARMY_FRACTION = 0.05			-- Countries will not send more than their forces time this number to aid another country
	NDefines.NAI.DIPLO_PREFER_OTHER_FACTION = -400		-- The country has yet to ask some other faction it would prefer to be a part of.
	NDefines.NTrade.DISTANCE_TRADE_FACTOR = -0.0001			-- Trade factor is modified by distance times this vanilla -.02
	NDefines.NAI.TRADEABLE_FACTORIES_FRACTION = 0.6	-- Will at most trade away this fraction of factories.
	NDefines.NDiplomacy.NOT_READY_FOR_WAR_BASE = -100 -- AI should be unwilling to enter accept a call to war if not ready ---for war against the relevant enemies. vanilla -50 - suggested define by SensitiveDannyBoi
	NDefines.NAI.LENDLEASE_FRACTION_OF_PRODUCTION = 0.1		-- Base fraction AI would send as lendlease 0.5 vanilla less base production used, perhaps will promote AI to send more?

	--- AI Defines
	NDefines.NAI.MICRO_POCKET_SIZE = 3						-- Pockets with a size equal to or lower than this will be mocroed by the AI, for efficiency.
	NDefines.NAI.UPGRADE_DIVISION_RELUCTANCE = .0042 -- aggressively trying to get the AI to upgrade divisions to newer templates, may work, may not, but it doesn't break anything. vanilla is 14, .0042 is just over 1 hour, where I believe the vanilla value at 14 = 14 days. So it should be checking to upgrade ONE division every single hour. 
	---NDefines.NAI.RESEARCH_BONUS_FACTOR = 4.5 				-- To which extent AI should care about bonuses to research
	---NDefines.NAI.RESEARCH_AHEAD_OF_TIME_FACTOR = 7.0 		-- To which extent AI should care about ahead of time penalties to research

	NDefines.NAI.RESERVE_TO_COMMITTED_BALANCE = 0.35  ----next test, remove if problematic

	------Better Lend Lease AI

	NDefines.NProduction.EQUIPMENT_LEND_LEASE_WEIGHT_FACTOR     = 0.0025
	NDefines.NProduction.LEND_LEASE_DELIVERY_TOTAL_DAYS = 15

	NDefines.NAI.DIPLOMACY_LEND_LEASE_MONTHS_TO_CANCEL = 16
	NDefines.NAI.MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE = 1500
	NDefines.NAI.MINIMUM_CONVOY_TO_ASK_LEND_LEASE = 500
	NDefines.NAI.MINIMUM_FUEL_DAYS_TO_ASK_LEND_LEASE = 10
	NDefines.NAI.MINIMUM_FUEL_DAYS_TO_ACCEPT_LEND_LEASE = 5

	NDefines.NAI.DIPLOMACY_ACCEPT_ATTACHE_OPINION_TRASHHOLD = 0



	---- BI Additions

	-- DEPLOYMENT LOGIC
		
		NDefines.NAI.START_TRAINING_EQUIPMENT_LEVEL = 0.8               -- AI will not start to train if equipment drops below this level
		NDefines.NAI.STOP_TRAINING_EQUIPMENT_LEVEL = 0.7                -- AI will not train if equipment drops below this level
				
		NDefines.NAI.MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_PEACETIME = 0.1		-- deployment will try to buffer a ratio of manpower (for reinforcements) during peace time
		NDefines.NAI.MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_WARTIME = 0.2			-- deployment will try to buffer a ratio of manpower (for reinforcements) during war time
		
		NDefines.NAI.DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_WARTIME = 0.1 				-- deployment will try to buffer a ratio of deployed manpower (for reinforcements) during war time
		NDefines.NAI.DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_PEACETIME = 0.1     		-- deployment will try to buffer a ratio of deployed manpower (for reinforcements) during peace time
		
		
	-- PRODUCTION LOGIC
	 
		NDefines.NAI.PRODUCTION_EQUIPMENT_SURPLUS_FACTOR_GARRISON = 0.15	-- Base value for how much of currently used equipment the AI will at least strive to have in stock for garrison forces
		NDefines.NAI.PRODUCTION_LINE_SWITCH_SURPLUS_NEEDED_MODIFIER = 0.0	-- Is modified by efficiency modifiers. WHAT THE FUCK DOES THIS DO
		
		NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_EXPENSIVE = 0.05      -- If produced item is expensive (producing less than one/week), wait to finish item if progress is above this
		NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_CHEAP = 0.75          -- If produced item is cheap (producing more than one/week), wait to finish item if progress is above this
		
		NDefines.NAI.DEFAULT_SUPPLY_TRUCK_BUFFER_RATIO = 0.1	-- ai will set to truck buffer ratio to this. can be modified by wanted_supply_trucks min_wanted_supply_trucks ai strats
		NDefines.NAI.DEFAULT_SUPPLY_TRAIN_NEED_FACTOR = 0.25     -- AI multiplies current train usage by this to determine desired nr of wanted trains. Can be modified by wanted_supply_train min_wanted_supply_trains ai strats.
			

	-- CONSTRUCTION LOGIC
		NDefines.NAI.MAX_THREAT_FOR_FIRST_YEAR_CIVILIAN_MODE = 0 -- above this threshold, ai will leave first year civilian factory mode which bumps it civilian factory scores while building
		NDefines.NAI.WAIT_YEARS_BEFORE_FREER_BUILDING = 0				-- The AI will skip considering certain buildings during the buildup phase, after htese many years it starts building them regardless of threat.
		NDefines.NAI.DOCKYARDS_PER_NAVAL_DESIRE_EFFECT = 0.0			-- Effects how much AI wants to build dockyards based on how navally focused they are in general. Recommended range -100.0 to 100.0.
		NDefines.NAI.BUILD_REFINERY_LACK_OF_RESOURCE_MODIFIER = 0.0	-- How much lack of resources are worth when evaluating what to build.
		
		NDefines.NAI.FIX_SUPPLY_BOTTLENECK_SATURATION_THRESHOLD = 0.75  -- Try to fix supply bottlenecks if supply node saturation exceeds this value.
		NDefines.NAI.UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS = 720      -- Check for and try to fix supply bottlenecks this often. (168 hours = 1 week)
		
		NDefines.NAI.BUILDING_TARGETS_BUILDING_PRIORITIES = {				-- buildings in order of pirority when considering building targets strategies. First has the greatest priority, omitted has the lowest. NOTE: not all buildings are supported by building targets strategies.
			'arms_factory',
			'infrastructure', 
			'industrial_complex',
			'rail_way',
		}

	-- BATTLEPLAN ACTIVATION
		
		NDefines.NAI.MAX_MICRO_ATTACKS_PER_ORDER = 4					-- affects performance; AI goes through its orders and checks if there are situations to take advantage of

		NDefines.NAI.FRONT_EVAL_UNIT_SUPPLY_AND_ORG_LACK_IMPACT = 0.2			-- scale how painful the AI thinks a combined lack of supply and organization is for units


		NDefines.NAI.AGGRESSIVENESS_CHECK_BASE = 2.0                            -- front comparison where ai will consider aggressive stance, unless it is already then the number above is used
		NDefines.NAI.AGGRESSIVENESS_CHECK_EASY_TARGET = -0.4                    -- if target nation is flagged as easy target we also adjust down the front comparison needed
		NDefines.NAI.AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED = 3.0				-- if front strength balance is at or above this value versus a party fortified enemy, we do a balanced attack
		NDefines.NAI.AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED_WEAK_POINTS = 1.5	-- if front strength balance is at or above this value versus a party fortified enemy, we rush attack weak points; below this value, we are careful
		
		NDefines.NAI.ATTACK_HEAVILY_DEFENDED_LIMIT = 1				-- AI will not launch attacks against heavily defended fronts unless they consider to have this level of advantage (1.0 = 100%)
		
		NDefines.NAI.FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.45 -- ai will consider a front fortified if this ratio of provinces has fort
		NDefines.NAI.HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.6 -- ai will consider a front super fortified if this ratio of provinces has lots of forts
		NDefines.NAI.ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS = 0.0		-- front unit request factor at max enemy fortification
		NDefines.NAI.ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS_MAX = 0.0 	-- max factor that can be added by enemy fortification
		
		NDefines.NAI.HOURS_BETWEEN_ENCIRCLEMENT_DISCOVERY = 360			  -- Per army, interval in hours between refresh of which provinces it considers make up potential encirclement points
		
		NDefines.NAI.DESPERATE_AI_MIN_UNIT_ASSIGN_TO_ESCAPE = 0			-- AI will assign at least this amount of units to break from desperate situations
		NDefines.NAI.DESPERATE_AI_WEAK_UNIT_STR_LIMIT = 0.8					-- ai will increase number of units assigned to break from desperate situations when units are start falling lower than this str limit
		NDefines.NAI.DESPERATE_AI_MIN_ORG_BEFORE_ATTACK = 0.5					-- ai will wait for this much org to attack an enemy prov in desperate situations
		NDefines.NAI.DESPERATE_AI_MIN_ORG_BEFORE_MOVE = 0.08					-- ai will wait for this much org to move in desperate situations
		NDefines.NAI.DESPERATE_ATTACK_WITHOUT_ORG_WHEN_NO_ORG_GAIN = 178		-- if ai can't regain enough org to attack in this many hours, it will go truly desperate and attack anyway (still has to wait for move org)
		
		NDefines.NAI.VP_LEVEL_IMPORTANCE_MEDIUM = 5				-- Victory points with values higher than or equal to this are considered to be of medium importance.
		
	-- INVASION LOGIC
		
		NDefines.NAI.ENEMY_NAVY_STRENGTH_DONT_BOTHER = 1.9						-- If the enemy has a navy at least these many times stronger that the own, don't bother invading
		NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE = 0.09			-- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend.
		NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE_DEFENSIVE = 0.1 -- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend, but while being a defensive country.
		
		NDefines.NAI.MAX_UNIT_RATIO_FOR_INVASIONS = 0.3							-- countries won't use armies more than this ratio of total units for invasions
		
		NDefines.NAI.MAX_DISTANCE_NAVAL_INVASION = 250.0						-- AI is extremely unwilling to plan naval invasions above this naval distance limit.
		NDefines.NAI.INVASION_COASTAL_PROVS_PER_ORDER = 14				-- AI will consider one extra invasion per number of provinces stated here (num orders = total coast / this)
		
		NDefines.NAI.MAX_INVASION_FRONT_SCORE = 2000							-- max score for naval invasion front scores
		NDefines.NAI.NAVAL_INVADED_AREA_PRIO_MULT = 2.0									-- fronts that belongs to recent invasions gets more prio
		NDefines.NAI.MIN_NUM_CONQUERED_PROVINCES_TO_DEPRIO_NAVAL_INVADED_FRONTS = 30	-- if you conquer this amount of provinces after a naval invasion, it will lose its prio status and will act as a regular front
		
		NDefines.NAI.FAILED_INVASION_AVOID_DURATION = 135                   -- after a failed invasion, AI will down-prioritize invading the same area again for this number of days
		
	-- RESEARCH 

		NDefines.NAI.RESEARCH_NEW_WEIGHT_FACTOR = 0 				-- if ai_focus need is 0 (which it always is now), THIS+1. always keep at 0 
		NDefines.NAI.RESEARCH_AHEAD_BONUS_FACTOR = -0.4          	-- AOT bonus * ( THIS * -1 ). has a large impact on score, -1 = ~double score
		NDefines.NAI.RESEARCH_BONUS_FACTOR = -0.5 					-- bonus * ( THIS * -1 ). has a large impact on score, -1 = ~double score
		NDefines.NAI.MAX_AHEAD_RESEARCH_PENALTY = 8            		-- if AOT debuff is above this, ai score is 0. 8 = 1 year
		NDefines.NAI.RESEARCH_AHEAD_OF_TIME_FACTOR = 8.0 			-- How steep the factor for AOT techs is
		NDefines.NAI.RESEARCH_BASE_DAYS = 100						-- ( THIS + modifier@research_speed ) * technology cost * 0.01
		NDefines.NAI.RESEARCH_MULTI_DOCTRINE_SCORE = 0.25           -- ai_score * THIS
		NDefines.NAI.XP_RATIO_REQUIRED_TO_RESEARCH_WITH_XP = 1.0	-- AI will at least need this amount of xp compared to cost of a tech to reserch it with XP			
		NDefines.NAI.RESEARCH_WITH_XP_AI_WEIGHT_MULT = 1.5 		-- AI will bump score of a research with this mult if it can use XP
		NDefines.NAI.RESEARCH_NEW_DOCTRINE_RANDOM_FACTOR = 0.0	-- How much randomness is allowed to contribute to do new research expressed as a factor of total tech weights. Higher means more random exploration.
	
-- MS Defines
	NDefines.NOperatives.MAX_RECRUITED_OPERATIVES = 500

-- NE Defines
	NDefines.NDiplomacy.MAX_TRUST_VALUE = 200
	NDefines.NDiplomacy.MIN_TRUST_VALUE = -500
	
-- RealisticArmsProduction Defines
	NDefines.NProduction.BASE_FACTORY_SPEED_MIL = 9
	NDefines.NProduction.BASE_FACTORY_SPEED_NAV = 5

	NDefines.NMilitary.UNIT_UPKEEP_ATTRITION = 0.03 							--Constant attrition value applied to armies.


	NDefines.NProduction.MAX_CIV_FACTORIES_PER_LINE = 10

	NDefines.NAir.FUEL_COST_MULT = 0.175
	NDefines.NMilitary.ARMY_FUEL_COST_MULT = 0.25
	NDefines.NNavy.FUEL_COST_MULT = 0.05

-- Tension Defines
	NDefines.NDiplomacy.TENSION_DECAY_DAILY = 0.025

-- Ten Support Companies Defines
	NDefines.NMilitary.MAX_DIVISION_SUPPORT_WIDTH = 2;
