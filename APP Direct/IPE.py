import json
 
def get_safe_meta_data_value(field):
    try:
        return document.get_meta_data_value(field)[-1]
    except Exception as e:
        return ''
 
tags_meta = get_safe_meta_data_value("appdirect_tags")
features_meta = get_safe_meta_data_value("appdirect_prd_features")
 
def get_children_list(child_array):
  list=""
  for child in child_array:
    list += child["name"] + ";"
  return list
 
def get_featurelist_list(f_array):
  list=""
  for feature in f_array:
    if feature["header"]:
      list += feature["header"] + ";"
  return list
 
#Get the fields from the tags json returned by the API
if tags_meta:
  tags_array = json.loads(tags_meta)
  for tag in tags_array: 
    if (tag['children']):
      if (tag['name'] == "Business Size") OR (tag['name'] == "Target Markets") :
        document.add_meta_data({'adp_company_size' : get_children_list(tag["children"])})
      if tag['name'] == "Industry":
        document.add_meta_data({'adp_industry' : get_children_list(tag["children"])})
      if tag['name'] == "Solutions":
        document.add_meta_data({'adp_solutions' : get_children_list(tag["children"])})
      if tag['name'] == "Discover Apps":
        document.add_meta_data({'adp_discoverapps' : get_children_list(tag["children"])})
 
#Get the features from the tags json returned by the API
if features_meta:
  features_array = json.loads(features_meta)
  document.add_meta_data({'adp_features' : get_featurelist_list(features_array)})