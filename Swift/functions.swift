// Vários formas de funções:
func function_without_parameters_and_without_return(){
    print("Teste de exibição")
}

func with_parameters_and_return(parameter1: Int, parameter2: String) -> Int{
    return parameter1 + 2
}

func show(str: String) {
    print("Showing: \(str)")
}

// Atribuindo a função anterior a uma constante 
let show_text = show

// Agora tanto show(str) como show_text(str) chamam referenciam a mesma função
show_text("Imprimindo")
show(str: "Imprimindo outra vez")


// Usando funções como parâmetros de entrada de outra função
func function_that_call_another(showing: (String) -> ()){
    showing("Imprimindo novamente")
}

function_that_call_another(showing: show)