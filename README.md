# ChatBox
ChatBox is a data pack utility for generating and displaying custom dialogue boxes in Minecraft: Java Edition. Within the data pack folder data/chatbox/functions is a Python script and an input text file. The input text file contains an example input, and when you run the Python script, it will generate dialogue functions from that input. Every dialogue that is displayed is global and seen by every player in the world.

Input format:  
The individual dialogues are separated by one or more empty lines. The input file can have an arbitrary number of dialogues which the Python script will generate. The first line in every dialogue is the header, and this denotes the name of the dialogue, the folder that it is generated in, and optionally the default sound. The header is in a square bracket argument. Each argument is comma-separated, and its value is denoted after the equal sign.  
After the header, you can have one to four lines for the dialogue. At any point in the dialogue, you can have a square bracket argument to change various parameters for the text. Additionally, putting a string of text in curly brackets makes the text appear instantly instead of one character at a time.

Arguments:  
name - The name of the dialogue.  
folder - The folder that the dialogue function generates in. If not present, it will generate in the root data/chatbox/functions/dialogue folder.  
sound - Which sound to play. It allows all numeric values, but only 0, 1, and 2 have sounds associated with them. Use -1 to make it play no sound at all.  
pause - The number of ticks to pause for.  
pace - The number of ticks between individual characters, used to slow down printing.  
justify - Changes which side of the dialogue box that the text prints on. Allowed values are "left", "center", and "right". Text is left justify by default.  
color - Changes the color of the text. Allowed values are the Minecraft color names.  
bold - Makes the text bold or not bold. Allowed values are "true" and "false".  
function - Makes the dialogue execute an arbitrary function at that particular time in the dialogue. Useful for chaining multiple dialogues together.  

Executing the dialogue:  
All dialogue functions are generated in data/chatbox/functions/dialogue/ with each dialogue being a different function.

Canceling dialogue:  
The function chatbox:visible/off will wipe the dialogue box and stop the current dialogue from printing. It does not, however, cancel scheduled functions in the dialogue, those will have to be canceled manually.



Sounds were made by baranek.  
ChatBox was inspired by a similar system by Ancientkingg and originally designed for Inanis.
