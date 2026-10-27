import { useEffect, useState } from 'react'
import { buscarPets } from '../services/petServices'

/*
  - pets, setPets -> armazena a lista de pets da API e atualiza a lista
  - carregando, setCarregando -> indica se a busca está acontecendo e informa ao react quandoa bsuca termina
  - erro, setErro -> indinca se houve falha ao buscar os dados e atualiza o estado de erro
*/

// Função de featch
// puxa os dados 
export function usePets() {
  const [pets, setPets] = useState([])
  const [carregando, setCarregando] = useState(true)
  const [erro, setErro] = useState(false)

  useEffect(() => {
    async function carregarPets() {
      try {
        const listaPets = await buscarPets()
        setPets(listaPets)
      } catch (erro) {
        console.error(erro)
        setErro(true)
      } finally {
        setCarregando(false)
      }
    }

    carregarPets()
  }, [])

  return { pets, carregando, erro }
}
