# Set visibility

execute if score #chatbox_visible_0 chat.value matches 0 run bossbar set chatbox:0 name ""
bossbar set chatbox:0 visible true
scoreboard players set #chatbox_visible_0 chat.value 1