// Card que vai exibir os pets na interface

function PetCard({ pet }) {
  return (
    <article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
                    
        <h3 className="text-xl font-bold text-petcare-dark">
          {pet.nome}
        </h3>
    
        <p className="mt-2 text-slate-600">
          Raça: {pet.raca}
        </p>
    
        <p className="mt-1 text-slate-600">
          Porte: {pet.porte}
        </p>
    
        <p className="mt-1 text-slate-600">
          Idade: {pet.idade} anos
        </p>
    
        <span className="mt-4 inline-block rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">
          {pet.status_adocao}
        </span>
    </article>
  )
}

export default PetCard