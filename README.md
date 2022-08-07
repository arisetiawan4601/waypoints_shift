Script to move the entire ardupilot waypoints mission to new location

## How to Use
``` bash
python shift_wp.py waypoints_file_name wp_anchor destination_lat destination_long
```

## Example
``` bash
python shift_wp.py wp_shift_test.waypoints 4 38.7896842 30.4733954
```

Load these two waypoints files to see how this works