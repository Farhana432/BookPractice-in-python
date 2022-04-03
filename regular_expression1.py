s = "Afganistan, Bangladesh,India,Japan,Vhutan,Tokio,USA,UK,Jarmany,Canada,England,Greenland,Iceland,New_Zeeland,switzerland,Netherlands"
countries = s.split(",")
print("Countries = ",countries)

item_list = [item for item in countries if item.endswith("land") or item.endswith("lands") or item.startswith("U")]

print("list_items : ",item_list)


