if (args == null || args.Length == 0)
    Console.WriteLine("No arguments passed in");
else
    foreach (string arg in args)
        Console.WriteLine(arg);


string link_name = System.IO.Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.SendTo), "TextureToVertexColor.lnk");
string exe_name = System.IO.Path.Combine(Environment.CurrentDirectory, "TextureToVertexColor_SendTo.exe");

Console.WriteLine($"link_name: {link_name}");
Console.WriteLine($"exe_name: {exe_name}");

Console.ReadKey();