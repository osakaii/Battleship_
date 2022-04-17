import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Log } from "../../Redux/axios";
import styles from "./LoginReg.module.scss";

function Login(props) {
  
  const [inputValue, setInputValue] = useState({
    username: "",
    password: "",
  });
  const navigate = useNavigate()
  useEffect(()=>{
    if(localStorage.getItem('Token')){
      navigate('/MainPage')
    }
  })


  //логин
  const login = async (e) => {
    e.preventDefault();
    let response = await Log(JSON.stringify(inputValue))
    setInputValue({ username: "", password: "" });
    if(response){
      navigate('/MainPage')
    }
  };

  return (
    <div className={styles.SignPage}>
      <div className={styles.container}>
        <h1>Login</h1>
        <form className={styles.form} onSubmit={(e) => login(e)}>
          <input
            value = {inputValue.username}
            className = {styles.input}
            type = "text"
            placeholder = "name"
            onChange = {(e) =>
              setInputValue({ ...inputValue, username: e.target.value })
            }
          />
          <input
            value = {inputValue.password}
            className = {styles.input}
            type = "text"
            placeholder = "password"
            onChange = {(e) =>
              setInputValue({ ...inputValue, password: e.target.value })
            }
          />
          <div className={styles.form_bottom}>
            <button >Login</button>
            <Link to="/reg">Registration</Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login;
