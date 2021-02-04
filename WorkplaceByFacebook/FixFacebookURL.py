# Title: Replace facebook.com url, which should be workplace.com

try:
    originaluri = document.get_meta_data_value("originaluri")[-1]
    clickableuri = document.get_meta_data_value("clickableuri")[-1]
    printableuri= document.get_meta_data_value("printableuri")[-1]
    uri = document.uri
    document.add_meta_data(
        {"originaluri": originaluri.replace("facebook.com", "workplace.com")})
    document.add_meta_data(
        {"clickableuri": clickableuri.replace("facebook.com", "workplace.com")})
    document.add_meta_data(
        {"printableuri": printableuri.replace("facebook.com", "workplace.com")})
    document.uri = uri.replace("facebook.com", "workplace.com")
except Exception as e:
    log(str(e))