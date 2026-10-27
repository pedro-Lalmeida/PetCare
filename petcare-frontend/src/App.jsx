// import { useEffect, useState } from 'react'
import { usePets } from './hooks/usePets'
import PetCard from './components/PetCard'



function App() {
  
  const { pets, carregando, erro } = usePets()

  return (
    <div className="min-h-screen bg-petcare-background text-slate-800">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5">
          <a href="#" className="text-2xl font-bold tracking-tight text-petcare-dark">
            PetCare<span className="text-petcare-primary">.</span>
          </a>

          <nav className="hidden items-center gap-8 md:flex">
            <a href="#inicio" className="text-sm font-medium hover:text-petcare-primary">
              Início
            </a>
            <a href="#pets" className="text-sm font-medium hover:text-petcare-primary">
              Conheça os pets
            </a>
            <a href="#sobre" className="text-sm font-medium hover:text-petcare-primary">
              Sobre
            </a>
          </nav>

          <button className="rounded-xl bg-petcare-primary px-5 py-3 text-sm font-semibold text-white transition hover:bg-petcare-dark">
            Entrar
          </button>
        </div>
      </header>

      <main>
        <section
          id="inicio"
          className="mx-auto grid max-w-7xl items-center gap-12 px-6 py-20 md:grid-cols-2 md:py-28"
        >
          <div>
            <span className="inline-flex rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-petcare-dark">
              A adoção começa com um encontro
            </span>

            <h1 className="mt-6 text-4xl font-extrabold leading-tight tracking-tight sm:text-5xl lg:text-6xl">
              Seu próximo melhor amigo está{" "}
              <span className="text-petcare-primary">esperando por você.</span>
            </h1>

            <p className="mt-6 max-w-xl text-lg leading-8 text-slate-600">
              Encontre um companheiro, conheça histórias especiais e transforme
              a vida de um animal por meio da adoção responsável.
            </p>

            <a
              href="#pets"
              className="mt-8 inline-flex rounded-xl bg-petcare-primary px-6 py-4 font-semibold text-white shadow-lg shadow-green-900/10 transition hover:-translate-y-0.5 hover:bg-petcare-dark"
            >
              Conhecer os pets <span className="ml-2">→</span>
            </a>

            <p className="mt-5 text-sm text-slate-500">
              Uma nova história pode começar hoje.
            </p>
          </div>

          <div className="relative flex min-h-72 items-center justify-center rounded-3xl bg-green-100 p-8 md:min-h-96">
            <div className="absolute right-8 top-8 h-24 w-24 rounded-full bg-amber-200/70" />
            <div className="absolute bottom-8 left-8 h-16 w-16 rounded-full bg-white/80" />

            <div className="relative text-center">
              <div className="text-8xl sm:text-9xl" aria-hidden="true">
                🐶
              </div>
              <p className="mt-5 rounded-2xl bg-white px-6 py-4 font-semibold shadow-sm">
                Todo pet merece um lar cheio de amor.
              </p>
            </div>
          </div>
        </section>

        <section id="pets" className="bg-white px-6 py-20">
          
          <div className="mt-10">
            {carregando && (
              <p className="text-center text-slate-500">
                Carregando pets...
              </p>
            )}
          
            {erro && (
              <p className="text-center text-red-600">
                Não foi possível carregar os pets.
                Tente novamente mais tarde.
              </p>
            )}
          
            {!carregando && !erro && pets.length === 0 && (
              <p className="text-center text-slate-500">
                Ainda não há pets cadastrados.
              </p>
            )}
          
            {!carregando && !erro && pets.length > 0 && (
              <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {pets.map((pet) => (<PetCard key={pet.id} pet={pet} />))}
              </div>
            )}
          </div>


        </section>
      </main>

      <footer id="sobre" className="border-t border-slate-200 bg-slate-50 px-6 py-8">
        <div className="mx-auto flex max-w-7xl flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
          <span className="font-bold text-petcare-dark">PetCare.</span>
          <p className="text-sm text-slate-500">
            Conectando animais a novos lares.
          </p>
        </div>
      </footer>
    </div>
  )
}

export default App
