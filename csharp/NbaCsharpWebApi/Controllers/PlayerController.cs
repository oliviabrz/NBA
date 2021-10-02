using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using NbaCsharpWebApi.Domain;
using NbaCsharpWebApi.Dto;

namespace NbaCsharpWebApi.Controllers
{
    [Route("api/csharp/[controller]")]
    [ApiController]
    public class PlayerController : ControllerBase
    {
        // constructor
        public PlayerController(PlayerModel playerModel)
        {
            PlayerModel = playerModel;
        }

        private PlayerModel PlayerModel { get; set; }

        // GET: api/Player
        [HttpGet("/list")]
        public async Task<IEnumerable<PlayerRecord>> GetList()
        {
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
