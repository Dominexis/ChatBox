# Set visibility

execute if score #chatbox_visible_9 chat.value matches 0 run bossbar set chatbox:9 name ""
bossbar set chatbox:9 visible true
scoreboard players set #chatbox_visible_9 chat.value 1