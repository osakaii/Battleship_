import React from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './JoinGame.module.scss'

function JoinGame(props) {
    const navigate = useNavigate()

    return (
        <div className= 'button' onClick={()=>{navigate('/MainPage/ServersList')}}>
            <h1 className={styles.h1}>Join</h1>
        </div>
    );
}

export default JoinGame;