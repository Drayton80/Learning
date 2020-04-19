// Definindo variáveis e constantes:
var variable = 10
let constant = 2 

// Em Swift a tipagem é estática e os tipos são inferidos, então
// não é possível atribuir um valor de outro tipo a uma variável
// já definida com um tipo especifico, como exemplo:
var integer_example = 12
// Tentar alterar para um string gerará um erro:
// integer_example = "twelve"

// É possível explicitar o tipo da variável ou constante da seguinte forma:
var double_example: Double = 2.0 // OBS.: se não for definido o tipo de um número de ponto flutuante, ele será definido como o tipo Double
var float_example: Float = 2.3
let string_example: String = "Test"
let character_example: Character = "c"

// Swift tem tipagem forte, logo sempre que se passa um valor ou variável como parâmetro de uma função, o compilador checará se os tipos esperados pela função são satisfeitos

// Para permitir que um tipo aceite o valor nulo, nil, é necessário fazer:
var integer: Int? = 1
integer = nil


let number_string = "1"
let number_integer = Int(number_string) // Pode gerar vazio, então o retorno é um tipo opcional
// Para fazer uso de um tipo opcional é preciso desempacotá-lo (unwrapping):
var sum = number_string! + 2
// Outra forma de unwrapping, aqui desempacota para testar se é um nil para executar algo dentro do if:
if let number = number_integer{
    print(100 % number)
}

// Em Swift não há ++ nem --, apenas += e -=