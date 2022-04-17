import React from 'react';
import styles from "./MainPage.module.scss"
import UserList from '../../components/UserList/UserList';
import DefaultPage from '../../components/defaulPage/DefaultPage';
import { Route, Routes } from 'react-router-dom';
import ServerPage from '../../components/ServersPage/ServerPage';
import GamePage from '../../components/GamePage/GamePage';

function MainPage(props) {
    return (
        <div>
            <UserList/>
            <Routes>
                <Route path = '/' element = {<DefaultPage/>}/>
                <Route path = '/ServersList' element = {<ServerPage/>}/>
                <Route path = '/Game/:gameCode' element = {<GamePage/>}/>
            </Routes>
        </div>
    );
}

export default MainPage;