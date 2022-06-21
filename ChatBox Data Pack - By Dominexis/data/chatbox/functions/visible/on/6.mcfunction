# Set visibility

execute if score #chatbox_visible_6 chat.value matches 0 run bossbar set chatbox:6 name ""
bossbar set chatbox:6 visible true
scoreboard players set #chatbox_visible_6 chat.value 1