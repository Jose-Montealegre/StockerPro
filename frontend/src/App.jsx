import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [dashboard, setDashboard] = useState(null)
  const [error, setError] = useState(false)
  const [section, setSection] = useState('dashboard')
  const [productos, setProductos] = useState([])
  const [categorias, setCategorias] =  useState([])
  const [movimientos, setMovimientos] = useState([])
  const [clientes, setClientes] = useState([])
  const [mostrarFormulario, setMostrarFormulario] = useState(false)
  const [guardando, setGuardando] = useState(false)
  const [mensaje, setMensaje] = useState('')
  const [errorProducto, setErrorProducto] = useState('')
  const [mensajeMovimiento, setMensajeMovimiento] = useState('')
  const [errorMovimiento, setErrorMovimiento] = useState('')
  const [guardandoMovimiento, setGuardandoMovimiento] = useState(false)
  const [nuevoProducto, setNuevoProducto] = useState({
    nombre: '',
    descripcion: '',
    precio: '',
    stock: '',
    category_id: ''
  })
  const [nuevoMovimiento, setNuevoMovimiento] = useState({
  product_id: '',
  tipo: 'ENTRADA',
  cantidad: ''
})
const [mostrarFormularioCliente, setMostrarFormularioCliente] = useState(false)

const [nuevoCliente, setNuevoCliente] = useState({
  nombre: '',
  documento: '',
  correo: '',
  telefono: ''
})
const [guardandoCliente, setGuardandoCliente] = useState(false)
const [mensajeCliente, setMensajeCliente] = useState('')
const [errorCliente, setErrorCliente] = useState('')
const [clienteEditando, setClienteEditando] = useState(null)
const [ventas, setVentas] = useState([])

const [mostrarFormularioVenta, setMostrarFormularioVenta] = useState(false)

const [nuevaVenta, setNuevaVenta] = useState({
  customer_id: '',
  items: [
    {
      product_id: '',
      cantidad: ''
    }
  ]
})

const [guardandoVenta, setGuardandoVenta] = useState(false)

const [mensajeVenta, setMensajeVenta] = useState('')

const [errorVenta, setErrorVenta] = useState('')
  
  

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

fetch('http://127.0.0.1:8000/movements')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error al cargar movimientos')
    }

    return response.json()
  })
  .then((data) => {
    setMovimientos(data)
    console.log('Movimientos:', data)
  })
  .catch((error) => {
    console.error('Error al cargar movimientos:', error)
  })

  fetch('http://127.0.0.1:8000/customers')
  .then((response) => {
    if (!response.ok) {
      throw new Error('No se pudieron cargar los clientes')
    }

    return response.json()
  })
  .then((data) => {
    setClientes(data)
  })
  .catch((error) => {
    console.error('Error al cargar clientes:', error)
  })

  fetch('http://127.0.0.1:8000/sales')
  .then((response) => {
    if (!response.ok) {
      throw new Error('No se pudieron cargar las ventas')
    }

    return response.json()
  })
  .then((data) => {
    setVentas(data)
  })
  .catch((error) => {
    console.error('Error al cargar ventas:', error)
  })

}, [])

if (error) {
  return <p>Error al conectar con el servidor.</p>
}

if (!dashboard) {
  return <p>Cargando datos...</p>
}

const productoSeleccionado = productos.find(
  (producto) => producto.id === Number(nuevoMovimiento.product_id)
)

const productoVentaSeleccionado = productos.find(
  (producto) =>
    producto.id === Number(nuevaVenta.items[0].product_id)
)

const subtotalVenta = productoVentaSeleccionado
  ? productoVentaSeleccionado.precio *
    Number(nuevaVenta.items[0].cantidad || 0)
  : 0



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

          <button
          className={`menu-item ${section === 'inventario' ? 'active' : ''}`}
          type="button"
          onClick={() => setSection('inventario')}
          >
          Inventario
        </button>

        <button
          className={`menu-item ${section === 'clientes' ? 'active' : ''}`}
          type="button"
          onClick={() => setSection('clientes')}
        >
          Clientes
        </button>

        <button
          className={`menu-item ${section === 'ventas' ? 'active' : ''}`}
          type="button"
          onClick={() => setSection('ventas')}
        >
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
  .then(async (response) => {
  const data = await response.json()

  if (!response.ok) {
    throw new Error(data.detail || 'No se pudo registrar el movimiento')
  }

  return data
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

{section === 'inventario' && (
  <>
    <header className="header">
      <h2>Inventario</h2>
      <p>Control de entradas y salidas de productos</p>
    </header>

    <section className="dashboard">
      <div className="dashboard-title">
        <h2>Movimientos de inventario</h2>
        <p>Registra entradas y salidas de productos.</p>
      </div>
      {mensajeMovimiento && (
        <div className="message success-message">
          {mensajeMovimiento}
        </div>
      )}
      {errorMovimiento && (
        <div className="message error-message">
          {errorMovimiento}
        </div>
      )}
      <form
  className="product-form"
  onSubmit={(e) => {
    e.preventDefault()

    setMensajeMovimiento('')
    setErrorMovimiento('')

    if (guardandoMovimiento) {
      return
    }

    setGuardandoMovimiento(true)

    const movimientoParaEnviar = {
      product_id: Number(nuevoMovimiento.product_id),
      tipo: nuevoMovimiento.tipo,
      cantidad: Number(nuevoMovimiento.cantidad)
    }

    fetch('http://127.0.0.1:8000/movements', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(movimientoParaEnviar)
})
  .then(async (response) => {
  const data = await response.json()

  if (!response.ok) {
    throw new Error(data.detail || 'No se pudo registrar el movimiento')
  }

  return data
})
  .then((data) => {
  console.log('Movimiento registrado:', data)

  setMensajeMovimiento('Movimiento registrado correctamente')

  setNuevoMovimiento({
    ...nuevoMovimiento,
    cantidad: ''
  })

  fetch('http://127.0.0.1:8000/products')
    .then((response) => response.json())
    .then((data) => {
      setProductos(data)
    })

    fetch('http://127.0.0.1:8000/dashboard/summary')
  .then((response) => response.json())
  .then((data) => {
    setDashboard(data)
  })

    fetch('http://127.0.0.1:8000/movements')
  .then((response) => response.json())
  .then((data) => {
    setMovimientos(data)
  })
})
  .catch((error) => {
  console.error('Error al registrar el movimiento:', error)
  setErrorMovimiento(error.message)
})
.finally(() => {
  setGuardandoMovimiento(false)
})
  }}
>
  <div className="form-group">
    <label htmlFor="producto-movimiento">Producto</label>

    <select
      id="producto-movimiento"
      value={nuevoMovimiento.product_id}
      onChange={(e) =>
        setNuevoMovimiento({
          ...nuevoMovimiento,
          product_id: e.target.value
        })
      }
    >
      <option value="">Seleccionar producto</option>

      {productos.map((producto) => (
        <option key={producto.id} value={producto.id}>
          {producto.nombre} — Stock: {producto.stock}
        </option>
      ))}
    </select>
  </div>

  {productoSeleccionado && (
  <div className="card">
    <h3>Stock actual</h3>
    <p>{productoSeleccionado.stock}</p>
  </div>
)}

<div className="form-row">
  <div className="form-group">
    <label htmlFor="tipo-movimiento">Tipo de movimiento</label>

    <select
      id="tipo-movimiento"
      value={nuevoMovimiento.tipo}
      onChange={(e) =>
        setNuevoMovimiento({
          ...nuevoMovimiento,
          tipo: e.target.value
        })
      }
    >
      <option value="ENTRADA">ENTRADA</option>
      <option value="SALIDA">SALIDA</option>
    </select>
  </div>

  <div className="form-group">
    <label htmlFor="cantidad-movimiento">Cantidad</label>

    <input
      id="cantidad-movimiento"
      type="number"
      min="1"
      placeholder="Ej: 5"
      value={nuevoMovimiento.cantidad}
      onChange={(e) =>
        setNuevoMovimiento({
          ...nuevoMovimiento,
          cantidad: e.target.value
        })
      }
    />
  </div>
</div>
<button
  className="btn-primary"
  type="submit"
  disabled={guardandoMovimiento}
>
  {guardandoMovimiento ? 'Registrando...' : 'Registrar movimiento'}
</button>

</form>

<div className="products-table">
  <div className="dashboard-title">
    <h2>Historial de movimientos</h2>
    <p>Consulta las entradas y salidas registradas.</p>
  </div>

  <table>
    <thead>
      <tr>
        <th>Producto</th>
        <th>Tipo</th>
        <th>Cantidad</th>
        <th>Stock anterior</th>
        <th>Stock resultante</th>
        <th>Fecha</th>
      </tr>
    </thead>

    <tbody>
      {[...movimientos].reverse().map((movimiento) => (
        <tr key={movimiento.id}>
          <td>{movimiento.producto.nombre}</td>
          <td>
  <span
    className={
      movimiento.tipo === 'ENTRADA'
        ? 'movement-badge entrada'
        : 'movement-badge salida'
    }
  >
    {movimiento.tipo}
  </span>
</td>
          <td>{movimiento.cantidad}</td>
          <td>{movimiento.stock_anterior ?? '-'}</td>
          <td>{movimiento.stock_resultante ?? '-'}</td>
          <td>
  {movimiento.fecha
    ? new Date(movimiento.fecha).toLocaleString('es-CO')
    : '-'}
        </td>
      </tr>
      ))}
    </tbody>
  </table>
</div>

    </section>
  </>
)}

{section === 'clientes' && (
  <>
    <header className="header">
      <h2>Clientes</h2>
      <p>Gestiona los clientes registrados en Stocker Pro</p>
    </header>

    <section className="dashboard">
      <div className="clientes-header">
      <div className="dashboard-title">
        <h2>Listado de clientes</h2>
        <p>Consulta y administra la información de tus clientes.</p>
      </div>

      <button
      className="btn-primary"
      type="button"
      onClick={() => setMostrarFormularioCliente(!mostrarFormularioCliente)}
    >
      {mostrarFormularioCliente ? 'Cancelar' : '+ Nuevo cliente'}
    </button>
  </div>

  {mensajeCliente && (
          <div className="message success-message">
          {mensajeCliente}
      </div>
)}

{errorCliente && (
  <div className="message error-message">
    {errorCliente}
  </div>
)}

    {mostrarFormularioCliente && (
  <form
  className="product-form"
  onSubmit={(e) => {
    e.preventDefault()

    setMensajeCliente('')
    setErrorCliente('')

    if (guardandoCliente) {
      return
    }

    setGuardandoCliente(true)

    const urlCliente = clienteEditando
  ? `http://127.0.0.1:8000/customers/${clienteEditando}`
  : 'http://127.0.0.1:8000/customers'

const metodoCliente = clienteEditando ? 'PUT' : 'POST'

fetch(urlCliente, {
  method: metodoCliente,
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(nuevoCliente)
})
      .then(async (response) => {
        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.detail || 'No se pudo crear el cliente')
        }

        return data
      })
      .then((data) => {
  if (clienteEditando) {
    setClientes(
      clientes.map((cliente) =>
        cliente.id === clienteEditando ? data : cliente
      )
    )

    setMensajeCliente('Cliente actualizado correctamente')
  } else {
    setClientes([...clientes, data])

    setMensajeCliente('Cliente registrado correctamente')
  }

  setNuevoCliente({
    nombre: '',
    documento: '',
    correo: '',
    telefono: ''
  })

  setClienteEditando(null)
  setMostrarFormularioCliente(false)
})
      .catch((error) => {
        console.error('Error al crear cliente:', error)
        setErrorCliente(error.message)
      })
      .finally(() => {
        setGuardandoCliente(false)
      })
  }}
>

    <div className="form-group">
      <label htmlFor="nombre-cliente">Nombre</label>
      <input
        id="nombre-cliente"
        type="text"
        placeholder="Ej: Laura Martínez"
        value={nuevoCliente.nombre}
        onChange={(e) =>
          setNuevoCliente({
            ...nuevoCliente,
            nombre: e.target.value
          })
        }
      />
    </div>

    <div className="form-group">
      <label htmlFor="documento-cliente">Documento</label>
      <input
        id="documento-cliente"
        type="text"
        placeholder="Ej: 1020304050"
        value={nuevoCliente.documento}
        onChange={(e) =>
          setNuevoCliente({
            ...nuevoCliente,
            documento: e.target.value
          })
        }
      />
    </div>

    <div className="form-group">
      <label htmlFor="correo-cliente">Correo</label>
      <input
        id="correo-cliente"
        type="email"
        placeholder="Ej: cliente@email.com"
        value={nuevoCliente.correo}
        onChange={(e) =>
          setNuevoCliente({
            ...nuevoCliente,
            correo: e.target.value
          })
        }
      />
    </div>

    <div className="form-group">
      <label htmlFor="telefono-cliente">Teléfono</label>
      <input
        id="telefono-cliente"
        type="text"
        placeholder="Ej: 3001234567"
        value={nuevoCliente.telefono}
        onChange={(e) =>
          setNuevoCliente({
            ...nuevoCliente,
            telefono: e.target.value
          })
        }
      />
    </div>

    <button
      className="btn-primary"
      type="submit"
      disabled={guardandoCliente}
    >
      {guardandoCliente
  ? 'Guardando...'
  : clienteEditando
    ? 'Actualizar cliente'
    : 'Guardar cliente'}
    </button>

  </form>
)}

      <div className="products-table">
  <table>
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Documento</th>
        <th>Correo</th>
        <th>Teléfono</th>
        <th>Acciones</th>
      </tr>
    </thead>

    <tbody>
      {clientes.map((cliente) => (
        <tr key={cliente.id}>
          <td>{cliente.nombre}</td>
          <td>{cliente.documento}</td>
          <td>{cliente.correo}</td>
          <td>{cliente.telefono}</td>

          <td>
  <button
    className="btn-primary"
    type="button"
    onClick={() => {
      setClienteEditando(cliente.id)

      setNuevoCliente({
        nombre: cliente.nombre,
        documento: cliente.documento,
        correo: cliente.correo,
        telefono: cliente.telefono
      })

      setMostrarFormularioCliente(true)
      setMensajeCliente('')
      setErrorCliente('')
    }}
        >
            Editar
          </button>
          <button
  className="btn-delete"
  type="button"
  onClick={() => {
    const confirmar = window.confirm(
      `¿Seguro que deseas eliminar a ${cliente.nombre}?`
    )

    if (!confirmar) {
      return
    }

    fetch(`http://127.0.0.1:8000/customers/${cliente.id}`, {
      method: 'DELETE'
    })
      .then(async (response) => {
        if (!response.ok) {
          const data = await response.json()
          throw new Error(data.detail || 'No se pudo eliminar el cliente')
        }

        setClientes(
          clientes.filter(
            (clienteActual) => clienteActual.id !== cliente.id
          )
        )

        setMensajeCliente('Cliente eliminado correctamente')
        setErrorCliente('')
      })
      .catch((error) => {
        console.error('Error al eliminar cliente:', error)
        setErrorCliente(error.message)
        setMensajeCliente('')
      })
  }}
>
  Eliminar
</button>
          </td>
        </tr>
      ))}
    </tbody>
  </table>
</div>
    </section>
  </>
)}

{section === 'ventas' && (
  <>
    <header className="header">
      <h2>Ventas</h2>
      <p>Registra y consulta las ventas realizadas en Stocker Pro</p>
    </header>

    <section className="dashboard">
      <div className="clientes-header">
        <div className="dashboard-title">
          <h2>Historial de ventas</h2>
          <p>Consulta las ventas registradas en el sistema.</p>
        </div>

        <button
          className="btn-primary"
          type="button"
          onClick={() => setMostrarFormularioVenta(!mostrarFormularioVenta)}
        >
          {mostrarFormularioVenta ? 'Cancelar' : '+ Nueva venta'}
        </button>
      </div>
      {mensajeVenta && (
  <p className="success-message">{mensajeVenta}</p>
)}

{errorVenta && (
  <p className="error-message">{errorVenta}</p>
)}
{mostrarFormularioVenta && (
  <form
  className="product-form"
  onSubmit={(e) => {
    e.preventDefault()

    setMensajeVenta('')
    setErrorVenta('')

    if (guardandoVenta) return

    setGuardandoVenta(true)

    const ventaParaEnviar = {
      customer_id: Number(nuevaVenta.customer_id),
      items: nuevaVenta.items.map((item) => ({
        product_id: Number(item.product_id),
        cantidad: Number(item.cantidad)
      }))
    }

    fetch('http://127.0.0.1:8000/sales', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(ventaParaEnviar)
    })
      .then(async (response) => {
        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.detail || 'No se pudo registrar la venta')
        }

        return data
      })
      .then((data) => {
        setVentas([...ventas, data])

        setMensajeVenta('Venta registrada correctamente')

        setNuevaVenta({
          customer_id: '',
          items: [
            {
              product_id: '',
              cantidad: ''
            }
          ]
        })

        setMostrarFormularioVenta(false)

        fetch('http://127.0.0.1:8000/products')
          .then((response) => response.json())
          .then((data) => setProductos(data))

        fetch('http://127.0.0.1:8000/dashboard/summary')
          .then((response) => response.json())
          .then((data) => setDashboard(data))

        fetch('http://127.0.0.1:8000/movements')
          .then((response) => response.json())
          .then((data) => setMovimientos(data))
      })
      .catch((error) => {
        setErrorVenta(error.message)
      })
      .finally(() => {
        setGuardandoVenta(false)
      })
  }}
>
    <div className="form-group">
      <label htmlFor="cliente-venta">Cliente</label>

      <select
        id="cliente-venta"
        value={nuevaVenta.customer_id}
        onChange={(e) =>
          setNuevaVenta({
            ...nuevaVenta,
            customer_id: e.target.value
          })
        }
      >
        <option value="">Seleccionar cliente</option>

        {clientes.map((cliente) => (
          <option key={cliente.id} value={cliente.id}>
            {cliente.nombre} — {cliente.documento}
          </option>
        ))}
      </select>
    </div>

    <div className="form-row">
      <div className="form-group">
        <label htmlFor="producto-venta">Producto</label>

        <select
          id="producto-venta"
          value={nuevaVenta.items[0].product_id}
          onChange={(e) =>
            setNuevaVenta({
              ...nuevaVenta,
              items: [
                {
                  ...nuevaVenta.items[0],
                  product_id: e.target.value
                }
              ]
            })
          }
        >
          <option value="">Seleccionar producto</option>

          {productos.map((producto) => (
            <option key={producto.id} value={producto.id}>
              {producto.nombre} — Stock: {producto.stock}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="cantidad-venta">Cantidad</label>

        <input
          id="cantidad-venta"
          type="number"
          min="1"
          placeholder="Ej: 2"
          value={nuevaVenta.items[0].cantidad}
          onChange={(e) =>
            setNuevaVenta({
              ...nuevaVenta,
              items: [
                {
                  ...nuevaVenta.items[0],
                  cantidad: e.target.value
                }
              ]
            })
          }
        />
      </div>
    </div>
    {productoVentaSeleccionado && (
  <div className="card sale-summary">
    <h3>Resumen de la venta</h3>

    <p>
      Producto: <strong>{productoVentaSeleccionado.nombre}</strong>
    </p>

    <p>
      Precio unitario:{' '}
      <strong>
        ${Number(productoVentaSeleccionado.precio).toLocaleString('es-CO')}
      </strong>
    </p>

    <p>
      Cantidad:{' '}
      <strong>{Number(nuevaVenta.items[0].cantidad || 0)}</strong>
    </p>

    <p>
      Total:{' '}
      <strong>
        ${Number(subtotalVenta).toLocaleString('es-CO')}
      </strong>
    </p>
  </div>

)}

<button
  className="btn-primary"
  type="submit"
  disabled={guardandoVenta}
>
  {guardandoVenta ? 'Registrando...' : 'Registrar venta'}
</button>
  </form>
)}
      <div className="table-container">
        <table className="products-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Cliente</th>
              <th>Total</th>
              <th>Fecha</th>
            </tr>
          </thead>

          <tbody>
            {ventas.map((venta) => (
              <tr key={venta.id}>
                <td>{venta.id}</td>
                <td>{venta.cliente.nombre}</td>
                <td>
                  ${Number(venta.total).toLocaleString('es-CO')}
                </td>
                <td>
                  {new Date(venta.fecha).toLocaleString('es-CO')}
                </td>
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