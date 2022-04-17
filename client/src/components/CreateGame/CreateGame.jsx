import React from 'react';
import styles from './CreateGame.module.scss'
import { createGame_req } from '../../Redux/axios';
import { useNavigate } from 'react-router-dom';

function CreateGame(props) {
    const navigate = useNavigate()

    const createNewGame = async() =>{
        const responseCreateGame = await createGame_req()
        if(responseCreateGame){
            localStorage.setItem('gameCode',responseCreateGame)
            navigate(`Game/${responseCreateGame}`)
        }else{
            console.error('Game wasnt created')
        }
        navigate(`/MainPage/Game/${responseCreateGame}`)
    }

    return (
        <div className='button' onClick={()=>createNewGame()}>
            <h1 className={styles.h1}>Create Game</h1>
        </div>
    );
}

export default CreateGame;