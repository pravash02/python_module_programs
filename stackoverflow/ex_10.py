import json
import flatdict
import openpyxl
import pandas as pd

data = json.loads("""{
    "result":[{
        "level": "L3_SW",
        "name": "L23",
        "type": "CM"
    },{
        "level": "L3_SW",
        "name": "SOFT",
        "type": "QM"
    }],
    "context":{
        "config": {
            "project_area_name": "XYZ",
            "component_name": "Configuration",
            "config_name": "_WorkOn",
            "bu": "H"
        },
        "meta": {
            "project": {
                "name": "_WorkOn",
                "key": "2023-05-02_96614cc50ac8dc7e121f7090",
                "started_at": "2023-05-02-16-00"
            },
            "task": {
                "started": "2023-05-02-16-00",
                "finished": "2023-05-02-16-00",
                "req_count": 1
            }
        }
    }
}
""")

d = dict(flatdict.FlatterDict(data))
# EITHER: column A: keys, column B: values
df = pd.DataFrame.from_dict(d, orient='index')
# df.to_excel("test_11.xlsx", header=False)

# OR: row 1: keys, row 2: values
# df = pd.DataFrame.from_dict([d])
# df.to_excel("test.xlsx", index=False)
print(df)
