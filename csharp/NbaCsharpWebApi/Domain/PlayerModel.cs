using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using NbaCsharpWebApi.DataAccess;
using NbaCsharpWebApi.Dto;

namespace NbaCsharpWebApi.Domain
{
    public class PlayerModel
    {
        public PlayerModel(DbDataService dbDataService, ILogger<PlayerModel> log)
        {
            DbDataService = dbDataService;
            Log = (Logger<PlayerModel>)log;
        }

        private DbDataService DbDataService { get; set; }
        private Logger<PlayerModel> Log { get; set; }

        public async Task<List<PlayerRecord>> GetPlayerList()
        {
            Log.LogDebug("GetPlayerList called");
            var playerList = await DbDataService.GetPlayerList();

            return playerList;
        }
    }
}
