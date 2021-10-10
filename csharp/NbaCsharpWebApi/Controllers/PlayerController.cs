using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NbaCsharpWebApi.Domain;
using NbaCsharpWebApi.Dto;

namespace NbaCsharpWebApi.Controllers
{
    [Route("api/csharp/player")]
    [ApiController]
    public class PlayerController : ControllerBase
    {
        // constructor
        public PlayerController(PlayerModel playerModel, ILogger<PlayerController> log)
        {
            PlayerModel = playerModel;
            Log = (Logger<PlayerController>)log;
        }

        private PlayerModel PlayerModel { get; set; }
        private Logger<PlayerController> Log { get; set; }

        // GET: api/Player
        [HttpGet("list")]
        public async Task<IEnumerable<PlayerRecord>> GetList()
        {
            Log.LogDebug("Get list called");
            var list = await PlayerModel.GetPlayerList();
            return list;
        }

    // GET: api/Player/5
    /*
    [HttpGet("{id}", Name = "Get")]
    public string Get(int id)
    {
        return "value";
    }*/
}
}
