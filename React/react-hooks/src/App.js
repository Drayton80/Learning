import { render } from '@testing-library/react';
import React, { useState, useEffect } from 'react';
// useEffect é um hook que possibilita ter acesso aos ciclos de vida de um componente


export default function App(){
  // Uma função não possui propriedades internamente dela pois ela não
  // é uma classe, então é necessário importar o hook useState
  // (Hooks possuem sempre esse use na frente, o que torna fácil
  // de identificar eles na chamada)
  // O parâmetro de entrada do useState é o estado inicial desse state
  // repositories é uma variável que armazenará os dados e setRepositories uma
  // função que permitirá fazer a alteração desses estados
  const [repositories, setRepositories] = useState([]);

  // O primeiro parâmetro é uma função que executa sempre que houver
  // alguma alteração na lista de variáveis definida no segundo parâmetro
  // É possível ter quantos useEffects se quiser ter em uma página
  useEffect(async () => {
    // Extrai-se todos os repositórios do github de minha conta
    const response = await fetch('https://api.github.com/users/Drayton80/repos');
    // Transforma em um JSON para ser possível utilizar
    const data = await response.json();
    // Utiliza-se a função definida no useState para alterar os repositories
    setRepositories(data);
  }, []); // A segunda variável indica que será apenas executado uma única vez, pois não há nenhuma dependência para executar

  // Apenas executará a função quando a propriedade repositories mudar
  useEffect(() => {
    const filtered = repositories.filter(repo => repo.favorite);

    document.title = `Você tem ${filtered.length} favoritos`;
  }, [repositories]);

  function handleFavorite(id) {
    const newRepositories = repositories.map(repo => {
      // Vai percorrer todos os repositórios e procurar aquele que bate com o id
      // passado para então alterar os repositórios como estavam + o favorito salvo
      // ou se o ID não encaixar com qualquer outro dos repositórios, retorna ele da mesma forma
      // Salva o inverso do que estiver salvo em favorite, se for true vira false e vice versa
      return repo.id === id ? { ...repo, favorite: !repo.favorite } : repo;
    });

    setRepositories(newRepositories);
  }

  return (
    <ul>
        { repositories.map(repo => (
          <li key={repo.id}>
            {repo.name}
            {repo.favorite == true && <span>(Favorito)</span>}
            <button onClick={() => handleFavorite(repo.id)}>Favoritar</button>
          </li>
        ))}
      </ul>
  );
}
