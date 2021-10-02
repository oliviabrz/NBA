using System;
namespace NbaCsharpWebApi.Dto
{
    public class PlayerRecord
    {
        public PlayerRecord()
        { }

        public int ID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Position { get; set; }
        public int HeightFeet { get; set; }
        public int HeightInches { get; set; }
        public int WeightPounds { get; set; }
        public int TeamID { get; set; }
    }
}
