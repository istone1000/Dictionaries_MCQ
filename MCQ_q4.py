provinces = {
    "Munster": {
        "county": "Cork",
        "town": "Kinsale"
    },
    "Leinster": {
        "county": "Kildare",
        "town": "Maynooth"
    },
    "Ulster": {
        "county": "Donegal",
        "town": "Killybegs"
    },
        "Connacht": {
        "county": "Mayo",
        "town": "Westport"
    },
}

for province, info in provinces.items():
    print(province, info)
    
print(provinces["Leinster"]["town"])
    