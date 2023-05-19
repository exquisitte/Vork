import React from 'react'

const Header = () => {
  return (
    <div className='Header'>
        <h1>Головна</h1>
        <div className="right-btn">
        <p>Вакансії</p>
        <p>Профіль</p>
        <p>Повідомлення</p>
        <button type='button'>Вхід</button>
        </div>
    </div>
  )
}

export default Header
