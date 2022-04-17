import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import MainPageButton from '../MainPageButton/MainPageButton';
import styles from './GamePage.module.scss'
import { useEffect } from 'react';
import { wsURL } from '../../const';
import Game from '../Game/Game';

function GamePage(props) {
    const gameCode = useParams().gameCode
    const [ isWaiting , setIsWaiting ] = useState(true)
    const [ webSocket, setWebSocket ] = useState({})

    useEffect(()=>{
        console.log('connected')
        setWebSocket( new WebSocket(wsURL + gameCode + '/'))
    },[])
    webSocket.onopen = (e) =>{
        console.log(e)
        webSocket.send(JSON.stringify({
            command: 'join',
            user_token: localStorage.Token
        }))
    }
    webSocket.onmessage = (e) =>{
        console.log(e)
        const gameStarted = JSON.parse(e.data)
        console.log(gameStarted)
        if(gameStarted.message == 'Game started'){
            setIsWaiting(false)
        }
    }
    return (
        <div className={styles.GamePage}>
            {
                isWaiting?
                <div>Waiting for Someone</div>
                :
                <Game webSocket/>
            }
            <MainPageButton/>
        </div>
    );
}

export default GamePage;