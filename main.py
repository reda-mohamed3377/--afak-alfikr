basic.show_icon(IconNames.HEART)
basic.show_leds("""
    . . . . #
    . . . # .
    # # # . .
    # . # . .
    . . . # #
    """)

def on_forever():
    pass
basic.forever(on_forever)
