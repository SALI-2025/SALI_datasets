import random

space_device_map = {
    'hallway': ['light', 'lock', 'humidifier', 'dehumidifier', 'camera', 'air_purifier', 'temp_humidity_sensor', 'door_sensor'],
    'livingRoom': ['light', 'window_sensor', 'curtain_motor', 'robot_vacuum', 'air_conditioner', 'tv', 'speaker', 'central_control', 'pet_feeder', 'pet_water_dispenser', 'air_quality_monitor', 'projector', 'treadmill'],
    'masterBedroom': ['light', 'window_sensor', 'curtain_motor', 'desk_lamp', 'door_sensor', 'bed_pressure_sensor', 'alarm_clock', 'bedside_lamp', 'night_light', 'air_conditioner'],
    'secondBedroom': ['light', 'window_sensor', 'curtain_motor', 'desk_lamp', 'door_sensor', 'bed_pressure_sensor', 'alarm_clock', 'bedside_lamp', 'night_light', 'heater', 'fan'],
    'study': ['light', 'desk_lamp', 'window_sensor', 'curtain_motor', 'speaker', 'tv', 'smart_screen', 'door_sensor'],
    'kitchen': ['light', 'window_sensor', 'door_sensor', 'smoke_alarm', 'range_hood', 'rice_cooker', 'oven'],
    'dining': ['light', 'window_sensor', 'curtain_motor', 'electric_kettle', 'motion_sensor'],
    'bathroom': ['light', 'water_heater', 'door_sensor', 'smart_toilet_seat', 'smart_toilet_pressure_sensor', 'washing_machine', 'night_light', 'bath_heater', 'ventilation_system'],
    'balcony': ['clothes_dryer', 'clothes_hanger']
}

operation_table = {
    "motion_sensor": {
        "motion_detection": ["detected", "not_detected"]
    },
    "lock": {
        "lock": ["lock", "unlock"]
    },
    "light": {
        "switch": ["on", "off"],
        "set_brightness": [str(i) for i in range(1, 101, 1)],
        "set_mode": ["guest_mode", "movie_mode", "dining_mode", "work_mode", "sleep_mode", "reading_mode", "gaming_mode"],
        "set_color": ["red", "green", "blue", "white"]
    },
    "bedside_lamp": {
        "switch": ["on", "off"],
        "set_brightness": [str(i) for i in range(1, 101, 1)]
    },
    "night_light": {
        "switch": ["on", "off"],
        "set_brightness": [str(i) for i in range(1, 101, 1)]
    },
    "desk_lamp": {
        "switch": ["on", "off"],
        "set_brightness": [str(i) for i in range(1, 101, 1)],
        "set_mode": ["guest_mode", "movie_mode", "dining_mode", "work_mode", "sleep_mode", "reading_mode", "study_mode"]
    },
    "door_sensor": {
        "open_close_detection": ["open", "close"]
    },
    "window_sensor": {
        "open_close_detection": ["open", "close"]
    },
    "bed_pressure_sensor": {
        "occupancy_detection": ["detected", "released"]
    },
    "curtain_motor": {
        "control": ["open", "close"]
    },
    "air_quality_monitor": {
        "switch": ["on", "off"],
        "pm25": [str(i) for i in range(1, 201, 1)],
        "pm10": [str(i) for i in range(1, 201, 1)],
        "temperature": [str(i) for i in range(15, 31, 1)],
        "humidity": [str(i) for i in range(11, 81, 1)]
    },
    "humidifier": {
        "switch": ["on", "off"],
        "set_target_humidity": [str(i) for i in range(11, 81, 1)],
        "set_power_gear": ["auto", "low", "medium", "high"]
    },
    "dehumidifier": {
        "switch": ["on", "off"],
        "set_target_humidity": [str(i) for i in range(11, 81, 1)],
        "set_power_gear": ["auto", "low", "high"]
    },
    "camera": {
        "switch": ["on", "off"],
        "recording": ["start", "stop"]
    },
    "treadmill": {
        "switch": ["on", "off"],
        "set_speed": ["low", "medium", "high"]
    },
    "air_purifier": {
        "switch": ["on", "off"],
        "set_mode": ["auto", "sleep"],
        "set_wind": ["1", "2", "3", "4"]
    },
    "robot_vacuum": {
        "switch": ["on", "off"],
        "set_mode": ["charge", "clean", "pause"]
    },
    "air_conditioner": {
        "switch": ["on", "off"],
        "temperature": [str(i) for i in range(15, 31, 1)],
        "set_mode": ["cooling", "heating", "sleeping"],
        "set_wind_speed": ["low", "medium", "high"]
    },
    "central_control": {
        "alerter": ["on", "off"],
        "alarm": ["start", "stop"]
    },
    "speaker": {
        "switch": ["on", "off"],
        "set_volume": [str(i) for i in range(1, 101, 1)],
        "play_music": ["western", "soft", "background"]
    },
    "pet_feeder": {
        "switch": ["on", "off"],
        "feed_dispensed": ["start", "stop"]
    },
    "pet_water_dispenser": {
        "switch": ["on", "off"],
        "water_dispensed": ["start", "stop"]
    },
    "temp_humidity_sensor": {
        "temperature": [str(i) for i in range(15, 31, 1)],
        "humidity": [str(i) for i in range(11, 81, 1)]
    },
    "projector": {
        "switch": ["on", "off"]
    },
    "smart_toilet_seat": {
        "switch": ["on", "off"]
    },
    "alarm_clock": {
        "sound": ["start"]
    },
    "fan": {
        "switch": ["on", "off"],
        "set_angle": ["off", "60", "90", "120"],
        "set_speed": ["low", "medium", "high"],
        "set_mode": ["normal", "natural", "sleep"]
    },
    "heater": {
        "switch": ["on", "off"],
        "set_gear": ["energy_saving", "quick_heat"],
        "set_target_temperature": [str(i) for i in range(15, 31, 1)],
    },
    "smart_screen": {
        "switch": ["on", "off"],
        "screen_off": ["on", "off"],
        "set_interface": ["HDMI", "USB"],
        "set_picture_mode": ["standard", "soft", "kids", "cinema", "game"],
        "set_volume": ["mute", "unmute"]
    },
    "range_hood": {
        "switch": ["on", "off"],
        "set_gear": ["low", "medium", "high"],
        "set_mode": ["manual", "auto_cruise", "auto_air_purification", "high_heat"]
    },
    "tv": {
        "switch": ["on", "off"],
        "screen_off": ["on", "off"],
        "set_interface": ["HDMI", "USB"],
        "set_picture_mode": ["standard", "soft", "kids", "cinema", "game"],
        "set_volume": ["mute", "unmute"]
    },
    "rice_cooker": {
        "set_action": ["start", "stop"],
        "set_mode": ["quick_cook", "soup", "steam_cook"],
        "set_work_time": [str(i) for i in range(50, 91, 20)]
    },
    "oven": {
        "switch": ["on", "off"],
        "set_mode": ["bake", "convection", "defrost", "steam"]
    },
    "smart_dishwasher": {
        "switch": ["on", "off"],
        "set_gear": ["auto", "low", "medium", "high"],
        "set_water_level": ["low", "medium", "high"]
    },
    "electric_kettle": {
        "switch": ["on", "off"]
    },
    "water_heater": {
        "switch": ["on", "off"],
        "set_temperature": [str(i) for i in range(31, 56, 5)],
    },
    "smart_toilet_pressure_sensor": {
        "occupancy_detection": ["detected", "released"]
    },
    "smart_toilet_lid": {
        "switch": ["on", "off"]
    },
    "bath_heater": {
        "switch": ["on", "off"]
    },
    "smoke_alarm": {
        "switch": ["on", "off"],
        "alarm": ["alarm"]
    },
    "ventilation_system": {
        "switch": ["on", "off"],
        "set_wind_speed": ["auto", "low", "medium", "high"]
    },
    "washing_machine": {
        "switch": ["on", "off"],
        "set_mode": ["quick", "delicate"],
        "set_water_level": ["low", "medium", "high"],
        "set_action": ["start", "pause"]
    },
    "clothes_dryer": {
        "switch": ["on", "off"],
        "set_dry_mode": ["air_dry", "regular_dry"],
        "set_action": ["start", "pause"]
    },
    "clothes_hanger": {
        "set_up_down": ["raise_to_top", "lower_to_bottom"],
        "set_switch_light": ["on", "off"]
    }
}



#Leaving Home Security
rule1 = [
    "livingRoom central_control alerter on",
    "hallway camera switch on",
    "hallway camera recording start",
    "livingRoom window_sensor open_close_detection close",
    "hallway door_sensor open_close_detection open",
    "hallway door_sensor open_close_detection close",
    "hallway lock lock lock",
]


#Peace of Mind Protection
rule2 = [
    "livingRoom central_control alerter on",
    "livingRoom window_sensor open_close_detection open",
    "livingRoom central_control alarm start",
]

#Disarming Security Upon Entry
rule3 = [
    "livingRoom lock lock unlock",
    "hallway door_sensor open_close_detection open",
    "hallway door_sensor open_close_detection close",
    "livingRoom central_control alerter off",
    "livingRoom camera switch off",
    "livingRoom light switch on",
]


#Waking Up
rule4 = [
    "masterBedroom alarm_clock sound start",
    "masterBedroom bedside_lamp switch on",
    "masterBedroom bed_pressure_sensor occupancy_detection released",
    "masterBedroom curtain_motor control open4",
    "masterBedroom door_sensor open_close_detection open",
]
rule5 = [
    "secondBedroom alarm_clock sound start",
    "secondBedroom bedside_lamp switch on",
    "secondBedroom bed_pressure_sensor occupancy_detection released",
    "secondBedroom curtain_motor control open",
    "secondBedroom door_sensor open_close_detection open",
]

# Napping
rule6 = [
    "secondBedroom door_sensor open_close_detection close",
    "secondBedroom fan switch on",
    "secondBedroom fan set_speed low",
    "secondBedroom fan set_mode sleep",
    "secondBedroom curtain_motor control close",
    "secondBedroom bed_pressure_sensor occupancy_detection detected",
]

# Night Sleep
rule9 = [
    "masterBedroom bedside_lamp switch off",
    "masterBedroom curtain_motor control close",
    "masterBedroom night_light switch on",
    "masterBedroom night_light set_brightness 60",
    "masterBedroom air_conditioner switch on",
    "masterBedroom air_conditioner set_mode sleeping",
]
rule10 = [
    "secondBedroom bedside_lamp switch off",
    "secondBedroom curtain_motor control close",
    "secondBedroom night_light switch on",
    "secondBedroom night_light set_brightness 60",
    "secondBedroom air_conditioner switch on",
    "secondBedroom air_conditioner set_mode sleeping",
]

#Studying
rule11 = [
    "secondBedroom light switch on",
    "secondBedroom desk_lamp switch on",
    "secondBedroom desk_lamp set_mode study_mode",
    "secondBedroom door_sensor open_close_detection close",
]

# Nighttime Wake-Up
rule12 = [
    "masterBedroom bed_pressure_sensor occupancy_detection released",
    "masterBedroom door_sensor open_close_detection open",
    "masterBedroom bedside_lamp switch on",
    "kitchen door_sensor open_close_detection open",
    "kitchen light switch on",
    "kitchen light set_brightness 30",
    "kitchen light switch off",
    "masterBedroom door_sensor open_close_detection close",
]
rule13 = [
    "secondBedroom bed_pressure_sensor occupancy_detection released",
    "secondBedroom door_sensor open_close_detection open",
    "secondBedroom bedside_lamp switch on",
    "bathroom door_sensor open_close_detection open",
    "bathroom night_light switch on",
    "bathroom night_light set_brightness 80",
    "bathroom door_sensor open_close_detection close",
    "secondBedroom door_sensor open_close_detection close",
]

# Exercising
rule14 = [
    "livingRoom speaker switch on",
    "livingRoom speaker play_music background",
    "hallway air_purifier switch on",
    "hallway air_purifier set_mode auto",
    "hallway air_purifier set_wind 3",
    "livingRoom treadmill switch on",
    "livingRoom treadmill set_speed medium",
]

# Cooling Down
rule15 = [
    "hallway temp_humidity_sensor temperature 25",
    "livingRoom window_sensor open_close_detection close",
    "masterBedroom window_sensor open_close_detection close",
    "masterBedroom air_conditioner switch on",
    "masterBedroom air_conditioner set_mode cooling",
    "masterBedroom air_conditioner set_wind_speed medium",
    "secondBedroom fan switch on",
    "secondBedroom fan set_angle 120",
    "secondBedroom fan set_mode natural",
    "secondBedroom fan set_speed medium",
]

# Keeping Warm
rule16 = [
    "hallway temp_humidity_sensor temperature 15",
    "livingRoom window_sensor open_close_detection close",
    "masterBedroom window_sensor open_close_detection close",
    "masterBedroom air_conditioner switch on",
    "masterBedroom air_conditioner set_mode heating",
    "masterBedroom air_conditioner set_wind_speed medium",
    "secondBedroom window_sensor open_close_detection close",
    "secondBedroom heater switch on",
    "secondBedroom heater set_gear energy_saving",
    "secondBedroom heater set_target_temperature 20",
]

# Working from Home
rule17 = [
    "study door_sensor open_close_detection open",
    "study light switch on",
    "study door_sensor open_close_detection close",
    "study desk_lamp switch on",
    "study desk_lamp set_brightness 70",
    "study desk_lamp set_mode work_mode",
    "study smart_screen switch on",
    "study smart_screen set_picture_mode standard",
    "study smart_screen set_volume mute",
]

# Reading
rule18 = [
    "study door_sensor open_close_detection open",
    "study curtain_motor control close",
    "study desk_lamp switch on",
    "study desk_lamp set_brightness 40",
    "study desk_lamp set_mode reading_mode",
    "study speaker switch on",
    "study speaker play_music soft",
    "study door_sensor open_close_detection close",
]

# Movie Watching
rule19 = [
    "livingRoom tv switch on",
    "livingRoom tv set_picture_mode cinema",
    "livingRoom projector switch on",
    "livingRoom curtain_motor control close",
    "livingRoom light set_brightness 10",
    "livingRoom light set_color white",
    "livingRoom light set_mode movie_mode",
]

# E-Sports
rule20 = [
    "study smart_screen switch on",
    "study smart_screen set_picture_mode game",
    "study smart_screen set_volume unmute",
    "study speaker switch on",
    "study speaker set_volume 80",
    "study light set_mode gaming_mode",
    "study curtain_motor control close",
    "study door_sensor open_close_detection close",
]

# Listening to Music
rule21 = [
    "livingRoom speaker switch on",
    "livingRoom speaker set_volume 100",
    "livingRoom speaker play_music western",
    "livingRoom light switch on",
    "livingRoom light set_brightness 70",
    "livingRoom light set_color blue",
    "livingRoom curtain_motor control close",
]

# Party
rule22 = [
    "livingRoom light switch on",
    "livingRoom light set_brightness 100",
    "livingRoom light set_mode guest_mode",
    "livingRoom light set_color green",
    "kitchen light switch on",
    "kitchen light set_brightness 100",
    "kitchen light set_mode guest_mode",
    "kitchen light set_color green",
    "dining light switch on",
    "dining light set_brightness 100",
    "dining light set_mode guest_mode",
    "dining light set_color green",
]

# Doing Laundry
rule23 = [
    "bathroom door_sensor open_close_detection open",
    "bathroom light switch on",
    "bathroom washing_machine switch on",
    "bathroom washing_machine set_mode quick",
    "bathroom washing_machine set_water_level low",
    "bathroom washing_machine set_action start",
]

# Drying Clothes
rule24 = [
    "bathroom washing_machine switch off",
    "bathroom light switch off",
    "bathroom door_sensor open_close_detection close",
    "balcony clothes_dryer switch on",
    "balcony clothes_dryer set_dry_mode regular_dry",
    "balcony clothes_dryer set_action start",
]

# Sun-Drying Clothes
rule25 = [
    "balcony clothes_dryer switch off",
    "balcony clothes_hanger set_up_down lower_to_bottom",
    "balcony clothes_hanger set_switch_light on",
    "balcony clothes_hanger set_up_down raise_to_top",
]

# Humidifying
rule26 = [
    "hallway temp_humidity_sensor humidity 20",
    "livingRoom window_sensor open_close_detection close",
    "masterBedroom window_sensor open_close_detection close",
    "secondBedroom window_sensor open_close_detection close",
    "hallway humidifier switch on",
    "hallway humidifier set_target_humidity 40",
    "hallway humidifier set_power_gear auto",
]

# Dehumidifying
rule27 = [
    "hallway temp_humidity_sensor humidity 60",
    "livingRoom window_sensor open_close_detection close",
    "masterBedroom window_sensor open_close_detection close",
    "secondBedroom window_sensor open_close_detection close",
    "hallway dehumidifier switch on",
    "hallway dehumidifier set_target_humidity 40",
    "hallway dehumidifier set_power_gear auto",
]

# Cleaning
rule28 = [
    "livingRoom robot_vacuum switch on",
    "livingRoom robot_vacuum set_mode clean",
]

# Air Purification
rule29 = [
    "livingRoom air_quality_monitor switch on",
    "livingRoom air_quality_monitor pm25 70",
    "livingRoom air_quality_monitor pm10 80",
    "livingRoom window_sensor open_close_detection close",
    "hallway air_purifier switch on",
    "hallway air_purifier set_mode auto",
    "hallway air_purifier set_wind 3",
]

# Showering
rule30 = [
    "bathroom door_sensor open_close_detection open",
    "bathroom light switch on",
    "bathroom water_heater switch on",
    "bathroom water_heater set_temperature 45",
    "bathroom light switch off",
]

# Start of Bathroom Use
rule31 = [
    "bathroom light switch on",
    "bathroom ventilation_system switch on",
    "bathroom ventilation_system set_wind_speed auto",
    "bathroom door_sensor open_close_detection close",    
    "bathroom smart_toilet_lid switch on",
    "bathroom smart_toilet_pressure_sensor occupancy_detection detected", 
]

# End of Bathroom Use
rule32 = [
    "bathroom smart_toilet_pressure_sensor occupancy_detection released", 
    "bathroom smart_toilet_lid switch off",
    "bathroom door_sensor open_close_detection open",   
    "bathroom ventilation_system switch off",
    "bathroom light switch off",
]

# Smoke Purification
rule33 = [
#    "kitchen smoke_alarm alarm alarm", 
    "kitchen range_hood switch on",
    "kitchen range_hood set_gear open",   
    "kitchen range_hood set_mode auto_cruise",
]

# Kitchen Cleaning
rule34 = [
    "kitchen smart_dishwasher switch on", 
    "kitchen smart_dishwasher set_gear auto",
    "kitchen smart_dishwasher set_water_level medium",   
]

# Preparing Breakfast
rule35 = [
    "kitchen door_sensor open_close_detection open",
    "kitchen light switch on",
    "kitchen oven switch on",
    "kitchen oven set_mode bake",   
    "dining electric_kettle switch on", 
    "dining motion_sensor motion_detection detected",
]

# Dinner
rule36 = [
    "dining light switch on",
    "dining curtain_motor control close", 
    "dining motion_sensor motion_detection detected",
]

# Pet Feeding
rule37 = [
    "livingRoom pet_feeder switch on",
    "livingRoom pet_feeder feed_dispensed start",
    "livingRoom pet_water_dispenser switch on", 
    "livingRoom pet_water_dispenser water_dispensed start", 
]