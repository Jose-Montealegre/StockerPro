import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [dashboard, setDashboard] = useState(null)
  const [error, setError] = useState(false)
  

useEffect(() => {
  fetch('http://127.0.0.1:8000/dashboard/summary')
    .then((response) => response.json())
    .then((data) => {
      setDashboard(data)
    })
    .catch((error) => {
      console.error('Error al cargar el dashboard:', error)
      setError(true)
    })
}, [])

if (error) {
  return <p>Error al conectar con el servidor.</p>
}

if (!dashboard) {
  return <p>Cargando datos...</p>
}

  return (
  <main className="app">
    <header className="header">
      <h1>Stocker Pro</h1>
      <p>Sistema de gestión de inventarios</p>
    </header>

    <section className="dashboard">
      <div className="dashboard-title">
        <h2>Resumen del inventario</h2>
        <p>Estado general de Stocker Pro</p>
      </div>

      <div className="cards">
        <div className="card">
          <h3>Productos</h3>
          <p>{dashboard.total_productos}</p>
        </div>

        <div className="card">
          <h3>Unidades</h3>
          <p>{dashboard.total_unidades}</p>
        </div>

        <div className="card">
          <h3>Stock bajo</h3>
          <p>{dashboard.productos_stock_bajo}</p>
        </div>

        <div className="card">
          <h3>Agotados</h3>
          <p>{dashboard.productos_agotados}</p>
        </div>

        <div className="card">
          <h3>Categorías</h3>
          <p>{dashboard.total_categorias}</p>
        </div>
      </div>
    </section>
  </main>
)
}

export default App 