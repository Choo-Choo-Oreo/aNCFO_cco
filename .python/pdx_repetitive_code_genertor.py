# This script generates repetitive PDX code blocks.
# It uses a template where `{name}` gets replaced with each item from a given list.
# For each item, it produces a unique block with condition checks and swaps,
# and writes all the blocks to a single text file.
template = """
text = {{
	trigger = {{
		has_country_flag = MRC_amc_primary_champion_{name}
	}}
	localization_key = MRC_amc_primary_champion_{name}_key
}}
"""

# Your full replacement list
items = [
    # ... (put the full list here)
	"light_fighter",
	"heavy_fighter",
	"light_cas",
	"light_naval",
	"tactical_cas",
	"tactical_naval",
	"carrier_fighter",
	"carrier_cas",
	"carrier_naval",
	"strategic_bomber",
	"maritime_patrol"
]

with open("generated_repetitive_code.txt", "w") as f:
    for name in items:
        f.write(template.format(name=name))
        # f.write("\n") # New Line

print("Done! Generated equipment code written to generated_repetitive_code.txt")
# This Python code is made by Choo_Choo_Oreo