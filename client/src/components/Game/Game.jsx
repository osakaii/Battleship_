import React from 'react';
import { useState } from 'react';
import styles from './Game.module.scss'
import GameArena from '../GameArena/GameArena';

function Game({ webSocket }) {
    const [gameIsStarted, setGameIsStarted] = useState(false)
    const goReady = () =>{
        webSocket.send(JSON.stringify({
            command: 'ready',

        }))
    }

    return (
        <div className={styles.Game}>
            <div>
                <GameArena type = "myArena"/>
                {
                    gameIsStarted && <GameArena type = "enemy"/>
                }
            </div>
            <button className='button' onClick={()=>goReady()}>Ready</button>
        </div>
    );
}

export default Game;