# Set visibility

execute if score #chatbox_visible_4 chat.value matches 0 run bossbar set chatbox:4 name ""
bossbar set chatbox:4 visible true
scoreboard players set #chatbox_visible_4 chat.value 1