using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using NbaCsharpWebApi.DataAccess;
using NbaCsharpWebApi.Dto;

namespace NbaCsharpWebApi.Domain
{
    public class PlayerModel
    {
        public PlayerModel(DbDataService dbDataService)
        {
            DbDataService = dbDataService;
        }

        private DbDataService DbDataService { get; set; }

        public async Task<List<PlayerRecord>> GetPlayerList()
        {
            var playerList = await DbDataService.GetPlayerList();

            return playerList;
        }
    }
}
