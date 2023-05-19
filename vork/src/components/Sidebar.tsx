import React from 'react'
import under_arrow from "../assets/under_arrow.png"

const Sidebar = () => {
  return (
    <div className='Sidebar'>
      <h1>ФІЛЬТР</h1>
      <div className="place">
        <h2>Місце роботи</h2>
      <div className="dropdown">
  <button className="dropbtn">Країна</button>
  <img src={under_arrow} alt="" />
  <div className="dropdown-content">
    <a href="#">A</a>
    <a href="#">B</a>
    <a href="#">C</a>
    </div>
</div>
<div className="region">
    <div className="dropdown">
  <button className="dropbtn">Область / Регіон</button>
  <img src={under_arrow} alt="" />
  <div className="dropdown-content">
    <a href="#">A</a>
    <a href="#">B</a>
    <a href="#">C</a>
    </div>
</div>
</div>
<div className="city1">
    <div className="dropdown">
  <button className="dropbtn">Місто</button>
  <img src={under_arrow} alt="" />
  <div className="dropdown-content">
    <a href="#">A</a>
    <a href="#">B</a>
    <a href="#">C</a>
    </div>
    </div>
</div>
<div className="salary1">
  <h2>Зарплата</h2>
  <div className="dropdown">
    <button className="dropbtn">Від</button>
    <img src={under_arrow} alt="" />
    <div className="dropdown-content">
      <a href="#">A</a>
      <a href="#">B</a>
      <a href="#">C</a>
    </div>
  </div>
  <div className="dropdown">
    <div className="right-dropdown">
      <button className="dropbtn">До</button>
      <img src={under_arrow} alt="" />
      <div className="dropdown-content">
        <a href="#">A</a>
        <a href="#">B</a>
        <a href="#">C</a>
      </div>
      
    </div>
    
  </div>
</div>
<div className="dropdown">
    <button className="dropbtn">Валюта</button>
    <img src={under_arrow} alt="" />
    <div className="dropdown-content">
      <a href="#">A</a>
      <a href="#">B</a>
      <a href="#">C</a>
    </div>
    <h3>Не вказано</h3>
  </div>
  <div className="type1">
    <h2>Вид зайнятості</h2>
    <p>Не повна</p>
    <p>Повна</p>
  </div>
  <div className="approach">
    <h2>Підходить</h2>
    <p>Кандидатам без досвіду</p>
    <p>Кандидатам без резюме</p>
    <p>Студентам</p>
    <p>Людям з інвалідністю</p>
    <p>Ветеранам</p>
    <p>Пенсіонерам</p>
  </div>
</div>
</div>
  )
}

export default Sidebar
