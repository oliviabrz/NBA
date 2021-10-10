using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using MySqlConnector;
using NbaCsharpWebApi.Dto;

namespace NbaCsharpWebApi.DataAccess
{
    public class DbDataService
    {
        public DbDataService(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        private IConfiguration Configuration { get; set; }

        /// <summary>
        /// get a list of players from database 
        /// </summary>
        /// <returns></returns>
        public async Task<List<PlayerRecord>> GetPlayerList()
        {
            var playerList = new List<PlayerRecord>();

            var connection = new MySqlConnection(Configuration["ConnectionStrings:Default"]);
            await connection.OpenAsync();

            using var command = new MySqlCommand(@"select ID, FirstName, LastName, Position,
                                                          HeightFeet, HeightInches, WeightPounds, TeamID
                                                   from NBA.Player limit 10", connection);
            using var reader = await command.ExecuteReaderAsync();
            while (await reader.ReadAsync())
            {
                // create new player record instance and populate with database data
                var player = new PlayerRecord();
                player.ID = reader.SafeGetInt("ID").GetValueOrDefault();
                player.FirstName = reader.GetString("FirstName");
                player.LastName = reader.GetString("LastName");
                player.Position = reader.GetString("Position");
                player.HeightFeet = reader.SafeGetInt("HeightFeet").GetValueOrDefault();
                player.HeightInches = reader.SafeGetInt("HeightInches").GetValueOrDefault();
                player.WeightPounds = reader.SafeGetInt("WeightPounds").GetValueOrDefault();
                player.TeamID = reader.SafeGetInt("TeamID").GetValueOrDefault();

                // add player record instance to player list
                playerList.Add(player);
            }

            return playerList;
        }

        
    }
}
