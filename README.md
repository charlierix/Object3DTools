# Object3DTools
tools and experiments for working with 3D files


## TextureToVertexColor
When using shapelab, I will download some .glb files to play with, but they are texture mapped and shapelab uses vertex colors

This is a python script for blender that takes a texture mapped object, bakes as vertex colored, exports to .obj files.  It works by kicking off an instance of blender in the background (no ui, the process quits when finished)

It can be executed directly from the command line (TextureToVertexColor/python/texture_to_vertexcolor.py).  The first line in the script is an example of how to call it

But using from command prompt is tedious, so I made a wrapper app that is invoked from send to.  When you run the exe (TextureToVertexColor/TextureToVertexColor_SendTo.exe) without params, it creates a shortcut to itself in the send to folder (%appdata%\Roaming\Microsoft\Windows\SendTo).  After that, just right click on a 3D file(s) -> send to -> Texture To VertexColor

If you don't trust running binaries off the internet, the source code is in TextureToVertexColor_SendTo, there's a post build event to copy the output to ..\TextureToVertexColor, so be sure to remove all but .gitignore before compiling

There are also some options in appsettings.json that will be used whenever the exe runs:
- subdivide_count will add triangles so that there are more vertices to color
- multi_obj_files will create separate .obj files for each object, since shapelab treats multiple objects in an .obj as one merged object


> [!NOTE]
> When I was figuring out how to bake objects, there was no option to target vertex colors, tutorial instructions weren't quite lined up with my ui.  It was because I was using a 2.something version.  When I installed blender 4.1, it all worked
