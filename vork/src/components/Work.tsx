import React from 'react'
import Ua from '../assets/🇺🇦.png'
import Save from '../assets/Save.png'

const Work = () => {
  return (
    <div className='Work'>
      <div className="container1">
        <div className="works">
          <div className="vacancy">
            <h1>Назва роботи</h1>
            <h2>Назва компанії</h2>
            <img src={Ua} alt="" className='Ua'/>
            <h3>Місто</h3>
            <p className='salary'>10 000 ₴ - 30 000 ₴</p>
            <p className='Opis'>Тут опис до зп</p>
            <p className='type'>Вид зайнятості</p>
            <p className='Years'>Тут скільки треба досвіду, яка освіта</p>
            <p className='Baka'>Тут головний опис вакансії</p>
            <img src={Save} alt="" className='save'/>
            <p className='Save'>Зберегти</p>
          </div>
        </div>
      </div>
      <div className="container2">
        <div className="works">
          <div className='vacancy'>
            <h1>Назва роботи</h1>
            <h2>Назва компанії</h2>
            <img src={Ua} alt="" className='Ua'/>
            <h3>Місто</h3>
            <p className='salary'>10 000 ₴ - 30 000 ₴</p>
            <p className='Opis'>Тут опис до зп</p>
            <p className='type'>Вид зайнятості</p>
            <p className='Years'>Тут скільки треба досвіду, яка освіта</p>
            <p className='Baka'>Тут головний опис вакансії</p>
            <img src={Save} alt="" className='save'/>
            <p className='Save'>Зберегти</p>
          </div>
        </div>
      </div>
      <div className="container3">
        <div className="works">
          <div className='vacancy'>
            <h1>Назва роботи</h1>
            <h2>Назва компанії</h2>
            <img src={Ua} alt="" className='Ua'/>
            <h3>Місто</h3>
            <p className='salary'>10 000 ₴ - 30 000 ₴</p>
            <p className='Opis'>Тут опис до зп</p>
            <p className='type'>Вид зайнятості</p>
            <p className='Years'>Тут скільки треба досвіду, яка освіта</p>
            <p className='Baka'>Тут головний опис вакансії</p>
            <img src={Save} alt="" className='save'/>
            <p className='Save'>Зберегти</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Work;
