from dis import dis
import math
import sys

def distance(target, origin):
  lon1 = math.radians(target[1])
  lon2 = math.radians(origin[1])
  lat1 = math.radians(target[0])
  lat2 = math.radians(origin[0])
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
  c = 2 * math.asin(math.sqrt(a))
  r = 6371 * 1000    
  return(c * r)

file_name = sys.argv[1]

wp_num = int(sys.argv[2])

f = open(file_name, "r")
first_line = f.readline()
missions = f.readlines()
f.close()

anchor_lat = missions[wp_num].split()[8]
anchor_long = missions[wp_num].split()[9]

origin_coordinate = [float(anchor_lat), float(anchor_long)]
target_coordinate = [float(sys.argv[3]), float(sys.argv[4])]

y_displacement = (target_coordinate[0] -  origin_coordinate[0]) / 0.0000089
x_displacement = (target_coordinate[1] -  origin_coordinate[1]) * math.cos(origin_coordinate[0] * 0.018) / 0.0000089
lenght_displacement = math.sqrt(math.pow(x_displacement, 2) + math.pow(y_displacement, 2))
displacement_unit_vector = [x_displacement / lenght_displacement, y_displacement / lenght_displacement]

shift_displacement = distance(target_coordinate, origin_coordinate)
rotated_displacement_unit_vector = [displacement_unit_vector[1], -1 * displacement_unit_vector[0]]
displacement = [displacement_unit_vector[0] * shift_displacement, displacement_unit_vector[1] * shift_displacement]

f = open(file_name + "_shifted.waypoints", "w")
f.write(first_line)

for wp in missions:
  new_lat = float(wp.split()[8]) + (displacement[1] * 0.0000089)
  new_long = float(wp.split()[9]) + (displacement[0] * 0.0000089) / math.cos(float(wp.split()[8]) * 0.018)
  f.write((wp.replace(wp.split()[8], str(new_lat))).replace(wp.split()[9], str(new_long)))
f.close()