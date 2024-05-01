using System.Diagnostics;

namespace TextureToVertexColor_SendTo
{
    public static class BlenderCaller
    {
        public static bool Call(string blender_exe, string exe_folder, string python_args, int subdivide_count)
        {
            var startInfo = new ProcessStartInfo()
            {
                FileName = blender_exe,
                Arguments = $" -b -P \"{Path.Combine(exe_folder, "python", "texture_to_vertexcolor.py")}\" -- {python_args}",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true,
            };

            bool had_error = false;

            using (Process process = Process.Start(startInfo))
            {
                while (!process.StandardOutput.EndOfStream)
                    Console.WriteLine(process.StandardOutput.ReadLine());

                while (!process.StandardError.EndOfStream)
                {
                    had_error = true;
                    Console.WriteLine(process.StandardError.ReadLine());
                }

                process.WaitForExit();
            }

            return had_error;
        }
    }
}
