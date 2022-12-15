def convert_list_to_dict(lsts):

  lsts_to_dict = {}
  for lst in lsts:
    key, value = lst[0], lst[1]
    lsts_to_dict[key] = value
  
  return lsts_to_dict