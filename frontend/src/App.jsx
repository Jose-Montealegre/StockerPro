import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [dashboard, setDashboard] = useState(null)
  const [error, setError] = useState(false)
  const [section, setSection] = useState('dashboard')
  const [productos, setProductos] = useState([])
  const [categorias, setCategorias] =  useState([])
  const [mostrarFormulario, setMostrarFormulario] = useState(false)
  const [guardando, setGuardando] = useState(false)
  const [mensaje, setMensaje] = useState('')
  const [errorProducto, setErrorProducto] = useState('')
  const [nuevoProducto, setNuevoProducto] = useState({
    nombre: '',
    descripcion: '',
    precio: '',
    stock: '',
    category_id: ''
  })
  
  

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

  fetch('http://127.0.0.1:8000/products')
  .then((response) => response.json())
  .then((data) => {
    console.log('Productos recibidos:', data)
    setProductos(data)
  })
  .catch((error) => {
    console.error('Error al cargar los productos:', error)
  })

fetch('http://127.0.0.1:8000/categories')
  .then((response) => response.json())
  .then((data) => {
    console.log('Categorías recibidas:', data)
    setCategorias(data)
  })
  .catch((error) => {
    console.error('Error al cargar las categorías:', error)
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
    <aside className="sidebar">
      <div className="brand">
        <h1>Stocker Pro</h1>
        <p>Sistema de gestión de inventarios</p>
      </div>

      <nav className="menu">
          <button
            className={`menu-item ${section === 'dashboard' ? 'active' : ''}`}
            type="button"
            onClick={() => setSection('dashboard')}
          >
            Dashboard
          </button>

          <button
            className={`menu-item ${section === 'productos' ? 'active' : ''}`}
            type="button"
            onClick={() => setSection('productos')}
          >
            Productos
          </button>

        <button className="menu-item" type="button">
          Inventario
        </button>

        <button className="menu-item" type="button">
          Clientes
        </button>

        <button className="menu-item" type="button">
          Ventas
        </button>

        <button className="menu-item" type="button">
          Reportes
        </button>

        <button className="menu-item" type="button">
          Recomendaciones
        </button>
      </nav>
    </aside>

    <section className="content">
      {section === 'dashboard' && (
        <>
        <header className='header'>
        <h2>Dashboard</h2>
        <p>Vista general de Stocker Pro</p>
      </header>

      <section className="dashboard">
        <div className="dashboard-title">
          <h2>Resumen del inventario</h2>
          <p>Estado general del negocio</p>
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
    </>
  
)}
  {section === 'productos' && (
  <>
    <header className="header">
      <h2>Productos</h2>
      <p>Gestión de productos de Stocker Pro</p>
    </header>

    <section className="dashboard">
      <div className="products-header">
        <div className="dashboard-title">
    <h2>Productos registrados</h2>
    <p>Listado actual de productos del inventario.</p>
  </div>

  <button
    className="btn-primary"
    type="button"
    onClick={() => setMostrarFormulario(true)}
  >
    + Nuevo producto
  </button>
</div>

{mensaje && (
  <div className="message success-message">
    {mensaje}
  </div>
)}

{errorProducto && (
  <div className="message error-message">
    {errorProducto}
  </div>
)}

{mostrarFormulario && (
  <div className="product-form">
    <div className="form-header">
      <h3>Nuevo producto</h3>

      <button
        type="button"
        className="btn-close"
        onClick={() => setMostrarFormulario(false)}
      >
        Cerrar
      </button>
    </div>

    <form 
    className="form-product"
    onSubmit={(e) => {
  e.preventDefault()
  setMensaje('')
  setErrorProducto('')

  if (guardando) {
    return
  }

  setGuardando(true)

  const productoParaEnviar = {
    nombre: nuevoProducto.nombre,
    descripcion: nuevoProducto.descripcion,
    precio: Number(nuevoProducto.precio),
    stock: Number(nuevoProducto.stock),
    category_id: Number(nuevoProducto.category_id)
  }

  fetch('http://127.0.0.1:8000/products', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(productoParaEnviar)
})
  .then((response) => {
    if (!response.ok) {
      throw new Error('No se pudo crear el producto')
    }

    return response.json()
  })
  .then((data) => {
    console.log('Producto creado:', data)

    setProductos([...productos, data])

    setNuevoProducto({
      nombre: '',
      descripcion: '',
      precio: '',
      stock: '',
      category_id: ''
    })

    setMostrarFormulario(false)
    setMensaje('Producto creado correctamente')

    fetch('http://127.0.0.1:8000/dashboard/summary')
      .then((response) => response.json())
      .then((data) => {
        setDashboard(data)
      })
  })
  .catch((error) => {
    console.error('Error al crear el producto:', error)
    setErrorProducto('Ocurrió un error al crear el producto')
  })
  .finally(() => {
    setGuardando(false)
  })
}}
    >
  <div className="form-group">
    <label htmlFor="nombre">Nombre</label>
    <input
      id="nombre"
      type="text"
      placeholder="Ej: Teclado Logitech K120"
      value={nuevoProducto.nombre}
      onChange={(e) =>
        setNuevoProducto({
          ...nuevoProducto,
          nombre: e.target.value
        })
      }
    />
  </div>

  <div className="form-group">
    <label htmlFor="descripcion">Descripción</label>
    <input
      id="descripcion"
      type="text"
      placeholder="Descripción del producto"
      value={nuevoProducto.descripcion}
      onChange={(e) =>
        setNuevoProducto({
          ...nuevoProducto,
          descripcion: e.target.value
        })
      }
    />
  </div>

  <div className="form-row">
    <div className="form-group">
      <label htmlFor="precio">Precio</label>
      <input
        id="precio"
        type="number"
        min="0"
        placeholder="Ej: 85000"
        value={nuevoProducto.precio}
        onChange={(e) =>
          setNuevoProducto({
            ...nuevoProducto,
            precio: e.target.value
          })
        }
      />
    </div>

    <div className="form-group">
      <label htmlFor="stock">Stock inicial</label>
      <input
        id="stock"
        type="number"
        min="0"
        placeholder="Ej: 10"
        value={nuevoProducto.stock}
        onChange={(e) =>
          setNuevoProducto({
            ...nuevoProducto,
            stock: e.target.value
          })
        }
      />
    </div>
  </div>

  <div className="form-group">
    <label htmlFor="categoria">Categoría</label>
    <select id="categoria"
    value={nuevoProducto.category_id}
    onChange={(e) =>
      setNuevoProducto({
        ...nuevoProducto,
        category_id: e.target.value
      })
    }
  >
    <option value="">Seleccionar categoría</option>

    {categorias.map((categoria) => (
      <option key={categoria.id} value={categoria.id}>
        {categoria.nombre}
      </option>
    ))}
    </select>
  </div>

  <button
  className="btn-primary"
  type="submit"
  disabled={guardando}
>
  {guardando ? 'Guardando...' : 'Guardar producto'}
</button>
</form>
  </div>
)}

      <div className="table-container">
        <table className="products-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Precio</th>
              <th>Stock</th>
              <th>Categoría</th>
            </tr>
          </thead>

          <tbody>
            {productos.map((producto) => (
              <tr key={producto.id}>
                <td>{producto.id}</td>
                <td>{producto.nombre}</td>
                <td>${producto.precio.toLocaleString('es-CO')}</td>
                <td>{producto.stock}</td>
                <td>{producto.categoria?.nombre || 'Sin categoría'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  </>
)}
</section>
  </main>
)
}

export default App 