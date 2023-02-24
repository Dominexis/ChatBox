# Set visibility

execute if score #chatbox_visible_7 chat.value matches 0 run bossbar set chatbox:7 name ""
bossbar set chatbox:7 visible true
scoreboard players set #chatbox_visible_7 chat.value 1