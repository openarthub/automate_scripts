#Import context from scene
import bpy

# NOTE
# - Total number is one up for total of card to make, 'cause need one more for cut the linear animation
# - For mor information about Euler Rotation https://docs.blender.org/manual/en/latest/advanced/appendices/rotations.html

# Create number for make objects booleans and this can cut the corner in bottom and left of card, this material has been in materials of card
def create_number():

    total_number = 21
    
    # Secound value to add in number for make booleans
    string_number_serie = "/20"
    
    # Object used to center number, the reference is taked form this object, if is needed move, be carefull
    center_point = bpy.data.objects["cubecenter"].dimensions.x
    
    # Loop for create number in serie
    for i in range(total_number):

        # First deselected all objects
        bpy.ops.object.select_all(action='DESELECT')
        # This get curve object to can make after edit a mesh object and can make boolean
        textBase = bpy.data.objects["textbase"]
        # Object is duplicated
        new_text = textBase.copy()
        # Copy same data nested of object
        new_text.data = textBase.data.copy()
        # Paste preview object duplicated to some collection
        bpy.data.collections["Collection"].objects.link(new_text)
        # Rename object
        new_text.name = "textbase" + str(i + 1) + string_number_serie
        # Select object (this is needed to edit)
        bpy.context.view_layer.objects.active = new_text
        new_text.select_set(True)
        
        # Open Edit Mode
        bpy.ops.object.mode_set(mode='EDIT')
        # Make a selecion of all characters in string of object curve
        bpy.ops.font.select_all()
        # Delete characters selected
        bpy.ops.font.delete(type="SELECTION")
        # Add new text
        bpy.ops.font.text_insert(text = str(i + 1) + string_number_serie, accent=False)
        # Return to Object Mode
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.mode_set(mode='OBJECT')
        # Convert curve object in mesh object (if is in curve object you can't make boolean)
        bpy.ops.object.convert(target='MESH')
        # Center text with reference on object in variable center_point
        x_to_move = center_point - new_text.dimensions.x
        new_text.location.x += x_to_move / 2


# Create object from anoter object base
def create_cards():
    x = 21

    #C = bpy.context

    name_base = "pipabasewitoutimggold"
    name_collection = "cardPipeGold"
    str_number_serie = "/20"

    # Get object to duplicate
    base = bpy.data.objects[name_base]

    # Loop for create cards
    for i in range(x):
        name_number_serie = "textbase" + str(i + 1) + str_number_serie
        # Duplicate object
        new_base = base.copy()
        # Copy same data nested
        new_base.data = base.data.copy()
        # Add object to some colletion
        bpy.data.collections[name_collection].objects.link(new_base)
        # Rename object
        new_base.name = "cardgyropipegold" + str(i + 1)
        # Add a new modifier, in this line is specific a Boolan
        new_base.modifiers.new(name="Bool", type='BOOLEAN')
        # Add a object to interact with modifier boolean
        new_base.modifiers["Bool"].object = bpy.data.objects[name_number_serie]
        # Select object to be boolean
        new_base.select_set(True)
        bpy.context.view_layer.objects.active = new_base
        # Apply modifier to object selected previus
        bpy.ops.object.modifier_apply(modifier = "Bool")

# Make animation for any objects created previusly in function 
def animate():
    
    x = 21
    
    # Time in frames per secound to animate
    animation_frames_time = 120
    
    #Loop for animate object
    for i in range(x):

        #deselect object preview and select card to animate
        bpy.ops.object.select_all(action='DESELECT')
        name_object = "cardgyropipegold" + str(i + 1)
        # Select object to animate
        object_to_anim = bpy.data.objects[name_object]
        
        # Initial state of object is hidden for render 'cause all object are in the same location
        object_to_anim.hide_render = True
        object_to_anim.keyframe_insert(data_path = "hide_render", frame = 0)

        # Init position in animation for rotate object
        object_to_anim.rotation_euler = [0,0,0]
        # Frame where init animaion
        frame_init = (animation_frames_time * i) + 1
        # Insert key animation and values to animate
        object_to_anim.keyframe_insert(data_path = "rotation_euler", frame = frame_init)
        
        # Make object visible for render
        object_to_anim.hide_render = False
        object_to_anim.keyframe_insert(data_path = "hide_render", frame = frame_init)
        
        # Make rotation 360 in axis Z
        object_to_anim.rotation_euler = [0,0,6.282722513089005]

        # Set end of rotate animation
        frame_end = frame_init + (animation_frames_time - 1)
        # Apply end of rotate animation insert a keframe
        object_to_anim.keyframe_insert(data_path = "rotation_euler", frame = frame_end)

        frame_end_hide = frame_end + 1
        # Make object hidden to render        
        object_to_anim.hide_render = True
        object_to_anim.keyframe_insert(data_path = "hide_render", frame = frame_end_hide)
        
        # Make interpolation of animation to linear, inital this value is curves
        for fc in object_to_anim.animation_data.action.fcurves:
            fc.extrapolation = 'LINEAR'

# Make animation for plane object, this is only one object 'cause is same image for this scene
def animate_image():

    total_cards = 21
    
    # Time in frames per secound to animate
    animation_frames_time = 120

    # Loop for animate object
    for i in range(total_cards):

        # Deselect all object
        bpy.ops.object.select_all(action='DESELECT')
        
        name_object = "planebase"
        # Select object to animate
        object_to_anim = bpy.data.objects[name_object]
        
        # Initial position to animate
        object_to_anim.rotation_euler = [1.570680628272251,0,0]
        # Initial frame to animate
        frame_init = (animation_frames_time * i) + 1
        # Adding initial key to animate
        object_to_anim.keyframe_insert(data_path = "rotation_euler", frame = frame_init)
        # Rotating object to position in rotation for make 360
        object_to_anim.rotation_euler = [1.570680628272251,0,6.282722513089005]
        frame_end = frame_init + (animation_frames_time - 1)
        # Adding final key to animate
        object_to_anim.keyframe_insert(data_path = "rotation_euler", frame = frame_end)

        # Loop for transform extrapolation curve animate to linear
        for fc in object_to_anim.animation_data.action.fcurves:
            fc.extrapolation = 'LINEAR'
            for kp in fc.keyframe_points:
                kp.handle_left_type  = 'VECTOR'
                kp.handle_right_type = 'VECTOR'

# Make render animation values previusly edited en blender         
def render_animation():
    bpy.context.scene.render.filepath = "C:/Users/usuario/Documents/proyectos/nft/renderscript/card_360_pipe_gold"
    bpy.ops.render.render(animation=True)

create_number()

create_cards()

animate()

animate_image()

# Code under this comment will be uncommented only for make animate card and execute from command line
# Save actual file
#bpy.ops.wm.save_mainfile()

#render_animation()