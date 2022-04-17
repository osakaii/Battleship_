import React from 'react';
import CreateGame from '../CreateGame/CreateGame';
import styles from './DefaultPage.module.scss'
import JoinGame from '../JoingGame/JoinGame';
import LogOut from '../LogOut/LogOut';

function DefaultPage(props) {
    return (
        <div className={styles.DefaultPage}>
            <div className={styles.container}>
                <CreateGame/>
                <JoinGame/>
                <LogOut/>
            </div>
        </div>
    );
}

export default DefaultPage;