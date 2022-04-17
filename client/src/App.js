
import { useEffect } from 'react';
import { Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import PrivateRoute from './components/PrivateRoute';
import ErrorPage from './Pages/ErrorPage/ErrorPage';
import Login from './Pages/Login and Reg/Login';
import MainPage from './Pages/MainPage/MainPage';
import Registration from './Pages/Login and Reg/Reg';

function App() {

  const navigate = useNavigate()

  useEffect(()=>{
    navigate('/login')
  },[])

  return (
    <div className="App">
      <Routes>
        <Route path = "/MainPage/*" element = {<PrivateRoute><MainPage/></PrivateRoute>}/>
        <Route path = '/login' element = {<Login/>}/>
        <Route path = '/reg' element = {<Registration/>}/>
        <Route path = '*' element = {<ErrorPage/>}/>
      </Routes>
    </div>
  );
}

export default App;
