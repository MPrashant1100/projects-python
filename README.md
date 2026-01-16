Python does:

--> Start pipeline
--> Read JSON file → Python dict
--> Validate that dict (structure + types)
--> Process numbers and compute results
--> Save results to output JSON
--> Log success
--> If any step fails → catch exception and log error