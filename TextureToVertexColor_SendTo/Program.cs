using TextureToVertexColor_SendTo;

if (args == null || args.Length == 0)
{
    SendToLinkCreator.CreateLink();
    Console.WriteLine("Created Send To link");
    Console.WriteLine("To use this program, right click a 3D object file (like a .glb) -> Send to -> Texture To VertexColor");
    Console.ReadKey();
    return;
}

Console.WriteLine("-------- Arguments --------");

foreach (string arg in args)
    Console.WriteLine(arg);

Console.ReadKey();