import React, { useEffect, useState } from "react";
import styles from "./ServerPage.module.scss";
import JoinGame from "../JoingGame/JoinGame";
import MainPageButton from "../MainPageButton/MainPageButton";
import { getGames } from "../../Redux/axios";
import { useNavigate } from "react-router-dom";

function ServerPage(props) {
  const [games, setGames] = useState([]);
  const [gameCode, setGameCode] = useState();
  const navigate = useNavigate()

  useEffect(()=>{
      const getGamesList = async () =>{
          const response = await getGames()
          setGames(response)
          console.log(response)
      }
      getGamesList()
      return ()=>{
          setGames([])
          setGameCode()
      }
  },[])

  // Вход в игру

  const joinGame = (gameCode) =>{
    localStorage.setItem('gameCode',gameCode)
    navigate(`/MainPage/Game/${gameCode}`)
  //     setGameCode(gameCode)
  //     setWs( new WebSocket(wsURL + gameCode + "/"))
  }

  // ws.onopen = (e) =>{
  //     ws.send(JSON.stringify({
  //         command: "join",
  //         user_token: localStorage.token,
  //         game_code: gameCode
  //     }))
  //     localStorage.setItem("game_code", gameCode)
  //     console.log(e)
  // }

  return (
    <div className={styles.ServerPage}>
      <MainPageButton/>
      <div className={styles.ServerList}>
        <h1>Servers</h1>
        <div>
          {games?.map((game) => {
            return (
              <div
                key={game.game_code}
                onClick={() => joinGame(game.game_code)}
                className={styles.gameCode_div}
              >
                <p className={styles.game_code}>{game.game_code}</p>
                <div className={styles.gameIcon}></div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default ServerPage;
