# Set visibility

execute if score #chatbox_visible_3 chat.value matches 0 run bossbar set chatbox:3 name ""
bossbar set chatbox:3 visible true
scoreboard players set #chatbox_visible_3 chat.value 1