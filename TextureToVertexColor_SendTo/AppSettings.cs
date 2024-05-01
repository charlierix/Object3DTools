using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TextureToVertexColor_SendTo
{
    public class AppSettings
    {
        private readonly IConfiguration _config;

        public AppSettings(IConfiguration config)
        {
            _config = config;
        }

        public string Blender_Exe => _config.GetValue<string>("blender_exe");

        public int SubDivide_Count => _config.GetValue<int>("subdivide_count");

        public bool Multi_Obj_Files => _config.GetValue<bool>("multi_obj_files");

        public bool Prompt_For_Close => _config.GetValue<bool>("prompt_for_close");
    }
}
