# Set visibility

execute if score #chatbox_visible_5 chat.value matches 0 run bossbar set chatbox:5 name ""
bossbar set chatbox:5 visible true
scoreboard players set #chatbox_visible_5 chat.value 1