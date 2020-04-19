// ARRAY:
// Arrays podem ter o tipo explicitado ou não:
let numbers: Array<Int> = [1,2,3,4] // Arrays criados com let são imutáveis
var words = ["one", "dog", "car"]

words.append("two")
words += ["cat", "bus"]

// Arrays apenas podem possuir elementos de um único tipo em Swift, então
// uma declaração deste tipo geraria erro:
let numbers_and_words = [1, 2, "3"]
// Tentar mudar um valor de um pré-existente também:
words[0] = 3

// Instanciando Arrays vazios:
var empty = [Int]()
var empty_too = Array<Int>()



// DICTIONARY:
// Dicionários podem ser instanciados das seguintes formas:
var prices = ["product 1": 30.0, "product 2": 3.5, "product 3": 40.0]
let prices_constant = ["product 1": 30.0, "product 2": 3.5]

prices["product 4"] = 34.0

// Para percorrer um dicionários usa-se tuplas:
for (key, value) in prices{
    print("\(key): costs \(value) R$")
}

// Instanciando dicionários vazios:
var service_prices = Dictionary<String, Double>()
var another_prices = [String: Double]()



// ENUM:
enum Compass{
    case North, South, East, West
}

var direction = Compass.South
direction = .East