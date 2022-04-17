import React from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './MainPageButton.module.scss'

function MainPageButton(props) {
    const navigate = useNavigate()

    const goMainMenu = () =>{
        navigate('/MainPage')
    }
    return (
        <div onClick={()=>goMainMenu()} className={styles.MainMenuButton}>
            Main Menu
        </div>
    );
}

export default MainPageButton;