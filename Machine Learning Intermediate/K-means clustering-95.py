## 2. Point Guards ##

# Enter code here.
point_guards = nba[nba["pos"] == "PG"]

## 4. Assist Turnover Ratio ##

point_guards = point_guards[point_guards['tov'] != 0]
point_guards["atr"] = point_guards["ast"] / point_guards["tov"]

## 11. Step 1 (Continued) ##

# Add the function, `assign_to_cluster`
# This creates the column, `cluster`, by applying assign_to_cluster row-by-row
# Uncomment when ready
def assign_to_cluster(row):
    largest = []
    for key in centroids_dict.keys():
        largest.append(calculate_distance(centroids_dict[key], [row["ppg"],row["atr"]]))
    return largest.index(min(largest))    
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

## 13. Step 2 ##

def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        temp_df = df[df["cluster"] == cluster_id]
        new_centroids_dict[cluster_id] = [np.mean(temp_df["ppg"]),np.mean(temp_df["atr"])]
    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)