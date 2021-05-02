using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace HexCoord
{
    public static class DevLog 
    {
        public static void ASSERT(bool condition, string message = "")
        {
            Debug.Assert(condition, message);
        }

        public static void Log( object obj )
        {
            Debug.Log( obj );
        }

        public static void Error( object obj )
        {
            Debug.LogError(obj);
        }

        public static void Warning( object obj )
        {
            Debug.LogWarning(obj);
        }
    }
}
