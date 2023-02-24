# Import things

import os



# Initialize parameters

path = os.path.dirname(os.path.realpath(__file__))

length_2 = ["!", "'", ",", ".", ":", ";", "i", "|"]
length_3 = ["`", "l"]
length_4 = [" ", "\"", "(", ")", "*", "I", "[", "]", "t", "{", "}"]
length_5 = ["<", ">", "f", "k"]
length_6 = ["#", "$", "&", "+", "-", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "=", "?", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "\\", "^", "_", "a", "b", "c", "d", "e", "g", "h", "j", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z"]
length_7 = ["@", "~"]

colors = ["black","dark_blue","dark_green","dark_aqua","dark_red","dark_purple","gold","gray","dark_gray","blue","green","aqua","red","light_purple","yellow","white"]
color_hexcodes = ["§0","§1","§2","§3","§4","§5","§6","§7","§8","§9","§a","§b","§c","§d","§e",""]



# Define functions
def length(string):
    # Iterate through string
    length = 0
    bold = "false"
    i = 0
    while i < len(string):
        if string[i] == "[":
            end_index = string.find("]", i)
            for argument in parse_argument(string[i+1:end_index]):
                if argument[0] == "bold":
                    bold = argument[1]
            i = end_index
        elif string[i] == "{":
            pass
        elif string[i] == "}":
            pass
        else:
            if string[i] in length_2:
                length += 2
            elif string[i] in length_3:
                length += 3
            elif string[i] in length_4:
                length += 4
            elif string[i] in length_5:
                length += 5
            elif string[i] in length_6:
                length += 6
            elif string[i] in length_7:
                length += 7
            else:
                length += 5
            if bold == "true":
                length += 1
        i += 1
    return length

def pos(length, justify, anchor):
    if justify == "left":
        return (anchor, anchor + length)
    elif justify == "center":
        return (anchor - length//2, anchor + length//2)
    elif justify == "right":
        return (anchor - length, anchor)

def binary(x):
    output = ""
    if x >= 32768:
        output += "f"
        x -= 32768
    if x >= 16384:
        output += "e"
        x -= 16384
    if x >= 8192:
        output += "d"
        x -= 8192
    if x >= 4096:
        output += "c"
        x -= 4096
    if x >= 2048:
        output += "b"
        x -= 2048
    if x >= 1024:
        output += "a"
        x -= 1024
    if x >= 512:
        output += "9"
        x -= 512
    if x >= 256:
        output += "8"
        x -= 256
    if x >= 128:
        output += "7"
        x -= 128
    if x >= 64:
        output += "6"
        x -= 64
    if x >= 32:
        output += "5"
        x -= 32
    if x >= 16:
        output += "4"
        x -= 16
    if x >= 8:
        output += "3"
        x -= 8
    if x >= 4:
        output += "2"
        x -= 4
    if x >= 2:
        output += "1"
        x -= 2
    if x >= 1:
        output += "0"
        x -= 1
    return output

def offset(x):
    if x >= 0:
        return "\"forward\":[\"" + binary(x) + "0\"],\"backward\":[\"0\"]"
    else:
        return "\"forward\":[\"0\"],\"backward\":[\"" + binary(abs(x)) + "0\"]"

def parse_argument(argument):
    argument.replace(" ", "")
    entries = argument.split(",")
    output_list = []
    for entry in entries:
        parsed_form = entry.split("=")
        output_list.append((parsed_form[0], parsed_form[1]))
    return output_list

def bold_code(boolean):
    if boolean == "false":
        return ""
    else:
        return "§l"
        



# Make dialogue folder
if not os.path.exists(path + "\\dialogue"):
    os.makedirs(path + "\\dialogue")

# Extract inputs as dialogues
input_file = open(path + "\\input.txt", "r")
dialogues = []
dialogue = []
empty_line = True
lines = input_file.read().split("\n")
lines.append("")
for line in lines:
    if line == "":
        if empty_line == False:
            dialogues.append(dialogue)
        empty_line = True
    else:
        if empty_line == True:
            dialogue = []
        dialogue.append(line)
        empty_line = False
input_file.close()

# Iterate through dialogues
for dialogue in dialogues:
    # Initialize header parameters
    name = "dialogue"
    folder = ""
    id = "0"
    sound = "0"
    sounds = ""
    color = "white"
    bold = "false"

    # Prepare header
    header = ""
    if dialogue[0][0] == "[":
        header = dialogue[0][1:-1]
    for argument in parse_argument(header):
        if argument[0] == "folder":
            folder = argument[1]
            folder.replace("/", "\\")
            if not os.path.exists(path + "\\dialogue\\" + folder):
                os.makedirs(path + "\\dialogue\\" + folder)
            folder += "\\"
        elif argument[0] == "name":
            name = argument[1]
        elif argument[0] == "id":
            id = argument[1]
        elif argument[0] == "sound":
            sound = argument[1]
        elif argument[0] == "color":
            color = argument[1]
        elif argument[0] == "bold":
            bold = argument[1]
    dialogue.pop(0)

    # Compute lengths of lines
    line_count = min(len(dialogue), 5)
    char_counts = [0, 0, 0, 0, 0]
    line_lengths = [0, 0, 0, 0, 0]
    for i in range(line_count):
        char_counts[i] = len(dialogue[i])
        line_lengths[i] = length(dialogue[i])

    # Initialize line parameters
    pace = 1
    line = 0
    position = 0
    line_anchor = [-120, -120, -120, -120, -120]
    line_justify = ["left", "left", "left", "left", "left"]
    output_lines = ["", "", "", "", ""]
    tick = 0
    function_calls = ""

    # Iterate through lines
    while True:
        # Parse an argument if it exists
        if dialogue[line][position] == "[":
            end_index = dialogue[line].find("]", position)
            for argument in parse_argument(dialogue[line][position+1:end_index]):
                if argument[0] == "sound":
                    sound = argument[1]
                elif argument[0] == "pace":
                    pace = int(argument[1])
                elif argument[0] == "pause":
                    output_lines[line] += ",\"\"" * int(argument[1])
                    sounds += ",-1" * int(argument[1])
                    tick += int(argument[1])
                elif argument[0] == "justify":
                    line_justify[line] = argument[1]
                    if argument[1] == "left":
                        line_anchor[line] = -120
                    elif argument[1] == "center":
                        line_anchor[line] = 0
                    elif argument[1] == "right":
                        line_anchor[line] = 120
                elif argument[0] == "function":
                    function_calls += "\nschedule function " + argument[1] + " " + str(tick) + "t replace"
                elif argument[0] == "color":
                    color = argument[1]
                elif argument[0] == "bold":
                    bold = argument[1]
            position = end_index
        else:

            # Add character(s) to line
            if dialogue[line][position] == "{":
                end_index = dialogue[line].find("}", position)
                output_lines[line] += ",\"" + color_hexcodes[colors.index(color)] + bold_code(bold) + dialogue[line][position+1:end_index] + "\""
                position = end_index
            else:
                output_lines[line] += ",\"" + color_hexcodes[colors.index(color)] + bold_code(bold) + dialogue[line][position] + "\""

            # Add sound
            sounds += "," + sound

            # Add empty characters for pace
            if pace > 1:
                output_lines[line] += ",\"\"" * (pace-1)
                sounds += ",-1" * (pace-1)
            tick += pace
        
        # Iterate through dialogue
        position += 1
        if position >= char_counts[line]:
            position = 0
            line += 1
            pace = 1
            if line >= line_count:
                break

    # Set offsets
    pos_1 = pos(line_lengths[0], line_justify[0], line_anchor[0])
    pos_2 = pos(line_lengths[1], line_justify[1], line_anchor[1])
    pos_3 = pos(line_lengths[2], line_justify[2], line_anchor[2])
    pos_4 = pos(line_lengths[3], line_justify[3], line_anchor[3])
    pos_5 = pos(line_lengths[4], line_justify[4], line_anchor[4])

    offset_1 = pos_1[0] - 129
    offset_2 = pos_2[0] - pos_1[1]
    offset_3 = pos_3[0] - pos_2[1]
    offset_4 = pos_4[0] - pos_3[1]
    offset_5 = pos_5[0] - pos_4[1]
    offset_6 = 128 - pos_5[1]

    # Create function
    function = open(path + "\\dialogue\\" + folder + name + ".mcfunction", "w", encoding="utf-8")
    function.write(
        "data modify storage chatbox:data display." + id + " set value {" +
        "line_1:{invisible:[\"@\"," + output_lines[0][1:] + "],visible:[\"@\"]}," +
        "line_2:{invisible:[\"@\"," + output_lines[1][1:] + "],visible:[\"@\"]}," +
        "line_3:{invisible:[\"@\"," + output_lines[2][1:] + "],visible:[\"@\"]}," +
        "line_4:{invisible:[\"@\"," + output_lines[3][1:] + "],visible:[\"@\"]}," +
        "line_5:{invisible:[\"@\"," + output_lines[4][1:] + "],visible:[\"@\"]}," +
        "sounds:[I;" + sounds[1:] + "]," +
        "offset_1:{" + offset(offset_1) + "}," +
        "offset_2:{" + offset(offset_2) + "}," +
        "offset_3:{" + offset(offset_3) + "}," +
        "offset_4:{" + offset(offset_4) + "}," +
        "offset_5:{" + offset(offset_5) + "}," +
        "offset_6:{" + offset(offset_6) + "}}\n" +
        "scoreboard players set #line_" + id + " chat.value 1\n" +
        "scoreboard players set #sound_" + id + " chat.value 0\n" +
        "function chatbox:visible/on/" + id + "\n" +
        "schedule function chatbox:display/" + id + " 1t replace"
        + function_calls
    )
    function.close()



# Print success
print("Generation successful")
input()