using System;

public class CoordinateSystem{
	private double _x;
	private double _y;
	
	public double x{
		get{
			return this._x;
		}
		
		set{
			this._x = value;
		}
	}
	
	public double y{
		get{
			return this._y;
		}
		
		set{
			this._y = value;
		}
	}
	
	public double r{
		get{
			double x = this._x;
			double y = this._y;
			
			return Math.Sqrt(x*x + y*y);
		}
		
		set{
			double o = this.o;
			double r = value;
			
			this._x = r * Math.Cos(o);
			this._y = r * Math.Sin(o);
		}
	}
	
	public double o{
		get{
			double x = this._x;
			double y = this._y;
			
			return Math.Atan2(y,x);
		}
		
		set{
			double o = value;
			double r = this.r;
			
			this._x = r * Math.Cos(o);
			this._y = r * Math.Sin(o);
		}
	}	
}

public class Program
{
	public static void Main()
	{
		// Teste de X e Y:
		CoordinateSystem coordinates = new CoordinateSystem();
		coordinates.x = 1;
		coordinates.y = 3;
		Console.WriteLine(coordinates.x);
		Console.WriteLine(coordinates.y);
		// Teste de R e O:
		coordinates.r = 2;
		coordinates.o = 0;
		Console.WriteLine(coordinates.r);
		Console.WriteLine(coordinates.o);
	}
}