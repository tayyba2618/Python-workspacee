# Travel Weather Planner

distance_mi = 200
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi == 0:
    print(False)

elif distance_mi <= 1 and not is_raining:
    print(True)

elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print(True)

elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True)

else:
    print(False)