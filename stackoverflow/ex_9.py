import pandas as pd


class ThirtyDayMonth(pd.DateOffset):
    def apply(self, other):
        return other + pd.DateOffset(days=30)


dates_360 = ['2022-01-01', '2022-02-01', '2022-03-01']

dates_adjusted = pd.to_datetime(dates_360, format='%Y-%m-%d') + ThirtyDayMonth()

print(dates_adjusted)
