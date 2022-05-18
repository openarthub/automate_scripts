# Script in Python for Blender

Files are in Folder "scripts"

## createAnimation360Card.py

Script for file named - card360ExportScript.blend

This script help to make card rotation in 360 degrees for 5 secound.

Next functions make a piece of code that make complete animation for us necessities.
If you want more information about specific thing in code, open file and you find more info.

```sh
def create_number():
```
`create_number()`: Create number for make objects booleans and this can cut the corner in bottom and left of card, material in this object has been in materials of card


```sh
def create_cards():
```
`create_number()`: Can create object from anoter object base and make any number of duplicates

```sh
def animate():
```
`animate()`: Make animation for any objects created previusly in function `create_cards()`, in this specific function add a animation rotating 360 degrees in axis Z, one an one per any object, all object are in same place, but we only need render one per time. So only when the card is animated are visible for render, after that the object are hidden

```sh
def animate_image():
```
`animate_image()`: Make animation some object object following animation maked previusly in function `animate()`, this object only animate one object because we need the same image.

```sh
def render_animation():
```
`render_animation()`: Start render animation with values saved in blender scenes. Don't recommend use this function until make more flexible the code

### Command Line

If you want to run this script with commando line, use something like:
```sh
"C:\path\Blender 3.0\blender.exe" -b "C:\path\card360ExportScript.blend" --python "C:\path\360cardscripttoanimate.py"
```

For more information about Blender Documentation:

[Blender Documentation]

For more information about Blender Command Line:

[Blender Command Line]

> This script found only for one Scene in specific, but should use the base for make more things.


[Blender Documentation]: <https://docs.blender.org/>
[Blender Command Line]: <https://docs.blender.org/manual/en/latest/advanced/command_line/>






