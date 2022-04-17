import React, { useState } from "react";
import { Link, Navigate } from "react-router-dom";
import styles from "./LoginReg.module.scss";
import { Register } from '../../Redux/axios';

function Registration(props) {
  const [inputValue, setInputValue] = useState({
    username: "",
    password: "",
  });

  //регистрация
  const reg = async (e) => {
    console.log(inputValue)
    e.preventDefault();
    let response = await Register(JSON.stringify(inputValue))
    setInputValue({ username: "", password: "" });
    if(response){
      Navigate('/login')
    }
  };
  return (
    <div className={styles.SignPage}>
      <div className={styles.container}>
        <h1>Registration</h1>
        <form className={styles.form} onSubmit={(e)=>reg(e)}>
          <input className={styles.input} type="text" placeholder="name" onChange={(e)=>setInputValue({...inputValue,username: e.target.value})}/>
          <input className={styles.input} type="text" placeholder="password" onChange={(e)=>setInputValue({...inputValue,password: e.target.value})}/>
          <div className={styles.form_bottom}>
            <button >Sign Up</button>
            <Link to="/login">Login</Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Registration;
