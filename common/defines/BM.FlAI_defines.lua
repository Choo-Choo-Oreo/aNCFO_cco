 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- FRONTLINE AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AGGRESSIVENESS
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.AGGRESSIVENESS_CHECK_BASE = 1.5                -- restore vanilla (1.4 → 1.5)
NDefines.NAI.AGGRESSIVENESS_CHECK_EASY_TARGET = -0.4        -- tone down significantly (-0.7 → -0.4)
NDefines.NAI.AGGRESSIVENESS_CHECK_CAREFUL = 0.7             -- slight increase from vanilla (0.6 → 0.7)
NDefines.NAI.AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED = 1.8    -- keep (minor effect)
NDefines.NAI.AGGRESSIVENESS_CHECK_FULLY_FORTIFIED = 8.0     -- keep (negligible in practice)
NDefines.NAI.AGGRESSIVENESS_CHECK_FULLY_FORTIFIED_POCKET = 4.0   -- tone down (-0.7 → 4.0)

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- RESEARCH
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 1

NDefines.NAI.MAX_AHEAD_RESEARCH_PENALTY = 7
NDefines.NAI.XP_RATIO_REQUIRED_TO_RESEARCH_WITH_XP = 3.0 -- AI will at least need this amount of xp compared to cost of a tech to reserch it with XP
NDefines.NAI.RESEARCH_WITH_XP_AI_WEIGHT_MULT = 1.5  -- AI will bump score of a research with this mult if it can use XP

NDefines.NAI.RESEARCH_NAVAL_DOCTRINE_NEED_GAIN_FACTOR = 0.075  -- Multiplies value based on relative naval industry size / country size.

NDefines.NAI.RESEARCH_NEW_WEIGHT_FACTOR = 0.5  -- Impact of previously unexplored tech weights. Higher means more random exploration.
NDefines.NAI.RESEARCH_AHEAD_OF_TIME_FACTOR = 5.0 -- To which extent AI should care about ahead of time penalties to research
NDefines.NAI.RESEARCH_BASE_DAYS = 60 -- AI adds a base number of days when weighting completion time for techs to ensure it doesn't only research quick techs

NDefines.NAI.RESEARCH_YEARS_BEHIND_FACTOR = 0.3  -- (was 0.2)  --To which extent AI should care about not falling behind (i.e. increase weight for old tech)

NDefines.NAI.RESEARCH_LAND_DOCTRINE_NEED_GAIN_FACTOR = 0.12  -- Multiplies value based on relative military industry size / country size.

NDefines.NAI.RESEARCH_AHEAD_BONUS_FACTOR = 10.0
NDefines.NAI.RESEARCH_BONUS_FACTOR = 2.0

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- DESIGNS
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- XP THRESHOLDS
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- Land (Tank Designer)
NDefines.NAI.DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_LAND = 35
NDefines.NAI.VARIANT_CREATION_XP_RESERVE_LAND = 25   -- Must be lower than cutoff

 -- Navy (Ship Designer)
NDefines.NAI.DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_NAVY = 50
NDefines.NAI.VARIANT_CREATION_XP_RESERVE_NAVY = 35   -- Must be lower than cutoff

 -- Air (Plane Designer)
NDefines.NAI.DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_AIR = 25
NDefines.NAI.VARIANT_CREATION_XP_RESERVE_AIR = 20   -- Must be lower than cutoff

 -- Legacy System
NDefines.NAI.DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_LAND = 35
NDefines.NAI.DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_NAVY = 25
NDefines.NAI.DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_AIR = 25

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- LAND DESIGN WEIGHTS (Weight = Alternative × Demand)
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- Alternative Factor
NDefines.NAI.LAND_DESIGN_ALTERNATIVE_ABSENT = 1000000   -- vanilla
NDefines.NAI.LAND_DESIGN_ALTERNATIVE_OF_LESSER_TECH = 10000
NDefines.NAI.LAND_DESIGN_ALTERNATIVE_OF_EQUAL_TECH = 100
NDefines.NAI.LAND_DESIGN_ALTERNATIVE_OF_GREATER_TECH = 1

 -- Demand Factor - IMPROVED for smarter prioritization
NDefines.NAI.LAND_DESIGN_DEMAND_FIELD_DIVISION = 25   -- vanilla 20 increased = prioritize combat units
NDefines.NAI.LAND_DESIGN_DEMAND_TRAINING_DIVISION = 15
NDefines.NAI.LAND_DESIGN_DEMAND_GARRISON_DIVISION = 8   -- vanilla 10 decreased = less garrison focus
NDefines.NAI.LAND_DESIGN_DEMAND_UNUSED_TEMPLATE = 1
NDefines.NAI.LAND_DESIGN_DEMAND_ABSENT = 0

 -- Cutoff
NDefines.NAI.LAND_DESIGN_CUTOFF_AS_PERCENTAGE_OF_MAX = 0.25   -- vanilla 0.25 lower = more variety

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- AIR DESIGN WEIGHTS
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- Alternative Factor
NDefines.NAI.AIR_DESIGN_ALTERNATIVE_ABSENT = 1000000   -- vanilla
NDefines.NAI.AIR_DESIGN_ALTERNATIVE_OF_LESSER_TECH = 10000
NDefines.NAI.AIR_DESIGN_ALTERNATIVE_OF_EQUAL_TECH = 100
NDefines.NAI.AIR_DESIGN_ALTERNATIVE_OF_GREATER_TECH = 1

 -- Demand Factor
NDefines.NAI.AIR_DESIGN_DEMAND_MAX = 33
NDefines.NAI.AIR_DESIGN_DEMAND_MIN = 1
NDefines.NAI.AIR_DESIGN_DEMAND_ABSENT = 0

 -- Cutoff
NDefines.NAI.AIR_DESIGN_CUTOFF_AS_PERCENTAGE_OF_MAX = 0.30   -- vanilla 0.25 slightly higher for air

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- XP SPENDING DESIRES - IMPROVED for design priority
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---

NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_LAND_DOCTRINE = 1.0     -- How quickly is desire to unlock land doctrines accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_NAVAL_DOCTRINE = 1.0    -- How quickly is desire to unlock naval doctrines accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_AIR_DOCTRINE = 1.0      -- How quickly is desire to unlock air doctrines accumulated?

NDefines.NAI.DESIRE_USE_XP_TO_UPDATE_LAND_TEMPLATE = 100.0     -- How quickly is desire to update/create templates accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UPGRADE_LAND_EQUIPMENT = 10.0   -- How quickly is desire to update/create land equipment variants accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UPGRADE_NAVAL_EQUIPMENT = 10.0  -- How quickly is desire to update/create naval equipment variants accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UPGRADE_AIR_EQUIPMENT = 10.0    -- How quickly is desire to update/create air equipment variants accumulated?

NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_ARMY_SPIRIT = 0.01       -- How quickly is desire to unlock army spirits accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_NAVY_SPIRIT = 0.01       -- How quickly is desire to unlock naval spirits accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_AIR_SPIRIT = 0.01        -- How quickly is desire to unlock air spirits accumulated?

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- RECALCULATION INTERVALS - IMPROVED for faster reaction
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_DOCTRINE = 7
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_TEMPLATE = 5   -- vanilla 7 faster template checks
NDefines.NAI.DAYS_BETWEEN_CHECK_BEST_EQUIPMENT = 5   -- vanilla 7 faster equipment checks

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- SPIRIT UNLOCKING
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
NDefines.NAI.UNLOCK_SPIRIT_AI_WILL_DO_FACTOR = 20
NDefines.NAI.UNLOCK_SPIRIT_MODIFIER_FACTOR = 0.05
NDefines.NAI.UNLOCK_SPIRIT_USE_TRUNCATION_SELECT = false
NDefines.NAI.UNLOCK_SPIRIT_TRUNCATION_SELECT_THRESHOLD = 0.8

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- EQUIPMENT UPGRADE SYSTEM - IMPROVED
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
NDefines.NAI.MAX_MODULAR_EQUIPMENT_EQUIPMENT_UPGRADE_COUNT_PER_PASS = 5   -- vanilla 4 faster upgrades
NDefines.NAI.EQUIPMENT_UPGRADE_VARIANT_MATCH_SCORE_FACTOR = 0.25   -- vanilla 0.2 values upgrades more

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- AI UPDATE FREQUENCIES - IMPROVED for responsiveness
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 ---NDefines.NAI.AI_UPDATE_ROLES_FREQUENCY_HOURS = 36   -- vanilla 48 faster role updates

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- DIVISION PRODUCTION & UPGRADES
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 --NDefines.NAI.WANTED_UNITS_INDUSTRY_FACTORY = 0.1  --1          -- How many units a country wants is partially based on how much military industry that is available


 --NDefines.NAI.MANPOWER_RATIO_REQUIRED_TO_PRIO_MOBILIZATION_LAW = 0.4 -- percentage of manpower in field is desired to be buffered for AI when it has upcoming wars or already at war. if it has less manpower it will prio manpower laws

 --NDefines.NAI.MIN_SUPPLY_USE_SANITY_CAP = 100                                 -- Ignore supply cap if below this value when deciding on how many divisions to produce.

 -- Calculating wanted nr of divisions
 -- INDUSTRY FACTOR: vanilla=1.60. Raising this makes factories translate into more desired divisions.
 -- At 2.5 a country with 50 MIC wants ~125 divisions worth of production pressure (up from ~80 vanilla).
 -- This is the primary lever to fix AI leaving gaps on the frontline due to insufficient unit ambition.
NDefines.NAI.WANTED_UNITS_INDUSTRY_FACTOR = 5                         -- How many units a country wants is partially based on how much military industry that is available
NDefines.NAI.WANTED_UNITS_THREAT_BASE = 0.7                              -- If no threat multiply min wanted units by this
 --NDefines.NAI.WANTED_UNITS_THREAT_MAX = 25.0                              -- Normalized threat is clamped to this
NDefines.NAI.WANTED_UNITS_WAR_THREAT_FACTOR = 1.5                        -- Factor threat with this if country is at war. this value is overriden by the value in ideology database if that value exceedes this.
NDefines.NAI.WANTED_UNITS_DANGEROUS_NEIGHBOR_FACTOR = 1.2                -- Factor if has dangerous neighbor (vanilla=1.15 slightly raised)
NDefines.NAI.WANTED_UNITS_MANPOWER_DIVISOR = 20000                       -- Normalizing divisor for AI manpower. Lower = wants more divisions per manpower pool (vanilla=21000)
 -- Weight rebalance: raise factory and front weights so production capacity drives unit ambition harder
NDefines.NAI.WANTED_UNITS_WEIGHT_FRONTS_WANT = 0.5                       -- Weight of front needs when computing final nr wanted units (vanilla=0.35)
NDefines.NAI.WANTED_UNITS_WEIGHT_FACTORIES = 0.6                         -- Weight of military factories when computing final nr wanted units (vanilla=0.45)
NDefines.NAI.WANTED_UNITS_WEIGHT_MANPOWER = 0.75                         -- Weight of manpower availability when computing final nr wanted units (vanilla=0.3 unchanged from our value)
NDefines.NAI.WANTED_UNITS_MIN_DEFENCE_FACTOR = 0.5 -- Factor on units required for min defence (vanilla=0.4 slightly raised)
 -- End of calculating wanted nr of divisions

NDefines.NAI.WANTED_UNITS_MAX_WANTED_CAP = 600

 ---NDefines.NAI.UPGRADE_DIVISION_RELUCTANCE = 0.0042  -- aggressively trying to get the AI to upgrade divisions to newer templates may work may not but it doesn't break anything. vanilla is 14 .0042 is just over 1 hour where I believe the vanilla value at 14 = 14 days. So it should be checking to upgrade ONE division every single hour. 
 ---NDefines.NAI.UPGRADE_PERCENTAGE_OF_FORCES = 1
 ---NDefines.NAI.STOP_TRAINING_FULLY_TRAINED_FACTOR = 0.99
 ---NDefines.NAI.UPGRADES_DEFICIT_LIMIT_DAYS = 60
NDefines.NAI.LOW_PRIO_TEMPLATE_BONUS_FOR_GARRISONS = 300000
NDefines.NAI.LOW_PRIO_TEMPLATE_PENALTY_FOR_FRONTS = -2000

NDefines.NAI.MIN_FIELD_STRENGTH_TO_BUILD_UNITS = 0.85 -- Cancel unit production if below this to get resources out to units in the field
NDefines.NAI.MIN_MANPOWER_TO_BUILD_UNITS = 0.5 -- Cancel unit production if below this to get resources out to units in the field

NDefines.NAI.DEPLOY_MIN_TRAINING_PEACE_FACTOR = 0.95 -- Required percentage of training (1.0 = 100%) for AI to deploy unit in peacetime
NDefines.NAI.DEPLOY_MIN_TRAINING_WAR_FACTOR = 0.35 -- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
NDefines.NAI.DEPLOY_MIN_TRAINING_SURRENDER_FACTOR = 0.5 -- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime while surrender progress is higher than 0 

NDefines.NAI.DEPLOY_MIN_EQUIPMENT_PEACE_FACTOR = 0.92 -- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in peacetime
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_WAR_FACTOR = 0.88 -- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_SURRENDER_FACTOR = 0.90 -- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime while surrender progress is higher than 0 
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_CAP_DEPLOY_FACTOR = 0.85   -- If training is capped by equipment deficit and we have reached that cap deploy unit anyway if percentage is above this (reinforce in field instead).

NDefines.NAI.MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_PEACETIME = 0.1 -- deployment will try to buffer a ratio of manpower (for reinforcements) during peace time
NDefines.NAI.MAX_AVAILABLE_MANPOWER_RATIO_TO_BUFFER_WARTIME = 0.2 -- deployment will try to buffer a ratio of manpower (for reinforcements) during war time

NDefines.NAI.DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_WARTIME = 0.1  -- deployment will try to buffer a ratio of deployed manpower (for reinforcements) during war time
NDefines.NAI.DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_PEACETIME = 0.1      -- deployment will try to buffer a ratio of deployed manpower (for reinforcements) during peace time

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- DIVISION UPGRADES
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.UPGRADE_DIVISION_RELUCTANCE = 10
NDefines.NAI.UPGRADE_PERCENTAGE_OF_FORCES = 0.05
NDefines.NAI.STOP_TRAINING_FULLY_TRAINED_FACTOR = 0.99
NDefines.NAI.UPGRADES_DEFICIT_LIMIT_DAYS = 365

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- EQUIPMENT PRODUCTION
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

NDefines.NAI.SHIPS_PRODUCTION_BASE_COST = 1
NDefines.NAI.NEEDED_NAVAL_FACTORIES_EXPENSIVE_SHIP_BONUS = 1000
NDefines.NAI.PRODUCTION_MAX_PROGRESS_TO_SWITCH_NAVAL = 0.001  -- temp fix
NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_CHEAP = 0.75

NDefines.NAI.NAVAL_DOCKYARDS_SHIP_FACTOR = 1000 -- The extent to which number of dockyards play into amount of sips a nation wants
NDefines.NAI.NAVAL_BASES_SHIP_FACTOR = 1000 -- The extent to which number of naval bases play into amount of sips a nation wants
NDefines.NAI.NAVAL_STATES_SHIP_FACTOR = 1000 -- The extent to which number of states play into amount of sips a nation wants

NDefines.NAI.PRODUCTION_UNAVAILABLE_RESORCE_FACTORY_FACTOR = 0.5

NDefines.NAI.RAILWAY_GUN_PRODUCTION_BASE_DIVISIONS_RATIO_PERCENT = 5
NDefines.NAI.RAILWAY_GUN_PRODUCTION_MIN_DIVISONS = 100
NDefines.NAI.RAILWAY_GUN_PRODUCTION_MIN_FACTORIES = 50

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- FUEL
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_ARMY_MAX_CONSUMPTION = 120
NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_AIR_MAX_CONSUMPTION = 120
NDefines.NAI.WANTED_MAX_FUEL_BUFFER_IN_DAYS_FOR_NAVY_MAX_CONSUMPTION = 120

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- DIPLOMACY
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

NDefines.NAI.DIPLOMACY_SEND_MAX_FACTION = 0.0
NDefines.NAI.MAX_REQUEST_EXPEDITIONARIES_ARMY_RATIO = 0.0
NDefines.NAI.GENERATE_WARGOAL_THREAT_BASELINE = 0.6
NDefines.NAI.DIPLOMACY_REJECTED_WAIT_MONTHS_BASE = 1 -- AI will not repeat offers until at least this time has passed and at most the double

 -- -- -- -- -- -- ---Volunteers Stuff -- -- -- -- -- -- ---
NDefines.NAI.SEND_VOLUNTEER_EVAL_BASE_DISTANCE = 175.0   -- How far away it will evaluate sending volunteers if not a major power
NDefines.NAI.SEND_VOLUNTEER_EVAL_MAJOER_POWER = 1.0  -- How willing major powers are to send volunteers.
NDefines.NAI.SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR = 0.2  -- How much AI containment factors into its evaluation of sending volunteers.

NDefines.NAI.DIPLO_PREFER_OTHER_FACTION = -400 -- The country has yet to ask some other faction it would prefer to be a part of.
NDefines.NDiplomacy.NOT_READY_FOR_WAR_BASE = -500  -- AI should be unwilling to enter accept a call to war if not ready  ---for war against the relevant enemies. vanilla -50 - suggested define by SensitiveDannyBoi

 --NDefines.NAI.SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY = 1000 -- Added to AI desire to send volunteers if recipent is same ideology (and AI can't declare war on recipient)
 --NDefines.NAI.SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR = 1500 -- Added to AI desire to send volunteers if recipent is same ideology and they are currently in civil war

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- PP
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 --NDefines.NAI.NEW_LEADER_EXTRA_PP_FACTOR = 1  --2.0  -- Country must have at least this many times extra PP to get new admirals or army leaders
 --NDefines.NAI.DIPLOMACY_IMPROVE_RELATION_COST_FACTOR = 7.0                        -- Desire to boost relations subtracts the cost multiplied by this

NDefines.NAI.HIGH_COMMAND_ADDED_WEIGHT_FACTOR = 10.0 -- Was 1.10 now 3x weight! (for XP gain)
NDefines.NAI.CHIEF_ADDED_WEIGHT_FACTOR = 1000 -- Was 2.4 now even higher
NDefines.NAI.ARMY_CHIEF_SCORE_MULTIPLIER = 7.5 -- Was 1.0 doubled
NDefines.NAI.AIR_CHIEF_SCORE_MULTIPLIER = 6.0 -- Was 1.0 doubled
NDefines.NAI.NAVY_CHIEF_SCORE_MULTIPLIER = 4.5 -- Was 1.0 doubled
NDefines.NAI.POLITICAL_ADVISOR_SCORE_MULTIPLIER = 100.0 -- Was 1.25 slight boost
NDefines.NAI.DESIGN_COMPANY_SCORE_MULTIPLIER = 1.5 -- Was 1.25 slight boost

NDefines.NAI.THEORIST_ACCEPTANCE_MULTIPLIER = 0.2 -- Was 0.7
NDefines.NAI.THEORIST_SCALING_WEIGHT_FACTOR_PER_NON_POLITICAL_ADVISORS = 0.05 -- Was 0.15

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- LAND AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.EASY_TARGET_FRONT_IMPORTANCE = 7.5
NDefines.NAI.MAIN_ENEMY_FRONT_IMPORTANCE = 5.0

NDefines.NAI.ASSIGN_TANKS_TO_WAR_FRONT = 12.0  -- Vanilla 6.0
NDefines.NAI.ASSIGN_TANKS_TO_NON_WAR_FRONT = 0.1  -- Vanilla 0.4

NDefines.NAI.UPDATE_SUPPLY_MOTORIZATION_FREQUENCY_HOURS = 20  -- Vanilla is 52  Check if activating motorization would improve supply situation this often.

NDefines.NAI.CANCEL_COMBAT_DISADVANTAGE_RATIO = 1.25 -- Vanilla 1.5                      -- If the enemy's advantage ratio over us during (normal) combat is more than <value> allow canceling the attack
NDefines.NAI.CANCEL_COMBAT_MIN_DURATION_HOURS = 60 -- Vanilla 48  -- Only allow canceling (normal) combat if at least <value> hours have passed
NDefines.NAI.CANCEL_INVASION_COMBAT_DISADVANTAGE_RATIO = 2.8 -- Vanilla 3.5  -- If the enemy's advantage ratio over us during invasion combat is more than <value> allow canceling the attack
NDefines.NAI.CANCEL_INVASION_COMBAT_MIN_DURATION_HOURS = 720 -- Vanilla 120 -- Only allow canceling invasion combat if at least <value> hours have passed

NDefines.NAI.REDEPLOY_DISTANCE_VS_ORDER_SIZE = 0.9                  -- Factor applied to the path length of a unit compared to length of an order to determine if it should use strategic redeployment
NDefines.NAI.UNIT_ASSIGNMENT_TERRAIN_IMPORTANCE = 10.0                  -- Terrain score for units are multiplied by this when the AI is deciding which front they should be assigned to

NDefines.NAI.FRONT_TERRAIN_DEFENSE_FACTOR = 7.0 -- Multiplier applied to unit defense modifier for terrain on front province multiplied by terrain importance
NDefines.NAI.FRONT_TERRAIN_ATTACK_FACTOR = 7.0 -- Multiplier applied to unit attack modifier for terrain on enemy front province multiplied by terrain importance

NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_LOW = 0.60 -- Minimum org % for a unit to actively attack an enemy unit when executing a plan
NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_LOW = 0.85 -- Minimum strength  % for a unit to actively attack an enemy unit when executing a plan

NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_MED = 0.40 -- (LOWMEDHIGH) corresponds to the plan execution agressiveness level.
NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_MED = 0.60

NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_HIGH = 0.30
NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_HIGH = 0.45

NDefines.NAI.PLAN_FACTION_STRONG_TO_EXECUTE = 0.35  -- Vanilla -0.5         -- % or more of units in an order to consider ececuting the plan
NDefines.NAI.PLAN_FACTION_NORMAL_TO_EXECUTE = 0.3   -- Vanilla -0.65  -- % or more of units in an order to consider ececuting the plan
NDefines.NAI.PLAN_FACTION_WEAK_TO_ABORT = 0.30   -- Vanilla -0.65         -- % or more of units in an order to consider ececuting the plan
NDefines.NAI.PLAN_AVG_PREPARATION_TO_EXECUTE = 0.4 -- Vanilla -0.5             -- % or more average plan preparation before executing

NDefines.NAI.FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.35
NDefines.NAI.HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.5


NDefines.NAI.DYNAMIC_STRATEGIES_THREAT_FACTOR = 8.0
NDefines.NAI.BASE_DISTANCE_TO_CARE = 400.0

NDefines.NAI.ASSIGN_MOUNTAINEERS_TO_MOUNTAINS = 50.0

 -- -- -- AI Superchargers  -- -- -- -- ---
 -- These 4 defines below genuinely make the AI somehow smarter and supercharges it with the right values
NDefines.NAI.FRONT_EVAL_UNIT_ACCURACY = 2.0 -- Vanilla 1.0 -- scale how stupid ai will act on fronts. 0 is potato
NDefines.NAI.FRONT_EVAL_UNIT_AIR_SUP_IMPACT = 2.0  -- Vanilla 1.0 -- scale how good the AI thinks air superiority is for units
NDefines.NAI.FRONT_EVAL_PERCENT_TO_ASSIST_ALLY_FRONT = 0.5   -- Vanilla 0.5  percentage of how many units the AI thinks it should have compared to an ally before considering sending units
NDefines.NAI.FRONT_EVAL_UNIT_SUPPLY_AND_ORG_LACK_IMPACT = 2.0 -- Vanilla 1.0; scale how painful the AI thinks a combined lack of supply and organization is for units

 ---NDefines.NAI.PLAN_STEP_COST_LIMIT = 15           --- vanilla 9; When stepping to draw a plan this cost makes it break if it hits hard terrain (multiplied by number of desired steps)
 ---NDefines.NAI.PLAN_STEP_COST_LIMIT_REDUCTION = 0.012    -- vanilla 3Cost limit is reduced per iteration making hard terrain less likely to be crossed the further into enemy territory it is
 ---NDefines.NAI.PLAN_ATTACK_DEPTH_FACTOR = 0.1 --- vanilla 0.5; Factor applied to size or enemy being attacked.
NDefines.NAI.MIN_AI_UNITS_PER_TILE_FOR_STANDARD_COHESION = 2.5

NDefines.NAI.FRONT_CUTOFF_MIN_EDGE_PROXIMITY = 2 --- vanilla 2; Minimum number of provinces to the front edge to determine for cutoff oportunity.
NDefines.NAI.FRONT_BULGE_RATIO_LOWER_CUTOFF = 0.85 --- vanilla 0.95; If local bulginess drops below this a point of interest is found
NDefines.NAI.FRONT_BULGE_RATIO_UPPER_CUTOFF = 1.4 --- vanilla 1.5; If total bulginess is lower than this the front is ignored.

NDefines.NAI.GARRISON_FRACTION = 0.0 -- DONT CHANGE THIS AS THIS FUCKS WITH VOLUNTEERS AND MAKE EM DO NOTHING AND BE PASSIVE How large part of a front should always be holding the line rather than advancing at the enemy
--NDefines.NAI.PLAN_ACTIVATION_MAJOR_WEIGHT_FACTOR = 1
--NDefines.NAI.PLAN_ACTIVATION_PLAYER_WEIGHT_FACTOR = 1 

NDefines.NAI.ASSIGN_FRONT_ARMY_SOFT_ATTACK_FACTOR = 0.1                  -- Importance of unit's ARMY_SOFT_ATTACK stat when assigning to a front
NDefines.NAI.ASSIGN_FRONT_ARMY_HARD_ATTACK_FACTOR = 0.1                 -- Importance of unit's ARMY_HARD_ATTACK stat when assigning to a front
NDefines.NAI.ASSIGN_FRONT_ARMY_BREAKTHROUGH_FACTOR = 0.1                -- Importance of unit's ARMY_BREAKTHROUGH stat when assigning to a front
NDefines.NAI.ASSIGN_DEFENSE_ARMY_DEFENSE_FACTOR = 3.0                 -- Importance of unit's ARMY_DEFENSE stat when assigning to an area defense order
NDefines.NAI.ASSIGN_DEFENSE_ARMY_ENTRENCHMENT_FACTOR = 2.0               -- Importance of unit's ARMY_ENTRENCHMENT stat when assigning to an area defense order
NDefines.NAI.ASSIGN_DEFENSE_TEMPLATE_CLASS_SCORE = 3.0                   -- Importance of unit's AI template class (AREA_DEFENSE CAVALRY) when assigning to an area defense order
NDefines.NAI.ASSIGN_INVASION_AMPHIBIOUS_ATTACK_FACTOR = 50.0             -- Importance of unit's amphibious attack adjuster when assigning to an invasion order
NDefines.NAI.ORDER_ASSIGNMENT_DISTANCE_FACTOR = 100.0                      -- When the AI assigns units to orders how much should distance be taken into account?
NDefines.NAI.UNIT_ASSIGNMENT_STATS_IMPORTANCE = 2.0                      -- Stats score for units are multiplied by this when the AI is deciding which front they should be assigned to

NDefines.NAI.ASSIGN_FRONT_TERRAIN_ATTACK_FACTOR = 0.1                    -- Importance of unit's terrain adjusted attack stat when assigning to a front
NDefines.NAI.ASSIGN_FRONT_TERRAIN_DEFENSE_FACTOR = 0.1                  -- Importance of unit's terrain adjusted defense stat when assigning to a front
NDefines.NAI.ASSIGN_FRONT_TERRAIN_MOVEMENT_FACTOR = 0.1                  -- Importance of unit's terrain adjusted movement stat when assigning to a front
NDefines.NAI.ASSIGN_DEFENSE_TERRAIN_ATTACK_FACTOR = 0.5                  -- Importance of unit's terrain adjusted attack stat when assigning to an area defense order
NDefines.NAI.ASSIGN_DEFENSE_TERRAIN_DEFENSE_FACTOR = 4.0                -- Importance of unit's terrain adjusted defense stat when assigning to an area defense order
NDefines.NAI.ASSIGN_DEFENSE_TERRAIN_MOVEMENT_FACTOR = 0.5                -- Importance of unit's terrain adjusted movement stat when assigning to an area defense order

NDefines.NAI.ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS = 1.0 -- front unit request factor at max enemy fortification
NDefines.NAI.ENEMY_FORTIFICATION_FACTOR_FOR_FRONT_REQUESTS_MAX = 0.1  -- max factor that can be added by enemy fortification

NDefines.NAI.AI_FRONT_MOVEMENT_FACTOR_FOR_READY = 0.50
NDefines.NAI.FRONT_REASSIGN_DISTANCE = 250.0

NDefines.NAI.ASSIGN_TANKS_TO_MOUNTAINS = -10.0
NDefines.NAI.ASSIGN_TANKS_TO_JUNGLE = -10.0

 --NDefines.NAI.STATE_CONTROL_FOR_AREA_DEFENSE = 0.70
 --NDefines.NAI.DIVISION_SUPPLY_RATIO_TO_MOTORIZE = 1
NDefines.NAI.ENTRENCHMENT_WEIGHT = 5.0
NDefines.NAI.MAX_MICRO_ATTACKS_PER_ORDER = 20
NDefines.NAI.MICRO_POCKET_SIZE = 5
NDefines.NAI.POCKET_DISTANCE_MAX = 6000


NDefines.NAI.MIN_PLAN_VALUE_TO_MICRO_INACTIVE = 0.0
NDefines.NAI.FRONT_UNITS_CAP_FACTOR = 13.0
NDefines.NAI.RAIDS_CREATE_FREQUENCY_DAYS = 20
NDefines.NAI.RAIDS_COMMAND_POWER_CAP_TO_CREATE = 150.0 
NDefines.NAI.COMMAND_POWER_BEFORE_SPEND_ON_TRAITS = 10.0
 --NDefines.NAI.LOCATION_BALANCE_TO_ADVANCE = 0.15

NDefines.NAI.PLAN_FRONT_SECTION_MAX_LENGTH = 10
NDefines.NAI.PLAN_FRONT_SECTION_MIN_LENGTH = 5

NDefines.NAI.MANPOWER_RATIO_CAREFULNESS_THRESHOLD = 0.25 -- Vanilla 0.05  -- if manpower ratio (available/used-by-army) is less than this start being more careful with plan execution (i.e. don't throw your men into the meat grinder if you're running out of manpower)

NDefines.NAI.DEFAULT_SUPPLY_TRUCK_BUFFER_RATIO = 2.0 --  -- Vanilla 1.5  -- ai will set to truck buffer ratio to this. can be modified by wanted_supply_trucks min_wanted_supply_trucks ai strats

 -- -- -- Changing Careful AI  -- -- -- -- ---

 -- So I don't know a single person who actually uses the careful attack plan. Therefore i'm gonna heavily change it for the AI use.

NDefines.NAI.PLAN_EXECUTE_CAREFUL_LIMIT = 5                 -- When looking for an attack target this score limit is required in the battle plan to consider province for attack
NDefines.NAI.PLAN_EXECUTE_CAREFUL_MAX_FORT = 7 -- If execution mode is set to careful units will not attack provinces with fort levels greater than or equal to this
 --                                                      ^^^ changed from 0.7
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- BATTLEPLANNER AI (KILL ME)
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

NDefines.NMilitary.PLAN_PORVINCE_AIRFIELD_LEVEL_FACTOR = 0.25 -- Bonus factor for airfield level

NDefines.NMilitary.PLAN_BLITZ_OPTIMISM = 0.3 -- Vanilla 0.2; Additional combat balance value in favor of blitzing side when considering targets (not a combat bonus just offsets planning)
NDefines.NMilitary.MIN_BALANCE_SCORE_TO_PROCEED_ATTACK = 0.15 -- Vanilla 0.2; A combat balance score of less than this will prevent auto attacking

NDefines.NMilitary.PLAN_SPREAD_ATTACK_WEIGHT = 300  -- 300.0  -- (was 12.0) -- The higher the value the less it should crowd provinces with multiple attacks.#WICHTIG
NDefines.NMilitary.PLAN_MIN_AUTOMATED_EMPTY_POCKET_SIZE = 10 -- (was 2)  -- The battle plan system will only automatically attack provinces in pockets that has no resistance and are no bigger than these many provinces
NDefines.NMilitary.FRONTLINE_EXPANSION_FACTOR = 0.0  -- #MOD was 0.0  -- was 0.6 -- When attacking along a frontline how much should units spread out as they advance. 0.0 means head (more or less) directly to the drawn frontline with no distractions
NDefines.NMilitary.FRONT_MIN_PATH_TO_REDEPLOY = 4  --#MOD  -- was 8 -- If a units path is at least this long to reach its front location it will strategically redeploy.

NDefines.NAI.PLAN_MIN_SIZE_FOR_FALLBACK = 25 -- Vanilla 50  -- A country with less provinces than this will not draw fallback plans but rather station their troops along the front
NDefines.NAI.FALLBACK_LOSING_FACTOR = 1.5  -- Vanilla 1.0  -- The lower this number the longer the AI will hold the line before sending them to the fallback line

NDefines.NMilitary.PLAN_PROVINCE_LOW_VP_IMPORTANCE_AREA = 4.0
NDefines.NMilitary.PLAN_PROVINCE_MEDIUM_VP_IMPORTANCE_AREA = 6.0
NDefines.NMilitary.PLAN_PROVINCE_HIGH_VP_IMPORTANCE_AREA = 20.0

NDefines.NMilitary.PLAN_PROVINCE_PORT_BASE_IMPORTANCE = 15.0 -- increased from 9.0 ; Added importance for area defense province with a port
NDefines.NMilitary.PLAN_PROVINCE_PORT_LEVEL_FACTOR = 0.5 -- Bonus factor for port level
NDefines.NMilitary.PLAN_PROVINCE_AIRFIELD_BASE_IMPORTANCE = 3.0 -- Added importance for area defense province with air field
NDefines.NMilitary.PLAN_PROVINCE_AIRFIELD_POPULATED_FACTOR = 1.5 -- Bonus factor when an airfield has planes on it
NDefines.NMilitary.PLAN_PROVINCE_AIRFIELD_LEVEL_FACTOR = 0.25 -- Bonus factor for airfield level
NDefines.NMilitary.PLAN_PROVINCE_RESISTANCE_BASE_IMPORTANCE = 10.0  -- Used when calculating the calue of defense area provinces for the battle plan system (factored by resistance level)
 ---NDefines.NMilitary.PLAN_STICKINESS_IGNORE_STACK_LIMIT = 1Unused  -- 1 == yes 0 == no. Alloes player to override prio to stack units where they want to.


 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- GARRISON AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- NAVY AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NNavy.MAX_CAPITALS_PER_AUTO_TASK_FORCE = 24  -- 5 -- maximum number of capital ships the auto-task force creation will put together when designing SurfaceActionGroup
NDefines.NNavy.MAX_SUBMARINES_PER_AUTO_TASK_FORCE = 96  -- 30 -- maximum number of submarines the auto-task force creation will put together when designing wolfpack
NDefines.NNavy.BEST_CAPITALS_TO_SCREENS_RATIO = 0.5  -- 0.25  -- capitals / screens ratio used for creating FEX groups in naval combat

NDefines.NAI.MIN_CAPITALS_FOR_CARRIER_TASKFORCE = 2 -- carrier fleets will at least have this amount of capitals 원래 6
NDefines.NAI.CAPITALS_TO_CARRIER_RATIO = 1 -- capital to carrier count in carrier taskfoces 원래 1.5
NDefines.NAI.SCREENS_TO_CAPITAL_RATIO = 3.0 -- screens to capital/carrier count in carrier & capital taskforces 원래 4.0

NDefines.NAI.MIN_MAIN_SHIP_RATIO = 0.5  -- 0.3                       -- if main ship ratio is below this steal other ships.
NDefines.NAI.MIN_SUPPORT_SHIP_RATIO = 0.5  -- 0.7                    -- if support ship ratio is below this steal other ships.
NDefines.NAI.MIN_MAIN_SHIP_RATIO_TO_REINFORCE = 0.5          -- the main ships will be tried to reinforce this level.
NDefines.NAI.MIN_SUPPORT_SHIP_RATIO_TO_REINFORCE = 0.5  -- 0.9       -- the support ships will be tried to reinforce this level.
NDefines.NAI.MIN_MAIN_SHIP_TO_SPARE = 0.5  -- 0.7                    -- can only steal ships from a task force if their main ship ratio is above this.
NDefines.NAI.MIN_SUPPORT_SHIP_TO_SPARE = 0.5  -- 1.0                 -- can only steal ships from a task force if their support ship ratio is above this.
NDefines.NAI.MIN_MAIN_SHIP_RATIO_TO_MERGE = 0.5  -- 0.7              -- try merge task force if main ship ratio is lower than this.
NDefines.NAI.MAX_MAIN_SHIP_RATIO_TO_MERGE = 1.0  -- 1.001            -- if resulting main ship ratio would be at most this allow merging into this task force.
NDefines.NAI.MAIN_SHIP_RATIO_TO_SPLIT = 2.0  -- 1.8                  -- if main ship ratio in a task force is larger than this split it. (If a carrier TF wants 4 carriers (see defines above) but it has more than [this * 4] carriers then we try to split the TF.)

NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING_PRIO_MAX_MINES = 250  -- highest mines for highest prio for mine missions

NDefines.NAI.MISSING_CONVOYS_BOOST_FACTOR = 75.0

NDefines.NAI.MIN_NAVAL_MISSION_PRIO_TO_ASSIGN = {   -- priorities for regions to get assigned to a mission
	0,  -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
	200,  -- PATROL
	50,  -- STRIKE FORCE  -- was 200
	200,  -- CONVOY RAIDING
	100,  -- CONVOY ESCORT
	200,  -- MINES PLANTING
	100,  -- MINES SWEEPING
	0,  -- TRAIN
	0,  -- RESERVE_FLEET
	100, -- NAVAL INVASION SUPPORT
}

NDefines.NAI.HIGH_PRIO_NAVAL_MISSION_SCORES = {   -- priorities for regions to get assigned to a mission
	0,  -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
	3800,  -- PATROL - 100000
	30000,  -- STRIKE FORCE 
	1500,  -- CONVOY RAIDING
	3000,  -- CONVOY ESCORT - 1000
	600,  -- MINES PLANTING
	300,  -- MINES SWEEPING
	0,  -- TRAIN
	0,  -- RESERVE_FLEET
	1000,  -- NAVAL INVASION SUPPORT
}

NDefines.NAI.MAX_MISSION_PER_TASKFORCE = {   -- max mission region/taskforce ratio
	0,  -- HOLD (consumes fuel HOLD_MISSION_MOVEMENT_COST fuel while moving)
	4,  -- PATROL
	8,  -- STRIKE FORCE  -- was 8
	1.5,  -- CONVOY RAIDING
	2,  -- CONVOY ESCORT
	2,  -- MINES PLANTING
	2,  -- MINES SWEEPING
	0,  -- TRAIN
	0,  -- RESERVE_FLEET
	10,  -- NAVAL INVASION SUPPORT
}

NDefines.NAI.NAVAL_MISSION_MINES_PLANTING_NEAR_OWNED = 80000
NDefines.NAI.NAVAL_MISSION_MINES_SWEEPING_NEAR_OWNED = 100000

 -- -- -- -- -- -- -- -- -- -- -- ---
 -- naval invasions
 -- -- -- -- -- -- -- -- -- -- -- ---

NDefines.NAI.MIN_INVASION_AREA_SIZE_FOR_FLOATING_HARBORS = 2  -- vanilla 15    -- AI will consider using floating harbors for naval invasion if invasion area is larger than this many provinces

 -- -- -- -- -- -- -- -- -- -- -- ---
 -- convoy escorts
 -- -- -- -- -- -- -- -- -- -- -- ---
NDefines.NAI.REGION_THREAT_PER_SUNK_CONVOY = 25  -- 25 -- Threat value per convoy sunk in a region. Decays over time.
NDefines.NAI.REGION_THREAT_LEVEL_TO_AVOID_REGION = 25 * 5  -- 25 * 10 -- How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY ) so the AI
NDefines.NAI.REGION_THREAT_LEVEL_TO_BLOCK_REGION = 25 * 200  -- 25 * 100 -- How much threat must be generated in region ( by REGION_THREAT_PER_SUNK_CONVOY ) so the AI will decide to mark the region as avoid

NDefines.NAI.CONVOY_ESCORT_MUL_FROM_NO_CONVOYS = 0  -- score multiplier when no convoys are around

NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX_CONVOY_THREAT = 500  -- 1500  -- AI will increase screen assignment for escort missions as threate increases

NDefines.NAI.MAX_SCREEN_FORCES_FOR_INVASION_SUPPORT = 0.2  -- 0  -- max ratio of screens forces to be used in naval invasion missions
NDefines.NAI.MAX_CAPITAL_FORCES_FOR_INVASION_SUPPORT = 0.2  -- 0  -- max ratio of capital forces to be used in naval invasion missions
NDefines.NAI.MAX_PATROL_TO_STRIKE_FORCE_RATIO = 8.0  -- 4.0 -- maximum patrol/strike force ratio

NDefines.NAI.PATROL_FLEETS_PER_INVASION_REGION_ON_PATH = 4  -- 2 -- How many STL patrol fleet templates should the AI try to use when generating dominance
NDefines.NAI.DANGEROUS_DISTANCE_TO_CAPITAL = 500.0  -- 1000.0 -- Distance in pixels from the target province to capital location where the AI will add the naval invasion defense importance

NDefines.NAI.SUGGESTED_NUM_MAX_CARRIERS = 8  -- 4 -- We don't know exactly how many planes we should use when evaluating AI build so we need a suggested number to start things off. ALso used for task force suggestions list.

NDefines.NAI.ESTIMATED_CONVOYS_PER_DIVISION = 18  -- Not always correct but mainly used to make sure AI does not go crazy vanilla 6
NDefines.NAI.NAVY_PREFERED_MAX_SIZE = 120  -- 25
NDefines.NAI.NAVAL_MISSION_INVASION_BASE = 30000  -- 1000  -- Base score for region with naval invasion (modified dynamically by prioritizing orders)

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AIR AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- ---
 -- Land combat
 -- -- -- -- -- -- -- -- -- -- -- ---
NDefines.NAir.AI_ALLOWED_PLANES_KEPT_IN_RESERVE = 0.0

NDefines.NAI.LAND_COMBAT_CAS_PER_ENEMY_ARMY = 20

 -- -- -- -- -- -- -- -- -- -- -- ---
 -- Defense
 -- -- -- -- -- -- -- -- -- -- -- ---
NDefines.NAI.LAND_DEFENSE_INTERSEPTORS_PER_BOMBERS = 1.0 -- Original = 1 Amount of air interceptor planes requested per enemy bomber

NDefines.NAI.DAYS_BETWEEN_AIR_PRIORITIES_UPDATE = 3 --- Vanilla 4  -- Amount of days between air ai updates priorities for air wings ( from 1 to N )

NDefines.NAI.LAND_DEFENSE_INTERSEPTORS_PER_PLANE = 0

 -- -- -- -- -- -- -- -- -- -- -- ---
 -- Str bombing
 -- -- -- -- -- -- -- -- -- -- -- ---

 -- -- -- -- -- -- -- -- -- -- -- ---
 -- Naval air
 -- -- -- -- -- -- -- -- -- -- -- ---

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AMRS MARKET AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.EQUIPMENT_MARKET_MAX_CIVS_FOR_PURCHASES_RATIO = 0.2             -- Ratio of available civilian factories to max use for equipment purchases (0.2 = 20 % so 50 available civs would mean max ca 10 civs to spend on purchases at any one time). Gets modified by equipment_market_spend_factories AI strategy.
NDefines.NAI.EQUIPMENT_MARKET_NR_DELIVERIES_SOFT_MAX = 7                    -- AI tries to adjust assigned factories and amount of equipment to keep nr deliveries at max this

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- LEND LEASE AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.DIPLOMACY_LEND_LEASE_MONTHS_TO_CANCEL = 16

NDefines.NAI.DIPLOMACY_ACCEPT_ATTACHE_OPINION_TRASHHOLD = 0


NDefines.NAI.MINIMUM_FUEL_DAYS_TO_ASK_LEND_LEASE = 60 -- AI will accept to lend lease fuel only if the player have less fuel than this number multiply by his max daily consumption.
NDefines.NAI.MINIMUM_FUEL_DAYS_TO_ACCEPT_LEND_LEASE = 60  -- AI will accept to lend lease fuel only if they have more fuel than this number multiply by their max daily consumption. Note that for a GiE asking to its host we divide this number by 2.

NDefines.NAI.PROPOSE_LEND_LEASE_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR = 50 -- Vanilla 25; Added to AI desire to propose lend lease if recipent is same ideology and they are currently in civil war

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- INTELLIGENCE AGENCY AI
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NOperatives.AGENCY_AI_BASE_NUM_FACTORIES = 10.0  --25.0
NDefines.NOperatives.AGENCY_AI_PER_UPGRADE_FACTORIES = 2.0  --6.0

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AI SUPPLY/LOGISTICS DEFINES 
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NSupply.AI_FRONT_DIVISIONS_PER_SUPPLY_POINT = 0.85
NDefines.NAI.MAX_DIST_PORT_RUSH = 40.0 --default 20.0 -- If a unit is in enemy territory with no supply it will consider nearby ports within this distance.

NDefines.NAI.AVERAGE_SUPPLY_USE_PESSIMISM = 2.0   -- Increased multiplier to reflect realistic supply usage.

NDefines.NAI.MAX_SUPPLY_DIVISOR = 2   -- Vanilla 1.75 -- To make sure the AI does not overdeploy divisions. Higher number means more supply per unit. van 2.0

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- UNIT ASSIGNMENT & FRONT MANAGEMENT
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.REVISITED_PROV_BOOST_FACTOR = 6    -- Vanilla 4  --When the AI picks units for a front it prioritises units already nearby.
NDefines.NAI.REASSIGN_TO_ANOTHER_FRONT_IF_IN_COMBAT_FACTOR = 0.15  -- Vanilla 0.2 --Factor for reassigning to another front if in combat. 0.0 < X < 1.0 means reluctant X > 1.0 means want to.
NDefines.NAI.REASSIGN_TO_ANOTHER_FRONT_FACTOR = 0.45   -- Vanilla 0.5 --Factor for reassigning to another front. 0.0 < X < 1.0 means reluctant X > 1.0 means want to.
NDefines.NAI.PLAN_VALUE_BONUS_FOR_MOVING_UNITS = 0.45 -- Vanilla 0.35   --AI plans gets a bonus when units are not moving and ready to fight
NDefines.NAI.PLAN_FRONTUNIT_DISTANCE_FACTOR= 8.0 -- Vanilla 10.0   --Factor for candidate units distance to front positions.
NDefines.NAI.AI_PREFERRED_TACTIC_WEEKLY_CHANGE_CHANCE = 0.10 -- Vanilla 0.05 --Chance for AI to select a new preferred tactic if they don't have one selected

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- LEADER ASSIGNMENT
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.ARMY_LEADER_ASSIGN_EMPTYNESS_MALUS= 0.3 -- Vanilla 0.2  ---Factor for avoiding assigning leaders that can lead large armies to small armies (a value of 0.2 reduces the score by max 20 %)
NDefines.NAI.ARMY_LEADER_ASSIGN_ARMY_ARMOR_SPEED_FACTOR= 30.0 -- Vanilla 20.0  --Importance of general's ARMY_ARMOR_SPEED_FACTOR modifier (proportional to armor ratio in the army)
NDefines.NAI.ARMY_LEADER_ASSIGN_ARMY_ARMOR_ATTACK_FACTOR = 30.0 -- Vanilla 20.0  ---Importance of general's ARMY_ARMOR_ATTACK_FACTOR modifier (proportional to armor ratio in the army)
NDefines.NAI.ARMY_LEADER_ASSIGN_BOOST_ARMOR_SKILL = 25.0 -- Vanilla 20.0 ---Importance of general's trait where armor skill is boosted e.g. armor_officer which boosts panzer_leader (proportional to armor ratio in the army)
NDefines.NAI.ARMY_LEADER_ASSIGN_ARMOR_LEADER_IF_NO_ARMOR = -1.0 -- Vanilla -0.5    ---Avoid assigning a general with armor skills to an army with no armor (can be negative)
NDefines.NAI.ARMY_LEADER_ASSIGN_AMPHIBIOUS_INVASION= 6.0  -- Vanilla 1.0  --If involved in invasion importance of general's AMPHIBIOUS_INVASION modifier
NDefines.NAI.ARMY_LEADER_ASSIGN_NAVAL_INVASION_PREPARATION = 6.0 -- Vanilla 1.0  --If involved in invasion importance of general's NAVAL_INVASION_PREPARATION modifier
NDefines.NAI.ARMY_LEADER_ASSIGN_KEEP_CURRENT_LEADER_FACTOR = 2.0 -- Vanilla 1.2         -- Boosts the score for keeping the current leader. Value > 1.0 favors the current leader.
NDefines.NAI.ARMY_LEADER_ASSIGN_DONT_STEAL_OTHER_FACTOR = 0.25 -- Vanilla 0.75           -- Reduces the score for leaders assigned elsewhere. Value < 1.0 discourages reassigning these leaders.

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AI FORCE CONCENTRATION DEFINES
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AIFC stands for "AI Force Concentration". Using acronym to keep define names shorter.
NDefines.NAI.AIFC_UPDATE_FREQUENCY_DAYS = 4  -- Vanilla 5                              -- How often will AI run its AI force concentration logic. Lowering this number may decrease performance.
NDefines.NAI.AIFC_FRESHNESS_BASE_VALUE = 30.0 -- Vanilla 45.0                            -- AIFC fronts have a "freshness value" which decreases if no progress is made. When it reaches zero it will give up on the current target and try another.
NDefines.NAI.AIFC_REFRESH_NEED_PER_DAY = 1.0                          -- Decrease freshness value with this every day.
NDefines.NAI.AIFC_REFRESH_NEED_SUPPLY_FACTOR_PER_DAY = 4.0 -- Vanilla 0.8              -- Decrease freshness value with this multiplied by average supply ratio every day.
NDefines.NAI.AIFC_FRESHNESS_ADD_ON_PROGRESS = 22.5   -- Vanilla 25.0                     -- Increase freshness value with this when we advance a province along the target path.
NDefines.NAI.AIFC_UNIT_RATIO_BASE = 0.12 -- Vanilla 0.15           mod 0.10                      -- After fulfilling minimum front unit needs this ratio of the "extra"/desired units can be allocated to AI force concentration duty
NDefines.NAI.AIFC_MAX_NR_FRONTS = 4                                      -- The X (this) fronts with highest AIFC score are considered for AI force concentration
NDefines.NAI.AIFC_CA_DIVISIONS_PER_PROVINCE = 2 -- Vanilla 3                      -- AI will use this as a baseline of how many divisions to have per province
NDefines.NAI.AIFC_ACTIVATE_AVG_ORG_RATIO_THRESHOLD = 0.38 -- Vanilla 0.2                 -- Only activate the offensive order if average organisation is above this.
NDefines.NAI.AIFC_ACTIVATE_IN_POSITION_RATIO_THRESHOLD = 0.3 -- Vanilla 0.3             -- Only activate the offensive order if divisions in position is more than this ratio.
NDefines.NAI.AIFC_OFFENSIVE_DEACTIVATION_DAYS_THRESHOLD = 5              -- Deactivate the offensive order only if the conditions have been unfulfilled for this many days.
NDefines.NAI.AIFC_UNIT_NUDGE_FREQUENCY_DAYS = 10.0 -- Vanilla 15                       -- On average every X day (randomly) check if another division (within same front) is better for AIFC based on score factors below.
 -- Unit offensiveness score factors for AIFC. Division stats are factored by this before adding up to total score.
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_BREAKTHROUGH = 12.0 -- Vanilla 11.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_SOFT_ATTACK = 12.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_HARD_ATTACK = 16.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_ARMOR = 80.0    -- Heavy incentive for Panzers
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_PIERCING = 8.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_HARDNESS = 800.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_SPEED = 15.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_INITIATIVE = 5.0
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_ORGANISATION = 1.0     -- Slightly positive: no more AI using garbage
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_HITPOINTS = 0.5
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_DEFENSE = -0.2
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_ENTRENCHMENT = -0.5
NDefines.NAI.AIFC_UNIT_OFFENSIVE_SCORE_FACTOR_EXPERIENCE = 500.0
 -- End of unit offensiveness score factors for AIFC
 -- Strategic target scoring for AIFC
NDefines.NAI.AIFC_TARGET_IGNORE_VP_THRESHOLD = 10                        -- VP target needs at leas this many victory points to be considered a target
NDefines.NAI.AIFC_TARGET_SUPPLY_HUB_BASE_SCORE = 25 -- Vanilla 200                    -- Base score for supply hubs
NDefines.NAI.AIFC_TARGET_NAVAL_BASE_BASE_SCORE = 15.0                    -- Base score for naval bases
NDefines.NAI.AIFC_TARGET_NAVAL_BASE_SCORE_PER_LEVEL = 2.0                -- Score for naval bases increases by this for each level
NDefines.NAI.AIFC_TARGET_VP_SCORE_FACTOR = 1.0                           -- Score for VPs increases by this for every victory point
NDefines.NAI.AIFC_TARGET_CAPITAL_SCORE_EXTRA = 10.0 -- Vanilla 5.0                    -- Extra score for Capitals (in addition to VP score)
NDefines.NAI.AIFC_TARGET_SHORT_PATH_PENALTY_FACTOR = 0.0                 -- Penalty factor for short AIFC paths (path <= 3 (including own start province))
NDefines.NAI.AIFC_TARGET_PERSISTED_FACTOR = 35.0    -- Vanilla 30.0                      -- Bonus factor for persisted targets (used to incentivize AI to select target again after e.g. front lines have reformed or save file is loaded)
 -- End of strategic target scoring for AIFC

 -- Offensive path scoring (cost multipliers) for AIFC
NDefines.NAI.AIFC_PATH_MAX_COST = 5.0 -- Vanilla 7.0                                   -- Only allow paths with total cost <= this. WARNING: increasing this value may cause stuttering and other performance issues (since AIFC will evaluate larger areas)
NDefines.NAI.AIFC_PATH_COST_ADJ_NORMAL = 1.0
NDefines.NAI.AIFC_PATH_COST_ADJ_STRAIT = 4.0
NDefines.NAI.AIFC_PATH_COST_ADJ_RIVER = 1.5
NDefines.NAI.AIFC_PATH_COST_ADJ_RIVER_LARGE = 2.3
NDefines.NAI.AIFC_PATH_COST_TRN_MOUNTAINS = 2.5 -- Vanilla 2.0
NDefines.NAI.AIFC_PATH_COST_TRN_FOREST = 1.15
NDefines.NAI.AIFC_PATH_COST_TRN_DESERT = 1.5
NDefines.NAI.AIFC_PATH_COST_TRN_HILLS = 1.2
NDefines.NAI.AIFC_PATH_COST_TRN_JUNGLE = 3.5  -- Vanilla 3.0
NDefines.NAI.AIFC_PATH_COST_TRN_PLAINS = 1.0 -- Vanilla 0.8
NDefines.NAI.AIFC_PATH_COST_TRN_URBAN = 0.8
NDefines.NAI.AIFC_PATH_COST_TRN_MARSH = 2.5
NDefines.NAI.AIFC_PATH_COST_PER_FORT_LEVEL = 0.55                         -- This multiplier is calculated as: 1.0 + <define>*fort_level    (only for fort levels > 0)
NDefines.NAI.AIFC_PATH_COST_HAS_SUPPLY_HUB = 0.50 -- Vanilla 0.5                         -- If the province we're entering has a supply hub
NDefines.NAI.AIFC_PATH_COST_HAS_NAVAL_BASE = 0.25 -- Vanilla 0.5                          -- If the province we're entering has a naval base
NDefines.NAI.AIFC_PATH_COST_RAILWAY_CONNECTION = 0.70 -- Vanilla 0.75                   -- If the provinces are connected by a railway with level > 0
 -- End of offensive path scoring for AIFC

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- AMINE'S PERSONAL TEST DEFINES  -- STABLE
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Fort Behavior Front Cohesion War Readiness  -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.DECLARE_WAR_MIN_FRONT_SIZE_TO_CONSIDER_FOR_NOT_READY = 0.08     -- vanilla 0.04
NDefines.NAI.MIN_FRONT_SIZE_TO_CONSIDER_STANDARD_COHESION = 12               -- vanilla 8
NDefines.NAI.FORTIFIED_MIN_ORG_FACTOR_TO_CONSIDER_A_FRONT_FORTIFIED = 0.55   -- vanilla 0.45
NDefines.NAI.AREA_DEFENSE_IMPORTANCE_FACTOR = 1.35                           -- vanilla 1.0

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Supply-Aware AI & Training Sanity  -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.MIN_SUPPLY_USE_SANITY_CAP = 150                   -- vanilla 100

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Combat Evaluation / Targeting Logic  -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NMilitary.COMBAT_VALUE_ORG_IMPORTANCE = 1.1      -- vanilla 1
NDefines.NMilitary.COMBAT_VALUE_STR_IMPORTANCE = 1.0       -- vanilla 1
NDefines.NMilitary.SOFT_ATTACK_TARGETING_FACTOR = 1.15     -- vanilla 1.0
NDefines.NMilitary.HARD_ATTACK_TARGETING_FACTOR = 1.35     -- vanilla 1.2

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Theatre Generation Merging & Unit Distribution  -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAITheatre.AI_THEATRE_AI_FRONT_MIN_DESIRED_RATIO = 0.65          -- vanilla 0.5
NDefines.NAITheatre.AI_THEATRE_DISTRIBUTION_MAX_SCORE = 2.4               -- vanilla 2.0
NDefines.NAITheatre.AI_THEATRE_DISTRIBUTION_PERCENTAGE_OF_MINIMUM_UNITS_TO_KEEP = 0.35   -- vanilla 0.25
NDefines.NAITheatre.AI_THEATRE_DISTRIBUTION_SAME_THEATRE_SCORE_MODIFIER = 0.35           -- vanilla 0.25

NDefines.NAITheatre.AI_THEATRE_GENERATION_MINIMUM_STATE_COUNT = 4         -- vanilla 3
NDefines.NAITheatre.AI_THEATRE_GENERATION_MAX_DISTANCE_TO_MERGE = 250    -- vanilla 200
NDefines.NAITheatre.AI_THEATRE_BREAKDOWN_MAX_DISTANCE_TO_MERGE = 350     -- new consistent with above
NDefines.NAITheatre.AI_THEATRE_GENERATION_BORDER_SIZE_RESTRICTION = 9     -- vanilla 7

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Air Logic  -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.MAX_AIR_REGIONS_TO_CARE_ABOUT = 10             -- vanilla 5

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Macro-Strategy: Guarantees Calling Allies War Entry  -- -- -- -- --
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.AI_GUARANTEE_DESIRE_WITH_PRESSURE_MODIFIER = -0.35    -- vanilla 0 (less spam guarantees)
NDefines.NAI.TENSION_MIN_FOR_GUARANTEE_VS_MINOR = 0.45             -- vanilla 0.25

NDefines.NAI.CALL_ALLY_BASE_DESIRE = 40                            -- vanilla 50
NDefines.NAI.CALL_ALLY_WAR_LENGTH_NR_MONTHS = 6                    -- vanilla 3
 --NDefines.NAI.CALL_ALLY_RELATIVE_ARMY_STRENGTH_THRESHOLD = 0.7      -- vanilla 0.5
NDefines.NAI.CALL_ALLY_RELATIVE_INDUSTRY_STRENGTH_THRESHOLD = 0.7  -- vanilla 0.5
NDefines.NAI.CALL_ALLY_LOSING_WAR_THRESHOLD = 0.15                 -- vanilla 0.3

NDefines.NAI.DIPLOMACY_CALL_ALLY_VALIDITY_DURATION = 75            -- vanilla 60
NDefines.NAI.JOIN_FACTION_BOTH_LOSING = -15                        -- vanilla -30

NDefines.NAI.MIN_DELIVERED_TRADE_FRACTION = 0.85                -- AI will cancel trade deals that are not able to deliver more than this fraction of the agreed amount   
NDefines.NAI.MIN_AI_SCORE_TO_ECONOMY_LAW_OVERRIDE_HARD_CODED_SCORE = -100.0

NDefines.NAI.MAX_VOLUNTEER_ARMY_FRACTION = 0.10
NDefines.NAI.DIPLOMACY_ACCEPT_VOLUNTEERS_BASE = 150
NDefines.NAI.DAYS_FUEL_REMAINING_TO_ENTER_FUEL_SAVING_MODE = 10
 --NDefines.NAI.MAX_FUEL_CONSUMPTION_RATIO_FOR_NAVY_TRAINING = 0.60
NDefines.NAI.TRADEABLE_FACTORIES_FRACTION = 1.0

NDefines.NAI.RESOURCE_WANT_PER_MISSING_BALANCE = 1.0
NDefines.NAI.RESOURCE_WANT_PER_CONSUMED = 0.15

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- -- -- Supply & Front Deployment (NSupply)  -- -- -- -- ---
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NSupply.AI_FRONT_MAX_UNITS_ENEMY_COUNT_FACTOR = 1.1      -- vanilla 1.2
NDefines.NSupply.AI_FRONT_MINIMUM_UNITS_PER_PROVINCE_FOR_SUPPLY_CALCULATIONS = 0.8  -- vanilla 1.0
NDefines.NAITheatre.AI_THEATRE_DISTRIBUTION_MAX_PERCENT_UNMET_DEMAND_PER_FRONT = 0.2    -- Percentage of how much fronts should request from other lower priority fronts 0 means once a front gets hold of a unit it stays there forever until its demand is reduced controlls shuffling of units.
NDefines.NAITheatre.AI_THEATRE_SUPPLY_CRISIS_LIMIT = 0.25

NDefines.NAI.UPDATE_SUPPLY_BOTTLENECKS_FREQUENCY_HOURS = 144  -- Vanilla 168      -- Check for and try to fix supply bottlenecks this often. (168 hours = 1 week)
NDefines.NAI.FIX_SUPPLY_BOTTLENECK_SATURATION_THRESHOLD = 0.6 -- Vanilla 0.85   -- Try to fix supply bottlenecks if supply node saturation exceeds this value.

 --- AI – Fuel & Trade Decisions
NDefines.NAI.MAX_FACTORY_TO_SPARE_FOR_MISSION_FUEL_TRADE = 0.5
NDefines.NAI.MAX_FACTORY_TO_SPARE_FOR_CRITICAL_MISSION_FUEL_TRADE = 0.5
NDefines.NAI.MAX_FACTORY_TO_TRADE_FOR_FUEL = 0.6
NDefines.NAI.FUEL_TRADE_PRIO_FOR_CONVOY_DEFENSE = 1
NDefines.NAI.MAX_FACTORY_TO_SPARE_FOR_MISSION_FUEL_TRADE_IN_PEACE = 0.6
NDefines.NAI.MAX_FACTORY_TO_SPARE_FOR_CRITICAL_MISSION_FUEL_TRADE_IN_PEACE = 0.6
NDefines.NAI.MAX_FACTORY_TO_TRADE_FOR_FUEL_IN_PEACE = 0.6
NDefines.NAI.FUEL_CONSUMPTION_MULT_FOR_FUEL_SAVING_MODE = 0.30
NDefines.NAI.FUEL_CONSUMPTION_MULT_REGULAR_FUEL_MODE = 1
NDefines.NAI.FUEL_CONSUMPTION_MULT_AGRESSIVE_FUEL_MODE = 6.0
 --NDefines.NAI.DAYS_FUEL_REMAINING_TO_ENTER_FUEL_SAVING_MODE = 60
NDefines.NAI.DAYS_FUEL_REMAINING_TO_ENTER_FUEL_SAVING_MODE_FUEL_RATIO = 0.33
NDefines.NAI.FUEL_RATIO_TO_EXIST_FUEL_SAVING_MODE = 0.5

 --- AI – Naval Taskforces & Priorities
NDefines.NAI.SCREENS_TO_CAPITAL_RATIO = 3.0
NDefines.NAI.CARRIER_TASKFORCE_MAX_CARRIER_COUNT = 4
NDefines.NAI.CAPITAL_TASKFORCE_MAX_CAPITAL_COUNT = 8
NDefines.NAI.SCREEN_TASKFORCE_MAX_SHIP_COUNT = 10
NDefines.NAI.SUB_TASKFORCE_MAX_SHIP_COUNT = 6
NDefines.NAI.REGION_CONVOY_DANGER_DAILY_DECAY = 4
NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MIN = 0.35
NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_CONVOY_DEFENSE_MAX = 0.80
NDefines.NAI.MIN_FUEL_RATIO_TO_NOT_IGNORE_STRIKE_FORCE_COST = 0.2
NDefines.NAI.MIN_FUEL_RATIO_TO_NOT_IGNORE_INVASION_SUPPORT_COST = 0

 --- AI – Lend Lease & Air Wing Requests

NDefines.NAI.PROPOSE_LEND_LEASE_AIDESIRE_SAME_IDEOLOGY = 100
NDefines.NAI.LENDLEASE_FRACTION_OF_PRODUCTION = 0.75
NDefines.NAI.LENDLEASE_FRACTION_OF_STOCKPILE = 0.75
NDefines.NAI.MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE = -100
NDefines.NAI.MINIMUM_CONVOY_TO_ASK_LEND_LEASE = 100
NDefines.NAI.LAND_COMBAT_CAS_PLANES_PER_ENEMY_ARMY_LIMIT = 300

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- AMINE'S PERSONAL TEST DEFINES  -- UNSTABLE (MIGHT GENUINELY SUPERCHARGE OR KILL THE MOD)
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- UNIT ORG/STR CLASSIFICATION THRESHOLDS
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Vanilla: WEAK 0.25 / NORMAL 0.35 / STRONG 0.75
 -- Raising STRONG means AI demands more readiness before committing to attacks. More patient fewer meatgrinder charges.
NDefines.NAI.ORG_UNIT_WEAK = 0.28           -- vanilla 0.25 | slight raise = AI pulls back weaker units sooner
NDefines.NAI.ORG_UNIT_NORMAL = 0.40         -- vanilla 0.35 | AI considers units "normal" only with more org
NDefines.NAI.ORG_UNIT_STRONG = 0.80         -- vanilla 0.75 | AI waits for genuinely strong org before attacking

 -- Vanilla: WEAK 0.30 / NORMAL 0.40 / STRONG 0.70
NDefines.NAI.STR_UNIT_WEAK = 0.33           -- vanilla 0.30 | pull back earlier when taking equipment losses
NDefines.NAI.STR_UNIT_NORMAL = 0.45         -- vanilla 0.40
NDefines.NAI.STR_UNIT_STRONG = 0.75         -- vanilla 0.70 | must have good equipment before being considered "strong"

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- DESPERATE AI BEHAVIOR
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Raising MIN_ORG_BEFORE_ATTACK stops the AI from throwing broken units into fortified positions.
 -- Raising DESPERATE_ATTACK hours gives the AI more patience to wait for org recovery before going truly desperate.
NDefines.NAI.DESPERATE_AI_MIN_UNIT_ASSIGN_TO_ESCAPE = 3 -- AI will assign at least this amount of units to break from desperate situations
NDefines.NAI.DESPERATE_AI_WEAK_UNIT_STR_LIMIT = 0.7 -- ai will increase number of units assigned to break from desperate situations when units are start falling lower than this str limit
NDefines.NAI.DESPERATE_AI_MIN_ORG_BEFORE_ATTACK = 0.35 -- ai will wait for this much org to attack an enemy prov in desperate situations
NDefines.NAI.DESPERATE_AI_MIN_ORG_BEFORE_MOVE = 0.15 -- ai will wait for this much org to move in desperate situations
NDefines.NAI.DESPERATE_ATTACK_WITHOUT_ORG_WHEN_NO_ORG_GAIN = 72 -- if ai can't regain enough org to attack in this many hours it will go truly desperate and attack anyway (still has to wait for move org)

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- LEADER ASSIGNMENT SKILL WEIGHTING
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Boosting skill-specific factors makes the AI pick the RIGHT general for the RIGHT job more consistently.
 -- Logistics/supply factors boosted most since supply-aware generalship is the biggest vanilla weakness.
NDefines.NAI.ARMY_LEADER_ASSIGN_OVERALL_SKILL_FACTOR = 60        -- vanilla 50  | general skill matters more
NDefines.NAI.ARMY_LEADER_ASSIGN_ATTACK_SKILL_FACTOR = 25         -- vanilla 20  | offense fronts get attack generals
NDefines.NAI.ARMY_LEADER_ASSIGN_DEFENSE_SKILL_FACTOR = 15        -- vanilla 10  | defense orders get defense generals
NDefines.NAI.ARMY_LEADER_ASSIGN_LOGISTICS_SKILL_FACTOR = 15      -- vanilla 7   | BIG boost: supply logistics matters a lot
NDefines.NAI.ARMY_LEADER_ASSIGN_PLANNING_SKILL_FACTOR = 12       -- vanilla 7   | planning speed for prepared attacks
NDefines.NAI.ARMY_LEADER_ASSIGN_PLANNING_SPEED = 0.20            -- vanilla 0.1 | AI values fast-planning generals more
NDefines.NAI.ARMY_LEADER_ASSIGN_SUPPLY_CONSUMPTION_FACTOR = 2.0  -- vanilla 1.0 | strongly prefer supply-efficient generals
NDefines.NAI.ARMY_LEADER_ASSIGN_OUT_OF_SUPPLY_FACTOR = 2.0       -- vanilla 1.0 | generals who handle supply shortage better
NDefines.NAI.ARMY_LEADER_ASSIGN_XP_GAIN_FACTOR = 3.0            -- vanilla 2.0 | prefer generals who level up faster
NDefines.NAI.ARMY_LEADER_ASSIGN_NR_TRAITS = 7                    -- vanilla 5   | more traits = higher score = picks experienced generals
NDefines.NAI.ARMY_LEADER_ASSIGN_TERRAIN_FACTOR = 0.4             -- vanilla 0.2 | terrain specialists assigned to matching fronts
NDefines.NAI.ARMY_LEADER_ASSIGN_WINTER_ATTRITION_FACTOR = 2.0    -- vanilla 1.0 | critical for Eastern Front gameplay
NDefines.NAI.ARMY_LEADER_ASSIGN_OVERCAPACITY = -300              -- vanilla -200 | harder penalty for oversized army assignments

 -- Defensive army-specific scoring (when AI assigns to area defense orders)
NDefines.NAI.ARMY_LEADER_ASSIGN_DEFENSE_OVERALL_SKILL_FACTOR = 15    -- vanilla 10
NDefines.NAI.ARMY_LEADER_ASSIGN_DEFENSE_DEFENSE_SKILL_FACTOR = 30    -- vanilla 20 | big boost for defense skill on defensive orders
NDefines.NAI.ARMY_LEADER_ASSIGN_DEFENSE_LOGISTICS_SKILL_FACTOR = 6   -- vanilla 3
NDefines.NAI.ARMY_LEADER_ASSIGN_DEFENSE_PLANNING_SKILL_FACTOR = 5    -- vanilla 3

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- ENCIRCLEMENT DISCOVERY
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Lower value = AI refreshes pocket detection more often = spots and reacts to encirclements faster.
NDefines.NAI.HOURS_BETWEEN_ENCIRCLEMENT_DISCOVERY = 288   -- vanilla 72 | check for pockets every 7 days instead of 3

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- RESERVE/COMMITTED COMBAT BALANCE
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Higher value = AI holds more units in reserve during combat = less all-in more tactical depth.
NDefines.NAI.RESERVE_TO_COMMITTED_BALANCE = 0.40    -- vanilla 0.30 | keeps ~40% reserve relative to committed divisions

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- NAVAL DOMINANCE MARGIN
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- How much ABOVE the required naval dominance threshold the AI tries to overshoot when contesting a sea region.
 -- Lower value = AI is satisfied with less excess dominance = redistributes task forces more efficiently.
 -- Vanilla 200 means AI always stacks 200 extra dominance points as a safety buffer.
NDefines.NAI.AI_MIN_DOMINANCE_MARGIN = 150   -- vanilla 200 | less naval overkill better fleet distribution

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- INVASION EXECUTION THRESHOLDS
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Higher UNITS_READY = AI waits until almost all divisions are ready before launching = fewer botched landings.

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- CONSTRUCTION BASE PRIORITIES (previously unset in mod = full vanilla)
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Slightly rebalancing to prioritize repair and military production over civ spam during wartime.
NDefines.NAI.CONSTRUCTION_PRIO_CIV_FACTORY = 0.75            -- vanilla 0.80 | slight reduction in peacetime civ priority
NDefines.NAI.CONSTRUCTION_PRIO_MIL_FACTORY = 0.80            -- vanilla 0.70 | slight boost for mil factory priority
NDefines.NAI.CONSTRUCTION_PRIO_INFRASTRUCTURE = 0.25         -- vanilla 0.20 | minor infra boost (helps supply reach)
NDefines.NAI.CONSTRUCTION_PRIO_FACTOR_REPAIRING = 0.50       -- vanilla 0.30 | AI repairs war damage much faster

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- DIVISION ROLE MATCHING
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- Boosts the score when a template matches the correct role (e.g. armored assigned to tank role).
 -- Higher = AI assigns templates to roles more precisely.
NDefines.NAI.DIVISION_MATCH_ROLE_BOOST_FACTOR = 1.5    -- vanilla 1.2 | stronger preference for role-matched templates

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- FORT AVOIDANCE
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.ATTACK_HEAVILY_DEFENDED_LIMIT = 1.35
NDefines.NAI.PLAN_VALUE_FORTIFICATION_LEVEL_MAX_PENALTY = -0.6
NDefines.NAI.FORT_LEVEL_TO_CONSIDER_HIGHLY_FORTIFIED = 3

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- TRAINING
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.START_TRAINING_EQUIPMENT_LEVEL = 0.25
NDefines.NAI.STOP_TRAINING_EQUIPMENT_LEVEL = 0.10
NDefines.NAI.START_TRAINING_SUPPLY_LEVEL = 0.25
NDefines.NAI.STOP_TRAINING_SUPPLY_LEVEL = 0.15

NDefines.NAI.MAX_FUEL_CONSUMPTION_RATIO_FOR_NAVY_TRAINING = 0.40
NDefines.NAI.MAX_FULLY_TRAINED_SHIP_RATIO_FOR_TRAINING = 0.90

NDefines.NAI.MAX_FUEL_CONSUMPTION_RATIO_FOR_AIR_TRAINING = 0.90

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- AGGRESSION BALANCE
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.PLAN_ACTIVATION_SUPERIORITY_AGGRO = 6.0
NDefines.NAI.PLAN_VALUE_TO_EXECUTE = -0.45
NDefines.NAI.SCARY_LEVEL_AVERAGE_DEFENSE = -0.6

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
 -- WEAK POINT / EXPLOITATION
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
NDefines.NAI.AGGRESSIVENESS_CHECK_PARTLY_FORTIFIED_WEAK_POINTS = 0.50
NDefines.NAI.AGGRESSIVENESS_BONUS_FOR_FRONTS_THAT_ARE_ON_HIGH_AGGRESSIVENESS = -0.55

 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- BLACK ICE TEST DEFINES  -- UNSTABLE (MIGHT GENUINELY SUPERCHARGE OR KILL THE MOD)
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ---
 -- PRODUCTION LOGIC
 
NDefines.NAI.PRODUCTION_EQUIPMENT_SURPLUS_FACTOR = 0.2 -- Base value for how much of currently used equipment the AI will at least strive to have in stock
NDefines.NAI.PRODUCTION_EQUIPMENT_SURPLUS_FACTOR_GARRISON = 0.25 -- Base value for how much of currently used equipment the AI will at least strive to have in stock for garrison forces
NDefines.NAI.PRODUCTION_LINE_SWITCH_SURPLUS_NEEDED_MODIFIER = 0.15 -- Is modified by efficiency modifiers. WHAT THE FUCK DOES THIS DO

NDefines.NAI.PRODUCTION_WAIT_TO_FINISH_IF_EXPENSIVE = 0.05       -- If produced item is expensive (producing less than one/week) wait to finish item if progress is above this

NDefines.NAI.PRODUCTION_CARRIER_PLANE_BUFFER_RATIO = 1.5 -- in addition to total deck size of carriers we want at list this ratio to buffer it
NDefines.NAI.PRODUCTION_CARRIER_PLANE_PRODUCTION_BOOST_TO_BUFFER = 4.0   -- production of carrier planes will go up by this ratio if we lack buffers

NDefines.NAI.DEFAULT_SUPPLY_TRAIN_NEED_FACTOR = 1.25      -- AI multiplies current train usage by this to determine desired nr of wanted trains. Can be modified by wanted_supply_train min_wanted_supply_trains ai strats.

NDefines.NAI.OPERATION_EQUIPMENT_NEED_PRODUCTION_MULT = 1.0  -- equipment requests for operations will be added the equipment needs that ai considers while assigning factories to production

 -- AIR REGION ASSIGNMENT LOGIC
NDefines.NAI.AIR_SCORE_DISTANCE_IMPACT = 0.5 -- Effect of distance applied to the score calculations ### Dont set this above 1 or the game breaks
NDefines.NAI.LAND_COMBAT_GUIDE_DISTANCE = 270.0 -- Distance within whch we'll care a bit more about sending planes regardless of whether our boiz are dying

NDefines.NAI.AI_AIR_MISSION_COVERAGE_TO_STAY_PUT = 0.66 -- AI will not rebase air wings on missions if their new mission target exceeds this percentage of region coverage
NDefines.NAI.AI_FRACTION_OF_FIGHTERS_RESERVED_FOR_INTERCEPTION = 0.25 --Percentage of fighters we reserve for interception vs AS
NDefines.NAI.MIN_ALLIED_DEFENSE_FACTOR_AIRWING_REQUESTS = 0.75 -- Airwing requests will be factored by a minimum of this when comparing own vs friendly troops in area
NDefines.NAI.AIR_SUPERIORITY_FOR_FRIENDLY_CAS_RATIO = 0.75 -- Demand at least this proportion of our cas planes as air superiority regardless of other needs


 -- PASSING THROUGH

NDefines.NAI.ENEMY_PASSING_THROUGH_PLANES_PER_BOMBER = 1.5 -- Amount of planes we assign to intercept enemies en-route to a location
NDefines.NAI.ENEMY_PASSING_THROUGH_PLANES_PER_FIGHTER = 2 -- Amount of planes we assign to intercept enemies en-route to a location
NDefines.NAI.ENEMY_PASSING_THROUGH_PLANES_PER_SUPPORT = 2 -- Amount of planes we assign to intercept enemies en-route to a location

NDefines.NAI.ENEMY_PASSING_THROUGH_PLANES_PER_BOMBER_NAVAL_REGION = 1.5 -- Amount of planes we assign to intercept enemies en-route to a location over a sea region
NDefines.NAI.ENEMY_PASSING_THROUGH_PLANES_PER_FIGHTER_NAVAL_REGION = 1.25 -- Amount of planes we assign to intercept enemies en-route to a location over a sea region
NDefines.NAI.ENEMY_PASSING_THROUGH_PLANES_PER_SUPPORT_NAVAL_REGION = 1.0 -- Amount of planes we assign to intercept enemies en-route to a location over a sea region
NDefines.NAI.NAVAL_DEFENSE_INTERCEPTION_IMPORTANCE_FACTOR = 5 -- Factor on added planes passing through region to strategic importance

 -- LAND DEFENSE
NDefines.NAI.LAND_DEFENSE_MIN_FACTORIES_FOR_AIR_IMPORTANCE = 0 -- If amount of factories is less importance of factories won't apply

NDefines.NAI.LAND_DEFENSE_RAID_IMPORTANCE = 500                  -- Strategic importance of detected raids targetting us
NDefines.NAI.LAND_DEFENSE_FIGHERS_PER_RAID = 100                 -- Amount of air superiority planes requested per detected raid targetting us
NDefines.NAI.LAND_DEFENSE_INTERCEPTORS_PER_RAID = 100            -- Amount of interceptor planes requested per detected raid targetting us

NDefines.NAI.LAND_DEFENSE_SAM_MISSILE_IMPORTANCE_FACTOR = 0.2 -- Importance factor of using sam missiles for regions strategic importance. Higher value will increase the usage
NDefines.NAI.LAND_COMBAT_MISSILE_IMPORTANCE_FACTOR = 1.5  -- Importance factor of using missiles for regions strategic importance. Higher value will increase the usage

 -- requested air wings
NDefines.NAI.LAND_DEFENSE_FIGHERS_PER_PLANE = 1.0 -- Amount of air superiority planes requested per enemy plane
NDefines.NAI.LAND_DEFENSE_INTERCEPTORS_PER_BOMBERS = 1.5 -- Amount of air interceptor planes requested per enemy bomber
NDefines.NAI.LAND_DEFENSE_INTERCEPTORS_PER_PLANE = 0.5 -- Amount of air interceptor planes requested per enemy plane (non bomber)

 -- region importance
NDefines.NAI.LAND_DEFENSE_AIR_SUPERIORITY_IMPORTANCE = 5 -- #  EXPERIMENTAL was at 0.1 Strategic importance of air superiority ( amount of enemy planes in area )
NDefines.NAI.LAND_DEFENSE_CIVIL_FACTORY_IMPORTANCE = 3 -- Strategic importance of civil factories
NDefines.NAI.LAND_DEFENSE_MILITARY_FACTORY_IMPORTANCE = 3 -- Strategic importance of military factories
NDefines.NAI.LAND_DEFENSE_NAVAL_FACTORY_IMPORTANCE = 2 -- Strategic importance of naval factories
NDefines.NAI.LAND_DEFENSE_SUPPLY_HUB_IMPORTANCE = 1              -- Strategic importance of supply hubs
NDefines.NAI.LAND_DEFENSE_AA_IMPORTANCE_FACTOR = 0.1 -- Factor of AA influence on strategic importance ( 0.0 - 1.0 )
NDefines.NAI.LAND_DEFENSE_INFRA_IMPORTANCE_FACTOR = 0.1 -- Factor of infrastructure influence on strategic importance ( 0.0 - 1.0 )
NDefines.NAI.LAND_DEFENSE_IMPORTANCE_SCALE = 2.5 -- Lend defence total importance scale (every land defence score get's multiplied by it)


 -- GROUND SUPPORT
 -- requested air wings
NDefines.NAI.LAND_COMBAT_FIGHTERS_PER_PLANE = 1.25 -- Amount of air superiority planes requested per enemy plane
NDefines.NAI.LAND_COMBAT_INTERCEPT_PER_PLANE = 0 -- Amount of interception planes requested per enemy plane
NDefines.NAI.LAND_COMBAT_CAS_PER_ENEMY_ARMY = 40 -- Amount of CAS planes requested per enemy army
NDefines.NAI.LAND_COMBAT_ANTI_LOGISTICS_PER_ENEMY_ARMY = 1      -- Amount of CAS planes requested per enemy army for anti-logistics
NDefines.NAI.LAND_COMBAT_CAS_PER_COMBAT = 20 -- Amount of CAS requested per combat
NDefines.NAI.LAND_COMBAT_BOMBERS_PER_LAND_FORT_LEVEL = 70 -- Amount of bomber planes requested per enemy land fort level
NDefines.NAI.LAND_COMBAT_BOMBERS_PER_COASTAL_FORT_LEVEL = 50 -- Amount of bomber planes requested per enemy coastal fort level
NDefines.NAI.LAND_COMBAT_MIN_EXCORT_PLANES = 100 -- Min amount of planes requested to excort operations

 -- region importance
NDefines.NAI.LAND_COMBAT_AIR_SUPERIORITY_IMPORTANCE = -0.1 -- Strategic importance of air superiority ( amount of enemy planes in area )
NDefines.NAI.LAND_COMBAT_OUR_ARMIES_AIR_IMPORTANCE = 25 -- Strategic importance of our armies
NDefines.NAI.LAND_COMBAT_OUR_COMBATS_AIR_IMPORTANCE = 90 -- Strategic importance of our armies in the combats
NDefines.NAI.LAND_COMBAT_FRIEND_ARMIES_AIR_IMPORTANCE = 10 -- Strategic importance of friendly armies
NDefines.NAI.LAND_COMBAT_FRIEND_COMBATS_AIR_IMPORTANCE = 25 -- Strategic importance of friendly armies in the combat
NDefines.NAI.LAND_COMBAT_ENEMY_ARMIES_AIR_IMPORTANCE = 20 -- Strategic importance of our armies
NDefines.NAI.LAND_COMBAT_ENEMY_LAND_FORTS_AIR_IMPORTANCE = 2 -- Strategic importance of enemy land forts in the region
NDefines.NAI.LAND_COMBAT_ENEMY_COASTAL_FORTS_AIR_IMPORTANCE = 1 -- Strategic importance of enemy coastal fronts in the region
NDefines.NAI.LAND_COMBAT_IMPORTANCE_SCALE = 5.5 -- Lend combat total importance scale (every land combat score get's multiplied by it)

NDefines.NAI.NUM_HOURS_SINCE_LAST_COMBAT_TO_SUPPORT_UNITS_VIA_AIR = 48 -- units will be considered in combat if they are just out of their last combat for air supporting
NDefines.NAI.AIR_AI_ENEMY_PROV_RATIO_FOR_COMBAT_REGION = 0.01  -- if a region has more than this ratio of provinces controlled by enemy AI will consider it as a combat zone while assigning planes


 -- STRATEGIC BOMBING
NDefines.NAI.STR_BOMB_MIN_ENEMY_FIGHTERS_IN_AREA = 4000 -- If amount of enemy fighters is higher than this mission won't perform
 -- requested air wings
NDefines.NAI.STR_BOMB_FIGHTERS_PER_PLANE = 1.75 -- Amount of air superiority planes requested per enemy plane
NDefines.NAI.STR_BOMB_PLANES_PER_CIV_FACTORY = 5 -- Amount of planes requested per enemy civ factory
NDefines.NAI.STR_BOMB_PLANES_PER_MIL_FACTORY = 5 -- Amount of planes requested per enemy military factory
NDefines.NAI.STR_BOMB_PLANES_PER_NAV_FACTORY = 5 -- Amount of planes requested per enemy naval factory
NDefines.NAI.STR_BOMB_PLANES_PER_SUPPLY_HUB = 0         -- THIS IS LOGISTICS STRIKE; Amount of planes requested per enemy supply node
NDefines.NAI.STR_BOMB_MIN_EXCORT_PLANES = 350 -- Min amount of planes requested to excort operations

 -- region importance
NDefines.NAI.STR_BOMB_AIR_SUPERIORITY_IMPORTANCE = -0.1 -- Strategic importance of air superiority ( amount of enemy planes in area )
NDefines.NAI.STR_BOMB_CIVIL_FACTORY_IMPORTANCE = 5 -- Strategic importance of enemy civil factories
NDefines.NAI.STR_BOMB_MILITARY_FACTORY_IMPORTANCE = 4 -- Strategic importance of enemy military factories
NDefines.NAI.STR_BOMB_NAVAL_FACTORY_IMPORTANCE = 2 -- Strategic importance of enemy naval factories
NDefines.NAI.STR_BOMB_SUPPLY_HUB_IMPORTANCE = 1                  -- Strategic importance of enemy supply hubs
NDefines.NAI.STR_BOMB_AA_IMPORTANCE_FACTOR = 0.5 -- Factor of AA influence on strategic importance ( 0.0 - 1.0 )
NDefines.NAI.STR_BOMB_INFRA_IMPORTANCE_FACTOR = 0.1 -- Factor of infrastructure influence on strategic importance ( 0.0 - 1.0 )
NDefines.NAI.STR_BOMB_IMPORTANCE_SCALE = 4.0 -- str bombing total importance scale (every str bombing score get's multiplied by it)

 -- NAVAL STRIKE 
 -- requested air wings
NDefines.NAI.NAVAL_FIGHTERS_PER_PLANE = 1.25 -- Amounts of air superiority planes requested per enemy plane
NDefines.NAI.NAVAL_STRIKE_PLANES_PER_ARMY = 25 -- Amount of planes requested per enemy army
NDefines.NAI.NAVAL_STRIKE_PLANES_PER_SHIP = 10 -- Amount of bombers requested per enemy ship
NDefines.NAI.PORT_STRIKE_PLANES_PER_SHIP = 8 -- Amount of bombers request per enemy ship in the port
NDefines.NAI.NAVAL_MIN_EXCORT_PLANES = 25 -- Min amount of planes requested to excort operations

 -- region importance
NDefines.NAI.NAVAL_AIR_SUPERIORITY_IMPORTANCE = -0.1 -- Strategic importance of air superiority ( amount of enemy planes in area )
NDefines.NAI.NAVAL_SHIP_AIR_IMPORTANCE = 75 -- Naval ship air importance
NDefines.NAI.NAVAL_SHIP_IN_PORT_AIR_IMPORTANCE = 50 -- Naval ship in the port air importance
NDefines.NAI.NAVAL_COMBAT_AIR_IMPORTANCE = 500.0 -- Naval combat air importance
NDefines.NAI.NAVAL_TRANSFER_AIR_IMPORTANCE = 50.0 -- Naval transfer air importance
NDefines.NAI.NAVAL_COMBAT_TRANSFER_AIR_IMPORTANCE = 750.0 -- Naval combat involving enemy land units
NDefines.NAI.NAVAL_IMPORTANCE_SCALE = 0.5 -- Naval total importance scale (every naval score get's multiplied by it)
NDefines.NAI.NAVAL_COMBAT_OUR_NAVY_MULT_ON_IMPORTANCE = 0.60 -- Naval region importance are scaled by our ships as well
NDefines.NAI.NAVAL_COMBAT_ALLY_NAVY_MULT_ON_IMPORTANCE = 0.25 -- Naval region importance are scaled by our ships as well
NDefines.NAI.NAVAL_COMBAT_MIN_OUR_NAVY_MULT_ON_IMPORTANCE = 1.0  -- Min scale factor for naval region importance from our ships
NDefines.NAI.NAVAL_COMBAT_MAX_OUR_NAVY_MULT_ON_IMPORTANCE = 2.0  -- Max scale factor for naval region importance from our ships

 -- NAVAL PATROL
NDefines.NAI.NAVAL_PATROL_PLANES_PER_SHIP_PATROLLING = 15 -- Amount of naval patrol planes per ship on a patrol mission
NDefines.NAI.NAVAL_PATROL_PLANES_PER_SHIP_RAIDING = 20 -- Amount of naval patrol planes per ship on a convoy raid mission
NDefines.NAI.NAVAL_PATROL_PLANES_PER_SHIP_ESCORTING = 25 -- Amount of naval patrol planes per ship on a convoy escort mission

 -- MINE PLANTING & SWEEPING
 -- requested air wings
NDefines.NAI.MINES_SWEEPING_PLANES_PER_MAX_MINES = 100  -- Amount of air wings request for mines sweeping when there is max amount of mines planted by enemy in certain region
NDefines.NAI.MINES_PLANTING_PLANES_PER_MAX_DESIRE = 100 -- Amount of air wings request for mines planting when there is max desire for it.

 -- region importance
NDefines.NAI.MINES_PLANTING_DESIRE_PER_HOME_STATE = 0.5 -- Scoring for how much do we want to plant naval mines with our air wings if the naval region is adjacent to a home state. Multiple adjacent states increases the score. Max sum of score is 1.0.
NDefines.NAI.MINES_PLANTING_DESIRE_PER_ENEMY_STATE = 0.2 -- Scoring for how much do we want to plant naval mines with our air wings if the naval region is adjacent to the enemy state. Multiple adjacent states increases the score. Max sum of score is 1.0.
NDefines.NAI.MINES_PLANTING_DESIRE_PER_NAVAL_THREAT = 250 -- How much threat must be generated in the naval region in order to get the maximum desire to plant naval mines in there.

NDefines.NAI.GIE_EXILE_AIR_MANPOWER_USAGE_RATIO = 0.2  -- AI will not deploy new exile wings when this percentage of available exile manpower is already used for wing recruitment.

 -- INVASION LOGIC

NDefines.NAI.ENEMY_HOME_AREA_RATIO_TO_DISABLE_INVASIONS = 0.3  -- if we are fighting against an enemy home area from our home area and if the enemy area is larger than this ratio non strategy invasions are disabled
NDefines.NAI.ENEMY_NAVY_STRENGTH_DONT_BOTHER = 1.9 -- If the enemy has a navy at least these many times stronger that the own don't bother invading
NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE = 0.09 -- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend.
NDefines.NAI.RELATIVE_STRENGTH_TO_INVADE_DEFENSIVE = 0.1 -- Compares the estimated strength of the country/faction compared to it's enemies to see if it should invade or stay at home to defend but while being a defensive country.

NDefines.NAI.MAX_INVASION_SIZE = 18 -- max invasion group size
NDefines.NAI.MAX_UNIT_RATIO_FOR_INVASIONS = 0.3 -- countries won't use armies more than this ratio of total units for invasions
NDefines.NAI.MIN_UNIT_RATIO_FOR_INVASIONS = 0.1                          -- don't allocate more divisions than this for naval invasions
NDefines.NAI.MIN_INVASION_PLAN_VALUE_TO_EXECUTE = 0.2 -- AI will only activate invasions if it is above this
NDefines.NAI.MIN_INVASION_ORG_FACTOR_TO_EXECUTE = 0.75 -- ai will only activate invasions if average org factor is above this
NDefines.NAI.MIN_INVASION_UNITS_READY_TO_EXECUTE = 0.9               -- ai will only activate invasions if this ratio of assigned units are ready

NDefines.NAI.MAX_DISTANCE_NAVAL_INVASION = 250 -- AI is extremely unwilling to plan naval invasions above this naval distance limit.
NDefines.NAI.INVASION_COASTAL_PROVS_PER_ORDER = 14 -- AI will consider one extra invasion per number of provinces stated here (num orders = total coast / this)

NDefines.NAI.NAVAL_INVADED_AREA_PRIO_DURATION = 90 -- after successful invasion AI will prio the enemy area for this number of days
NDefines.NAI.NAVAL_INVADED_AREA_PRIO_MULT = 2.0 -- fronts that belongs to recent invasions gets more prio
NDefines.NAI.MIN_NUM_CONQUERED_PROVINCES_TO_DEPRIO_NAVAL_INVADED_FRONTS = 30 -- if you conquer this amount of provinces after a naval invasion it will lose its prio status and will act as a regular front

NDefines.NAI.INVASION_TARGET_DISTANCE_DENOMINATOR = 1000             -- When selecting invasion target divide this with (pixel) distance to get distance score factor. (Doesn't really affect the relative scoring but it affects the linearity of the score function.)
NDefines.NAI.INVASION_TARGET_NO_PORT_FACTOR = 0.2                    -- When selecting invasion target multiply score with this if the target has no port
NDefines.NAI.INVASION_TARGET_TRUNCATION_SELECT_THRESHOLD = 0.75       -- When selecting invasion target use this threshold for truncation selection. (1.0 means select highest scored target 0.0 means select randomly from all possible target 0.5 means select randomly from all targets with more than 50 % of highest score)
NDefines.NAI.INVASION_TARGET_PRIO_NOT_ENEMY_FACTOR = 0.17            -- When calculating priority for an invasion factor the score with this if the target is not an actual enemy.

NDefines.NAI.FAILED_INVASION_AVOID_DURATION = 60                    -- after a failed invasion AI will down-prioritize invading the same area again for this number of days
NDefines.NAI.FAILED_INVASION_AREA_PRIO_FACTOR = 0.5                  -- for every failed invasion on an area factor that area's invasion prio with this value
NDefines.NAI.FAILED_INVASION_PORT_PRIO_FACTOR = 0.66                 -- for every failed invasion on a target port (province) factor the chance that we try to invade that same port again (relative to other ports)

NDefines.NAI.MIN_INVASION_AREA_SIZE_FOR_FLOATING_HARBORS = 1    -- AI will consider using floating harbors for naval invasion if invasion area is larger than this many provinces

 -- ARMY LOGIC
NDefines.NAI.MAX_UNITS_FACTOR_AREA_ORDER = 1.0 -- Factor for max number of units to assign to area defense orders
NDefines.NAI.DESIRED_UNITS_FACTOR_AREA_ORDER = 0.9 -- Factor for desired number of units to assign to area defense orders
NDefines.NAI.MIN_UNITS_FACTOR_AREA_ORDER = 0.75 -- Factor for min number of units to assign to area defense orders

NDefines.NAI.MAX_UNITS_FACTOR_FRONT_ORDER = 1.0 -- Factor for max number of units to assign to area front orders
NDefines.NAI.DESIRED_UNITS_FACTOR_FRONT_ORDER = 1.1 -- Factor for desired number of units to assign to area front orders
NDefines.NAI.MIN_UNITS_FACTOR_FRONT_ORDER = 1.0 -- Factor for min number of units to assign to area front orders

NDefines.NAI.MAX_UNITS_FACTOR_INVASION_ORDER = 1.0 -- Factor for max number of units to assign to naval invasion orders
NDefines.NAI.DESIRED_UNITS_FACTOR_INVASION_ORDER = 1.0 -- Factor for desired number of units to assign to naval invasion orders
NDefines.NAI.MIN_UNITS_FACTOR_INVASION_ORDER = 1.0 -- Factor for min number of units to assign to naval invasion orders

 -- AREA DEFENCE

NDefines.NAI.AREA_DEFENSE_BASE_IMPORTANCE = 30 -- Area defense order base importance value (used for determining order of troop selections)
NDefines.NAI.AREA_DEFENSE_CIVIL_WAR_IMPORTANCE = 30 -- Area defense order importance value when a country is in a civil war as target or revolter. -- 0 = Never 1 = Infantry/Artillery 2 = Go wild
NDefines.NAI.AREA_DEFENSE_IMPORTANCE_FACTOR = 1.0                -- used to balance defensive area importance vs other fronts
NDefines.NAI.STATE_CONTROL_FOR_AREA_DEFENSE = 1.0 -- To avoid AI sending area defense to area with very little foothold

 -- Which settings will AI use for area defense by default
NDefines.NAI.AREA_DEFENSE_SETTING_VP = true
NDefines.NAI.AREA_DEFENSE_SETTING_PORTS = true
NDefines.NAI.AREA_DEFENSE_SETTING_AIRBASES = true
NDefines.NAI.AREA_DEFENSE_SETTING_BORDERS = false
NDefines.NAI.AREA_DEFENSE_SETTING_FORTS = false
NDefines.NAI.AREA_DEFENSE_SETTING_COASTLINES = true
NDefines.NAI.AREA_DEFENSE_SETTING_RAILWAYS = false
NDefines.NAI.AREA_DEFENSE_SETTING_FACILITY = false

NDefines.NAI.AREA_DEFENSE_MINCAP_MAX_CAPITAL_DEFENSE = 100               -- MaxUnits for capital defense is at least this. (basically use capital defense as a buffer if we have "too many units")
NDefines.NAI.AREA_DEFENSE_MINCAP_DESIRED_CAPITAL_DEFENSE = 8             -- DesiredUnits for capital defense is at least this.
NDefines.NAI.AREA_DEFENSE_MINCAP_MAX_HOME_AREA = 10                      -- MaxUnits for home area is at least this.
NDefines.NAI.AREA_DEFENSE_MINCAP_DESIRED_HOME_AREA = 3                   -- DesiredUnits for home area is at least this.

 -- these are all 3 numbers for min desired max unit need weights for area defense
NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_VP_WEIGHT = { 1.0, 1.0, 1.0 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_VP_WEIGHT = { 0.5, 1.0, 2.0 }
NDefines.NAI.AREA_DEFENSE_HOME_VP_WEIGHT = { 0.01, 0.5, 1.0 }
NDefines.NAI.AREA_DEFENSE_OTHER_VP_WEIGHT = { 0.0, 0.1, 0.5 }

NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_COAST_WEIGHT = { 0.0, 0.1, 0.2 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_COAST_WEIGHT = { 0.0, 0.5, 1.0 }
NDefines.NAI.AREA_DEFENSE_HOME_COAST_WEIGHT = { 0.0, 0.2, 0.4 }
NDefines.NAI.AREA_DEFENSE_OTHER_COAST_WEIGHT = { 0.0, 0.1, 0.2 }

NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_BASE_WEIGHT = { 0.2, 1.0, 1.0 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_BASE_WEIGHT = { 0.2, 1.0, 1.5 }
NDefines.NAI.AREA_DEFENSE_HOME_BASE_WEIGHT = { 0.1, 1.0, 1.0 }
NDefines.NAI.AREA_DEFENSE_OTHER_BASE_WEIGHT = { 0.0, 0.0, 0.1 }

 -- -- BATTLEPLAN FRONT PROVINCE SCORES
 -- only one of these 4 is used per province
NDefines.NMilitary.PLAN_PROVINCE_BASE_IMPORTANCE = 4.0 -- Used when calculating the calue of front and defense area provinces for the battle plan system
NDefines.NMilitary.PLAN_PROVINCE_LOW_VP_IMPORTANCE_FRONT = 4.0     -- Used when calculating the calue of fronts in the battle plan system
NDefines.NMilitary.PLAN_PROVINCE_MEDIUM_VP_IMPORTANCE_FRONT = 4.5  -- Used when calculating the calue of fronts in the battle plan system
NDefines.NMilitary.PLAN_PROVINCE_HIGH_VP_IMPORTANCE_FRONT = 5.0   -- Used when calculating the calue of fronts in the battle plan system
    
NDefines.NMilitary.PLAN_NEIGHBORING_ENEMY_PROVINCE_FACTOR = 0.35 -- When calculating the importance of provinces it takes number of enemy provinces into account factored by this
NDefines.NMilitary.PLAN_SHARED_FRONT_PROV_IMPORTANCE_FACTOR = 0.65 -- If fornt orders share end provinces they should each have a somewhat reduced prio due to it being shared.
NDefines.NMilitary.PLAN_PROVINCE_VP_PORT_FACTOR = 0.25  

 -- -- 

NDefines.NMilitary.MIN_VP_NEEDED_FOR_DEFENSE_ORDER_ASSIGNMENTS = 1.0  -- If a province has more than this VP unit controller will try to assign units that prov

NDefines.NMilitary.PLAN_PROVINCE_LOW_VP_DEFENSE_THRESHOLD = 2.0       -- For area defense VP orders what are the thresholds for "low" "medium" and "high" VP values
NDefines.NMilitary.PLAN_PROVINCE_MEDIUM_VP_DEFENSE_THRESHOLD = 8.0    -- see above
NDefines.NMilitary.PLAN_PROVINCE_HIGH_VP_DEFENSE_THRESHOLD = 25.0     -- see above
NDefines.NMilitary.PLAN_PROVINCE_LOW_VP_DEFENSE_IMPORTANCE = 2.0      -- For area defense VP orders use this value for relative importance
NDefines.NMilitary.PLAN_PROVINCE_MEDIUM_VP_DEFENSE_IMPORTANCE = 5.0   -- see above
NDefines.NMilitary.PLAN_PROVINCE_HIGH_VP_DEFENSE_IMPORTANCE = 10.0    -- see above
NDefines.NMilitary.PLAN_PROVINCE_CAPITAL_DEFENSE_IMPORTANCE = 50.0    -- For area defense VP orders boost importance value with this if it's the capital

NDefines.NMilitary.PLAN_PORVINCE_PORT_BASE_IMPORTANCE = 4.0 -- Added importance for area defense province with a port
NDefines.NMilitary.PLAN_PORVINCE_PORT_LEVEL_FACTOR = 2.0 -- Bonus factor for port level
NDefines.NMilitary.PLAN_PORVINCE_AIRFIELD_BASE_IMPORTANCE = 2.0 -- Added importance for area defense province with air field
NDefines.NMilitary.PLAN_PORVINCE_AIRFIELD_POPULATED_FACTOR = 1.5 -- Bonus factor when an airfield has planes on it
NDefines.NMilitary.PLAN_PORVINCE_RESISTANCE_BASE_IMPORTANCE = 0.0  -- Used when calculating the calue of defense area provinces for the battle plan system (factored by resistance level)
NDefines.NMilitary.PLAN_AREA_DEFENSE_HAS_RAIL_IMPORTANCE = 1.5 -- Used when calculating the value of defense area provinces for the battle plan system
NDefines.NMilitary.PLAN_AREA_DEFENSE_HAS_SUPPLY_NODE = 14.0 -- Used when calculating the value of defense area provinces for the battle plan system
NDefines.NMilitary.PLAN_AREA_DEFENSE_FACILITY = 15.0                -- Used when calculating the value of defense area provinces for the battle plan system

 -- These need to result in province value > 1.0 for it to matter.
NDefines.NMilitary.PLAN_AREA_DEFENSE_ENEMY_CONTROLLER_SCORE = 15.0 -- Score applied to provinces in the defense area order controlled by enemies
NDefines.NMilitary.PLAN_AREA_DEFENSE_ENEMY_UNIT_FACTOR = -2.0 -- Factor applied to province score in area defense order per enemy unit in that province
NDefines.NMilitary.PLAN_AREA_DEFENSE_FORT_IMPORTANCE = 0.25 -- Used when calculating the calue of defense area provinces for the battle plan system works as multipliers on the rest
NDefines.NMilitary.PLAN_AREA_DEFENSE_COASTAL_FORT_IMPORTANCE = 3.0 -- Used when calculating the calue of defense area provinces for the battle plan system
NDefines.NMilitary.PLAN_AREA_DEFENSE_COAST_NO_FORT_IMPORTANCE = 1.1 -- Used when calculating the calue of defense area provinces for the battle plan system

NDefines.NMilitary.PLAN_STICKINESS_FACTOR = 100.0 -- Factor used in unitcontroller when prioritizing units for locations

NDefines.NMilitary.PLAN_PROVINCE_PRIO_DISTRIBUTION_MIN = 0.7 -- Lowest fraction of divisions that will be distributed based on province priority
NDefines.NMilitary.PLAN_PROVINCE_PRIO_DISTRIBUTION_MAX = 1.0 -- Highest fraction of divisions that will be distributed based on province priority
NDefines.NMilitary.PLAN_PROVINCE_PRIO_DISTRIBUTION_DPP_HIGH = 4.0  -- At what divisions per province should we use PLAN_PROVINCE_PRIO_DISTRIBUTION_MIN
NDefines.NMilitary.PLAN_PROVINCE_PRIO_DISTRIBUTION_DPP_LOW = 1.5 -- At what divisions per province should we use PLAN_PROVINCE_PRIO_DISTRIBUTION_MAX

 -- order by EExecutionType: careful balanced rush <skip> weak rush
NDefines.NMilitary.PLAN_EXECUTE_SUPPLY_CHECK = { 1.0, 0.0, 0.0, 1.0, 0.0 }  -- for each execution mode how careful should we be with supply (1.0 means full required supply available zero is no limit).

NDefines.NMilitary.PLAN_MAX_PROGRESS_TO_JOIN = 0.35 -- If combat has lower progress than this support attacks are allowed