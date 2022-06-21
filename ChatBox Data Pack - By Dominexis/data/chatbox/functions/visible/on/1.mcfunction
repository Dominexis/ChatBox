# Set visibility

execute if score #chatbox_visible_1 chat.value matches 0 run bossbar set chatbox:1 name ""
bossbar set chatbox:1 visible true
scoreboard players set #chatbox_visible_1 chat.value 1