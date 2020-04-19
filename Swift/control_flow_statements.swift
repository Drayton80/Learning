// Operador ternário:
var condition = true
let result = (condition) ? "se for verdadeiro a condição" : "se for falsa"

// If e Else:
let temperature = 21

if temperature > 30 {
    print("acima de 30")
} else if temperature > 20 {
    print("Acima de 20")
} else {
    print("20 e abaixo")
}

// Switch:
let test = 2

switch test {
// 1...4 define um intervalo (tipo Range) que vai de 1 até 4 (incluindo o 4 também)
case 1...4:
    print("test 1")
// Valor exatamente igual a 5
case 5:
    print("test 2")
// Range de 6 aé 10
case 6..<11:
    print("test 3")
default:
    print("test 4")
}

// Do While:
var optional_integer: Int? // inicialmente nil, pois não atribuímos nenhum valor

repeat {
    optional_integer = 20
} while optional_integer == nil

// While:
var i = 0
var text = ""

while i < 20 {
    text += String(i) + " "
    i += 1
}

print(text)

// For:
for i in 0...2 {
    print("i=\(i)")
}