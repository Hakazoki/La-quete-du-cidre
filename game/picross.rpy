## Picross / Nonogram
# To create a piece of picross puzzle data, as below, supply a 2D array, laid out as the size of your puzzle
# Put True if that square is correct, False if not.
# The class should calculate everything else!
define EXAMPLE_5X5_PICROSS_PUZZLE = PicrossPuzzle([
    [False, True, False, True, False],
    [False, True, False, True, False],
    [False, False, False, False, False],
    [True, False, False, False, True],
    [True, True, True, True, True],
])

define EXAMPLE_10X5_PICROSS_PUZZLE = PicrossPuzzle([
    [False, True, False, True, True, False, True, False, True],
    [False, False, False, True, False, True, False, True, True],
    [False, False, False, True, False, True, False, True, True],
    [False, False, False, True, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
])

define EXAMPLE_10X10_PICROSS_PUZZLE = PicrossPuzzle([
    [False, True, False, True, True, False, True, False, True],
    [False, False, False, True, False, True, False, True, True],
    [False, False, False, True, False, True, False, True, True],
    [False, False, False, True, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
    [False, False, False, False, False, True, False, True, True],
])

define PUZZLE_EPEE = PicrossPuzzle([
    [False, False, False, False, False, False, False, False, True, True],
    [False, False, False, False, False, False, False, True, True, True],
    [False, False, False, False, False, False, True, True, True, False],
    [False, False, False, False, False, True, True, True, False, False],
    [False, False, False, False, True, True, True, False, False, False],
    [False, False, False, True, True, True, False, False, False, False],
    [False, True, True, True, True, False, False, False, False, False],
    [False, True, True, True, False, False, False, False, False, False],
    [True, True, True, False, False, False, False, False, False, False],
    [True, True, False, False, False, False, False, False, False, False],
])

define PUZZLE_BOUCLIER = PicrossPuzzle([
    [True, True, True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, False, False, True],
    [True, False, True, True, True, True, True, True, False, True],
    [True, False, True, True, True, True, True, True, False, True],
    [True, False, True, True, True, True, True, True, False, True],
    [False, True, False, True, True, True, True, False, True, False],
    [False, True, False, False, True, True, False, False, True, False],
    [False, False, True, False, False, False, False, True, False, False],
    [False, False, False, True, False, False, True, False, False, False],
    [False, False, False, False, True, True, False, False, False, False],
])

define PUZZLE_CRANE = PicrossPuzzle([
    [False, False, True, True, True, True, True, True, False, False],
    [False, True, True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, True, True, True],
    [True, True, False, False, True, True, False, False, True, True],
    [True, True, False, False, True, True, False, False, True, True],
    [True, True, True, True, True, True, True, True, True, True],
    [False, True, True, True, False, False, True, True, True, False],
    [False, False, True, True, True, True, True, True, False, False],
    [False, False, False, True, False, False, True, False, False, False],
    [False, False, False, True, True, True, True, False, False, False],
])

# Examples
## Jump to this label to get a look at how this works!
label picross_example:

    "Picross example \nUse LMB to mark a tile as correct, RMB to mark a tile as incorrect"

    menu:
        "5x5 example":
            call screen picross(EXAMPLE_5X5_PICROSS_PUZZLE)
            jump picross_example
        "10x5 example":
            call screen picross(EXAMPLE_10X5_PICROSS_PUZZLE)
            jump picross_example
        "10x10 example":
            call screen picross(EXAMPLE_10X10_PICROSS_PUZZLE, complete_action=Jump("picross_example_jump"))
            jump picross_example
        "Exit":
            pass
    
    return

label picross_example_jump:
    "this puzzle jumped to a different label when complete"

    jump picross_example

# Styles and Visuals
define picross_box_size = 75
define picross_numberbox_size = 150

image picross_screen_background = Solid("#920050", xysize=(1920, 1080))

style picross_tile_base:
    xysize (picross_box_size, picross_box_size)

style picross_button is picross_tile_base:
    background Solid("#fff")
    hover_background Solid("#cf8310")

style picross_button_highlight is picross_tile_base:
    background Solid("#ffebcd")

style picross_correct is picross_tile_base:
    background Solid("#1399ce")

style picross_correct_elimninated is picross_correct:
    foreground Text("X", color="#a81010", size=28, align=(0.5, 0.5))

style picross_incorrect is picross_tile_base:
    background Solid("#a8a8a8")

style picross_incorrect_elimninated is picross_incorrect:
    foreground Text("X", color="#a81010", size=28, align=(0.5, 0.5))

style picross_tile_background:
    background Solid("#000000")
    padding(5, 5, 5, 5)
    align (0.5, 0.5)

style picross_number_display_frame:
    background Frame(Solid("#fff", xysize=(10, 10)))
    padding (0, 0, 0, 0)

style picross_number_display_frame_highlighted is picross_number_display_frame:
    background Frame(Solid("#ffebcd", xysize=(10, 10)))

style picross_number_display_horizontal:
    xysize (picross_numberbox_size, picross_box_size) spacing 15
    align (1.0, 0.5)

style picross_number_display_vertical:
    xysize (picross_box_size, picross_numberbox_size) spacing 15
    align (0.5, 1.0)

style picross_number_text_incomplete:
    color "#000000"
    align (0.5, 0.5) 
    text_align 0.5

style picross_grid_spacing:
    spacing 2

style picross_complete_frame:
    align (0.5, 0.5)
    padding (15, 15, 15, 15)

style picross_status_hbox:
    align (0.5, 0.5)
    spacing 50

# Data
default active_picross_data = None

python early:
    class PicrossPuzzle():
        def __init__(self, tile_data):
            """
            Parameters:
            -----------
            tile_data : bool[][]
                A 2D list of bools, arranged as humanly readable to correspond to the layout of the picross grid
            """
            self.tile_data = tile_data
            self.x_count = len(tile_data[0])
            self.y_count = len(tile_data)
            self.row_displays = []
            self.collumn_displays = []

            for y in range(self.y_count):
                row_counts = [[]]

                for x in range(self.x_count):
                    if self.get_row(y)[x]:
                        row_counts[-1].append((x, y))
                    elif len(row_counts[-1]) != 0:
                        row_counts.append([])
                if len(row_counts) > 1 and len(row_counts[-1]) == 0:
                    row_counts.pop()
                self.row_displays.append(row_counts)

            for x in range(self.x_count):
                collumn_counts = [[]]
                for y in range(self.y_count):
                    if self.get_column(x)[y]:
                        collumn_counts[-1].append((x, y))
                    elif len(collumn_counts[-1]) != 0:
                        collumn_counts.append([])

                if len(collumn_counts) > 1 and len(collumn_counts[-1]) == 0:
                    collumn_counts.pop()
                self.collumn_displays.append(collumn_counts)
        
        def get_column(self, x):
            column = []
            for row in range(self.y_count):
                column.append(self.get_row(row)[x])
            return column

        def get_row(self, y):
            return self.tile_data[y]

# Functions
init python:
    def setup_picross_data(data):
        global active_picross_data
        active_picross_data = [[None] * data.x_count for i in range(data.y_count)]
        
    def eliminate_picross_tile(tile_id, new_state):
        global active_picross_data
        active_picross_data[tile_id[1]][tile_id[0]] = new_state
        if get_picross_completion_percent() == 1:
            renpy.set_screen_variable("hovered_tile", None)

    def get_picross_mistake_count():
        global active_picross_data
        picross_mistake_count = 0
        for i in range(len(active_picross_data)):
            for j in range(len(active_picross_data[i])):
                if active_picross_data[i][j] == False:
                    picross_mistake_count += 1
        return picross_mistake_count

    def get_picross_completion_percent():
        global active_picross_data
        picross_completed_count = 0
        for i in range(len(active_picross_data)):
            for j in range(len(active_picross_data[i])):
                if active_picross_data[i][j] is not None:
                    picross_completed_count += 1

        return float(picross_completed_count) / (len(active_picross_data) * len(active_picross_data[0]))

# Screens
screen picross(picross_data, complete_action=Return()):
    on "show" action Function(setup_picross_data, picross_data)
    default hovered_tile = None

    add "picross_screen_background"
    if not active_picross_data is None:
        vbox:
            align (0.5, 0.5)
            # Mistakes and completion %
            hbox:
                style "picross_status_hbox"
                text _("Mistakes: {0}".format(get_picross_mistake_count()))
                text _("Completion: {0}%".format(int(get_picross_completion_percent()*100)))
            frame:
                style "picross_tile_background"
        
                vbox:
                    style "picross_grid_spacing"
                    ## Number displays
                    hbox:
                        style "picross_grid_spacing"
                        null width picross_numberbox_size
                        for x in range(picross_data.x_count):
                            frame style ("picross_number_display_frame_highlighted" if hovered_tile is not None and hovered_tile[0] == x else "picross_number_display_frame"):
                                vbox:
                                    style "picross_number_display_vertical"
                                    for i in picross_data.collumn_displays[x]:
                                        text str(len(i)) style "picross_number_text_incomplete"
                    hbox:
                        style "picross_grid_spacing"
                        vbox:
                            style "picross_grid_spacing"
                            for y in range(picross_data.y_count):
                                frame style ("picross_number_display_frame_highlighted" if hovered_tile is not None and hovered_tile[1] == y else "picross_number_display_frame"):
                                    hbox:
                                        style "picross_number_display_horizontal"
                                        for i in picross_data.row_displays[y]:
                                            text str(len(i)) style "picross_number_text_incomplete"

                        ## Actual grid
                        grid picross_data.x_count picross_data.y_count:
                            style "picross_grid_spacing"
                            for y in range(picross_data.y_count):
                                for x in range(picross_data.x_count):
                                    use picross_tile((x, y), picross_data.get_row(y)[x], hovered_tile, SetScreenVariable("hovered_tile", (x, y)), SetScreenVariable("hovered_tile", None))
        # Complete Message
        if get_picross_completion_percent() == 1:
            frame:
                style "picross_complete_frame"
                vbox:
                    text _("Complete!")
                    textbutton _("Continue >>") action [SetVariable("active_picross_data", None), complete_action]

screen picross_tile(tile_id, is_valid, hovered_tile, hovered_action, unhovered_action):
    button:
        if get_picross_completion_percent() != 1:
            hovered hovered_action
            unhovered unhovered_action

        if active_picross_data[tile_id[1]][tile_id[0]] is None:
            style ("picross_button_highlight" if hovered_tile is not None and not tile_id == hovered_tile and (hovered_tile[0] == tile_id[0] or hovered_tile[1] == tile_id[1]) else "picross_button")
            ## LMB to choose tile as correct
            action Function(eliminate_picross_tile, tile_id, is_valid)
            # RMB to eliminate tile as empty
            alternate Function(eliminate_picross_tile, tile_id, not is_valid)
        else:
            action NullAction()
            if active_picross_data[tile_id[1]][tile_id[0]]:
                if is_valid:
                    style "picross_correct"
                else:
                    style "picross_incorrect"
            else:
                if is_valid:
                    style "picross_correct_elimninated"
                else:
                    style "picross_incorrect_elimninated"
