using System;
using MySqlConnector;

namespace NbaCsharpWebApi.DataAccess
{
    public static class DataAccessExtensions
    {
        public static string SafeGetString(this MySqlDataReader reader, int colIndex)
        {
            if (!reader.IsDBNull(colIndex))
            {
                return reader.GetString(colIndex);
            }
            else
            {
                return null;
            }
        }

        public static string SafeGetString(this MySqlDataReader reader, string colName)
        {
            int colIndex = reader.GetOrdinal(colName);

            if (!reader.IsDBNull(colIndex))
            {
                return reader.GetString(colIndex);
            }
            else
            {
                return null;
            }
        }

        public static int? SafeGetInt(this MySqlDataReader reader, int colIndex)
        {
            if (!reader.IsDBNull(colIndex))
            {
                return reader.GetInt32(colIndex);
            }
            else
            {
                return null;
            }
        }

        public static int? SafeGetInt(this MySqlDataReader reader, string colName)
        {
            int colIndex = reader.GetOrdinal(colName);

            if (!reader.IsDBNull(colIndex))
            {
                return reader.GetInt32(colIndex);
            }
            else
            {
                return null;
            }
        }
    }

}
