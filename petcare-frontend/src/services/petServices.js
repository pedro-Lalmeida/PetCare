
const API_URL = 'http://127.0.0.1:8000/api/v1'

export async function buscarPets() {
  const resposta = await fetch(`${API_URL}/pets/`)

  if (!resposta.ok) {
    throw new Error('Não foi possível buscar os pets.')
  }

  const dados = await resposta.json()

  return dados.results ?? dados
}
