using System;

public class CoordinateSystem{
	private float _x;
	private float _y;
	
	public float x{
		get{
			return this._x;
		}
		
		set{
			this._x = value;
		}
	}
	
	public float y{
		get{
			return this._y;
		}
		
		set{
			this._y = value;
		}
	}
	
	public float r{
		get{
			float x = this._x;
			float y = this._y;
			
			return (float) Math.Sqrt(x*x + y*y);
		}
		
		set{
			float o = this.o;
			float r = value;
			
			this._x = r * (float) Math.Cos(o);
			this._y = r * (float) Math.Sin(o);
		}
	}
	
	public float o{
		get{
			float x = this._x;
			float y = this._y;
			
			return (float) Math.Atan2(y,x);
		}
		
		set{
			float o = value;
			float r = this.r;
			
			this._x = r * (float) Math.Cos(o);
			this._y = r * (float) Math.Sin(o);
		}
	}	
}

public class Program
{
	public static void Main()
	{
		// Teste:
		CoordinateSystem coordinates = new CoordinateSystem();
		coordinates.x = 1;
		coordinates.y = (float) Math.Sqrt(3);
		Console.WriteLine(coordinates.r);
		Console.WriteLine(coordinates.o);
	}
}