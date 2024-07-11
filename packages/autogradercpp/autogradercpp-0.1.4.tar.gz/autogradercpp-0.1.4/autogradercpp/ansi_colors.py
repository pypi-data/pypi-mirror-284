FOREGROUND_COLORS={
    "black":30,
    "red":31,
    "green":32,
    "yellow":33,
    "blue":34,
    "magenta":35,
    "cyan":36,
    "white":37,
    "default":39,
    "reset":0,
    "bright_black":90,
    "bright_red":91,
    "bright_green":92,
    "bright_yellow":93,
    "bright_blue":94,
    "bright_magenta":95,
    "bright_cyan":96,
    "bright_white":97,
    "bold":1,
    "italic":3,
    "underline":4,
}
BACKGROUND_COLORS={
    "black":40,
    "red":41,
    "green":42,
    "yellow":43,
    "blue":44,
    "magenta":45,
    "cyan":46,
    "white":47,
    "default":49,
    "reset":0,
    "bright_black":100,
    "bright_red":101,
    "bright_green":102,
    "bright_yellow":103,
    "bright_blue":104,
    "bright_magenta":105,
    "bright_cyan":106,
    "bright_white":107,
}
ERROR_COLOR = BACKGROUND_COLORS['red']
TEST_EVAL_COLOR = FOREGROUND_COLORS['yellow']
TEXT_EXPECTED_COLOR = FOREGROUND_COLORS['bright_green']
TEXT_FOUND_COLOR = FOREGROUND_COLORS['bright_red']
TEST_PASSED_COLOR=BACKGROUND_COLORS['green']
TEST_FAILED_COLOR= BACKGROUND_COLORS['magenta']

def colorize_line(line, color_code):
    return f"\033[{color_code}m{line}\033[0m"
