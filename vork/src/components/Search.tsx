import React from 'react'
import Search1 from "../assets/search (1) 5.png"

const Search = () => {
  return (
    <div>
    <div className='Search'>
      <input type="text" placeholder='Пошук роботи'/>
      <img src={Search1} alt="" />
    </div>
    <div className="city">
        <input type="text" placeholder='Вся Україна'/>
        <img src={Search1} alt="" />
    </div>
    <div className="find">
        <button>Знайти вакансії</button>
    </div>
    <div className="example">
    <h1>Наприклад:</h1>
    <p>Кухар, Менеджер, Касир</p>
    </div>
    <div className="work">
    <h1>236481</h1>
    <p>Нових вакансії</p>
    </div>
    </div>
  )
}

export default Search
