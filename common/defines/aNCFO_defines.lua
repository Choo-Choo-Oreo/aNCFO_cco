		-- aNCFO Defines
NDefines.NGame.START_DATE = "1924.1.1.12"
NDefines.NGame.END_DATE = "1949.1.1.1"
NDefines.NGame.MAP_SCALE_PIXEL_TO_KM = 7.8254
NDefines.NGame.HANDS_OFF_START_TAG = "LLA"
NDefines.NBuildings.MAX_SHARED_SLOTS = 55


		-- frontlineai Defines


--Hello, if you're looking to put this in a modpack, ask and link, but jokes on you, it's compatible in theory with literally every mod so you shouldn't have to put it in a modpack!						
		
NDefines.NAI.GARRISON_FRACTION = 0.2					-- How large part of a front should always be holding the line rather than advancing at the enemy
	
NDefines.NAI.DIPLOMACY_REJECTED_WAIT_MONTHS_BASE = 1	-- AI will not repeat offers until at least this time has passed, and at most the double
	
NDefines.NAI.MIN_INVASION_PLAN_VALUE_TO_EXECUTE	 = 0.0	-- AI will typically avoid carrying out a plan it below this value (0.0 is considered balanced).

NDefines.NAI.ENTRENCHMENT_WEIGHT = 4.0					-- AI should favour units with less entrenchment when assigning units around.

NDefines.NAI.UNIT_ASSIGNMENT_TERRAIN_IMPORTANCE = 20.0	--- diminshed by 4x because of Greece-- Terrain score for units are multiplied by this when the AI is deciding which front they should be assigned to
	
NDefines.NAI.SEND_VOLUNTEER_EVAL_BASE_DISTANCE = 175.0  -- How far away it will evaluate sending volunteers if not a major power
NDefines.NAI.SEND_VOLUNTEER_EVAL_MAJOER_POWER = 1.0 	-- How willing major powers are to send volunteers.
NDefines.NAI.SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR = 0.9 -- How much AI containment factors into its evaluation of sending volunteers.

NDefines.NAI.PLAN_ACTIVATION_SUPERIORITY_AGGRO = 10 --default 1.0		-- How aggressive a country is in activating a plan based on how superiour their force is.
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

-------------------------
-- RESEARCH
-------------------------

-------------------------
-- DESIGNS
-------------------------

NDefines.NAI.REFIT_SHIP_RELUCTANCE = 5000							-- How often to consider refitting to new equipment variants for ships in the field
NDefines.NAI.REFIT_SHIP_PERCENTAGE_OF_FORCES = 0.30				-- How big part of the navy that should be considered for refitting

NDefines.NAI.DIVISION_DESIGN_MANPOWER_WEIGHT = 0 --0.005
NDefines.NAI.DIVISION_DESIGN_STOCKPILE_WEIGHT = 0 --0.01
NDefines.NAI.DIVISION_DESIGN_COMBAT_WIDTH_TARGET_WEIGHT = -10000 -- -200	        -- This score is reduced the farther the width is from the target width (if set)

NDefines.NAI.UPGRADE_PERCENTAGE_OF_FORCES = 0.25 --0.1
NDefines.NAI.UPGRADES_DEFICIT_LIMIT_DAYS = 180 --365 --50      ---test if it makes ai more sufficient remove if problematic                     -- Ai will avoid upgrading units in the field to new templates if it takes longer than this to fullfill their equipment need

-------------------------
-- DIVISION PRODUCTION
-------------------------

NDefines.NAI.MANPOWER_RATIO_REQUIRED_TO_PRIO_MOBILIZATION_LAW = 0.4		-- percentage of manpower in field is desired to be buffered for AI when it has upcoming wars or already at war. if it has less manpower, it will prio manpower laws

NDefines.NAI.DEPLOY_MIN_TRAINING_SURRENDER_FACTOR = 0.5		-- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime while surrender progress is higher than 0 
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_SURRENDER_FACTOR = 0.8	-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime while surrender progress is higher than 0 
NDefines.NAI.DEPLOY_MIN_TRAINING_PEACE_FACTOR = 0.4		-- Required percentage of training (1.0 = 100%) for AI to deploy unit in peacetime
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_PEACE_FACTOR = 0.9	-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in peacetime
NDefines.NAI.DEPLOY_MIN_TRAINING_WAR_FACTOR = 0.9		-- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_WAR_FACTOR = 0.9		-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_CAP_DEPLOY_FACTOR = 0.85 -- If training is capped by equipment deficit and we have reached that cap, deploy unit anyway if percentage is above this (reinforce in field instead).

-------------------------
-- EQUIPMENT PRODUCTION
-------------------------

NDefines.NAI.PRODUCTION_EQUIPMENT_SURPLUS_FACTOR = 1 -- [0.4] -- Base value for how much of currently used equipment the AI will at least strive to have in stock


NDefines.NAI.SHIPS_PRODUCTION_BASE_COST = 1
NDefines.NAI.NEEDED_NAVAL_FACTORIES_EXPENSIVE_SHIP_BONUS = 1000
NDefines.NAI.PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL = 0.001 -- temp fix
NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_EXPENSIVE = 0.01
NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_CHEAP = 0.01

NDefines.NAI.NAVAL_DOCKYARDS_SHIP_FACTOR = 1000			-- The extent to which number of dockyards play into amount of sips a nation wants
NDefines.NAI.NAVAL_BASES_SHIP_FACTOR = 1000				-- The extent to which number of naval bases play into amount of sips a nation wants
NDefines.NAI.NAVAL_STATES_SHIP_FACTOR = 1000			-- The extent to which number of states play into amount of sips a nation wants

-------------------------
-- FUEL
-------------------------

NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_ARMY_MAX_CONSUMPTION = 365  -- AI will try to buffer at least this amount of days on max consumption, will trade if necesarry and will go into fuel saving mode/aggresive mode using this buffer 
NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_AIR_MAX_CONSUMPTION  = 365  -- AI will try to buffer at least this amount of days on max consumption, will trade if necesarry and will go into fuel saving mode/aggresive mode using this buffer
NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_NAVY_MAX_CONSUMPTION = 365  -- AI will try to buffer at least this amount of days on max consumption, will trade if necesarry and will go into fuel saving mode/aggresive mode using this buffer

-------------------------
-- DIPLOMACY
-------------------------

NDefines.NAI.DIPLOMACY_SEND_MAX_FACTION = 0.75


NDefines.NAI.GENERATE_WARGOAL_THREAT_BASELINE = 0.6

NDefines.NAI.LENDLEASE_FRACTION_OF_PRODUCTION = 0.25 --0.5
NDefines.NAI.LENDLEASE_FRACTION_OF_STOCKPILE = 0.125 --0.25

-------------------------
-- PP
-------------------------

NDefines.NAI.NEW_LEADER_EXTRA_PP_FACTOR = 1 --2.0								 -- Country must have at least this many times extra PP to get new admirals or army leaders

NDefines.NAI.DIPLOMACY_IMPROVE_RELATION_COST_FACTOR = 7.0                       -- Desire to boost relations subtracts the cost multiplied by this

NDefines.NAI.COMMAND_POWER_BEFORE_SPEND_ON_TRAITS = 65.0

-------------------------
-- LAND AI
-------------------------

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
	
-------------------------
-- NAVY AI
-------------------------

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


NDefines.NAI.ENEMY_NAVY_STRENGTH_DONT_BOTHER = 3							-- If the enemy has a navy at least these many times stronger that the own, don't bother invading
NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE = 0 --0.08			-- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend.
NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE_DEFENSIVE = 0 --0.4	-- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend, but while being a defensive country.


NDefines.NAI.INVASION_DISTANCE_RANDOMNESS = 600	---more long naval invasions test delete if problematic								-- This higher the value the more unpredictable the invasions. Compares to actual map distance in pixels.
NDefines.NAI.INVASION_COASTAL_PROVS_PER_ORDER = 12 --24								-- AI will consider one extra invasion per number of provinces stated here (num orders = total coast / this)


NDefines.NAI.MAX_INVASION_SIZE = 18 --24									-- max invasion group size


-------------------------
-- convoy escorts
-------------------------


NDefines.NAI.REGION_THREAT_LEVEL_TO_BLOCK_REGION = 25 * 200		-- How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY ) so the AI will decide to mark the region as avoid
NDefines.NAI.REGION_CONVOY_DANGER_DAILY_DECAY = 2				-- When convoys are sunk it generates threat in the region which the AI uses to prio nalval missions

NDefines.NAI.CONVOY_ESCORT_MUL_FROM_NO_CONVOYS = 0 -- score multiplier when no convoys are around


NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MIN = 0.40 --0.20 -- maximum ratio of all screen-ships forces to be used in convoy defense (increases up to max as AI loses convoys).
NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX = 0.6 --0.70 -- maximum ratio of all screen-ships forces to be used in convoy defense (increases up to max as AI loses convoys).

NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX_CONVOY_THREAT = 500 -- 1500 -- AI will increase screen assignment for escort missions as threate increases


-------------------------
-- AIR AI
-------------------------


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


-- Land Defines
NDefines.NMilitary.PLAN_EXECUTE_BALANCED_LIMIT = -10.0			-- When looking for an attach target, this score limit ---is required in the battle plan to consider province for attack suggested define by SensitiveDannyBoi
NDefines.NMilitary.PLAN_PORVINCE_PORT_BASE_IMPORTANCE = 18.0		-- Added importance for area defense province with a port
NDefines.NMilitary.PLAN_PORVINCE_PORT_LEVEL_FACTOR = 0.5			-- Bonus factor for port level
NDefines.NAI.AREA_DEFENSE_CIVIL_WAR_IMPORTANCE = 5.0				-- Area defense order importance value when a country is in a civil war as target or revolter. vanilla 10000 lolwut?? am I missing something here :
NDefines.NMilitary.PLAN_PORVINCE_RESISTANCE_BASE_IMPORTANCE = 150.0 -- Used when calculating the calue of defense area provinces for the battle plan system (factored by resistance level) vanilla 10.0
NDefines.NMilitary.PLAN_PROVINCE_LOW_VP_IMPORTANCE_FRONT = 1.0    -- Used when calculating the calue of fronts in the battle plan system vanilla 2.0


-- Navy Defines
NDefines.NAI.ESTIMATED_CONVOYS_PER_DIVISION = 18			-- Not always correct, but mainly used to make sure AI does not go crazy vanilla 6
NDefines.NAI.MAX_DISTANCE_NAVAL_INVASION = 100.0				-- AI is extremely unwilling to plan naval invasions above this naval distance limit. van 250 this value is multiplied by 15.92 I think for the actual km distance, aka 250 ='s almost 4k km.
NDefines.NAI.NAVY_PREFERED_MAX_SIZE = 50
NDefines.NAI.RESEARCH_NAVAL_DOCTRINE_NEED_GAIN_FACTOR = 0.075 -- Multiplies value based on relative naval industry size / country size.
NDefines.NAI.NAVAL_MISSION_INVASION_BASE = 30000					-- Base score for region with naval invasion (modified dynamically by prioritizing orders)

-- Diplo Defines
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

-- AI Defines
NDefines.NAI.MICRO_POCKET_SIZE = 2						-- Pockets with a size equal to or lower than this will be mocroed by the AI, for efficiency.
NDefines.NAI.UPGRADE_DIVISION_RELUCTANCE = .0042 -- aggressively trying to get the AI to upgrade divisions to newer templates, may work, may not, but it doesn't break anything. vanilla is 14, .0042 is just over 1 hour, where I believe the vanilla value at 14 = 14 days. So it should be checking to upgrade ONE division every single hour. 
NDefines.NAI.RESEARCH_BONUS_FACTOR = 4.5 				-- To which extent AI should care about bonuses to research
NDefines.NAI.RESEARCH_AHEAD_OF_TIME_FACTOR = 7.0 		-- To which extent AI should care about ahead of time penalties to research
NDefines.NAI.COMBINED_ARMS_LEVEL = 1                    -- 0 = Never, 1 = Infantry/Artillery, 2 = Go wild

NDefines.NAI.RESERVE_TO_COMMITTED_BALANCE = 0.3  ----next test, remove if problematic

-- Better Lend Lease AI

NDefines.NProduction.EQUIPMENT_LEND_LEASE_WEIGHT_FACTOR     = 0.0025
NDefines.NProduction.LEND_LEASE_DELIVERY_TOTAL_DAYS = 15

NDefines.NAI.DIPLOMACY_LEND_LEASE_MONTHS_TO_CANCEL = 16
NDefines.NAI.MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE = 1500
NDefines.NAI.MINIMUM_CONVOY_TO_ASK_LEND_LEASE = 500
NDefines.NAI.MINIMUM_FUEL_DAYS_TO_ASK_LEND_LEASE = 10
NDefines.NAI.MINIMUM_FUEL_DAYS_TO_ACCEPT_LEND_LEASE = 5

NDefines.NAI.DIPLOMACY_ACCEPT_ATTACHE_OPINION_TRASHHOLD = 0


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