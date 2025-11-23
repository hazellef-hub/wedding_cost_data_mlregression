import pandas as pd
import numpy as np

np.random.seed(42)
n = 300

# Wedding types
wedding_types = ["destination", "local", "backyard", "resort", "civil", "elopement"]

# Catering styles & menus
catering_styles = ["buffet", "plated", "cocktail"]
menu_types = ["standard", "premium", "luxury"]

# Seasons, days, entertainment
seasons = ["spring", "summer", "fall", "winter"]
wedding_days = ["weekday", "weekend"]
entertainment_types = ["dj", "live_band", "none"]

# Generate guests with strict rules
guest_count = []
w_type_list = []

for _ in range(n):
    w = np.random.choice(wedding_types)
    w_type_list.append(w)

    if w == "elopement":
        guest_count.append(np.random.randint(2, 6))  # 2–5 guests
    elif w == "civil":
        guest_count.append(np.random.randint(2, 11))  # 2–10 guests
    else:
        # Normal weddings: 20–200+
        if np.random.rand() < 0.1:
            guest_count.append(np.random.randint(200, 251))
        else:
            guest_count.append(np.random.randint(20, 200))

guest_count = np.array(guest_count)
wedding_type = np.array(w_type_list)

# Generate other features
decor_level = np.random.randint(1, 6, n)
flower_package_level = np.random.randint(1, 6, n)
photographer_hours = np.random.randint(2, 11, n)
videographer = np.random.randint(0, 2, n)
catering_style = np.random.choice(catering_styles, n)
menu_type = np.random.choice(menu_types, n)
season = np.random.choice(seasons, n)
wedding_day = np.random.choice(wedding_days, n)
dress_budget = np.random.randint(300, 6000, n)
travel_required = np.random.randint(0, 2, n)
room_block_count = np.random.randint(0, 25, n)
entertainment_type = np.random.choice(entertainment_types, n)
makeup_hair_package = np.random.randint(1, 4, n)
coordinator_package = np.random.choice(["none", "basic", "full"], n)

# Base cost
base_cost = 3000 + guest_count * np.random.uniform(50, 100)

# Modify based on wedding type with strict ranges
def adjust_for_type(base, wtype, guests, travel):
    if wtype == "elopement":
        cost = np.random.uniform(3000, 20000)
        if travel:
            cost *= 1.3  # destination elopement
        return cost

    if wtype == "civil":
        cost = np.random.uniform(3000, 10000)
        return cost

    if wtype == "backyard":
        return base * 0.7

    if wtype == "local":
        return base

    if wtype == "destination":
        return base * 1.4 + 3000

    if wtype == "resort":
        return base * 1.9 + 6000

    return base

# Component costs
decor_cost = decor_level * np.random.uniform(600, 2000)
flower_cost = flower_package_level * np.random.uniform(400, 1200)
photo_cost = photographer_hours * 300
video_cost = videographer * 2000
menu_multiplier = np.where(menu_type == "standard", 1,
                    np.where(menu_type == "premium", 1.5, 2.4))
menu_cost = guest_count * 30 * menu_multiplier
season_multiplier = np.where(season == "summer", 1.25,
                     np.where(season == "spring", 1.15, 1.0))
day_multiplier = np.where(wedding_day == "weekend", 1.15, 1.0)
travel_cost = travel_required * np.random.uniform(1500, 6000)
entertainment_cost = np.where(entertainment_type == "none", 0,
                        np.where(entertainment_type == "dj", 1500, 4000))
coordinator_cost = np.where(coordinator_package == "none", 0,
                       np.where(coordinator_package == "basic", 1800, 4000))

# Total raw cost (for non-elopement/civil)
total_raw = (base_cost + decor_cost + flower_cost + photo_cost + video_cost +
             menu_cost + travel_cost + entertainment_cost + coordinator_cost +
             dress_budget * 0.6)

# Final cost with type rules applied
total_cost = np.array([
    adjust_for_type(total_raw[i], wedding_type[i], guest_count[i], travel_required[i])
    for i in range(n)
])

# Apply multipliers only for non-elopement/civil
mask = ~np.isin(wedding_type, ["elopement", "civil"])
total_cost[mask] *= season_multiplier[mask]
total_cost[mask] *= day_multiplier[mask]

# Ensure minimum threshold realistically applied
for i in range(n):
    if wedding_type[i] == "elopement":
        total_cost[i] = max(total_cost[i], 3000)
    elif wedding_type[i] == "civil":
        total_cost[i] = max(total_cost[i], 3000)
    else:
        total_cost[i] = max(total_cost[i], 8000)

df = pd.DataFrame({
    "guest_count": guest_count,
    "wedding_type": wedding_type,
    "decor_level": decor_level,
    "flower_package_level": flower_package_level,
    "photographer_hours": photographer_hours,
    "videographer": videographer,
    "catering_style": catering_style,
    "menu_type": menu_type,
    "season": season,
    "wedding_day": wedding_day,
    "dress_budget": dress_budget,
    "travel_required": travel_required,
    "room_block_count": room_block_count,
    "entertainment_type": entertainment_type,
    "makeup_hair_package": makeup_hair_package,
    "coordinator_package": coordinator_package,
    "total_cost_usd": np.round(total_cost, 2)
})

file_path = "/mnt/data/wedding_cost_dataset_v3.csv"
df.to_csv(file_path, index=False)

file_path
