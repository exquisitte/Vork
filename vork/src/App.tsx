import { useCallback, useState } from 'react'
import "./styles/style.css"
import Sidebar from './components/Sidebar'
import Header from './components/Header'
import Search from './components/Search'
import Work from './components/Work'
import Main from './components/Main'
import Green from "./assets/Green.png"
import Blue from "./assets/Blue.png"
import Footer from './components/Footer'

function App() {
  return (
    <>
      <div className="App">
        <img  src={Green} alt="" />
        <img className="Blue" src={Blue} alt="" />
        <Main/>
        <Sidebar />
        <Header />
        <Search />
        <Work />
        <Footer />
      </div>
    </>
  )
}

export default App
