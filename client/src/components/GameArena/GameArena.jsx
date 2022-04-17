import React, { useEffect, useState } from 'react';
import styles from './GameArena.module.scss'

function GameArena(props) {
    
    const [gameGrid, setGameGrid] = useState()
    let array = []

    for (let i = 1; i <= 25; i++) {
        let cell = {
          position: "x" + i,
          ship: false,
          shooted: false,
        };
        array.push(cell);
    }
    useEffect(()=>{
        setGameGrid(array)
    },[])

    const createShip = (index) =>{
        if(!gameGrid[index].ship){
            let tempArr = gameGrid.slice(0)
            tempArr[index].ship = true
            setGameGrid(tempArr);
        }else{
            let tempArr = gameGrid.slice(0)
            tempArr[index].ship = false
            setGameGrid(tempArr);
        }
    } 
    return (
        <div className={styles.gameGrid}>
            {   
                gameGrid?.map((el, index)=>{
                    return(
                        <div 
                        key={el.position}
                        className={el.ship ? styles.cell + " " + styles.ship : styles.cell}
                        onClick={()=>createShip(index)}></div>
                    )
                })
            }
        </div>
    );
}

export default GameArena;