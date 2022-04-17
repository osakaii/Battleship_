import React, { useEffect, useState } from 'react';
import { getUsers } from '../../Redux/axios';
import styles from './UserList.module.scss'

function UserList(props) {
    const [users, setUsers] = useState([]);
    const [listClass, setListClass] = useState(true)

    //Get Users
    useEffect(() => {
      const fetchData = async () =>{
        const response = await getUsers();
        setUsers(response);
        console.log(users);
      }
      fetchData()
    }, []);
  
    const toggleList = () =>{
      listClass ? setListClass(false): setListClass(true)
    }
  
    return (
      <div className={ listClass ? styles.userList : `${styles.userList} ${styles.closed}` }>
        <h1 className={styles.UsersText}>USERS</h1>
        <input type="text" className={styles.searchInput} placeholder="search"/>
        {users?.map((user) => {
          return <div className={styles.user} key={user.id}>{user.username}</div>;
        })}
        <div className={listClass? styles.open : `${styles.open} ${styles.closedButton}`} onClick={toggleList}></div>
      </div>
    );
}

export default UserList;