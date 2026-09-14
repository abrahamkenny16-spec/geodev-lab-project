# Data notes

## GRID3 Nigeria operational LGA boundaries  
-Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
- downloaded: 4/9/2026
- 775 features, Polygons
-columns: ID_0(Integer), ISO (text), NAME_O (text), ID_1(integer), NAME_1(text), ID_2(integer), NAME_2(text), TYPE_2(text), ENGTYPE_2(text), NL_NAME_2(text), VARNAME_2(text)
- No nulls in NAME_O
-Covers my LGA fully

##OSM roads, extracted via QuickOSM
-Query: highway=* within ETI-OSA LGA
-Extracted: 14/9/2026
-13,674 features, lines
-Columns: text and integer
- Coverage looks good in the whole area, sparse at the edge due to water

##GRID 3 Nigeria Health facilities
- Source:https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about
- Downloaded: 4/9/2026
- 51,022 features, points
- columns: globalid(text), nhfr_uid(integer), nhfr_facil(text), country(text), iso(text), state(text), lga(text), lga_name_d(decimal), ward(text), ward_name_(decimal), facility_n(text), facility_1(text), ownership(text), ownership_(text), facility_1(text), facility_2(text), latitude(decimal), longitude(decimal), geocoordin(text), last_updat(text) 
- No nulls
- covers my LGA fully
