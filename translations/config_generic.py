# Based on the Places Data Schema revision 6 (5/18/2015)
# https://github.com/nationalparkservice/places-data/wiki/Places-Data-Schema-Guide
# with ogr2osm, the GIS field names are case sensitive
# with arc2osm, all GIS field names are converted to upper case
# all osm/Places tags should be lower case

# All config files must have defaults, fieldmap, altnames and valuemap

# default tags for generic features in Places
defaults = {}

# values map one to one from GIS field name to Places tag
fieldmap = {
    # GIS_FieldName : Places Tag
    # 'PLACESID': 'nps:places_id'  # Ignore - managed by system
    'NAME': 'name',
    'ALTNAME': 'nps:alt_name',
    'SHORTNAME': 'nps:short_name',
    'UNITCODE': 'nps:unit_code',
    'UNITNAME': 'nps:unit_name',
    'GROUPCODE': 'nps:group_code',
    'REGIONCODE': 'nps:region_code',
    'LOCATIONID': 'nps:location_id',
    'ASSETID': 'nps:asset_id',
    'ISEXTANT': 'nps:is_extant',
    'MAPMETHOD': 'nps:map_method',
    'MAPSOURCE': 'source',
    'SRCESCALE': 'nps:source_scale',
    'SOURCEDATE': 'nps:source_date',
    'XYERROR': 'nps:xy_error',
    'NOTES': 'note',
    'RESTRICT': 'nps:restriction',
    'DISTRIBUTE': 'nps:distribute',
    'CREATEDATE': 'nps:create_date',
    'CREATEUSER': 'nps:create_user',
    'EDITDATE': 'nps:edit_date',
    'EDITUSER': 'nps:edit_user',
    'FEATUREID': 'nps:feature_id',
    'GEOMETRYID': 'nps:source_id',
}

# alternate GIS field names.
altnames = {
    # GIS Standard FieldName: List of alternate spellings of field name
    'UNITCODE': ['UNIT_CODE'],
    'UNITNAME': ['UNIT_NAME'],
    'GROUPCODE': ['GROUP_CODE', 'ADMIN_UNIT_CODE'],
    'REGIONCODE': ['REGION_CODE'],
    'LOCATIONID': ['LOCATION_ID', 'FMSSID', 'FMSS_ID', 'FMSS_LOCATION_ID'],
    'ASSETID': ['ASSET_ID', 'FMSS_ASSET_ID'],
    'ISEXTANT': ['IS_EXTANT'],
    'MAPMETHOD': ['MAP_METHOD'],
    'MAPSOURCE': ['MAP_SOURCE'],
    'SRCESCALE': ['SOURCESCALE','SOURCE_SCALE'],
    'SOURCEDATE': ['SOURCE_DATE', 'SRCEDATE'],
    'XYERROR': ['XY_ERROR', 'HORIZONTALERROR', 'HORIZONTAL_ERROR', 'HERROR'],
    'NOTES': ['GIS_NOTES', 'NOTE', 'GIS_NOTE', 'REMARKS', 'COMMENTS'],
    'RESTRICT': ['RESTRICTION', 'RESTRICT_STATUS', 'RESTRICTION_STATUS',
                 'RESTRICTSTATUS', 'RESTRICTIONSTATUS'],
    'DISTRIBUTE': ['DISTRIBUTION', 'PUBLICLY_DISTRIBUTE',
                   'PUBLICLYDISTRIBUTE'],
    'CREATEDATE': ['CREATE_DATE', 'CREATED_DATE'],
    'CREATEUSER': ['CREATE_USER', 'CREATED_USER'],
    'EDITDATE': ['EDIT_DATE', 'LAST_EDIT_DATE', 'LAST_EDITED_DATE'],
    'EDITUSER': ['EDIT_USER', 'LAST_EDIT_USER', 'LAST_EDITED_USER'],
    'FEATUREID': ['FEATURE_ID'],
    'GEOMETRYID': ['GEOMETRY_ID'],
}

valuemap = {}
