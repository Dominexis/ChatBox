# Set visibility

execute if score #chatbox_visible_2 chat.value matches 0 run bossbar set chatbox:2 name ""
bossbar set chatbox:2 visible true
scoreboard players set #chatbox_visible_2 chat.value 1