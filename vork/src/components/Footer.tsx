import React from 'react'
import left from '../assets/left-arrow.png'
import right from '../assets/right-arrow.png'

const Footer = () => {
  return (
    <div className='Footer'>
      <img className="left_arrow" src={left} alt="" />
      <img className="right_arrow" src={right} alt="" />
      <div className="numbers" style={{ marginLeft: '20px' }}>
        <div className="number-row">
          <p>1</p>
          <p>2</p>
          <p>3</p>
          <p>...</p>
          <p>400</p>
        </div>
      </div>
    </div>
  )
}

export default Footer