def get_safe_meta_data_value(field):
  try:
    return document.get_meta_data_value(field)[-1]
  except Exception as e:
    return None

docType = get_safe_meta_data_value("documenttype")

if docType and docType != "Modules":
  # Don't waste our time, reject the doc
  document.reject()