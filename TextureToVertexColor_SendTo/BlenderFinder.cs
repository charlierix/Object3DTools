using Microsoft.Extensions.FileSystemGlobbing;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace TextureToVertexColor_SendTo
{
    public static class BlenderFinder
    {
        public static string FindBlenderExe(string config_value)
        {
            // They put the link in the config, so use that
            if (!string.IsNullOrWhiteSpace(config_value) && File.Exists(config_value))
                return config_value;

            // Iterate over all drives, looking for "Program Files\Blender Foundation\Blender X.X.X"
            var matches = new List<(string folder, Version version)>();

            foreach (var drive in DriveInfo.GetDrives())
            {
                string blender_base = Path.Combine(drive.Name, "Program Files", "Blender Foundation");

                if (!Directory.Exists(blender_base))
                    continue;

                foreach (string version_folder in Directory.GetDirectories(blender_base))
                {
                    string version_name = Path.GetFileName(version_folder);     // it's called GetFileName, but it returns the string after that last \

                    if (!version_name.StartsWith("Blender "))
                        continue;

                    string number = version_name.Substring(8);
                    if (Regex.IsMatch(number, @"^\d+$"))
                        number += ".0";     // version won't parse an integer, so put a .0 after

                    if (Version.TryParse(number, out Version version))
                        matches.Add((version_folder, version));
                }
            }

            // Choose the latest version
            return matches.
                OrderByDescending(o => o.version).
                Select(o => Path.Combine(o.folder, "blender.exe")).
                Where(o => File.Exists(o)).
                FirstOrDefault();
        }
    }
}
