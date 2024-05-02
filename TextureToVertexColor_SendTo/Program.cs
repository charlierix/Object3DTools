using TextureToVertexColor_SendTo;
using Microsoft.Extensions.Configuration;

try
{
    // Load appsettings.json
    string exe_folder = Path.GetDirectoryName(Environment.ProcessPath);
    var builder = new ConfigurationBuilder().
        SetBasePath(exe_folder).
        AddJsonFile("appsettings.json", optional: false);

    var config = new AppSettings(builder.Build());

    // If no args, create a sendto link
    if (args == null || args.Length == 0)
    {
        SendToLinkCreator.CreateLink();
        Console.WriteLine("Created Send To link");
        Console.WriteLine("To use this program, right click a 3D object file (like a .glb) -> Send to -> Texture To VertexColor");
        Console.ReadKey();
        return;
    }

    // Get location of blender.exe
    string blender_exe = BlenderFinder.FindBlenderExe(config.Blender_Exe);
    if (string.IsNullOrEmpty(blender_exe))
    {
        Console.WriteLine("Couldn't find blender.exe");
        Console.ReadKey();
        return;
    }

    // Run blender with the python script for each file selected (could probably do it in parallel, but in series
    // feels safer)
    bool had_error = false;
    foreach (string arg in args)
    {
        string python_args = $"-s {config.SubDivide_Count}";
        if (config.Multi_Obj_Files)
            python_args += " -m True";
        python_args += $" -f \"{arg}\"";

        had_error |= BlenderCaller.Call(blender_exe, exe_folder, python_args, config.SubDivide_Count);

        Console.WriteLine();
    }

    if (had_error || config.Prompt_For_Close)
    {
        Console.WriteLine();
        Console.WriteLine("Finished.  Press any key to continue...");
        Console.ReadKey();
    }
}
catch (Exception ex)
{
    Console.WriteLine();
    Console.WriteLine(ex.ToString());
    Console.WriteLine();
    Console.WriteLine("Press any key to continue...");
    Console.ReadKey();
}
