# import pandas as pd
#
# pd.options.display.float_format = '{:f}'.format
# df = pd.DataFrame({"t": [0.0], "value": [2342381610260758529]})
# df["v2"] = df.apply(lambda s: s["value"], axis=1)
# print(df)

import pandas as pd
from decimal import Decimal

pd.options.display.float_format = '{:f}'.format
df = pd.DataFrame({"t": [0.0], "value": ["2342381610260758529"]})

df["v2"] = df["value"].apply(lambda x: Decimal(x))

print(df)
