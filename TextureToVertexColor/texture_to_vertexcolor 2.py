# set render engine to cycles

# set world surface color to FFF
# in viewport shading props, uncheck "scene lights".  keep "scene world"
    # delete all lights (probably not necessary)

# iterate objects
    # remove image texture


    # ------- I think these might be unnecessary steps
    # add a vertex color
    # remape shader output from material to 


# ------------------------------

# Make sure you're using blender 4.1    :)

# Import your 3D model

# Remove any lights

# Go to world properties and set the surface color to white (with default gray, the bake ends up too dark)

# In the Object Data properties tab, choose render engine: cycles


# ************************ extra ************************
# Assign an image texture to the Base Color in the material properties
#   this will already be done when it's a texture mapped .glb

# Change the viewport shading to Material Preview to ensure the texture is displayed (top right icons O O 0 O)
# *******************************************************


# For Each Object

    # In the Object Data Properties panel, locate the Color Attributes section
        # Click the “+” button to add a new vertex color layer      --- it might be important that each object gets a uniquely named color attribute

    # ************************ extra ************************
    # Before baking, it's really fiddly about knowing the source image      --- in later attempts, I'm getting it to work without these steps
        # In the top left dropdown, change from Object Mode to Vertex Paint --- may not be necessary, but chatgpt kept saying to --- do this after baking to see the result (object mode doesn't show vertex coloring)
            # NOTE: if you choose another object, the vertex paint will be latched on to the previous (icon in the scene tree).  Uncheck that icon to vertex paint the currently selected object
        # In the bottom left, change the panel from timeline to shader editor
        # Click on the texture image's shape (orange title bar)
    # *******************************************************

    # Expand bake section
        # change target to Active Color Attribute

    # Click the Bake button

    # Export .obj
        # NOTE: this needs to be done for each object, since .obj doesn't support hierarchies.  If all objects get exported into the same .obj, shapelab turns them into a single combined object
        # check selected only (be sure to only select the objects you want exported)
        # uncheck materials export
        # check geometry colors




# (after exporting, it flips back to Object Mode.  Choose Vertex Paint mode while in the solid color viewport shading mode)