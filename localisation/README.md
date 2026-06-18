# Localisation & File Structure Guidelines

To maintain compatibility and ensure high-quality standards for the mod, all contributors must adhere to the following protocols:

## 1. Localisation Management
* **Standard Localisation:** Place all original mod strings in the standard directory: `localisation/[language]`.
* **Overwrites:** Any localisation files imported from other mods or intended to override base game text must be placed in the `localisation/replace` folder.
* **The "Writer's Rule":** English localisation files are reserved for designated **Writers** only. Localisers must exercise extreme caution when handling these files to maintain narrative consistency.
* **Priority Languages:** We officially support and prioritize **English**, **Russian**, and **Chinese**.

## 2. Content Organization
* **Modular File Structure:** When developing content for a specific country (tags), create a dedicated file for that nation.
* **Internal Sorting:** Ensure all entries within country-specific files (events, ideas, focuses) are logically sorted and commented to prevent merge conflicts and spaghetti code.
