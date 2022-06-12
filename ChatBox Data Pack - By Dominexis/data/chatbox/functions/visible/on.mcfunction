# Set visibility

execute if score #chatbox_visible chat.value matches 0 run bossbar set chatbox:chatbox name ""
bossbar set chatbox:chatbox players @a
scoreboard players set #chatbox_visible chat.value 1