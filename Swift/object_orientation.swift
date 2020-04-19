// CLASSES E OBJETOS:
// Definição de classe:
class Vehicle{
    var model: String
    var number: Int
    var max_speed: Double
    var wheels: Int
    
    // Construtor:
    init(model: String, number: Int, max_spd: Double, whls: Int){
        self.model = model
        self.number = number
        max_speed = max_spd
        wheels = whls
    }
    
    // Método que será sobrescrito:
    func description(){
        print("It's a vehicle")
    }

    // Gets e Sets:
    func set_model(model: String){
        self.model = model
    }

    func get_model() -> String{
        return model
    }

    func set_number(number: Int){
        self.number = number
    }

    func get_number() -> Int{
        return number
    }

    func set_max_speed(max_speed: Double){
        self.max_speed = max_speed
    }

    func get_max_speed() -> Double{
        return max_speed
    }

    func set_wheels(wheels: Int){
        self.wheels = wheels
    }

    func get_wheels() -> Int{
        return wheels
    }
}

// Classe Car herda de Vehicle
class Car: Vehicle{
    // Modificação no construtor:
    init(model: String, number: Int, max_speed: Double){
        super.init(model: model, number: number, max_spd: max_speed, whls: 4)
    }

    // Classe sobrescrita:
    override func description(){
        print("It's a car")
    }
}

// Exemplo de instanciação de Objeto da classe Car:
let some_car = Car(model: "Model X", number: 123, max_speed: 245.0)



// PROTOCOL:
// É um conceito similar a interfaces de Java:
protocol MathOperation{
    func calculate(v1: Double, v2: Double) -> Double
}

class Sum: MathOperation{
    func calculate(v1: Double, v2: Double) -> Double{
        return v1 + v2
    }
}

class Subtraction: MathOperation{
    func calculate(v1: Double, v2: Double) -> Double{
        return v1 - v2
    }
}



// EXTENSIONS:
/* Extensões são estruturas que permitem que qualquer classe do Swift (seja ela definida 
pelo desenvolvedor ou pelos frameworks) seja reaberta e métodos possam ser adicionados a ela.*/
extension String {
    func onlyVogals() -> String {
        var vogals = ""
        
        for c in self.characters {
            let letter = "\(c)"
            if (letter == "a" || letter == "e" || letter == "i" || 
                letter == "o" || letter == "u") {
                vogals += letter
            }
        }
        
        return vogals
    }
}

let hello = "Hello, World!"
print(hello.onlyVogals())
// Será printado: "eoo"