## 3. Summarizing major categories ##

all_ages_major_categories = {}
recent_grads_major_categories = {}
all_major_category = set(all_ages["Major_category"])
recent_grads_category = set(recent_grads["Major_category"]) 
find_value = 0
t2 = 0

for value in all_major_category:
   find_value = all_ages[all_ages["Major_category"] == value]["Total"].sum()
   all_ages_major_categories[value] = find_value

for value in recent_grads_category:
    t2 = recent_grads[recent_grads["Major_category"]==value]["Total"].sum()
    recent_grads_major_categories[value] = t2


## 4. Low wage jobs rates ##

low_wage_percent = 0.0
low_wages = recent_grads["Low_wage_jobs"].sum()
total = recent_grads["Total"].sum()
low_wage_percent = float(low_wages/total)

## 5. Comparing datasets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index
recent_grads_lower_unemp_count = 0
all_ages_lower_unemp_count = 0

for m in majors:
    rg = recent_grads[recent_grads["Major"] == m]
    ag = all_ages[all_ages["Major"] == m]
    u_rg = rg["Unemployment_rate"].values[0]
    u_ag = ag["Unemployment_rate"].values[0]
    if u_rg < u_ag:
        recent_grads_lower_unemp_count += 1
    elif u_rg> u_ag:
        all_ages_lower_unemp_count += 1
    
    