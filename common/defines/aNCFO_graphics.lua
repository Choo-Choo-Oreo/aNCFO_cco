-- GFX for clearer visuals
	NDefines_Graphics.NMapMode.MAP_MODE_MANPOWER_RANGE_MAX = 5000000

-- Map‐icon priorities
	NDefines.NMapIcons.STRATEGIC_AIR_PRIORITY_AIR_MISSION = 290

-- Victory Point icons
	NDefines.NGraphics.VICTORY_POINT_MAP_ICON_TEXT_CUTOFF = {300, 500, 1500}

-- Unit‐icon grouping distances
	NDefines.NGraphics.MAP_ICONS_GROUP_CAM_DISTANCE                         = 100
	NDefines.NGraphics.MAP_ICONS_STATE_GROUP_CAM_DISTANCE                   = 325.0
	NDefines.NGraphics.MAP_ICONS_STRATEGIC_GROUP_CAM_DISTANCE               = 400
	NDefines.NGraphics.MAP_ICONS_STRATEGIC_AREA_HUGE                        = 220
	NDefines.NGraphics.MAP_ICONS_STATE_HUGE                                 = 100
	NDefines.NGraphics.MAP_ICONS_GROUP_SPLIT_SELECTED_LIMIT                 = 10
	NDefines.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE           = 200
	NDefines.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC = 0

-- Command‐group preset colors
	NDefines.NGraphics.COMMANDGROUP_PRESET_COLORS_HSV = {
	    0.0/360.0, 1.0, 0.75,    -- red
	    10.0/360.0, 1.0, 0.75,   -- orange
	    60.0/360.0, 1.0, 0.75,   -- yellow
	    120.0/360.0, 0.85, 0.75, -- green
	    155.0/360.0, 1.0, 0.75,  -- greenish
	    180.0/360.0, 1.0, 0.75,  -- turquoise
	    220.0/360.0, 1.0, 0.75,  -- blue
	    260.0/360.0, 1.0, 0.85,  -- dark purple
	    330.0/360.0, 0, 0.75     -- white
	}

-- Camera and icon distances
	NDefines.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT     = 20
	NDefines.NGraphics.AIRBASE_ICON_DISTANCE_CUTOFF        = 700
	NDefines.NGraphics.NAVALBASE_ICON_DISTANCE_CUTOFF      = 700
	NDefines_Graphics.NGraphics.RADAR_ICON_DISTANCE_CUTOFF = 700

-- Strategic Air map colors
	NDefines.NGraphics.STRATEGIC_AIR_COLOR_BAD     = {0.65, 0, 0, 1}
	NDefines.NGraphics.STRATEGIC_AIR_COLOR_GOOD    = {0, 0.65, 0, 1}
	NDefines.NGraphics.STRATEGIC_AIR_COLOR_AVERAGE = {0.65, 0.65, 0, 1}
	NDefines.NGraphics.STRATEGIC_AIR_COLOR_NEUTRAL = {130.0/255,130.0/255,130.0/255,1}

-- Gradient borders (strategic regions & supply areas)
	NDefines.NGraphics.GRADIENT_BORDERS_THICKNESS_STRATEGIC_REGIONS = 250.0
	NDefines.NGraphics.GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_A     = 250
	NDefines.NGraphics.GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_B     = 250

-- Resistance map colors
	NDefines.NGraphics.RESISTANCE_COLOR_GOOD    = {0.0, 0.65, 0, 1}
	NDefines.NGraphics.RESISTANCE_COLOR_AVERAGE = {0.65, 0.65, 0, 1}
	NDefines.NGraphics.RESISTANCE_COLOR_BAD     = {0.65, 0, 0, 1}

-- Miscellaneous NGraphics overrides
	NDefines.NGraphics.ROOT_FRONT_OFFSET = 2

-- Border‐selection overrides (in the same place as in 00_graphics.lua)
	NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_STATE_R    = 0.5
	NDefines_Graphics.NGraphics.BORDER_COLOR_SELECTION_PROVINCE_R = 1.0

-- Gradient‐borders thickness and outline overrides
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_COUNTRY_CENTER_THICKNESS = 0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_DIPLOMACY      = 1
	-- NDefines_Graphics.NGraphics.BORDER_WIDTH                              = 1.0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_FIELD_COUNTRY_LOW        = 0.0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_FIELD_COUNTRY_HIGH       = 9000.0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_COUNTRY_LOW    = 0.0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_COUNTRY_HIGH   = 35.0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_STATE          = 1.0
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_COUNTRY   = 0.98
	-- NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OUTLINE_CUTOFF_DIPLOMACY = 0.98

-- Country‐color modifiers
	NDefines_Graphics.NGraphics.COUNTRY_COLOR_SATURATION_MODIFIER = 0.725 -- Vintage 0.725 -- Default 0.60
	NDefines_Graphics.NGraphics.COUNTRY_COLOR_BRIGHTNESS_MODIFIER = 0.80  -- Vintage 0.70  -- Default 0.80



-- Terrain Mapmod
	NDefines_Graphics.NMapMode.MAP_MODE_TERRAIN_TRANSPARENCY = 1.0							-- Default 0.5
	NDefines_Graphics.NMapMode.MAP_MODE_NAVAL_TERRAIN_TRANSPARENCY = 1.0					-- Default 0.8
	NDefines_Graphics.NGraphics.GRADIENT_BORDERS_CAMERA_DISTANCE_OVERRIDE_TERRAIN = 0.20	-- Default 0.39
