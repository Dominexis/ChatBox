# Iterate through characters and lines

execute if score #line_4 chat.value matches 1 unless data storage chatbox:data display.4.line_1.invisible[1] run scoreboard players add #line_4 chat.value 1
execute if score #line_4 chat.value matches 2 unless data storage chatbox:data display.4.line_2.invisible[1] run scoreboard players add #line_4 chat.value 1
execute if score #line_4 chat.value matches 3 unless data storage chatbox:data display.4.line_3.invisible[1] run scoreboard players add #line_4 chat.value 1
execute if score #line_4 chat.value matches 4 unless data storage chatbox:data display.4.line_4.invisible[1] run scoreboard players add #line_4 chat.value 1
execute if score #line_4 chat.value matches 5 unless data storage chatbox:data display.4.line_5.invisible[1] run scoreboard players add #line_4 chat.value 1

execute if score #line_4 chat.value matches 1 run data modify storage chatbox:data display.4.line_1.visible append from storage chatbox:data display.4.line_1.invisible[1]
execute if score #line_4 chat.value matches 2 run data modify storage chatbox:data display.4.line_2.visible append from storage chatbox:data display.4.line_2.invisible[1]
execute if score #line_4 chat.value matches 3 run data modify storage chatbox:data display.4.line_3.visible append from storage chatbox:data display.4.line_3.invisible[1]
execute if score #line_4 chat.value matches 4 run data modify storage chatbox:data display.4.line_4.visible append from storage chatbox:data display.4.line_4.invisible[1]
execute if score #line_4 chat.value matches 5 run data modify storage chatbox:data display.4.line_5.visible append from storage chatbox:data display.4.line_5.invisible[1]

execute if score #line_4 chat.value matches 1 run data remove storage chatbox:data display.4.line_1.invisible[1]
execute if score #line_4 chat.value matches 2 run data remove storage chatbox:data display.4.line_2.invisible[1]
execute if score #line_4 chat.value matches 3 run data remove storage chatbox:data display.4.line_3.invisible[1]
execute if score #line_4 chat.value matches 4 run data remove storage chatbox:data display.4.line_4.invisible[1]
execute if score #line_4 chat.value matches 5 run data remove storage chatbox:data display.4.line_5.invisible[1]







# Play sound

execute if score #line_4 chat.value matches 1..5 if data storage chatbox:data display.4.sounds[0] store result score #sound_4 chat.value run data get storage chatbox:data display.4.sounds[0]
execute if score #line_4 chat.value matches 1..5 if data storage chatbox:data display.4.sounds[0] run data remove storage chatbox:data display.4.sounds[0]

execute if score #line_4 chat.value matches 1..5 if score #sound_4 chat.value matches 4 as @a[scores={chat.id=4}] at @s run playsound chatbox:dialogue.type_0 master @s
execute if score #line_4 chat.value matches 1..5 if score #sound_4 chat.value matches 1 as @a[scores={chat.id=4}] at @s run playsound chatbox:dialogue.type_1 master @s
execute if score #line_4 chat.value matches 1..5 if score #sound_4 chat.value matches 2 as @a[scores={chat.id=4}] at @s run playsound chatbox:dialogue.type_2 master @s







# Set bossbar name

execute if score #line_4 chat.value matches 1..5 run bossbar set chatbox:4 name ["",{"text":"0","font":"chatbox:background"},{"nbt":"display.4.offset_1.forward","storage":"chatbox:data","interpret":true,"font":"chatbox:forward"},{"nbt":"display.4.offset_1.backward","storage":"chatbox:data","interpret":true,"font":"chatbox:backward"},{"nbt":"display.4.line_1.visible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_1"},{"nbt":"display.4.line_1.invisible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_invisible"},{"nbt":"display.4.offset_2.forward","storage":"chatbox:data","interpret":true,"font":"chatbox:forward"},{"nbt":"display.4.offset_2.backward","storage":"chatbox:data","interpret":true,"font":"chatbox:backward"},{"nbt":"display.4.line_2.visible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_2"},{"nbt":"display.4.line_2.invisible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_invisible"},{"nbt":"display.4.offset_3.forward","storage":"chatbox:data","interpret":true,"font":"chatbox:forward"},{"nbt":"display.4.offset_3.backward","storage":"chatbox:data","interpret":true,"font":"chatbox:backward"},{"nbt":"display.4.line_3.visible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_3"},{"nbt":"display.4.line_3.invisible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_invisible"},{"nbt":"display.4.offset_4.forward","storage":"chatbox:data","interpret":true,"font":"chatbox:forward"},{"nbt":"display.4.offset_4.backward","storage":"chatbox:data","interpret":true,"font":"chatbox:backward"},{"nbt":"display.4.line_4.visible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_4"},{"nbt":"display.4.line_4.invisible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_invisible"},{"nbt":"display.4.offset_5.forward","storage":"chatbox:data","interpret":true,"font":"chatbox:forward"},{"nbt":"display.4.offset_5.backward","storage":"chatbox:data","interpret":true,"font":"chatbox:backward"},{"nbt":"display.4.line_5.visible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_5"},{"nbt":"display.4.line_5.invisible","storage":"chatbox:data","interpret":true,"font":"chatbox:line_invisible"},{"nbt":"display.4.offset_6.forward","storage":"chatbox:data","interpret":true,"font":"chatbox:forward"},{"nbt":"display.4.offset_6.backward","storage":"chatbox:data","interpret":true,"font":"chatbox:backward"}]







# Run function again

execute if score #line_4 chat.value matches 1..5 run schedule function chatbox:display/4 1t replace