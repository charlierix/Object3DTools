using System.Diagnostics;
using TextureToVertexColor_SendTo;

// If no args, create a sendto link
if (args == null || args.Length == 0)
{
    SendToLinkCreator.CreateLink();
    Console.WriteLine("Created Send To link");
    Console.WriteLine("To use this program, right click a 3D object file (like a .glb) -> Send to -> Texture To VertexColor");
    Console.ReadKey();
    return;
}

string blender_exe = BlenderFinder.FindBlenderExe();
if (string.IsNullOrEmpty(blender_exe))
{
    Console.WriteLine("Couldn't find blender.exe");
    Console.ReadKey();
    return;
}

// Run blender with the python script for each file selected (could probably do it in parallel, but in series
// feels safer)
//foreach (string arg in args)
//{

string arg = @"D:\models\!research\texture to vertex\violin.glb";


var startInfo = new ProcessStartInfo()
{
    //FileName = blender_exe,
    //Arguments = $" -b -P \"texture_to_vertexcolor.py\" -- \"{arg}\"",

    FileName = "python.exe",
    Arguments = $"\"D:\\!dev\\Object3DTools\\TextureToVertexColor\\tester.py\" -- \"{arg}\"",

    RedirectStandardOutput = true,
    RedirectStandardError = true,
    UseShellExecute = false,
    CreateNoWindow = true,
};

using (Process process = Process.Start(startInfo))
{
    while (!process.StandardOutput.EndOfStream)
        Console.WriteLine(process.StandardOutput.ReadLine());

    while (!process.StandardError.EndOfStream)
        Console.WriteLine(process.StandardError.ReadLine());

    process.WaitForExit();
}
//}

Console.ReadKey();