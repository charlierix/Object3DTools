using System.Diagnostics;

namespace TextureToVertexColor_SendTo
{
    public static class BlenderCaller
    {
        public static (string[] output, bool had_error) Call(string blender_exe, string exe_folder, string filename_3D, int subdivide_count)
        {
            var startInfo = new ProcessStartInfo()
            {
                //FileName = blender_exe,
                //Arguments = $" -b -P \"texture_to_vertexcolor.py\" -- \"{arg}\"",

                FileName = "python.exe",
                Arguments = $"\"{Path.Combine(exe_folder, "python", "tester.py")}\" -- \"{filename_3D}\"",

                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true,
            };

            bool had_error = false;
            var output = new List<string>();

            using (Process process = Process.Start(startInfo))
            {
                while (!process.StandardOutput.EndOfStream)
                    output.Add(process.StandardOutput.ReadLine());

                while (!process.StandardError.EndOfStream)
                {
                    had_error = true;
                    output.Add(process.StandardError.ReadLine());
                }

                process.WaitForExit();
            }

            return (output.ToArray(), had_error);
        }
    }
}
