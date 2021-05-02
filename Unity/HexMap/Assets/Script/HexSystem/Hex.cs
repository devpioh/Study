using System;
using System.Collections;
using System.Collections.Generic;

namespace HexCoord
{
    public struct Hex 
    {
        public readonly int x, z, y;        // q r s
    
        public Hex(int x, int y, int z)
        {
            this.x = x;
            this.y = y;
            this.z = z;

            DevLog.ASSERT(0 == x + y + z, "must be x + y + z = 0");
        }

        public Hex(int row, int col)
        {
            this.x = row;
            this.y = (-row) - col;
            this.z = col;

            DevLog.ASSERT(0 == this.x + this.y + this.z, "must be x + y + z = 0");
        }

        public Hex(int[] array)
        {
            this.x = array[0];
            this.y = array[1];
            this.z = array[2];
            
            DevLog.ASSERT(0 == x + y + z, "must be x + y + z = 0");
        }

        public Hex(Hex hex)
        {
            x = hex.x;
            y = hex.y;
            z = hex.z;
        }

        public int Length()
        {
            //[todo]
            int ax = 0 > x ? -x : x;
            int ay = 0 > y ? -y : y;
            int az = 0 > z ? -z : z;
            return (int)((ax + ay + az) / 2); 
        }

        public int Distance(Hex target)
        {
            return (this - target).Length();
        }

        public Hex ToClockwise(bool right = true)
        {
            return right ? new Hex(-z, -y, -x) : new Hex(-y, -x, -z);
        }

        public override bool Equals(object obj)
        {
            var hex = (Hex)obj;
            return x == hex.x && y == hex.y && z == hex.z;
        }

        public bool Equals(Hex hex)
        {
            return x == hex.x && y == hex.y && z == hex.z;
        }

        //[todo]
        public override int GetHashCode()
        {
            int result  = x.GetHashCode();
            result      = (31 * result) + y.GetHashCode();
            result      = (31 * result) + z.GetHashCode();
            return result;
            //return base.GetHashCode();
        }

        public override string ToString()                   { return $"({x.ToString()}, {y.ToString()}, {z.ToString()})"; }

        public static bool operator == (Hex h1, Hex h2)     { return h1.x == h2.x && h1.y == h2.y && h1.z == h2.z; }
        public static bool operator != (Hex h1, Hex h2)     { return !(h1 == h2); }
        public static Hex operator + (Hex h1, Hex h2)       { return new Hex(h1.x + h2.x, h1.y + h2.y, h1.z + h2.z);  }
        public static Hex operator - (Hex h1, Hex h2)       { return new Hex(h1.x - h2.x, h1.y - h2.y, h1.z - h2.z);  }
        public static Hex operator * (Hex hex, int s)       { return new Hex(hex.x * s, hex.y * s, hex.z * s); }
    }
}
