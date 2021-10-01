using System;
using System.Collections.Generic;

namespace NbaCsharpWebApi.Domain
{
    public class PlayerModel
    {
        public PlayerModel()
        {

        }

        public List<string> GetPlayerList()
        {
            return new List<string> { "helloworld" };
        }
    }
}
