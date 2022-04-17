import React from 'react';
import styles from './LogOut.module.scss'
import { Logout } from '../../Redux/axios';

function LogOut(props) {

    return (
        <div className = {`button`} id={styles.LeaveGame} onClick={() => Logout()}>
            <h1 className={styles.h1}>Leave</h1>
        </div>
    );
}

export default LogOut;