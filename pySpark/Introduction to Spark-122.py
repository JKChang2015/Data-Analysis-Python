## 10. Filter ##

def filter_year(line):
    if line[0] != 'YEAR':
        return True
    else:
        return False

filtered_daily_show = daily_show.filter(lambda line: filter_year(line))