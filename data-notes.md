# Data notes

## GRID3 Nigeria operational LGA boundaries  
-Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
- downloaded: 4/9/2026
- 775 features, Polygons
-columns: ID_0(Integer), ISO (text), NAME_O (text), ID_1(integer), NAME_1(text), ID_2(integer), NAME_2(text), TYPE_2(text), ENGTYPE_2(text), NL_NAME_2(text), VARNAME_2(text)
- No nulls in NAME_O
-Covers my LGA fully
- COMPLETENESS: good and falls in the right places. compared my own LGA: covers the entire area.
- POSITIONAL: boundaries align well with satellite imagery, no systematic offset visible
- ATTRIBUTE: 100% carry surface tag, and each LGA can be separated.
- FITNESS: adequate for analysis purposes. 

##OSM roads, extracted via QuickOSM
-Query: highway=* within ETI-OSA LGA
-Extracted: 14/9/2026
-13,674 features, lines
-Columns: text and integer
- Coverage looks good in the whole area, sparse at the edge due to water
- COMPLETENESS: good in built-up area. compared my own street: all the roads are present. Sparse at the edge due to water.
- CURRENCY: most edits are recent. All roads are present
- POSITIONAL: roads align well with satellite imagery, no systematic offset visible
- ATTRIBUTE: only 18% carry surface tag, so paved and unpaved cannot be separated reliably
- FITNESS: adequate for access analysis in the built-up area. Not adequate for a paved-road question. 

##GRID 3 Nigeria Health facilities
- Source:https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about
- Downloaded: 4/9/2026
- 51,022 features, points
- columns: globalid(text), nhfr_uid(integer), nhfr_facil(text), country(text), iso(text), state(text), lga(text), lga_name_d(decimal), ward(text), ward_name_(decimal), facility_n(text), facility_1(text), ownership(text), ownership_(text), facility_1(text), facility_2(text), latitude(decimal), longitude(decimal), geocoordin(text), last_updat(text) 
- No nulls
- Covers my LGA fully
- COMPLETENESS: good in the LGA. compared my own street: not all hospitals are present.
- CURRENCY: most edits are not recent. All hospitals are present
- POSITIONAL: hospitals align well with satellite imagery, no systematic offset visible
- ATTRIBUTE: only 80% carry ownership and facility type, so primary health center and primary health clinic can be separated reliably. Also, government and profit can be separated reliably
- FITNESS: adequate for access analysis in the LGA. 

##CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Eti-Osa LGA, extracted from GRID3 Nigeria operational LGA boundaries
- All layers clipped to the study area, then reprojected to EPSG:32631 (UTM 31N)
- Area Check: Eti-Osa LGA 180.67km2, matches published figure
- Working files in project, raw files untouched
