"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

arcade.open_window(1400, 800, "Drawing Example")

# Set the background color
arcade.set_background_color((39, 150, 40))

# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()